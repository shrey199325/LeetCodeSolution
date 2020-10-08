# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class LinkedList(object):
    def __init__(self):
        self.root = None
        
    def insert(self, node, new_node):
        if self.root is None:
            self.root = new_node
        elif node.next is None:
            node.next = new_node
        else:
            node.next = self.insert(node.next, new_node)
        return node if node else self.root
            
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = LinkedList()
        while l1 or l2:
            if l1 is None:
                print("Only second linked list is present")
                print("Insert value: {}".format(l1.val))
                return curr.insert(curr.root, l2)
            elif l2 is None:
                print("Only first linked list is present")
                print("Insert value: {}".format(l1.val))
                return curr.insert(curr.root, l1)
            elif l1.val<=l2.val:
                print("inserting val: {}".format(l1.val))
                curr.root = curr.insert(curr.root, ListNode(l1.val))
                l1 = l1.next
            else:
                print("inserting val: {}".format(l2.val))
                curr.root = curr.insert(curr.root, ListNode(l2.val))
                l2 = l2.next
        return curr.root
    

l1 = ListNode(10)
l1.next = ListNode(12)
l1.next.next = ListNode(14)
l2 = ListNode(11)
ll = Solution().mergeTwoLists(l1, l2)
#ll = Solution().mergeTwoLists(l1, None)
print("root: {}".format(ll.val))
while ll.next:
    ll = ll.next
    print("next: {}".format(ll.val))
    
