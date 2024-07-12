def f(x,y):
    return np.sin(x)**10+np.cos(10+y*x)*np.cos(x)
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,50)
y=np.linspace(0,5,40)
x,y=np.meshgrid(x,y)
z=f(x,y)
fig=plt.contour(x,y,z,colors='cyan');
plt.show()