## AdaDGS: An adaptive black-box optimization method with directional Gaussian smoothing for high-dimensional multi-modal functions.
This repository contains Python code for testing adaptive Directional Gaussian smoothing (AdaDGS) method on high-dimensional multi-modal benchmark functions. This method was  developed in the paper [*AdaDGS: An adaptive black-box optimization method with a nonlocal directional Gaussian smoothing gradient*](https://arxiv.org/abs/2011.02009) by Hoang Tran and Guannan Zhang. 

The local gradient points to the direction of the steepest slope in an infinitesimal neighborhood. An optimizer guided by the local gradient is often trapped in local optima when the loss landscape is multi-modal. A directional Gaussian smoothing (DGS) approach was recently proposed in [1] and used to define a truly nonlocal gradient, referred to as the DGS gradient, for high-dimensional black-box optimization. Promising results show that replacing the traditional local gradient with the DGS gradient can significantly improve the performance of gradient-based methods in optimizing highly multi-modal functions with global structures. However, the optimal performance of the DGS gradient may rely on fine tuning of two important hyper-parameters, i.e., the smoothing radius and the learning rate. In this paper, we present a simple, yet ingenious and efficient adaptive approach for optimization with the DGS gradient, which removes the need of hyper-parameter fine tuning. Since the DGS gradient generally points to a good search direction, we perform a line search along the DGS direction to determine the step size at each iteration. The learned step size in turn will inform us of the scale of function landscape in the surrounding area, based on which we adjust the smoothing radius accordingly for the next iteration. We present experimental results on high-dimensional benchmark functions, an airfoil design problem and a game content generation problem. The AdaDGS method has shown superior performance over several the state-of-the-art black-box optimization methods.

### Illustration of the nonlocal DGS gradient
<div align="center"> 
<figure>
  <p><img src="Benchmark Functions/image/DGS_illustration.png" alt="DGS_gradient illustration" height="400">
  <figcaption> <b>Figure 1</b>: Illustration of the nonlocal exploration capability of the DGS gradient in [1] in minimizing a multi-modal function F(x). In the central plot,the blue arrow points to the local gradient direction and the red arrow points to the DGS gradient direction. The top and right plots show the directionally smoothed loss functions along the two axes. Because the DGS gradient captures the global structure of F(x), it can point to a direction much closer to the global minimum than the local gradient.</figcaption>
</figure>
</div>


### Features of the code
- Directionally smoothing objective functions with Gaussian kernel for nonlocal exploration in each direction  
- Gauss-Hermite quadrature for approximating DGS gradient
- Backtracking line search for adaptively updating smoothing radius and step size 
- (Optional) Random generation of smoothing directions to enhance exploration 

### Benchmark functions 

The functions listed below are some of the common functions and datasets used for testing optimization algorithms. They are grouped according to similarities in their significant physical properties and shapes. Each page contains information about the corresponding function or dataset. 

- [Ackley function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Ackley.md)
- [Alpine function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Alpine.md)
- [Bent Cigar function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/BentCigar.md)
- [Cosine Mixture function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/CosineMixture.md)
- [Csendes function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Csendes.md)
- [Deb function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Deb.md)
- [Different Powers function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/DifferentPowers.md)
- [Dixon-Price function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/DixonPrice.md)
- [Ellipsoidal function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Ellipsoidal.md)
- [Griewank function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Griewank.md)
- [Langermann function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Langermann.md)
- [Levy function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Levy.md)
- [Michalewicz function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Michalewicz.md)
- [Mishra 2 function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Mishra2.md)
- [Mishra 11 function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Mishra11.md)
- [Pathological function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Pathological.md)
- [Pinter function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Pinter.md)
- [Powell function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Powell.md)
- [Qing function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Qing.md)
- [Quintic function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Quintic.md)
- [Rastrigin function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Rastrigin.md)
- [Ripple function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Ripple.md)
- [Rosenbrock function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Rosenbrock.md)
- [Salomon function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Salomon.md)
- [Schaffer function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Schaffer.md)
- [Schaffer F6 function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/SchafferF6.md)
- [Schwefel function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Schwefel.md)
- [SharpRidge function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/SharpRidge.md)
- [Shubert function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Shubert.md)
- [Step function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Step.md)
- [Stepint function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Stepint.md)
- [Streched function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Streched.md)
- [Styblinsky-Tang function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Styblinsky-Tang.md)
- [Sum Squares function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/SumSquares.md)
- [Trid function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Trid.md)
- [Trigonometric function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Trigonometric.md)
- [Vincent function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Vincent.md)
- [Wavy function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Wavy.md)
- [Weierstrass function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Weierstrass.md)
- [Xin-She Yang function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/XinSheYang.md)
- [Zakharov function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Zakharov.md)

### Related papers 

[1] J. Zhang, H. Tran, D. Lu, G. Zhang, [A Novel Evolution Strategy with Directional Gaussian Smoothing for Blackbox Optimization](https://arxiv.org/pdf/2002.03001.pdf), arXiv:2002.03001, 2020. 

[2] H. Tran, G. Zhang, [AdaDGS: An adaptive black-box optimization method with a nonlocal directional Gaussian smoothing gradient](https://arxiv.org/abs/2011.02009), arXiv:2011.02009, 2020.

[3] J. Zhang, S. Bi, and G. Zhang, A directional Gaussian smoothing optimization method for computational inverse design in nanophotonics, <b>Materials & Design<\b>, 197 (1), pp. 109213, 2021.
