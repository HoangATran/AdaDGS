## Directional Gaussian smoothing (DGS) for blackbox optimization
This repository contains Python code for testing Directional Gaussian smoothing (DGS) method on high-dimensional benchmark functions. This method was first introduced in the paper [*A Novel Evolution Strategy with Directional Gaussian Smoothing for Blackbox Optimization*](https://arxiv.org/pdf/2002.03001.pdf) by Jiaxin Zhang, Hoang Tran, Dan Lu and Guannan Zhang. 

### Features
- Directionally smoothing objective functions with Gaussian kernel for nonlocal exploration in each direction  
- Gauss-Hermite quadrature for approximating DGS gradient
- Backtracking line search for adaptively updating smoothing radius and step size 
- (Optional) Random generation of smoothing directions to enhance exploration 

### Benchmark functions 

The functions listed below are some of the common functions and datasets used for testing optimization algorithms. They are grouped according to similarities in their significant physical properties and shapes. Each page contains information about the corresponding function or dataset, as well as MATLAB and R implementations. 

### Related papers 

1. J. Zhang, H. Tran, D. Lu, G. Zhang, [A Novel Evolution Strategy with Directional Gaussian Smoothing for Blackbox Optimization](https://arxiv.org/pdf/2002.03001.pdf), submitted, 2020. 
2. H. Tran, G. Zhang, AdaDGS: An adaptive black-box optimization method with a nonlocal directional Gaussian smoothing gradient, submitted, 2020.
