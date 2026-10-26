import numpy as np

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

print(np.vstack((a, b)))   # b is placed under a, shape (4, 2)
print(np.hstack((a, b)))   # b is placed to the right of a, shape (2, 4)
print(np.concatenate((a, b), axis=0))  # same as vstack
print(np.concatenate((a, b), axis=1))  # same as hstack