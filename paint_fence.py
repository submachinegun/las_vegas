
def numWays( n, k):  
        """ 
        :type n: int 
        :type k: int 
        :rtype: int 
        """  
	if n == 0 or k == 0:
		return 0
	if n == 1:
		return k
	last_s, last_d = k, k * (k - 1)
	for i in range(3, n + 1):
		temp_d = (k - 1) * (last_s + last_d)
		last_s = last_d
		last_d = temp_d
	return last_d + last_s

if __name__ == '__main__':
	print numWays(2,3)
