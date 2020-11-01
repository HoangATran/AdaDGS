#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:02:05 2020

@author: htp

- CHANGE: Improving grad_adapt radius adjusting
- CHANGE: Brute_force line search is not limited by the boundary now
- ADD: reflection trick for box constraints. To turn on constrained optimization, un-commenting to_domain function (not so good results though) 
- ADD: Allowing testing randomly rotated functions
- ADD: Outputting to cvs file
- REMOVE: BFGS and Wolfe line search
"""

import numpy as np
from numpy import pi, sqrt
from scipy.special import roots_hermite
from scipy.stats import special_ortho_group
import numpy.matlib
import random
import setup_param_v2

import csv
from os import path

#----------------------------------------------------------
# supporting functions
#----------------------------------------------------------
def gramschmidt(A):
    Q = np.zeros(A.shape)
    Q[0,:] = A[0,:] / np.linalg.norm(A[0,:])
    
    for k in range(1,A.shape[1]):
        u = A[k,:]
        for j in range(0,k):
           u = u - np.dot(Q[j,:],A[k,:]) * Q[j,:]
        Q[k,:] = u / np.linalg.norm(u)
        
    return Q

def to_unit_cube(x, lb, ub):
    """Project to [0, 1]^d from hypercube with bounds lb and ub"""
    assert np.all(lb < ub) and lb.ndim == 1 and ub.ndim == 1 and x.ndim == 2
    xx = (x - lb) / (ub - lb)
    return xx


def from_unit_cube(x, lb, ub):
    """Project from [0, 1]^d to hypercube with bounds lb and ub"""
    assert np.all(lb < ub) and lb.ndim == 1 and ub.ndim == 1 and x.ndim == 2
    xx = x * (ub - lb) + lb
    return xx

def to_domain(x, lb, ub): 
    assert np.all(lb < ub) and lb.ndim == 1 and ub.ndim == 1 and x.ndim == 2
    x0 = np.zeros_like(x)
    width = ub-lb
    for j in range(np.shape(x)[0]): 
        ldist = x[j,:]-lb
        rdist = ub-x[j,:]
        for i in range(np.shape(x)[1]): 
            if ldist[i]>0:
                if (ldist[i]//width[i]) % 2 == 0: 
                    x0[j,i] = lb[i] + (ldist[i] % width[i])
                else: 
                    x0[j,i] = ub[i] - (ldist[i] % width[i])
            else:
                if (rdist[i]//width[i]) % 2 == 0: 
                    x0[j,i] = ub[i] - (rdist[i] % width[i])
                else: 
                    x0[j,i] = lb[i] + (rdist[i] % width[i])    
    return x0

#----------------------------------------------------------
# Translated and rotated function and DGS gradient estimators
#----------------------------------------------------------          
def RTfun_m(x,T,lt,dim): 
    return(fun_m(np.matmul(x-lt,T),dim))
        
def DGS_grad(X,T,lt,radius):
    gh_value_mat_rot = np.matmul(gh_value_mat,A.transpose())        
    X_all_center = np.matlib.repmat(X,GH_pts*dim,1) + radius * sqrt(2.0) * gh_value_mat_rot
#    X_all_center = to_domain(X_all_center, lb, ub)
    Y_all_center = np.reshape(np.multiply(RTfun_m(X_all_center,T,lt,dim), gh_value_vec), (GH_pts, dim),order='F')
    grad = np.matmul(gh_weight, Y_all_center) * sqrt(2)/sqrt(pi)/radius 
    grad = np.squeeze(np.matmul(A, np.expand_dims(grad, axis=1)),axis=1)    
    return grad, (GH_pts-1)*dim
            
#----------------------------------------------------------
# main program
#----------------------------------------------------------

# import parameter 
f_name = setup_param_v2.f_name 
fun_m = setup_param_v2.fun_m
bound = setup_param_v2.bound 
dim = setup_param_v2.dim                    # function dimension
n_iter = setup_param_v2.n_iter              # number of iteration 
GH_pts = setup_param_v2.GH_pts              # number of GH points in each dimension     
x_opt = setup_param_v2.x_opt              # number of GH points in each dimension                     
 
# number of initial samples
n_init = 1          
lb = bound[0] * np.ones(dim)
ub = bound[1] * np.ones(dim)
wi = bound[1] - bound[0]

# The number of trials
num_trial = 20

translation = True
rotation = True
save     = True
radius_rule = 'grad_adapt'  # OPTION: pol_decay, grad_adapt
dir_rule = 'GD'             # OPTION: GD, BFGS
ls_rule  = 'brute_force'    # OPTION: brute_force, Wolfe, pol_decay

#-------------

if radius_rule == 'pol_decay': 
    rr_init = setup_param_v2.rr_init        # starting radius 
    rr_end = setup_param_v2.rr_end          # end radius
    rr_decay = setup_param_v2.rr_decay      # radius decay
    
elif radius_rule == 'grad_adapt': 
    ps = 1        # adjust radius (ps * step). Default: 1 
    pw = 5        # initialize radius (pw * width). Default: 5
    eps = 1e-3      # tolerance of relative update for resetting radius. Default: 1e-3
    res_step = 10   # only reset radius after at least (res_step) iterates. Default: 10 
    
#-------------
    
if ls_rule == 'pol_decay': 
    lr_init = setup_param_v2.lr_init        # starting learning rate 
    lr_end = setup_param_v2.lr_end          # end learning rate 
    lr_decay = setup_param_v2.lr_decay      # learning rate decay
      
elif ls_rule == 'brute_force': 
    tau = 0.9       # decreasing rate for LS. Default: 0.9 
    num_ls = 200    # number of points used for LS. Default: 200 
    
# GH values and weights    
gh = roots_hermite(GH_pts)
gh_value = np.expand_dims(gh[0], axis=1)
gh_weight = gh[1]

# GH point matrix
gh_value_mat = np.zeros((GH_pts*dim, dim))
gh_value_vec = np.zeros(GH_pts*dim)

for i in range(dim):
    gh_value_mat[GH_pts*i:GH_pts*(i+1),i] = gh[0]
    gh_value_vec[GH_pts*i:GH_pts*(i+1)] = gh[0]
    
# main loop 
for itry in range(num_trial):
    
    print('------------------------------')
    print('Trial',itry)
    
    if not(rotation): 
        T = np.eye(dim)
    else: 
        T = special_ortho_group.rvs(dim)
        
    print('Rotation matrix:', T)
    
    if not(translation): 
        lt = np.zeros((1,dim)) 
    else: 
        new_x_opt = np.random.rand(1, dim)
        new_x_opt = from_unit_cube(new_x_opt, lb+0.1*(ub-lb), ub-0.1*(ub-lb))  # new optima lies in a subdomain 
        lt = new_x_opt - x_opt 
    
#    print('Translation vector', lt)
    
    #-------------------------------------------------------------

    # generate initial samples   
    X_init = np.random.rand(n_init, dim)
    X_init = from_unit_cube(X_init, lb, ub)
    fX_init = np.array(RTfun_m(X_init,T,lt,dim))

    # select the minimum point as the starting point 
    fX_init_best = fX_init.min()
    X_init_best = X_init[np.argmin(fX_init),:]
    print('F initial:',fX_init_best)

    f_value = []
    num_eval_array = [0]
    f_value.append(fX_init_best)
    X_center = X_init_best 

    A = np.eye(dim)
    
    # initializing number of function evaluations
    num_eval = 0 
    
    # size of update step. Initialization
    step     = 0
    # relative update. Initialization 
    upd = 0
    rel_upd  = 0 
    # record the reset iteration 
    reset_id = 0 
    # number of reset
    num_reset = 0
    max_num_reset = 5
        
    #...............................................................................#
    for j in range(n_iter):
        
        ############################ update ############################
        #----------radius------------
        if radius_rule == 'pol_decay': 
            rr = (rr_init - rr_end) * (1.0 - (np.float(j)/np.float(n_iter-1)))**rr_decay + rr_end
        elif radius_rule == 'grad_adapt':
            if ((upd==0) or (rel_upd < eps)) and ((j==0) or (j-reset_id >= res_step)):
#            if (step < eps * wi) and ((j==0) or (j-reset_id >= res_step)): 
                rr = random.gauss(pw*wi, 0.1*pw*wi) 
                reset_id = j
                
                num_reset +=1
#                if num_reset > max_num_reset: break
            else: 
                rr = (random.gauss(ps, 0.1*ps)*step + rr)/2
        
        #----------direction------------
        grad, num = DGS_grad(X_center,T,lt,rr)
        num_eval += num 
        norm_grad = np.linalg.norm(grad)
            
        #----------line_search------------
        if ls_rule == 'pol_decay': 
            alpha = (lr_init - lr_end) * (1.0 - (np.float(j)/np.float(n_iter-1)))**lr_decay + lr_end
            xnew = X_center - alpha*grad
            fnew = RTfun_m(np.expand_dims(xnew,axis=0),T,lt,dim)
            
        elif ls_rule == 'brute_force':
            xnew = X_center
            fnew  = RTfun_m(np.expand_dims(xnew,axis=0),T,lt,dim)[0]
            
            # max length of line search: diagonal length of the domain 
            beta = np.sqrt(dim)*wi/(norm_grad+1.e-10) 
            
            for l in range(num_ls):
                xl = np.expand_dims(X_center - grad * beta * (tau**l),axis=0)
                # xl = to_domain(xl, lb, ub) 
                fl = RTfun_m(xl,T,lt,dim)[0]
                if fl < fnew :
                    xnew = xl.flatten()
                    fnew = fl
            
            num_eval += num_ls 
        
        num_eval_array.append(num_eval)                                        
        f_value.append(fnew)
        step = np.linalg.norm(xnew-X_center)
        
        upd = np.abs(f_value[-1] - f_value[-2])
        rel_upd = np.abs(f_value[-1] - f_value[-2])/np.abs(f_value[-2])

        print(j+1, num_eval, fnew, norm_grad, step, rr) 
            
        X_center = xnew
    
#    Xr_opt = np.matmul(X_center,T)
#    
#    print(Xr_opt)
#    
#    if (np.min(Xr_opt - lb) >= 0) and (np.max(Xr_opt - ub) <= 0): 
#        print('Solution is INSIDE search domain')
#    else: 
#        print('Solution is OUTSIDE search domain')
        
    print('optimization is done')
    
    # output to file 
    if save == True: 
        outfile = 'output/RT_bench_func_6000D/' + f_name + '.csv'  
        if path.isfile(outfile) == False: 
            with open(outfile, mode = 'w', newline='') as f: 
                writer = csv.writer(f)
                writer.writerow(num_eval_array)
                writer.writerow(f_value)
        else:
            with open(outfile, mode = 'a', newline='') as f: 
                writer = csv.writer(f)
                writer.writerow(f_value)
        f.close()

    








