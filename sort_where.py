import numpy as np

scores = np.array([92, 85, 90, 64, 78, 55])

print(np.sort(scores))
print(np.argsort(scores))          # indexes of the values from low to high
print(scores[np.argsort(scores)])  # same order as np.sort
print(np.where(scores >= 75, "pass", "fail"))
print(np.clip(scores, 60, 90))     # anything below 60 becomes 60, above 90 becomes 90