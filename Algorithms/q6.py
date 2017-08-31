'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

import numpy as np
import math

arr1 = []
arr2 = []

for i in range(1,101):
	n = i*i
	arr1.append(n)

num1 = sum(arr1)

for i in range(1,101):
	arr2.append(i)

num2 = (sum(arr2))*(sum(arr2))

print (num2 - num1)
