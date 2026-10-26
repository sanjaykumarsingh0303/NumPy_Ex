import numpy as np

prices = np.array([10, 20, 30])          # shape (3,)
qty = np.array([[1, 2, 1],
                [0, 1, 3]])               # shape (2, 3)

print(qty @ prices)   # shape (2,)  -> [80, 110]

x = np.array([[1, 2],
              [3, 4]])
y = np.array([[5, 6],
              [7, 8]])
print(x @ y)
print(x * y)          # cell-by-cell, a different operation