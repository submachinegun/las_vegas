#!/usr/bin/env python


import unittest

class Myclass:
	"""
	Find the longest substring with at most M distinct characters.
	"""
	def find_longest_substring(self, s, m):
		if m > len(s):
			return s
		d = dict()
		start = 0
		ret = ''
		for i in range(len(s)):
			d[s[i]] = i
			while len(d) > m:
				if d[s[start]] == start:
					del d[s[start]]
				start += 1
			if i - start + 1 > len(ret):
				ret = s[start: i - start + 1]
		return ret


