'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import numpy as np
import math

for a in range(1001):
	for b in range(1001):
		for c in range(1001):
			if a*a + b*b == c*c:
				if a + b + c == 1000:
					print(a*b*c)
