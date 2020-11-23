#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 2 08:21:34 2020

@author: htp
"""

import numpy as np
from numpy import pi, sqrt
from scipy.special import roots_hermite
from scipy.stats import special_ortho_group
import numpy.matlib
import random
from getfunc import getfunc  
import argparse
import os
import csv
import datetime

#----------------------------------------------------------
# supporting functions
#----------------------------------------------------------
def from_unit_cube(x, lb, ub):
    """Project from [0, 1]^d to hypercube with bounds lb and ub"""
    assert np.all(lb < ub) and lb.ndim == 1 and ub.ndim == 1 and x.ndim == 2
    xx = x * (ub - lb) + lb
    return xx


#----------------------------------------------------------
# Translated and rotated function and DGS gradient estimators
#----------------------------------------------------------          
def RTfun_m(x,T,lt,dim): 
    return(fun_m(np.matmul(x-lt,T),dim))
        
def DGS_grad(X,T,lt,radius):
    gh_value_mat_rot = np.matmul(gh_value_mat,A.transpose())        
    X_all_center = np.matlib.repmat(X,GH_pts*dim,1) + radius * sqrt(2.0) * gh_value_mat_rot
    Y_all_center = np.reshape(np.multiply(RTfun_m(X_all_center,T,lt,dim), gh_value_vec), (GH_pts, dim),order='F')
    grad = np.matmul(gh_weight, Y_all_center) * sqrt(2)/sqrt(pi)/radius 
    grad = np.squeeze(np.matmul(A, np.expand_dims(grad, axis=1)),axis=1)    
    return grad, (GH_pts-1)*dim
            
#----------------------------------------------------------
# import test function from command line 
#----------------------------------------------------------
    
parser = argparse.ArgumentParser(description='Test AdaDGS on high-dimensional functions')
parser.add_argument('--f_name', default=None, help='function name')
parser.add_argument('--dim', default=1000, type=int, help='dimension (default: 1000)')
parser.add_argument('--n_iter', default=None, type=int, help='number of iterations (default: 10-200 depending on test functions)')
parser.add_argument('--num_trial', default=20, type=int, help='number of trials (default: 20)')
parser.add_argument('--translation', action='store_false', default=True, help='random translation (default: True)')
parser.add_argument('--rotation', action='store_false', default=True, help='random translation (default: True)')
parser.add_argument('--save', action='store_true', default=False, help='save results (default: False)')

args = parser.parse_args()

# import parameter 
f_name      = args.f_name            # function name
dim         = args.dim               # function dimension. Default: 1000
num_trial   = args.num_trial         # number of trials. Default: 20
n_iter_args = args.n_iter            # number of iterations. Default: 10-200 depending on test functions      
save        = args.save              # save results to file. Default: False 
translation = args.translation       # apply random translation to test functions 
rotation    = args.rotation          # apply random rotation to test functions 

# get function, bound, its optimal state and default number of iterations from the function name.  
fun_m, bound, x_opt, n_iter = getfunc(f_name,dim,n_iter_args)   
                                                                    
# number of initial samples
n_init = 1          
lb = bound[0] * np.ones(dim)    # lower boundary
ub = bound[1] * np.ones(dim)    # upper boundary
wi = bound[1] - bound[0]        # domain width

# naming CSV file for saving results. Using current timestamp for file ID 
if save == True: 
    outfile = 'results/' + f_name + str(dim) + '_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'  

#----------------------------------------------------------
# hyperparameters
#----------------------------------------------------------

GH_pts = 5                          # number of GH points per direction

lmax   = np.sqrt(dim)*wi            # maximum search length. Default: diagonal of search domain 
tau    = 0.9                        # contraction rate. Default: 0.9                             
num_ls = int((GH_pts-1)*dim*0.05)   # number of points used for LS. Default: 5% of function evaluations used for computing DGS gradient
                                    # if GH_pts is even, num_ls = int(GH_pts*dim*0.05) 

pw = 5 * wi                         # initial radius. Default: 5 * width
 
eps = 1e-3                          # tolerance of relative update for resetting radius. Default: 1e-3
res_step = 10                       # minimum number of step between radius reset. Default: 10 

#----------------------------------------------------------
# GH values and weights    
#----------------------------------------------------------
gh = roots_hermite(GH_pts)
gh_value = np.expand_dims(gh[0], axis=1)
gh_weight = gh[1]

# GH point matrix
gh_value_mat = np.zeros((GH_pts*dim, dim))
gh_value_vec = np.zeros(GH_pts*dim)

for i in range(dim):
    gh_value_mat[GH_pts*i:GH_pts*(i+1),i] = gh[0]
    gh_value_vec[GH_pts*i:GH_pts*(i+1)] = gh[0]
 
    
#########################################################    
# MAIN LOOP
######################################################### 

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
    
    
    #...............................................................................#
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
    
    num_eval = 0    # number of function evaluations. Initialization
    step     = 0    # size of update step. Initialization
     
    upd = 0         # absolute update. Initialization
    rel_upd  = 0    # relative update. Initialization
    
    reset_id = 0    # last step of radius reset. Initialization

        
    for j in range(n_iter):
        
        #.............................. update ..............................#
        
        #----------radius------------
        if ((upd==0) or (rel_upd < eps)) and ((j==0) or (j-reset_id >= res_step)):
            rr = random.gauss(pw, 0.1*pw) 
            reset_id = j
        else: 
            rr = (step + rr)/2
        
        #----------direction------------
        grad, num = DGS_grad(X_center,T,lt,rr)
        num_eval += num 
        norm_grad = np.linalg.norm(grad)
            
        #----------line_search------------
        xnew = X_center
        fnew  = RTfun_m(np.expand_dims(xnew,axis=0),T,lt,dim)[0]
        
        beta = lmax/(norm_grad+1.e-10) # max learning rate
        
        for l in range(num_ls):
            xl = np.expand_dims(X_center - grad * beta * (tau**l),axis=0)
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
         
    print('optimization is done')
    
    # output to file 
    if save == True: 
        if not os.path.exists('results'):
            os.makedirs('results')
        if not os.path.isfile(outfile): 
            with open(outfile, mode = 'w', newline='') as f: 
                writer = csv.writer(f)
                writer.writerow(num_eval_array)
                writer.writerow(f_value)
        else:
            with open(outfile, mode = 'a', newline='') as f: 
                writer = csv.writer(f)
                writer.writerow(f_value)
        f.close()
       








