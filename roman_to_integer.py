import unittest

class Solution:

	def roman_2_int(self,s):
		R_to_I = {'I':1, 'V':5, 'X': 10, 'L':50, 'C': 100, 'D':500, 'M':1000}
		last,ret = -1, 0
		for c in s:
			cur = R_to_I[c]
			if last != -1 and last < cur:
				ret -= last
				cur -= last
			ret += cur
			last = cur
		return ret
class TestSolution(unittest.TestCase):
	def test_roman_2_int(self):
		s = Solution()
		self.assertEqual(s.roman_2_int('MLXVI'), 1066)
		self.assertEqual(s.roman_2_int('II'), 2)
		self.assertEqual(s.roman_2_int('MCMXC'), 1990)
if __name__ == '__main__':
	unittest.main()
	 
