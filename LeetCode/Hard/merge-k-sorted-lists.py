"""
23. Merge k Sorted Lists
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self, root=None):
        self.root = root
        self.end = self.root

    def add_node(self, node):
        if not self.root:
            self.root = node
            self.end = self.root
        else:
            self.end.next = node
            self.end = self.end.next
        return self.root

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = LinkedList()
        while any(lists):
            mini = None
            rec_dict = None
            for index, i in enumerate(lists):
                if not i:
                    continue
                if mini is not None and i.val<mini:
                    mini, rec_dict = i.val, index
                elif mini is None:
                    mini, rec_dict = i.val, index
            res.add_node(ListNode(mini))
            lists[rec_dict] = lists[rec_dict].next
        return res.root
