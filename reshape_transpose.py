import numpy as np

a = np.arange(12)
grid = a.reshape(3, 4)

print(grid)
print(grid.T)            # swap rows and columns, shape (4, 3)
print(grid.ravel())      # back to one row of 12 numbers
print(a.reshape(2, 2, 3))