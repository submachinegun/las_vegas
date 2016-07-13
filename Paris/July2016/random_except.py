#!/usr/bin/evn python


class MyClass:
	"""
	Given a function rand(N) which return an integer from 0 to n - 1 with probability 1/N
	Create a funtion rand_except(N, L) which return an integer from 0 to n - 1 but not in a SORTED list
	such as {2, 4, 9}. 
	Require uniform distribution.
	""" 
	def rand(self, N):
		return radom.uniform(0, N - 1)

	def rand_except(self, N, L):
		n = self.rand(N)
		while n in L:
			n = self.rand(N)
		return n
		
