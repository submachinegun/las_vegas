#! /user/bin/env python
"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
class Myclass:
	def multiply_I(self, A, B):
		m, k, n = len(A), len(A[0]), len(B[0])
		ret = [[0 for x in range(n)] for y in range(m)]
		for i in range(m):
			for j in range(k):
				if A[i][j]:
					for z in range(n):
						if B[j][z]:
							ret[i][z] += A[i][j] * B[j][z]
		return ret

	def encode_matrix_tuple(self, A):
		ret = []
		for i in range(len(A)):
			for j in range(len(A[0])):
				if A[i][j]:
					ret.append((i, j, A[i][j]))
		return ret

	def encode_matrix_array(self, A):
		ret = [[]] * len(A)
		for i in range(len(A)):
			for j in range(len(A[0])):
				if A[i][j]:
					ret[i].append((j, A[i][j]))
		print ret
		return ret

	def multiply_II(self, A, B):
		b = self.encode_matrix_array(B)
		m, k, n = len(A), len(B), len(B[0])
		ret = [[0] * n for i in range(m)]
		for i in range(m):
			for j in range(k):
				if A[i][j]:
					for tup in b[j]:
						ret[i][tup[0]] += A[i][j] * tup[1]
		return ret


if __name__ == '__main__':
	m = Myclass()
	A = [[1, 0, 0], [-1, 0, 3]]
	B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
	print m.multiply_I(A, B)
	print m.multiply_II(A, B)
