import numpy as np

scores = np.array([
  [10,20,30],
  [65,76,87],
  [91,70,99],
  [55,56,87]
])

print(f"first student:{scores[0]}")        # first student
print(scores[:, 1])     # every student's second subject
print(scores[1:3, 0])   # students 1 and 2, first subject
print(scores[-1, -1])
