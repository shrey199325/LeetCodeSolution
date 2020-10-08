import pdb


class Queue():
    def __init__(self, c):
        self.val = c
        self.prev = None
        

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        cdict = {')':'(', '}':'{', ']':'['}
        closing = [')', '}', ']']
        curr = None
        pdb.set_trace()
        for c in s:
            if c in closing:
                if curr == None:
                    return False
                if cdict[c]==curr.val:
                    curr = curr.prev
                else:
                    return False
            else:
                tmp = Queue(c)
                tmp.prev = curr
                curr = tmp
        return True

print(isValid('{[]}'))
