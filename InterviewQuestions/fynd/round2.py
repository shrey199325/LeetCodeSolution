# node from the end of a Linked List
# n = 2
#        l   r
# Input: aa->bb->cc->dd->ee->ff->ee
# Output: ff


class Solution:
    def solution(self, head, n):
        l = r = head
        for i in range(n-1):
                r = r.next
        while r.next:
            l = l.next
            r = r.next
        return l