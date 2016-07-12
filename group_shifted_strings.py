import collections

class Solution:
	def groupStrings(self, strings):
		"""
		:type strings: List[str]
		:rtype: List[[List[str]]]
		"""
		shift = collections.defaultdict(list)
		for s in strings:
			code = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
			print code
			shift[code].append(s) 
		return map(sorted, shift.values())

if __name__ == '__main__':
	strings = ['abc', 'bcd', 'acef', 'xyz', 'az', 'ba', 'a', 'z']
	s = Solution()
	print s.groupStrings(strings)
