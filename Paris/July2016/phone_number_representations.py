#!/usr/bin/evn python


class MyClass:
	"""
	Find all combinations of phone number representation, with restriction that the words can only be
	from a dictionary, with possible digits at front/end, such as HOMEDEPOT or 800 TARGET 234
	"""
	def phone_number_combinations(self, num, words):
		"""
		:type num:str
		:type words:[str]
		:rtype: [str]
		"""
		ret = []
		if not num:
			return ret
		d = {'2':('a', 'b', 'c'), '3':('d', 'e', 'f'), '4':('g', 'h', 'i'), '5': ('j', 'k', 'l'), 
		'6': ('m','n','o'), '7': ('p','q','r','s'), '8':('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
		self.dfs(0, '', num, words, d, ret)
		return ret

	def dfs(self, i, pre, num, words, d, ret):
		"""
		:type i: int
		:type pre: str
		:type num: str
		:type words: list
		:type d: dict
		:type ret: list
		:rtype: None
		"""
		if i == len(num):
			ret.append(pre)
			return
		
			
