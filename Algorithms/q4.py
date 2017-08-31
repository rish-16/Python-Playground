'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import numpy as np
import math

arr = []
arr2 = []

for i in range(1000):
	for j in range(1000):
		if i > 99 and j > 99:
			product = i * j

			text = str(product)

			if text == text[::-1]:
				arr.append(text)

for no in arr:
	num = int(no)
	arr2.append(num)

print (max(arr2))
