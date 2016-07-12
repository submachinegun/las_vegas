#! /usr/bin/env python
"""
Check if an integer is the sum of two square
"""

import math
import unittest


class Myclass:
	def check(self, n):
		"""
		:tpye n:int
		rtype:bool
		"""
		# square of even: pow(2*k,2) = 4*k^2 = 0(mod 4)
		# square of odd: pow(2*k+1, 2) = 1(mod 4)
		# sum of two square: even^2 + even^2 = 0(mod 4), odd^2 + odd^2 = 2(mod 4), even^2 + odd^2 = 1(mod 4) 
		return n % 4 != 3

	
	def check_two_loop(self, n):
		"""
		:type n: int
		rtype:bool
		"""
		for i in range(1, int(math.sqrt(n)) + 1):
			for j in range(1, int(math.sqrt(n)) + 1):
				if i**2 + j **2 == n:
					return True
		return False	


class MyclassTest(unittest.TestCase):
	def test(self):
		mm = Myclass()
		self.assertEqual(mm.check(18), True)
		self.assertEqual(mm.check(19), False)
		self.assertEqual(mm.check_two_loop(18), True)	
		self.assertEqual(mm.check_two_loop(17), True)
		self.assertEqual(mm.check_two_loop(19), False)


if __name__ == '__main__':
	unittest.main()
