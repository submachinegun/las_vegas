
"""
Given a non-negative number represented as a singly linked list of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
"""


import sys
sys.path.insert(0, 'data_structure')
from ListNode import ListNode
from PrintAll import Print

class Myclass:
	def plus_one(self, head):
		new_head = self.reverse(head)
		p, pre = new_head, None
		add = 1
		while p and add:
			val = p.val + add
			add = val / 10
			p.val = val % 10
			pre = p
			p = p.next
		if add:
			pre.next = ListNode(1)
		head = self.reverse(new_head)
		return head

	def reverse(self, head):
		if not head or not head.next:
			return head
		pre, cur = None, head
		while cur:
			next = cur.next
			cur.next = pre
			pre = cur
			cur = next
		return pre


if __name__ == '__main__':
	l1, l2, l3 = ListNode(9), ListNode(9), ListNode(9)
	l1.next = l2
	l2.next = l3
	p = Print()
	m = Myclass()
	l = m.plus_one(l1)
	p.print_list_nodes(l)
			 
	
