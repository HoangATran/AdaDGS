## Bent Cigar function

<div align="center"> <img src="https://latex.codecogs.com/svg.latex?&space;f(\mathbf{x})=x_1^2+10^6{\sum_{i=2}^d{x_i}^2}." title="BentCigar" /> </div>

The Bent Cigar function represents convex and anisotropic landscapes. There is a sharp ridge defined along <img src="https://latex.codecogs.com/svg.latex?&space;x_2^2+\cdots+x_d^2=0" title=" "/> that must be followed to reach the global minimum, which creates difficulties for optimizations algorithms. 
- Initial search domain: <img src="https://latex.codecogs.com/svg.latex?&space;\mathbf{x}\in[-100,100]^d" title=" "/>.
- Global minimum: <img src="https://latex.codecogs.com/svg.latex?&space;f(\mathbf{x}_{opt})=0" title=" "/> &nbsp; at <img src="https://latex.codecogs.com/svg.latex?&space;\mathbf{x}_{opt}=(0,\ldots,0)" title=" "/>.

<div align="center"> 
  <img src="image/BentCigar.jpg" alt="BentCigar" height="400"/> 
  <! <img src="image/bent_error_plot.jpg" alt="error" height="380"/> 
</div>


