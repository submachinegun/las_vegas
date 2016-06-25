import sys

def shortestDistance(words, word1, word2):
	index1, index2, min_len = -1, -1, sys.maxint
	for i in range(len(words)):
		if words[i] == word1:
			if index2 != -1:
				min_len = min(min_len, i - index2)
			index1 = i
		elif words[i] == word2:
			if index1 != -1:
				min_len = min(min_len, i - index1)
			index2 = i
	print min_len

if __name__ == '__main__':
	words = ['practice', 'makes', 'perfect', 'coding', 'makes']
	word1, word2 = 'coding','makes'
	shortestDistance(words, word1, word2)
