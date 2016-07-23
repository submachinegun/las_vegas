#!/usr/bin/env python


class Myclass:
	"""
	Assume you have an array of length n initialized with all 0's and are given k update operations.
	Each operation is represented as a triplet: [startIndex, endIndex, inc] 
	which increments each element of subarray A[startIndex ... endIndex] 
	(startIndex and endIndex inclusive) with inc.
	Return the modified array after all k operations were executed.
	"""
		
	def update_k(self, n, ope):
		"""
		:type ope:[(startIndex, endIndex, inc)]*k
		:rtype void
		"""
		ret = [0] * n
		for o in ope:
			ret[o[0]] += o[2]
			if o[1] + 1 < n:
				ret[o[1] + 1] -= o[2]
		value = 0
		for i in range( n):
			value += ret[i] 
			ret[i] = value
		return ret

if __name__ == '__main__':
	m = Myclass()
	print m.update_k(5, [(1,3,2), (2,4,3), (0,2,-2)])
		
