import unittest

class solution:
	def is_strobogrammatic(self, num):
		turn_map = {'9':'6', '6': '9', '1':'1', '8':'8'}
		i, j = 0, len(num) - 1
		while i < j:
			if num[i] not in turn_map or num[j] != turn_map[num[i]]:
				return False
			i += 1
			j -= 1
		return True

class solution_test(unittest.TestCase):
	def test(self):
		s = solution() 
		self.assertEqual(s.is_strobogrammatic('818'), True)
		self.assertEqual(s.is_strobogrammatic('69'), True)
		self.assertEqual(s.is_strobogrammatic('11'), True)
		self.assertEqual(s.is_strobogrammatic('33'), False)

if __name__ == '__main__':
	unittest.main()
