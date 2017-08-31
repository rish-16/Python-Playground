'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import numpy as np
import math

for n in range(1000000):
	for i in range(1,11):
		if n % i == 0:
			print ('Yes')
		else:
			print ('No')
