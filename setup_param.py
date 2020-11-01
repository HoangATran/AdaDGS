#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
"""
Created on Tue Aug 18 23:46:07 2020

@author: htp
"""

import bench_func
from cma import bbobbenchmarks as bn
import numpy as np
from numpy import pi

test_fun = 3

# Choose the test function accroding to the list. The preferred hyper-parameters are included in each case. 

#------------------------------
#----- 2000D functions ------

# 1: Sphere
# 2: Rastrigin
# 3: Ackley
# 4: Schwefel 
# 5: Schaffer
# 6: Ellipsoidal
# 7: Rosenbrock
# 8: Trigonometric
# 9: Quintic 
# 10: Alpine
# 11: Shubert
# 12: Styblinsky-Tang
# 13: BentCigar
# 14: SharpRidge
# 15: Solomon
# 16: Different Powers
# 17: Weierstrass
# 18: wavy
# 19: Michalewicz
# 20: Mishra 11
# 21: Langermann
# 22: Powell
# 23: Deb


#------------------------------
#----- 1000D functions ------

# 101-123

#-----------------------------------
#----- BBOB noiseless functions -----
#--run with [...]_BBOB.py file only --

#1001: Sphere 
#1002: Ellipsoidal
#1003: Rastrigin
#1004: Buche-Rastrigin
#1005: Linear Slope
#1006: Attractive Sector
#1007: Step Ellipsoidal
#1008: Rosenbrock,original
#1009: Rosenbrock,rotated 
#1010: Ellipsoidal,rotated 
#1011: Discus
#1012: Bent Cigar 
#1013: Sharp Ridge
#1014: Different Powers
#1015: Rastrigin, rotated
#1016: Weierstrass
#1017: Schaffers F7 
#1018: Schaffers F7,moderately ill-conditioned 
#1019: Composite Griewank-Rosenbrock 
#1020: Schwefel
#1021: Gallagher’s Gaussian 101-me Peaks
#1022: Gallagher’s Gaussian 21-hi Peaks
#1023: Katsuura 
#1024: Lunacek bi-Rastrigin

if test_fun == 1:
    f_name = 'Sphere2000D'
    fun_m = bench_func.sphere_m
    bound = [-5.12, 5.12] 
    dim = 2000
    n_iter = 10
    GH_pts = 5
    lr_init = 1.0        
    lr_end = 0.01           
    rr_init = 1        
    rr_end = 0.0001          
    lr_decay = 2      
    rr_decay = 2   
    x_opt = np.zeros((1,dim))  
        
elif test_fun == 2:
    f_name = 'Rastrigin6000D'
    fun_m = bench_func.rastrigin_m
    bound = [-5.12, 5.12]
    dim = 6000
#    GH_pts = 21
    GH_pts = 5
    lr_init = 0.5        
    lr_end = 0.001
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.5          
    rr_decay = 2      
#    n_iter = 20
    n_iter = 50
    x_opt = np.zeros((1,dim))
        
elif test_fun == 3:
    f_name = 'ackley6000D'
    fun_m = bench_func.ackley_m
    bound = [-32.5, 32.5]
    dim = 6000                   
#    GH_pts = 3
#    lr_init = 8000        
#    lr_end = 0.001
#    lr_decay = 4           
#    rr_init = 2        
#    rr_end = 0.001          
#    rr_decay = 2 
    GH_pts = 5
    lr_init = 6.5
    lr_end = 0.065
    lr_decay = 2           
    rr_init = 6.5        
    rr_end = 0.065          
    rr_decay = 2   
    n_iter = 50
    x_opt = np.zeros((1,dim))  

elif test_fun == 4: 
    f_name = 'Schwefel2000D'
    fun_m = bench_func.schwefel_m
    bound = [-500., 500.] 
    dim = 2000
    GH_pts = 5
    lr_init = 10        
    lr_end = 1
    lr_decay = 1           
    rr_init = 1        
    rr_end = 0.1          
    rr_decay = 2      
    n_iter = 60
    x_opt = 420.9687*np.ones((1,dim))
    
elif test_fun == 5: 
    f_name = 'Schaffer2000D'
    fun_m = bench_func.schaffer_m
    bound = [-100., 100.] 
    dim = 2000
    GH_pts = 5
    lr_init = 5        
    lr_end = 0.001
    lr_decay = 1           
    rr_init = 50        
    rr_end = 0.001          
    rr_decay = 2      
    n_iter = 70
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 6: 
    f_name = 'Ellipsoidal2000D'
    fun_m = bench_func.ellipsoidal_m
    bound = [-2., 2.] 
    dim = 2000
    GH_pts = 5
    lr_init = 0.4        
    lr_end = 0.004
    lr_decay = 2           
    rr_init = 0.4        
    rr_end = 0.004          
    rr_decay = 2     
    n_iter = 300
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 7:
    f_name = 'Rosenbrock2000D'
    fun_m = bench_func.rosenbrock_m
    bound = [-5., 10.] 
    dim = 2000
    GH_pts = 5
    lr_init = 1.5        
    lr_end = 0.15
    lr_decay = 2           
    rr_init = 1.5        
    rr_end = 0.15          
    rr_decay = 4      
    n_iter = 50
    x_opt = np.ones((1,dim))
    
elif test_fun == 8:
    f_name = 'Trigonometric2000D' 
    fun_m = bench_func.trigonometric2_m
    bound = [-500, 500]
    dim = 2000
    GH_pts = 5
    lr_init = 100        
    lr_end = 1
    lr_decay = 2           
    rr_init = 100        
    rr_end = 1          
    rr_decay = 2      
    n_iter = 40
    x_opt = 0.9*np.ones((1,dim))

elif test_fun == 9:
    f_name = 'Quintic2000D' 
    fun_m = bench_func.quintic_m
    bound = [-10, 10]
    dim = 2000
    GH_pts = 5
    lr_init = 2        
    lr_end = 0.02
    lr_decay = 2           
    rr_init = 2        
    rr_end = 0.02          
    rr_decay = 2      
    n_iter = 120
    x_opt = -np.ones((1,dim))

elif test_fun == 10:
    f_name = 'Alpine2000D' 
    fun_m = bench_func.alpine_m
    bound = [-10, 10]
    dim = 2000
    GH_pts = 5
    lr_init = 2        
    lr_end = 0.02
    lr_decay = 2           
    rr_init = 2        
    rr_end = 0.02          
    rr_decay = 2      
    n_iter = 120
    x_opt = np.zeros((1,dim))  

elif test_fun == 11:
    f_name = 'Shubert2000D' 
    fun_m = bench_func.shubert3_m
    bound = [-10, 10]
    dim = 2000
    GH_pts = 5
    lr_init = 2        
    lr_end = 0.02
    lr_decay = 2           
    rr_init = 2        
    rr_end = 0.02          
    rr_decay = 2      
    n_iter = 70
    x_opt = -1.11409*np.ones((1,dim))
    
elif test_fun == 12:
    f_name = 'Styblinsky2000D' 
    fun_m = bench_func.styblinski_m
    bound = [-5, 5]
    dim = 2000
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 40
    x_opt = -2.903534*np.ones((1,dim))

elif test_fun == 13:
    f_name = 'BentCigar2000D' 
    fun_m = bench_func.bentcigar_m
    bound = [-100, 100]
    dim = 2000
    GH_pts = 5
    lr_init = 20        
    lr_end = 0.2
    lr_decay = 2           
    rr_init = 20        
    rr_end = 0.2          
    rr_decay = 2      
    n_iter = 50
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 14:
    f_name = 'SharpRidge2000D' 
    fun_m = bench_func.sharp_ridge_m
    bound = [-10, 10]
    dim = 2000
    GH_pts = 5
    lr_init = 0.4        
    lr_end = 0.0001
    lr_decay = 3           
    rr_init = 0.5        
    rr_end = 0.1          
    rr_decay = 0.5      
    n_iter = 50
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 15:
    f_name = 'Solomon2000D' 
    fun_m = bench_func.solomon_m
    bound = [-100, 100]
    dim = 2000
    GH_pts = 5
    lr_init = 20        
    lr_end = 0.2
    lr_decay = 2           
    rr_init = 20        
    rr_end = 0.2          
    rr_decay = 2      
    n_iter = 60
    x_opt = np.zeros((1,dim))  

elif test_fun == 16:
    f_name = 'DifferentPowers2000D' 
    fun_m = bench_func.diffpower_m
    bound = [-5, 5]
    dim = 2000
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 17:
    f_name = 'Weierstrass2000D' 
    fun_m = bench_func.weierstrass_m
    bound = [-.5, .5]
    dim = 2000
    GH_pts = 5
    lr_init = 0.1        
    lr_end = 0.001
    lr_decay = 2           
    rr_init = 0.1        
    rr_end = 0.001          
    rr_decay = 2      
    n_iter = 80
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 18:
    f_name = 'Wavy2000D' 
    fun_m = bench_func.wavy_m
    bound = [-pi, pi]
    dim = 2000
    GH_pts = 5
    lr_init = pi/5        
    lr_end = pi/500
    lr_decay = 2           
    rr_init = pi/5        
    rr_end = pi/500          
    rr_decay = 2      
    n_iter = 60
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 19:
    f_name = 'Michalewicz2000D' 
    fun_m = bench_func.michalewicz_m
    bound = [0, pi]
    dim = 2000
    GH_pts = 5
    lr_init = pi/10        
    lr_end = pi/1000
    lr_decay = 2           
    rr_init = pi/10        
    rr_end = pi/1000          
    rr_decay = 2      
    n_iter = 100
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 20:
    f_name = 'Mishra2000D' 
    fun_m = bench_func.mishra_m
    bound = [-3, 3]
    dim = 2000
    GH_pts = 5
    lr_init = 0.6      
    lr_end = 0.006
    lr_decay = 2           
    rr_init = 0.6        
    rr_end = 0.006          
    rr_decay = 2      
    n_iter = 100
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 21:
    f_name = 'Langermann2000D' 
    fun_m = bench_func.langermann_m
    bound = [0, 10]
    dim = 2000
    GH_pts = 5
    lr_init = 1      
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 22:
    f_name = 'Powell2000D' 
    fun_m = bench_func.powell_m
    bound = [-4, 5]
    dim = 2000
    GH_pts = 5
    lr_init = 0.9      
    lr_end = 0.009
    lr_decay = 2           
    rr_init = 0.9       
    rr_end = 0.009          
    rr_decay = 2      
    n_iter = 200
    x_opt = np.zeros((1,dim))  
    
elif test_fun == 23:
    f_name = 'Deb2000D' 
    fun_m = bench_func.deb_m
    bound = [-1, 1]
    dim = 2000
    GH_pts = 5
    lr_init = 0.2      
    lr_end = 0.002
    lr_decay = 2           
    rr_init = 0.2      
    rr_end = 0.002          
    rr_decay = 2      
    n_iter = 60
    x_opt = np.zeros((1,dim))  

#-------------------------------------------------------
      
if test_fun == 101:
    f_name = 'Sphere1000D'
    fun_m = bench_func.sphere_m
    bound = [-5.12, 5.12] 
    dim = 1000
    n_iter = 500
    GH_pts = 5
    lr_init = 1.0        
    lr_end = 0.01           
    rr_init = 1        
    rr_end = 0.0001          
    lr_decay = 2      
    rr_decay = 2      
    n_iter = 30
    x_opt = np.zeros((1,dim))
  
        
elif test_fun == 102:
    f_name = 'Rastrigin1000D'
    fun_m = bench_func.rastrigin_m
    bound = [-5.12, 5.12]
    dim = 1000
#    GH_pts = 21
    GH_pts = 5
    lr_init = 0.5        
    lr_end = 0.001
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.5          
    rr_decay = 2      
#    n_iter = 20
    n_iter = 50
    x_opt = np.zeros((1,dim))
        
elif test_fun == 103:
    f_name = 'ackley1000D'
    fun_m = bench_func.ackley_m
    bound = [-32.5, 32.5]
    dim = 1000                   
#    GH_pts = 3
#    lr_init = 8000        
#    lr_end = 0.001
#    lr_decay = 4           
#    rr_init = 2        
#    rr_end = 0.001          
#    rr_decay = 2 
    GH_pts = 5
    lr_init = 6.5
    lr_end = 0.065
    lr_decay = 2           
    rr_init = 6.5        
    rr_end = 0.065          
    rr_decay = 2   
    n_iter = 50
    x_opt = np.zeros((1,dim))


elif test_fun == 104: 
    f_name = 'Schwefel1000D'
    fun_m = bench_func.schwefel_m
    bound = [-500., 500.] 
    dim = 1000
    GH_pts = 5
    lr_init = 10        
    lr_end = 1
    lr_decay = 1           
    rr_init = 1        
    rr_end = 0.1          
    rr_decay = 2      
    n_iter = 50
    x_opt = 420.9687*np.ones((1,dim))

    
elif test_fun == 105: 
    f_name = 'Schaffer1000D'
    fun_m = bench_func.schaffer_m
    bound = [-100., 100.] 
    dim = 1000
    GH_pts = 5
    lr_init = 5        
    lr_end = 0.001
    lr_decay = 1           
    rr_init = 50        
    rr_end = 0.001          
    rr_decay = 2      
    n_iter = 100
    x_opt = np.zeros((1,dim))

    
elif test_fun == 106: 
    f_name = 'Ellipsoidal1000D'
    fun_m = bench_func.ellipsoidal_m
    bound = [-2., 2.] 
    dim = 1000
    GH_pts = 5
    lr_init = 0.4        
    lr_end = 0.004
    lr_decay = 2           
    rr_init = 0.4        
    rr_end = 0.004          
    rr_decay = 2     
    n_iter = 300
    x_opt = np.zeros((1,dim))
    
elif test_fun == 107:
    f_name = 'Rosenbrock1000D'
    fun_m = bench_func.rosenbrock_m
    bound = [-5., 10.] 
    dim = 1000
    GH_pts = 5
    lr_init = 1.5        
    lr_end = 0.15
    lr_decay = 2           
    rr_init = 1.5        
    rr_end = 0.15          
    rr_decay = 4      
    n_iter = 60
    x_opt = np.ones((1,dim))
    
elif test_fun == 108:
    f_name = 'Trigonometric1000D' 
    fun_m = bench_func.trigonometric2_m
    bound = [-500, 500]
    dim = 1000
    GH_pts = 5
    lr_init = 100        
    lr_end = 1
    lr_decay = 2           
    rr_init = 100        
    rr_end = 1          
    rr_decay = 2      
    n_iter = 50
    x_opt = 0.9*np.ones((1,dim))

elif test_fun == 109:
    f_name = 'Quintic1000D' 
    fun_m = bench_func.quintic_m
    bound = [-10, 10]
    dim = 1000
    GH_pts = 5
    lr_init = 2        
    lr_end = 0.02
    lr_decay = 2           
    rr_init = 2        
    rr_end = 0.02          
    rr_decay = 2      
    n_iter = 120
    x_opt = -np.ones((1,dim))

elif test_fun == 110:
    f_name = 'Alpine1000D' 
    fun_m = bench_func.alpine_m
    bound = [-10, 10]
    dim = 1000
    GH_pts = 5
    lr_init = 2        
    lr_end = 0.02
    lr_decay = 2           
    rr_init = 2        
    rr_end = 0.02          
    rr_decay = 2      
    n_iter = 150
    x_opt = np.zeros((1,dim))

elif test_fun == 111:
    f_name = 'Shubert1000D' 
    fun_m = bench_func.shubert3_m
    bound = [-10, 10]
    dim = 1000
    GH_pts = 5
    lr_init = 2        
    lr_end = 0.02
    lr_decay = 2           
    rr_init = 2        
    rr_end = 0.02          
    rr_decay = 2      
    n_iter = 60
    x_opt = -1.11409*np.ones((1,dim))
    
elif test_fun == 112:
    f_name = 'Styblinsky1000D' 
    fun_m = bench_func.styblinski_m
    bound = [-5, 5]
    dim = 1000
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 60
    x_opt = -2.903534*np.ones((1,dim))
    
    
elif test_fun == 113:
    f_name = 'BentCigar1000D' 
    fun_m = bench_func.bentcigar_m
    bound = [-100, 100]
    dim = 1000
    GH_pts = 5
    lr_init = 20        
    lr_end = 0.2
    lr_decay = 2           
    rr_init = 20        
    rr_end = 0.2          
    rr_decay = 2      
    n_iter = 50
    x_opt = np.zeros((1,dim))

elif test_fun == 114:
    f_name = 'SharpRidge1000D' 
    fun_m = bench_func.sharp_ridge_m
    bound = [-10, 10]
    dim = 1000
    GH_pts = 5
    lr_init = 2        
    lr_end = 0.02
    lr_decay = 2           
    rr_init = 2        
    rr_end = 0.02          
    rr_decay = 2      
    n_iter = 50
    x_opt = np.zeros((1,dim))

elif test_fun == 115:
    f_name = 'Solomon1000D' 
    fun_m = bench_func.solomon_m
    bound = [-100, 100]
    dim = 1000
    GH_pts = 5
    lr_init = 20        
    lr_end = 0.2
    lr_decay = 2           
    rr_init = 20        
    rr_end = 0.2          
    rr_decay = 2      
    n_iter = 60
    x_opt = np.zeros((1,dim))
    
elif test_fun == 116:
    f_name = 'DifferentPowers1000D' 
    fun_m = bench_func.diffpower_m
    bound = [-5, 5]
    dim = 1000
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    x_opt = np.zeros((1,dim))
    
elif test_fun == 117:
    f_name = 'Weierstrass1000D' 
    fun_m = bench_func.weierstrass_m
    bound = [-.5, .5]
    dim = 1000
    GH_pts = 5
    lr_init = 0.1        
    lr_end = 0.001
    lr_decay = 2           
    rr_init = 0.1        
    rr_end = 0.001          
    rr_decay = 2      
    n_iter = 80
    x_opt = np.zeros((1,dim))
    
elif test_fun == 118:
    f_name = 'Wavy1000D' 
    fun_m = bench_func.wavy_m
    bound = [-pi, pi]
    dim = 1000
    GH_pts = 5
    lr_init = pi/5        
    lr_end = pi/500
    lr_decay = 2           
    rr_init = pi/5        
    rr_end = pi/500          
    rr_decay = 2      
    n_iter = 60
    x_opt = np.zeros((1,dim))
    
elif test_fun == 119:
    f_name = 'Michalewicz1000D' 
    fun_m = bench_func.michalewicz_m
    bound = [0, pi]
    dim = 1000
    GH_pts = 5
    lr_init = pi/10        
    lr_end = pi/1000
    lr_decay = 2           
    rr_init = pi/10        
    rr_end = pi/1000          
    rr_decay = 2      
    n_iter = 70
    x_opt = np.zeros((1,dim))  # un-identified
    
elif test_fun == 120:
    f_name = 'Mishra1000D' 
    fun_m = bench_func.mishra_m
    bound = [-3, 3]
    dim = 1000
    GH_pts = 5
    lr_init = 0.6      
    lr_end = 0.006
    lr_decay = 2           
    rr_init = 0.6        
    rr_end = 0.006          
    rr_decay = 2      
    n_iter = 30
    x_opt = np.zeros((1,dim))

elif test_fun == 121:
    f_name = 'Langermann1000D' 
    fun_m = bench_func.langermann_m
    bound = [0, 10]
    dim = 1000
    GH_pts = 5
    lr_init = 1      
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    x_opt = np.zeros((1,dim))  # un-identified
    
elif test_fun == 122:
    f_name = 'Powell1000D' 
    fun_m = bench_func.powell_m
    bound = [-4, 5]
    dim = 1000
    GH_pts = 5
    lr_init = 0.9      
    lr_end = 0.009
    lr_decay = 2           
    rr_init = 0.9       
    rr_end = 0.009          
    rr_decay = 2      
    n_iter = 200
    x_opt = np.zeros((1,dim))
    
elif test_fun == 123:
    f_name = 'Deb1000D' 
    fun_m = bench_func.deb_m
    bound = [-1., 1.]
    dim = 1000
    GH_pts = 5
    lr_init = 0.2      
    lr_end = 0.002
    lr_decay = 2           
    rr_init = 0.2       
    rr_end = 0.002          
    rr_decay = 2      
    n_iter = 60
    x_opt = np.zeros((1,dim))   # periodic
    
#-------------------------------------------------------

elif test_fun == 1001: 
    f_name = 'F1-Sphere-' 
    fun_m = bn.F1
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1002: 
    f_name = 'F2-Ellipsoidal-' 
    fun_m = bn.F2
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1003: 
    f_name = 'F3-Rastrigin-' 
    fun_m = bn.F3
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100

elif test_fun == 1004: 
    f_name = 'F4-BucheRastrgin-' 
    fun_m = bn.F4
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1005: 
    f_name = 'F5-LinearSlope-' 
    fun_m = bn.F5
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1006: 
    f_name = 'F6-AttractiveSector-' 
    fun_m = bn.F6
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1007: 
    f_name = 'F7-StepEllipsoidal-' 
    fun_m = bn.F7
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1008: 
    f_name = 'F8-Rosenbrock_orig-' 
    fun_m = bn.F8
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1009: 
    f_name = 'F9-Rosenbrock_rotated-' 
    fun_m = bn.F9
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1010: 
    f_name = 'F10-Ellipsoidal-' 
    fun_m = bn.F10
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100

elif test_fun == 1011: 
    f_name = 'F11-Discus-' 
    fun_m = bn.F11
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1012: 
    f_name = 'F12-BentCigar-' 
    fun_m = bn.F12
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1013: 
    f_name = 'F13-SharpRidge-' 
    fun_m = bn.F13
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1014: 
    f_name = 'F14-DifferentPowers-' 
    fun_m = bn.F14
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1015: 
    f_name = 'F15-Rastrigin-' 
    fun_m = bn.F15
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1016: 
    f_name = 'F16-Weierstrass-' 
    fun_m = bn.F16
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1017: 
    f_name = 'F17-SchaffersF7-' 
    fun_m = bn.F17
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1018: 
    f_name = 'F18-SchafferF7_illcon-' 
    fun_m = bn.F18
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1019: 
    f_name = 'F19-GriewankRosenbrock-' 
    fun_m = bn.F19
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1020: 
    f_name = 'F20-Schwefel-' 
    fun_m = bn.F20
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1021: 
    f_name = 'F21-Gaussian101me-' 
    fun_m = bn.F21
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1022: 
    f_name = 'F22-Gaussian21hi-' 
    fun_m = bn.F22
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1023: 
    f_name = 'F23-Katsuura-' 
    fun_m = bn.F23
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
elif test_fun == 1024: 
    f_name = 'F24-Lunacek_biRastrigin-' 
    fun_m = bn.F24
    bound = [-5, 5]
    GH_pts = 5
    lr_init = 1        
    lr_end = 0.01
    lr_decay = 2           
    rr_init = 1        
    rr_end = 0.01          
    rr_decay = 2      
    n_iter = 100
    
    
