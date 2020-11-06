## Ackley function

<div align="center"> <img src="https://latex.codecogs.com/svg.latex?&space;f(\mathbf{x})=-a\exp(-b\sqrt{\frac{1}{d}\sum_{i=1}^dx_i^2})-\exp(\frac{1}{d}\sum_{i=1}^d\cos(cx_i))+a+\exp(1)" title="Ackley" /> </div>

where <img src="https://latex.codecogs.com/svg.latex?&space;a=20,b=0.2,c=2\pi" title="Ackley_param" />. The Ackley function represents non-convex landscapes with nearly flat outer region.  The function poses a risk for optimization algorithms, particularly hill-climbing algorithms, to be trapped in one of its many local minima.

- Initial search domain: <img src="https://latex.codecogs.com/svg.latex?&space;\mathbf{x}\in{[-32.768,32.768]}^d" title=" "/>.
- Global minimum: <img src="https://latex.codecogs.com/svg.latex?&space;f(\mathbf{x}^{*})=0," title=" "/> &nbsp; at &nbsp; <img src="https://latex.codecogs.com/svg.latex?&space;\mathbf{x}^{*}=(0,\ldots,0)"/>.

<div align="center"> 
  <img src="image/ackley.jpg" alt="ackley" height="400"/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="image/Ackley_error_plot.jpg" alt="error" height="380"/>
</div>



