def quick_sort(array):
	quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, l, r):
	if l < r:
		p = partition_hoare(array, l, r)
		print array
		quick_sort_helper(array, l, p - 1)
		quick_sort_helper(array, p + 1, r)


def partition_lomuto(array, l, r):
	pivot = array[r]
	i = l
	for j in range(l, r):
		if array[j] <= pivot:
			array[i], array[j] = array[j], array[i]
			i += 1
	array[i], array[r] = array[r], array[i]
	return i


def partition_hoare(array, l, r):
	pivot = array[l]
	i, j = l, r
	while True:
		while array[i] < pivot:
			i += 1
		while array[j] > pivot:
			j -= 1
		if i >= j:
			return j
		array[i], array[j] = array[j], array[i]
		i += 1
		j -= 1


if __name__ == '__main__':
	A = [3,7,8,5,2,1,9,5,4]
	print A
	quick_sort(A)
	print A
