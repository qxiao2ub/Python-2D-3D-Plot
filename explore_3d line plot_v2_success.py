#https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
#https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

#P_ijt = np.linspace(-90,90,100)
P_ijt = np.arange(0.1, 28.6, 0.01)

#define parameters
a = -85
b = 55
c_ijt = 39
d_ijt = 60
T = 16
m = 3
n = 6

#define functions

#(1st-define W_ijt)
W_ijt_up = a + b - a*b + c_ijt*m -a*c_ijt*m+m * P_ijt - b*m*P_ijt - c_ijt * m*m *P_ijt

W_ijt_down = (-1+b+c_ijt*m)*n

W_ijt = W_ijt_up / W_ijt_down

#(2nd-define U_ijt)
U_ijt_up = b*d_ijt*W_ijt + c_ijt*d_ijt*m*W_ijt

U_ijt_down = T*(a+b+c_ijt*m+m*P_ijt+n*W_ijt)

U_ijt = U_ijt_up / U_ijt_down

#(3rd-define objective functions-here is simple objective no sum, only one pair of data)
Z_single_up = P_ijt*(b*d_ijt+c_ijt*d_ijt*m-n*T*U_ijt)

Z_single_down = a+b+m*(c_ijt+P_ijt)

Z_single = Z_single_up / Z_single_down

#plot 3d line
ax.plot(P_ijt, U_ijt, Z_single, label='P_ijt, U_ijt, Z')
ax.legend()

ax.set_xlabel('P_ijt')
ax.set_ylabel('U_ijt')
ax.set_zlabel('Z')

plt.show()
