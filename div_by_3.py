import numpy as np
A1 = np.arange(1,101,1)
A2 = np.reshape(A1,(10,10))
A = A1**2
print(A)
divisible = A%3
A3 = A[divide==0]
print(A3)
np.save('div_by_3.npy', A3)