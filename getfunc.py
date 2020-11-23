#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:00:21 2020

@author: htp
"""

import numpy as np
import bench_func
from numpy import pi

def getfunc(f_name,dim,n_iter_args): 
    if f_name.lower() == 'sphere':
        fun_m = bench_func.sphere_m
        bound = [-5.12, 5.12] 
        x_opt = np.zeros((1,dim))  
        n_iter=10 if n_iter_args is None else n_iter_args
                        
            
    elif f_name.lower() == 'rastrigin':
        fun_m = bench_func.rastrigin_m
        bound = [-5.12, 5.12]
        x_opt = np.zeros((1,dim))
        n_iter=50 if n_iter_args is None else n_iter_args

            
    elif f_name.lower() == 'ackley':    
        fun_m = bench_func.ackley_m
        bound = [-32.5, 32.5]
        x_opt = np.zeros((1,dim))
        n_iter=50 if n_iter_args is None else n_iter_args

        
    elif f_name.lower() == 'schaffer': 
        fun_m = bench_func.schaffer_m
        bound = [-100., 100.] 
        x_opt = np.zeros((1,dim))
        n_iter=70 if n_iter_args is None else n_iter_args
        
        
    elif f_name.lower() == 'ellipsoidal':
        fun_m = bench_func.ellipsoidal_m
        bound = [-2., 2.] 
        x_opt = np.zeros((1,dim))  
        n_iter=200 if n_iter_args is None else n_iter_args
        
        
    elif f_name.lower() == 'rosenbrock':
        fun_m = bench_func.rosenbrock_m
        bound = [-5., 10.] 
        x_opt = np.ones((1,dim))
        n_iter=50 if n_iter_args is None else n_iter_args


        
    elif f_name.lower() == 'trigonometric':
        fun_m = bench_func.trigonometric2_m
        bound = [-500, 500]
        x_opt = 0.9*np.ones((1,dim))
        n_iter=40 if n_iter_args is None else n_iter_args

    
    elif f_name.lower() == 'quintic':
        fun_m = bench_func.quintic_m
        bound = [-10, 10] 
        x_opt = -np.ones((1,dim))
        n_iter=120 if n_iter_args is None else n_iter_args

    
    elif f_name.lower() == 'alpine':
        fun_m = bench_func.alpine_m
        bound = [-10, 10]
        x_opt = np.zeros((1,dim)) 
        n_iter=120 if n_iter_args is None else n_iter_args

       
    elif f_name.lower() == 'styblinsky':
        fun_m = bench_func.styblinski_m
        bound = [-5, 5]     
        x_opt = -2.903534*np.ones((1,dim))
        n_iter=40 if n_iter_args is None else n_iter_args

     
    elif f_name.lower() == 'sharpridge':
        fun_m = bench_func.sharp_ridge_m
        bound = [-10, 10]    
        x_opt = np.zeros((1,dim))  
        n_iter=50 if n_iter_args is None else n_iter_args
        
        
    elif f_name.lower() == 'salomon':
        fun_m = bench_func.salomon_m
        bound = [-100, 100]
        x_opt = np.zeros((1,dim)) 
        n_iter=60 if n_iter_args is None else n_iter_args

        
    elif f_name.lower() == 'wavy':
        fun_m = bench_func.wavy_m
        bound = [-pi, pi]     
        x_opt = np.zeros((1,dim)) 
        n_iter=60 if n_iter_args is None else n_iter_args

    return fun_m, bound, x_opt, n_iter
