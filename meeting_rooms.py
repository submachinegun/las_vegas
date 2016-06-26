class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


class Solution:
	def canAttend(self, intervals):
		intervals.sort(key=lambda x: x.start)
		for i in range(1, len(intervals)):
			if intervals[i].start < intervals[i - 1].end:
				return False
		return True


if __name__ == '__main__':
	t1, t2, t3 = Interval(s=0,e=30), Interval(s=0,e=10), Interval(s=30,e= 40)
	time = [t1, t2, t3]
	print Solution().canAttend(time)
