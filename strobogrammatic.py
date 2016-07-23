import unittest


class solution:


	def is_strobogrammatic(self, num):
		_TURN_MAP = {'9':'6', '6':'9', '1':'1', '8':'8', '0':'0'}
		i, j = 0, len(num) - 1
		while i < j:
			if num[i] not in _TURN_MAP or num[j] != _TURN_MAP[num[i]]:
				return False
			i += 1
			j -= 1
		return True

class solution_test(unittest.TestCase):


	def test(self):
		s = solution() 
		self.assertEqual(s.is_strobogrammatic('818'), True)
		self.assertEqual(s.is_strobogrammatic('1691'), True)
		self.assertEqual(s.is_strobogrammatic('6009'), True)
		self.assertEqual(s.is_strobogrammatic('33'), False)


if __name__ == '__main__':
	unittest.main()
