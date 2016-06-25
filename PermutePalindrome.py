import collections

def canPermutePalindrom(s):
	return sum( v % 2 for v in collections.Counter(s).values()) < 2

if __name__ == '__main__':
	s = 'carerac'
	print canPermutePalindrom(s)
