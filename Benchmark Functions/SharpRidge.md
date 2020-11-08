## Sharp Ridge function


<div align="center"> <img src="https://latex.codecogs.com/svg.latex?&space;f(x)=x_1^2+100\sqrt{\sum_{i=2}^d x_i^2}." title="SharpRidge" /> </div>

The Sharp Ridge function represents convex and anisotropic landscapes. There is a sharp ridge defined along <img src="https://latex.codecogs.com/svg.latex?&space;x_2^2+\cdots+x_d^2=0" title=""/> that must be followed to reach the global minimum, which creates difficulties for optimizations algorithms. 
- Initial search domain: <img src="https://latex.codecogs.com/svg.latex?&space;\mathbf{x}\in[-10,10]^d" title=" "/>.
- Global minimum: <img src="https://latex.codecogs.com/svg.latex?&space;f(\mathbf{x}_{opt})=0" title=" "/> &nbsp; at &nbsp; <img src="https://latex.codecogs.com/svg.latex?&space;\mathbf{x}_{opt}=(0,\cdots,0)" title=" "/>.

<div align="center"> 
  <img src="image/SharpRidge.jpg" alt="SharpRidge" height="400"/> 
  <! <img src="image/sharp_error_plot.jpg" alt="error" height="380"/>/>
</div>



