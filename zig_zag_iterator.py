#! /usr/bin/env python
"""
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18): The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].
"""
import itertools


class Myclass:
	def __init__(self, k_vectors):
		self.iter_list = []
		self.list_size = []
		for v in k_vectors:
			self.iter_list.append(iter(v))
			self.list_size.append(len(v))
	
	def __iter__(self):
		self.turn = 0
		return self
	
	def next(self):
		if self.iter_list:
			cur_iter = self.turn % len(self.iter_list)
			ret = self.iter_list[cur_iter].next()
			self.list_size[cur_iter] -= 1
			if self.list_size[cur_iter] == 0:
				del self.iter_list[cur_iter]
				del self.list_size[cur_iter]
			else:
				self.turn += 1
			return ret
		else:
			raise StopIteration
		

if __name__ == '__main__':
	m = Myclass([[1, 2],[3,4],[5,6], [7]])
	for x in m:
		print x
