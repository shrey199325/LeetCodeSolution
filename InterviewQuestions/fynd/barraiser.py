if __name__ == "__main__":
    print("main")


# string palin
# "aaaaaaaaaaaaa"
# "abcbadda"
# o/p = abcba
# "abcd"
# o/p = "a"

class Solution:
    def solution(self, s):
        # write the solution here.
        if len(s) == 1:
            print(s)
            return
        if len(s) == 2:
            if s == s[::-1]:
                print(s)
            else:
                print(s[0])
            return
        max_left = 0
        max_right = 0
        max_diff = -1
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l > max_diff:
                    max_diff, max_left, max_right = r-l, l, r
                l -= 1
                r += 1
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l > max_diff:
                    max_diff, max_left, max_right = r-l, l, r
                l -= 1
                r += 1
        print(s[max_left:max_right+1])

# 0 1   2    3 4
# a a   b    a a
#     l,r
# a a b b a a
#     l r
# a
# aaaaaaa
# s = "aabaa"
# Solution().solution(s)

# s = "aabbaa"
# Solution().solution(s)

# s = "aaaa"
# Solution().solution(s)

# s = "a"
# Solution().solution(s)

# s = "abcbadda"
# Solution().solution(s)

# s = "abccbadda"
# Solution().solution(s)

s = "parrallel"
Solution().solution(s)



"""
Other
#
class Solution:
    @staticmethod
    def solution(s):
        # write the solution here..  
        pass    
      
def main():
  line = input()
  ret = Solution.solution(line)
  print(ret)

if __name__ == '__main__':
    main()


# class Alpha:
#     # def __new__(cls):
#     #     print("new")

#     def __init__(self, a):
#         self.a = a

#     def __call__(self):
#         print("Object call")
    
#     def __str__(self):
#         return "Alpha object"


# obj = Alpha(10)
# obj()
# print(obj)



# Teacher
# Student

# Student.object.get(Q(__starts_with__name="Shrey"))
# select * from Student where name line "Shrey%";
"""