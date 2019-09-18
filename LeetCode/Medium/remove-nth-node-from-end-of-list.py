"""
19. Remove Nth Node From End of List
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def del_n_from_end(self, node, n):
        if not node:
            return None, n - 1
        node.next, n_new = self.del_n_from_end(node.next, n)
        if n_new == "Done":
            return node, n_new
        elif n_new == 0:
            return node.next, "Done"
        else:
            return node, n_new - 1

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        return self.del_n_from_end(head, n)


# sol = Solution()
# ll = ListNode(1)
# ll.next = ListNode(2)
# ll.next.next = ListNode(3)
# ll.next.next.next = ListNode(4)
# ll.next.next.next.next = ListNode(5)
#
# head, _ = sol.removeNthFromEnd(ll, 3)
#
# while head:
#     print(head.val)
#     head = head.next
