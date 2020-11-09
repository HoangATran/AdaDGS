## Powell function

<img src="https://latex.codecogs.com/svg.latex?&space;f(\mathbf{x})=\sum_{i=1}^{d/4}[(x_{4i-3}+10x_{4i-2})^2+5(x_{4i-1}-x_{4i})^2+(x_{4i-2}-2x_{4i-1})^4+10(x_{4i-3}-x_{4i})^4]" title="Powell" />

where <img src="https://latex.codecogs.com/svg.latex?&space;a=20,b=0.2,c=2\pi" title="Ackley_param" />. The Ackley function represents *non-convex* landscapes with *nearly flat outer region*.  The function poses a risk for optimization algorithms, particularly hill-climbing algorithms, to be trapped in one of its many local minima.

The initial search domain is <img src="https://latex.codecogs.com/svg.latex?&space;x\in{[-32.768,32.768]}^d" title=" "/>. The global minimum is <img src="https://latex.codecogs.com/svg.latex?&space;f(x_{opt})=0" title=" "/>.

![Powell](image/Powell.jpg)



