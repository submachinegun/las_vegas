#!/usr/bin/env python


class Myclass:
	"""
	Assume you have an array of length n initialized with all 0's and are given k update operations.
	Each operation is represented as a triplet: [startIndex, endIndex, inc] 
	which increments each element of subarray A[startIndex ... endIndex] 
	(startIndex and endIndex inclusive) with inc.
	Return the modified array after all k operations were executed.
	"""
	def __init__(self, n):
		self.A = [0] * n

	def _update(self, startIndex, endIndex, inc):
		startIndex = max(startIndex, 0)
		endIndex = min(n - 1, endIndex)
		for i in range(startIndex, endIndex + 1):
			self.A[i] += inc
		
	def update_k(self, ope):
		"""
		:type ope:[(startIndex, endIndex, inc)]*k
		:rtype void
		"""
		
