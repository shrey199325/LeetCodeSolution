'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

sum = ListNode(1)

temp = ListNode(10)
sum.next = temp
temp.next = ListNode(11)

temp = temp.next

temp.next = ListNode(12)


while sum:
    print("{}".format(sum.val))
    sum = sum.next
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = l1.val+l2.val
        sum = ListNode(temp)
        l1, l2 = l1.next, l2.next
        tempVal = None
        carry = 0
        while l1 or l2:
            if l1 and l2:
                temp = (l1.val+l2.val+carry)%10
                if not sum.next:
                    tempVal = ListNode(temp)
                    sum.next = tempVal
                else:
                    tempVal.next = ListNode(temp)
                    tempVal = tempVal.next
                carry = (l1.val+l2.val+carry)/10
            elif l1:
                temp = (l1.val+carry)%10
                if not sum.next:
                    tempVal = ListNode(l1.val)
                    sum.next = tempVal
                else:
                    tempVal.next = ListNode(l1.val)
                    tempVal = tempVal.next
                carry = (l1.val+carry)/10
            else:
                temp = (l2.val+carry)%10
                if not sum.next:
                    tempVal = ListNode(l2.val)
                    sum.next = tempVal
                else:
                    tempVal.next = ListNode(l2.val)
                    tempVal = tempVal.next
                carry = (l2.val+carry)/10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sum
    
