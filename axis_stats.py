import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 88, 92],
])

print(marks.mean())        # one number for the whole table
print(marks.mean(axis=0))  # mean of each subject (down the columns)
print(marks.mean(axis=1))  # mean of each student (across the row)
print(marks.sum(axis=0))