#! /usr/bin/env python
"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
word1 and word2 may be the same and they represent two individual words in the list.
For example,
"""


import collections
import sys


class Myclass:
	def shorest_words_dis(self, words, word1, word2):
		index = collections.defaultdict(list)
		for i in range(len(words)):
			if words[i] == word1:
				index[word1].append(i)
			elif words[i] == word2:
				index[word2].append(i)
		print index
		ret, i, j =  sys.maxint, 0, 0
		if len(index) == 1:
			j = 1
		while i < len(index[word1]) and j < len(index[word2]):
			if index[word1][i] != index[word2][j]:
				ret = min(ret, abs(index[word1][i] - index[word2][j]))
			if index[word1][i] <= index[word2][j]:
				i += 1
			else:		
				j += 1
		return ret


	def shorest_words_dis_ii(self, words, word1, word2):
		ret, i, j = sys.maxint, 0, 1
		n = len(words)
		while i < n and j < n:
			while i < n and words[i] != word1:
				i += 1
			while j < n and words[j] != word2:
				j += 1
			if i < n and j < n and i != j:
				ret = min(ret, abs(i - j))
			if i <= j:
				i += 1
			else:
				j += 1
		return ret

if __name__ == '__main__':
	m = Myclass()
	words = ["practice", "makes", "perfect", "coding", "makes"]
	word1, word2 = 'makes', 'coding'
	print m.shorest_words_dis_ii(words, word1, word2)
		
		 
