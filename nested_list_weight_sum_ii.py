#! /usr/bin/env python
"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)
"""



class Myclass:
	def weight_sum(self, A):
		layer_sum = [0]
		self.weight_sum_helper(A, 0, 0, layer_sum, 0)
		w = len(layer_sum)
		print layer_sum
		ret = 0
		for x in layer_sum:
			ret += w * x
			w -= 1
		return ret

	def weight_sum_helper(self, A, i, pre_sum, layer_sum, layer):
		print A, i, pre_sum
		print
		if i == len(A):
			layer_sum[layer] = pre_sum
			return pre_sum
		if type(A[i]) is int:
			self.weight_sum_helper(A, i + 1, pre_sum + A[i], layer_sum, layer)
		else:	
			layer_sum.append(0)
			this_sum = self.weight_sum_helper(A[i], 0, 0, layer_sum, layer + 1)
			self.weight_sum_helper(A, i + 1, pre_sum + this_sum, layer_sum, layer)


if __name__ == '__main__':
	m = Myclass()
	A =  [1,[4,[6]]]
	#A = [1, 2, 3, 4, 5]
	print m.weight_sum(A)

	
