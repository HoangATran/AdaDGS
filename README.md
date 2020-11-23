## AdaDGS: An adaptive black-box optimization method with directional Gaussian smoothing for high-dimensional multi-modal functions.
This repository contains Python code for testing adaptive Directional Gaussian smoothing (AdaDGS) method on high-dimensional multi-modal benchmark functions. This method was  developed in the paper [*AdaDGS: An adaptive black-box optimization method with a nonlocal directional Gaussian smoothing gradient*](https://arxiv.org/abs/2011.02009) by Hoang Tran and Guannan Zhang. 

The local gradient points to the direction of the steepest slope in an infinitesimal neighborhood. An optimizer guided by the local gradient is often trapped in local optima when the loss landscape is multi-modal. A directional Gaussian smoothing (DGS) approach was recently proposed in [1] and used to define a truly nonlocal gradient, referred to as the DGS gradient, for high-dimensional black-box optimization. Promising results show that replacing the traditional local gradient with the DGS gradient can significantly improve the performance of gradient-based methods in optimizing highly multi-modal functions with global structures. However, the optimal performance of the DGS gradient may rely on fine tuning of two important hyper-parameters, i.e., the smoothing radius and the learning rate. In this paper, we present a simple, yet ingenious and efficient adaptive approach for optimization with the DGS gradient, which removes the need of hyper-parameter fine tuning. Since the DGS gradient generally points to a good search direction, we perform a line search along the DGS direction to determine the step size at each iteration. The learned step size in turn will inform us of the scale of function landscape in the surrounding area, based on which we adjust the smoothing radius accordingly for the next iteration. This the code in this repository serves the purposes of reproducing the results in [2] on optimizing high-dimensional multi-modal benchmark functions.  


### Illustration of the DGS gradient in 2D
<div align="center"> 
<figure>
  <p><img src="Benchmark Functions/image/DGS_illustration.png" alt="DGS_gradient illustration" height="400">
  <figcaption> <b>Figure 1</b>: Illustration of the nonlocal exploration capability of the DGS gradient in [1] in minimizing a multi-modal function F(x). In the central plot,the blue arrow points to the local gradient direction and the red arrow points to the DGS gradient direction. The top and right plots show the directionally smoothed loss functions along the two axes. Because the DGS gradient captures the global structure of F(x), it can point to a direction much closer to the global minimum than the local gradient.</figcaption>
</figure>
</div>


### Features 
- Directionally smoothing objective functions with Gaussian kernel for nonlocal exploration in each direction  
- Gauss-Hermite quadrature for approximating DGS gradient
- Backtracking line search for adaptively updating smoothing radius and step size 

### AdaDGS codes
This is the example code to run AdaDGS algorithm for optimizing high-dimensional benchmark functions

```
python AdaDGS.py --f_name='ackley'
```
The above code will test the performance of AdaDGS on Ackley function. The list of benchmark functions currently supported by our code is shown below. By default, the function dimension is 1000, number of trials is 20, number of iterations varying from 10-200 depending on the function (see the function's page for details). We apply a random translation and then a random rotation to make the problem more general. The user can customize their test using the following flags: 
--dim: function dimension 
--n_iter: number of iterations
--num_trial: number of trials 
--no-translation: do not apply random translation on test function
--no-rotation: do not apply random rotation on test function 
--save: save the results to the folder 'results'

### Benchmark functions 

The functions listed below are some of the common functions and datasets used for testing optimization algorithms. They are grouped according to similarities in their significant physical properties and shapes. Each page contains information about the corresponding function or dataset. 

- 'ackley': [Ackley function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Ackley.md)
- 'alpine': [Alpine function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Alpine.md)
- 'ellipsoidal': [Ellipsoidal function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Ellipsoidal.md)
- 'quintic': [Quintic function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Quintic.md)
- 'rastrigin': [Rastrigin function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Rastrigin.md)
- 'rosenbrock': [Rosenbrock function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Rosenbrock.md)
- 'salomon': [Salomon function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Salomon.md)
- 'schaffer': [Schaffer F7 function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Schaffer.md)
- 'sharpridge': [Sharp Ridge function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/SharpRidge.md)
- 'sphere': [Sphere function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Sphere.md)
- 'styblinsky': [Styblinsky-Tang function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Styblinsky-Tang.md)
- 'trigonometric': [Trigonometric function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Trigonometric.md)
- 'wavy': [Wavy function](https://github.com/HoangATran/Directional-Gaussian-smoothing/blob/main/Benchmark%20Functions/Wavy.md)

### Related papers 

[1] J. Zhang, H. Tran, D. Lu, G. Zhang, [A Novel Evolution Strategy with Directional Gaussian Smoothing for Blackbox Optimization](https://arxiv.org/pdf/2002.03001.pdf), arXiv:2002.03001, 2020. 

[2] H. Tran, G. Zhang, [AdaDGS: An adaptive black-box optimization method with a nonlocal directional Gaussian smoothing gradient](https://arxiv.org/abs/2011.02009), arXiv:2011.02009, 2020.

[3] J. Zhang, S. Bi, and G. Zhang, [A directional Gaussian smoothing optimization method for computational inverse design in nanophotonics](https://www.sciencedirect.com/science/article/pii/S0264127520307486), <b>Materials & Design</b>, 197 (1), pp. 109213, 2021.
