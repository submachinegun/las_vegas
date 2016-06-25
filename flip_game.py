def filp(s):
	ret, n, ls = [], len(s), list(s)
	for i in range(1, n):
		if ls[i] == '+' and ls[i - 1] == '+':
			ls[i] = ls[i - 1] = '-'
			ret.append(''.join(ls))
			ls[i] = ls[i - 1] = '+'
	print ret

if __name__ == '__main__':
	filp('++++')
