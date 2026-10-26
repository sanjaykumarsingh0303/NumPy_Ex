import numpy as np
a = np.arange(10).reshape(2,5)
print(a)
print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)
print(a.real)
print(a.imag)
print(a.flat)
print(a.flatten())


b = np.arange(24).reshape(2, 3, 4)  # 3d array
print(b)


c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)
print(c.shape)
print(c.size)
print(c.ndim)
print(c.dtype)
print(c.itemsize)
print(c.nbytes)
print(c.real)
print(c.imag)
print(c.flat)
print(c.flatten())


d = np.zeros((2,3))
print(d)


e= np.array([20, 30, 40, 50])
f = np.arange(4)
print(e+f)


g = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])

for i in g:
    for j in i:
        for k in j:
            print(k)