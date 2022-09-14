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
            min_ = None
            rec_dict = None
            for index, i in enumerate(lists):
                if not i:
                    continue
                if min_ is not None and i.val<min_:
                    min_, rec_dict = i.val, index
                elif min_ is None:
                    min_, rec_dict = i.val, index
            res.add_node(ListNode(min_))
            lists[rec_dict] = lists[rec_dict].next
        return res.root


class Solution2:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) > 1:
            merged_lists = []
            for i in range(1, len(lists), 2):
                merged_lists.append(self.merge_two_lists(lists[i - 1], lists[i]))
            lists = merged_lists
        return lists

    @staticmethod
    def merge_two_lists(l1, l2):
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
