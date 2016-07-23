#!/usr/bin/env python


class Myclass:
	"""
	Given an unsorted array nums, 
	reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
	For example, given nums = [3, 5, 2, 1, 6, 4],
	one possible answer is [1, 6, 2, 5, 3, 4].
	"""
	def wiggle_sort(self, A):
		"""
		:type A:[int]
		:rtype: void
		"""
		for i in range(1, len(A)):
			if i % 2 and A[i] < A[i - 1]:
				A[i], A[i - 1] = A[i - 1], A[i]
			elif i % 2 == 0 and A[i] > A[i - 1]:
				A[i], A[i - 1] = A[i - 1], A[i]
	
	def wiggle_sort_II(self, A):
		A = sorted(A)
		for i in range(2, len(A)):
			A[i], A[i - 1] = A[i - 1], A[i]



if __name__ == '__main__':
	m = Myclass()
	A = [1,3,5,2,4,6]
	m.wiggle_sort(A)
	print A
	A = [3, 5, 2, 1, 6, 4]
	m.wiggle_sort_II(A)
	print A 
