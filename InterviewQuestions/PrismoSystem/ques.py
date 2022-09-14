"""
a-b-c-d

stack_main = a, b
main_browser = c
stack_secondary = d


a, b, c





Q2:

['lion', 'tiger', 'buffalo', 'goat', "elephant"]
arr = [4, 5, 7, 4, 8]
 0  1  2  3  4
max_ = 8
min_ = 4
    +
  + +
  + +
 ++ +
+++++
+++++
+++++
+++++


  *
 ***
8->4
   if arr[i] < max_:
      print("")

"""
from typing import List


def solution(ques: List[str]):
    arr = []
    max_= len(ques[0])
    for i in ques:
        arr.append(len(i))
        max_ = max(len(i), max_)
    while max_ > 0:
        j = 0
        while j < len(arr):
            if arr[j] < max_:
                print(" ", end="")
            else:
                print("+", end="")
            j += 1
        max_ -= 1
        print()


ques = ['lion', 'tiger', 'buffalo', 'goat', "elephant"]
solution(ques)