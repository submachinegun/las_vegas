#!/usr/bin/evn python


import math


class Myclass:
	"""
	One string has only one extra character than the other other string. Find it out.
	e.g cxcc, ccc. output :x
	"""
	def find_extra_char(self, s1, s2):
		"""
		:type s1:str
		:type s2:str
		:rtype: str
		"""
		if not s1:
			return s2
		if not s2:
			return s1
		n1 = self.encode(s1)
		n2 = self.encode(s2)
		dif = n1 ^ n2
		return chr(ord('a') + int(math.log(dif & ~(dif - 1), 2)))

	def encode(self, s):
		ret = 1
		for c in s:
			ret |= (1 << (ord(c) - ord('a')))
		return ret


if __name__ == '__main__':
	m = Myclass()
	print m.find_extra_char('aa', 'ab')
	print m.find_extra_char('abcx', 'abc')
