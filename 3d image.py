import numpy 
from matplotlib import pyplot
a=numpy.linspace(-5,5,25)
b=numpy.linspace(-5,5,25)
x,y=numpy.meshgrid(a,b)
z=numpy.sin(numpy.sqrt(x**2+y**2))
fig=py