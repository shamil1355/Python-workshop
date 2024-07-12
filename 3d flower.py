def f(x,y):
    return np.sin(np.sqrt(x**2+y**2))
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D as ax
ax=plt.axes(projection='3d')
x=np.linspace(-6,6,30)
y=np.linspace(-6,6,30)
X,Y=np.meshgrid(x,y)
Z= f(X,Y)
fig=plt.figure()
ax.contour3D(X,Y,Z,100,cmap='BrBG')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(6,6)
plt.show()
