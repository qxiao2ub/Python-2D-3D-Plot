import matplotlib.pyplot as plt
import numpy as np

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

#2d plot
plt.plot(P_ijt, Z_single)
#plt.plot(P_ijt, U_ijt)
#plt.plot(P_ijt, W_ijt)
plt.show

plt.xlabel('P_ijt')
plt.ylabel('Z')
plt.title('P_ijt & Z')
#plt.plot(P_ijt, U_ijt)
#plt.axis('loose')

#plt.show()
