# import numpy as np
from numpy import array

N = int(input())
numbers = input().split()

# numbers = np.array(numbers,dtype=float)
numbers = array(numbers, dtype=float)

print(sorted(numbers))
