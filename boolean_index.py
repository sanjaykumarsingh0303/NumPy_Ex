import numpy as np

scores = np.array([89,78,49,58,77,70])
passed = scores>=75

print(passed)
print(scores[passed])
print(scores[scores < 80])