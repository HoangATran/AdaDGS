## AdaDGS: Adaptive blackbox optimization method with directional Gaussian smoothing gradient 
This repository contains Python code for testing Directional Gaussian smoothing (DGS) method on high-dimensional benchmark functions. This method was first introduced in the paper [*A Novel Evolution Strategy with Directional Gaussian Smoothing for Blackbox Optimization*](https://arxiv.org/pdf/2002.03001.pdf) by Jiaxin Zhang, Hoang Tran, Dan Lu and Guannan Zhang. 

### Features
- Directionally smoothing objective functions with Gaussian kernel for nonlocal exploration in each direction  
- Gauss-Hermite quadrature for approximating DGS gradient
- Backtracking line search for adaptively updating smoothing radius and step size 
- (Optional) Random generation of smoothing directions to enhance exploration 

### Benchmark functions 

The functions listed below are some of the common functions and datasets used for testing optimization algorithms. They are grouped according to similarities in their significant physical properties and shapes. Each page contains information about the corresponding function or dataset. 
- [Ackley function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Ackley.md)
- [Rastrigin function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Rastrigin.md)
- [Schwefel function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Schwefel.md)
- [Schaffer function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Schaffer.md)
- [Ellipsoidal function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Ellipsoidal.md)
- [Rosenbrock function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Rosenbrock.md)
- [Trigonometric function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Trigonometric.md)
- [Quintic function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Quintic.md)
- [Alpine function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Alpine.md)
- [Shubert function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Shubert.md)
- [Styblinsky-Tang function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Styblinsky-Tang.md)
- [BentCigar function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/BentCigar.md)
- [SharpRidge function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/SharpRidge.md)
- [Solomon function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Solomon.md)
- [Different Powers function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/DifferentPowers.md)
- [Weierstrass function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Weierstrass.md)
- [Mishra 11 function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Mishra11.md)
- [Langermann function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Langermann.md)
- [Powell function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Powell.md)
- [Deb function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Deb.md)

### Related papers 

1. J. Zhang, H. Tran, D. Lu, G. Zhang, [A Novel Evolution Strategy with Directional Gaussian Smoothing for Blackbox Optimization](https://arxiv.org/pdf/2002.03001.pdf), submitted, 2020. 
2. H. Tran, G. Zhang, AdaDGS: An adaptive black-box optimization method with a nonlocal directional Gaussian smoothing gradient, submitted, 2020.
