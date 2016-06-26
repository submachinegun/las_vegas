def depthSum(nestedList):
	print  depthSumHelper(nestedList, 1)


def depthSumHelper(nestedList, depth):
	sum = 0
	for item in nestedList:
		if isinstance(item, int):
			sum += item * depth
		else:
			sum += depthSumHelper(item, depth+1)
	return sum


if __name__ == '__main__':
	list = [[1,1], 2, [4, [6]]]
	depthSum(list)	
