#!/usr/bin/env python


import sys
sys.path.insert(0, '../data_structure')
from data_structure.TreeNode import TreeNode
import collections

class Myclass:
	"""
	Given a binary tree, find all leaves and then remove those leaves. Then repeat the previous steps until the tree is empty.

Example:
Given binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Returns [4, 5, 3], [2], [1].

Explanation:
1. Remove the leaves [4, 5, 3] from the tree

          1
         / 
        2          
2. Remove the leaf [2] from the tree

          1          
3. Remove the leaf [1] from the tree

          []         
Returns [4, 5, 3], [2], [1].

	"""
	def find_all_leaves(self, root):
		"""
		:type root: TreeNode
		:rtype [[TreeNode]]
		"""
		ret = collections.defaultdict(list)
		if not root:
			return ret
		self.find_all_leaves_helper(root, ret)
		return ret.values()

	def find_all_leaves_helper(self, root, ret):
		"""
		:type root: TreeNode
		:type ret: {}
		:rtype: int
		"""
		if not root:
			return -1
		level = 1 + max(self.find_all_leaves_helper(root.left, ret), self.find_all_leaves_helper(root.right, ret))
		ret[level].append(root.val)
		return level
	
	def find_all_leaves_remove(self, root):
		ret = []
		while root:
			level = []
			root = self.find_all_leaves_remove_helper(root, level)
			ret.append(level)
		return ret

	def find_all_leaves_remove_helper(self, root, level):
		if not root:
			return None
		if not root.left and not root.right:
			level.append(root.val)
			return None
		root.left = self.find_all_leaves_remove_helper(root.left, level)
		root.right = self.find_all_leaves_remove_helper(root.right, level)
		return root
			

if __name__ == '__main__':
	m = Myclass()
	root, r2, r3, r4, r5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
	root.left = r2
	root.right = r3
	r2.left = r4
	r2.right = r5
	print m.find_all_leaves(root)
	print m.find_all_leaves_remove(root)
