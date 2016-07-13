#!/usr/bin/env python


class Myclass:
	"""
	An abbreviation of a word follows the form <first letter><number><last letter>.
	Below are some examples of word abbreviations:

	a) it                      --> it    (no abbreviation)

     	     1
	b) d|o|g                   --> d1g

              	      1    1  1
     	     1---5----0----5--8
	c) i|nternationalizatio|n  --> i18n

               	      1
     	     1---5----0
	d) l|ocalizatio|n          --> l10n

	Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. 
	A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

	Example: 
		Given dictionary = [ "deer", "door", "cake", "card" ]

		isUnique("dear") -> false
		isUnique("cart") -> true
		isUnique("cane") -> false
		isUnique("make") -> true 
	"""
	def isUnique(self, w, d):
		"""
		:type w:str
		:type d:[]
		:rtype: bool
		"""
		f_d = filter(lambda x: len(x) == len(w), d)
		if len(w) <= 2:
			return w not in f_d
		abr_w = ''.join([w[0], str(len(w) - 2), w[-1]])
		for word in f_d:
			if word[0] == w[0] and word[-1] == w[-1]:
				return False
		return True
	
	def isUniqueII(self, w, d):
		m = set()
		for word in d:
			abbr_w = word[0] + str(len(word) - 2) + word[-1]
			m.add(abbr_w)
		abbr = w[0] + str(len(w) - 2) + w[-1]
		return abbr not in m	


if __name__ == '__main__':
	m = Myclass()
	d = [ "deer", "door", "cake", "card" ]
	print m.isUnique("dear", d)
	print m.isUnique("cart", d)
	print m.isUnique("cane", d)
	print m.isUnique("make", d) 
	print
	print m.isUniqueII("dear", d)
	print m.isUniqueII("cart", d)
	print m.isUniqueII("cane", d)
	print m.isUniqueII("make", d) 
	
