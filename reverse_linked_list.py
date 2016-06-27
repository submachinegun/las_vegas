from data_structure import ListNode


class Solution(object):

  def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur, pre = head, None
    while cur is not None:
      next = cur.next
      cur.next = pre
      pre = cur
      cur = next
    return pre
