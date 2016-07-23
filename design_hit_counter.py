#! /usr/bin/env python
"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""

class Counter(object):
	queue = []
	
	def hit(self, t):
		self.queue.append(t)
	
	def getHits(self, t):
		while self.queue[0] <= t - 300:
			del self.queue[0]
		print len(self.queue)

class CounterII:
	hit_num = [0] * 300
	timestamp = [0] * 300

	def hit(self, t):
		index = t % 300 - 1
		if self.timestamp[index] == 0 or t == self.timestamp[index]:
			self.hit_num[index] += 1
		else:
			self.hit_num[index] = 1
		self.timestamp[index] = t

	def getHits(self, t):
		print sum(self.hit_num[x] for x in range(300) if self.timestamp[x] > t - 300)
		
if __name__ == '__main__':
	c = CounterII()
	c.hit(1)
	c.hit(1)
	c.hit(2)
	c.hit(3)
	c.hit(4)
	c.getHits(300)
	c.getHits(301)
	c.hit(304)
	c.hit(304)
	c.getHits(306)
