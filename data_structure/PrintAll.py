#! /usr/bin/env python


from ListNode import ListNode
class Print:
	def print_list_nodes(self, head):
		cur = head
		while cur:
			print str(cur.val) + '->',
			cur = cur.next


if __name__ == '__main__':
	l1, l2, l3 = ListNode(1), ListNode(2), ListNode(3)
	l1.next = l2
	l2.next = l3
	p = Print()
	p.print_list_nodes(l1)
