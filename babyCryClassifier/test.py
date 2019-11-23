import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

a = np.resize(a, (2,2,1))
b = np.resize(b, (2,2,1))

c=np.append(a, b, axis=2)
print(c)

