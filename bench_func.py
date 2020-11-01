#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:15:48 2020

@author: htp
"""

import numpy as np
from numpy import abs, cos, exp, pi, sin, sqrt, sum, prod
import numpy.matlib
import random

#...............................................................................
def branin_m(x, dim, a = 1.0, b = 5.1/(4.0*pi**2.0), c = 5.0/pi, r = 6.0, s = 10.0, t = 1.0/(8.0*pi)):
    
    y = a * (x[:,1]-b*x[:,0]**2 + c * x[:,0] - r)**2.0 + s *(1.0-t) * cos(x[:,0]) + s 
    
    return y

#...............................................................................
def dropwave_m(x, dim):
    
    y = - (1.0 + cos(12.0 * sqrt(x[:,0]**2 + x[:,1]**2))) / (0.5 * (x[:,0]**2+x[:,1]**2) + 2.0)
    
    return y

#...............................................................................
def cross_tray_m(x, dim):
    
#     y = -0.0001 * (abs(sin(x[:,0])*sin(x[:,1])*exp(abs(100.0-sqrt(x[:,0]**2+x[:,1]**2)/pi))))+1.0)**0.1
    
    y = -0.0001 * (abs(sin(x[:,1])*sin(x[:,0])*exp(abs(100.0-sqrt(x[:,0]**2+x[:,1]**2)/pi)))+1.0)**0.1
    
    return y

#...............................................................................
def sphere_m(x, dim):
    y = sum( x**2, axis=1)
    return y

#...............................................................................
def sum_square_m(x, dim):
    y = 0
    for i in range(dim):
        y = y + i * x[:,i]**2 
    return y

#...............................................................................
def ackley_m( x, dim, a=20, b=0.2, c=2*pi ):
    
    """     10 ackley test function
            input bounds:  -32.768 <= xi <= 32.768, i = 1..10
            global optimum: (0),
            min function value = 0
    """
    x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
    #     n = len(x)
    n = dim
    s1 = sum( x**2, axis=1)
    s2 = sum( cos( c * x ), axis=1)
    y = -a*exp( -b*sqrt( s1 / n )) - exp( s2 / n ) + a + exp(1)
    return 1.0*y

#...............................................................................
def re_ackley_m( x, dim, a=20, b=0.2, c=2*pi ):
    
    """     10 ackley test function
            input bounds:  -32.768 <= xi <= 32.768, i = 1..10
            global optimum: (0),
            min function value = 0
    """
    x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
    #     n = len(x)
    n = dim
    s1 = sum( x**2, axis=1)
    s2 = sum( cos( c * x ), axis=1)
    y = -a*exp( -b*sqrt( s1 / n )) - exp( s2 / n ) + a + exp(1)
    return 100.0*y

#...............................................................................
def levy_m( x, dim):
    
    """     10 Levy test function
            input bounds:  -10 <= xi <= 10, i = 1..10
            global optimum: (1),
            min function value = 0
    """
    x = np.asarray_chkfinite(x)
    #     n = len(x)
    z = 1 + (x - 1) / 4
    return (sin( pi * z[:,0] )**2
        + sum( (z[:,:-1] - 1)**2 * (1 + 10 * sin( pi * z[:,:-1] + 1 )**2 ), axis=1)
        +       (z[:,-1] - 1)**2 * (1 + sin( 2 * pi * z[:,-1] )**2 ))

#...............................................................................
def rastrigin_m( x , dim):
        
    """     10 Rastrigin test function
            input bounds:  -5.12 <= xi <= 5.12, i = 1..10
            global optimum: (0),
            min function value = 0
    """
    x = np.asarray_chkfinite(x)
    #     n = len(x)
    n = dim
    return 10*n + sum( x**2 - 10 * cos( 2 * pi * x ), axis=1)


#...............................................................................
def hyperellipsoid_m(x, dim):
    y = 0
    for i in range(dim):
        y = y + (10 ** i) * x[:,i]**2 
    return y 


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
def schwefel_m(x,dim): 
    y = 0
    for i in range(dim):
    	xi = x[:,i]
    	y = y + xi*sin(sqrt(abs(xi)))
    y = 418.9829*dim - y;y
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
def shubert3_m(x, dim): 
    return sum(sin(2*x+1) + 2*sin(3*x+2) + 3*sin(4*x+3) + 4*sin(5*x+4) + 5*sin(6*x+5), axis=1)
 
#...............................................................................
def styblinski_m(x, dim):     
    return 0.5*sum(x**4 - 16*x**2 + 5*x, axis=1)

#...............................................................................
def bentcigar_m(x, dim):     
    for i in range(1,dim): 
        x[:,i] = 10**3 * x[:,i]
    return sum(x**2, axis=1)

#...............................................................................
def sharp_ridge_m(x, dim):
    s = sum(x[:,1:]**2, axis=1)
    return (x[:,0]**2 + 100*sqrt(s))

#...............................................................................
def solomon_m(x, dim): 
    s = sqrt(sum(x**2, axis=1)) 
    return (1-cos(2*pi*s)) + 0.1*s

#...............................................................................
def diffpower_m(x, dim): 
    y = 0 
    for i in range(dim): 
        y += abs(x[:,i])**(2+4*i/(dim-1))
    return sqrt(y)

#...............................................................................
def weierstrass_m(x, dim): 
    y = 0
    kmax = 20
    a = 0.5 
    b = 3
    for k in range(kmax+1): 
        y += sum((a**k) * cos(2*pi*(b**k)*(x+0.5))  - (a**k) * cos(pi*(b**k)),axis=1)      
    return y

#...............................................................................
def wavy_m(x, dim):     
    k = 10
    return 1 - sum(cos(k*x)*exp(-x**2/2), axis=1)/dim

#...............................................................................
def michalewicz_m(x,dim): 
    m = 10
    y = 0
    for i in range(dim):
        y += -sin(x[:,i])*(sin((i+1)*x[:,i]**2/pi))**(2*m)
    return y

#...............................................................................
def mishra_m(x,dim): 
    am = sum(abs(x),axis=1)/dim
    gm = prod(abs(x),axis=1)**(1/dim)
    return (am-gm)**2

#...............................................................................
def langermann_m(x,dim):
    m = 5 
    random.seed(1)
    a = [[random.randint(1,10) for _ in range(dim)] for _ in range(m)]
    random.seed()
    c = [1,2,5,2,3]
    y = 0
    for i in range(m): 
        xi = x-np.matlib.repmat(np.array(a[i][:]),np.shape(x)[0],1)
        s = sum(xi**2,axis=1)
        y += c[i] * exp(-s/pi) * cos(pi*s)
    return y

#...............................................................................
def powell_m(x,dim):
    y = sum((x[:,0::4] + 10*x[:,1::4])**2 + 5*(x[:,2::4]-x[:,3::4])**2 + (x[:,1::4]-2*x[:,2::4])**4 + 10*(x[:,0::4]-x[:,3::4])**4,axis=1)
    return y

#...............................................................................
def deb_m(x,dim): 
    return -sum((sin(5*pi*x))**6,axis=1)/dim
        