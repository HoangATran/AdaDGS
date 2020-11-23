#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:15:48 2020

@author: htp
"""

import numpy as np
from numpy import abs, cos, exp, pi, sin, sqrt, sum
import numpy.matlib

#...............................................................................
def sphere_m(x, dim):
    y = sum( x**2, axis=1)
    return y

#...............................................................................
def ackley_m( x, dim, a=20, b=0.2, c=2*pi ):
    x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
    #     n = len(x)
    n = dim
    s1 = sum( x**2, axis=1)
    s2 = sum( cos( c * x ), axis=1)
    y = -a*exp( -b*sqrt( s1 / n )) - exp( s2 / n ) + a + exp(1)
    return 1.0*y


#...............................................................................
def rastrigin_m( x , dim):        
    x = np.asarray_chkfinite(x)
    #     n = len(x)
    n = dim
    return 10*n + sum( x**2 - 10 * cos( 2 * pi * x ), axis=1)

#...............................................................................
def rosenbrock_m(x, dim):
    y = 0
    # for i in range(dim-1):
    #     xi = x[:,i]
    #     xt = x[:,i+1]
    #     y = y + 100*(xt-xi**2)**2 + (xi-1)**2
    y = sum(100*(x[:,1:dim] - x[:,0:dim-1]**2)**2 + (x[:,0:dim-1]-1)**2, axis=1)

    return y

#...............................................................................
def schaffer_m(x, dim):
    y = 0
    for i in range(dim-1):
        xi = x[:,i]
        xt = x[:,i+1]
        s = sqrt(xi**2 + xt**2)
        y = y + sqrt(s) + sqrt(s)*(sin(50*np.power(s,0.2)))**2
    y = y**2/(dim-1)
    return y

#...............................................................................
def ellipsoidal_m(x,dim):
    mat = np.arange(dim)
    mat = np.matlib.repmat(mat,np.shape(x)[0],1)
    return sum((10**(6*mat/(dim-1))) * (x**2), axis =1)

#...............................................................................
def trigonometric2_m(x, dim): 
    y = 1 + sum(8*(sin(7*(x - 0.9)**2))**2 + 6*(sin(14*(x - 0.9)**2))**2 + (x- 0.9)**2, axis=1)
    return y

#...............................................................................
def quintic_m(x, dim): 
    return sum(abs(x**5 - 3*x**4 + 4*x**3 + 2*x**2 - 10*x - 4), axis=1)

#...............................................................................
def alpine_m(x, dim): 
    return sum(abs(x*sin(x) + 0.1*x), axis=1)

#...............................................................................
def styblinski_m(x, dim):     
    return 0.5*sum(x**4 - 16*x**2 + 5*x, axis=1)

#...............................................................................
def sharp_ridge_m(x, dim):
    s = sum(x[:,1:]**2, axis=1)
    return (x[:,0]**2 + 100*sqrt(s))

#...............................................................................
def salomon_m(x, dim): 
    s = sqrt(sum(x**2, axis=1)) 
    return (1-cos(2*pi*s)) + 0.1*s

#...............................................................................
def wavy_m(x, dim):     
    k = 10
    return 1 - sum(cos(k*x)*exp(-x**2/2), axis=1)/dim


        