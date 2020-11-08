## Rosenbrock function

<div align="center"> <img src="https://latex.codecogs.com/svg.latex?&space;f(\mathbf{x})=\sum_{i=1}^{d-1}[100(x_{i+1}-x_i^2)^2+(x_i-1)^2]." title="Rosenbrock"/> </div>

The Rosenbrock function is unimodal, and the global minimum lies in a bending ridge, which needs to be followed to reach solution. The ridge changes its orientation <img src="https://latex.codecogs.com/svg.latex?&space;d-1" title=" "/> times. 

- Initial search domain: <img src="https://latex.codecogs.com/svg.latex?&space;\mathbf{x}\in[-5,10]^d" title=" "/>.
- Global minimum: <img src="https://latex.codecogs.com/svg.latex?&space;f(\mathbf{x}_{opt})=0" title=" "/> &nbsp; at &nbsp; <img src="https://latex.codecogs.com/svg.latex?&space;\mathbf{x}_{opt}=(1,\ldots,1)" title=" "/>.

<div align="center"> 
  <img src="image/Rosenbrock.jpg" alt="Rosenbrock" height="400"/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="image/rosen_error_plot.jpg" alt="error" height="380"/>
</div>



