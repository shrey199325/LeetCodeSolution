#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'incrStack' function below.
#
# The function accepts STRING_ARRAY operations as parameter.
#


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, v: str) -> int:
        self.stack.append(int(v))
        return self.stack[-1]

    def pop(self) -> int:
        self.stack.pop()
        return self.stack[-1] if self.stack else None

    def inc(self, n: str, v: str) -> int:
        inc_value: int = int(v)
        for i in range(min(int(n), len(self.stack))):
            self.stack[i] += inc_value
        return self.stack[-1] if self.stack else None

class Stack2:
    def __init__(self):
        self.stack = []
        self.inc_list = []

    def push(self, v: str) -> int:
        self.stack.append(int(v))
        self.inc_list.append(0)
        return self.stack[-1] + self.inc_list[-1]

    def pop(self) -> int:
        self.stack.pop()
        if len(self.inc_list) >= 2:
            self.inc_list[-2] += self.inc_list[-1]
        self.inc_list.pop()
        return self.stack[-1] + self.inc_list[-1] if self.stack else None

    def inc(self, n: str, v: str) -> int:
        inc_value: int = int(v)
        self.inc_list[int(n) - 1] += inc_value
        return self.stack[-1] + self.inc_list[-1] if self.stack else None


def incrStack(operations):
    # Write your code here
    EMPTY = "EMPTY"
    stack = Stack()
    func_call = {
        "push": stack.push,
        "pop": stack.pop,
        "inc": stack.inc
    }
    for i in operations:
        func_tuple = i.split()
        result = (
            func_call[func_tuple[0]]() if func_tuple[0] == "pop" else
            func_call[func_tuple[0]](*func_tuple[1:])
        )
        print(result if result is not None else EMPTY, end="\t")

def incrStack2(operations):
    # Write your code here
    EMPTY = "EMPTY"
    stack = Stack2()
    func_call = {
        "push": stack.push,
        "pop": stack.pop,
        "inc": stack.inc
    }
    for i in operations:
        func_tuple = i.split()
        result = (
            func_call[func_tuple[0]]() if func_tuple[0] == "pop" else
            func_call[func_tuple[0]](*func_tuple[1:])
        )
        print(result if result is not None else EMPTY, end="\t")

A = [
    ["push 1", "inc 1 -1", "pop"],
    ["push 1", "push 2", "push 3", "push 1", "push 0", "push 10", "inc 2 100", "inc 2 100", "inc 2 100", "inc 2 100", "pop", "pop", "pop", "pop", "pop", "pop"]
]
print("Solution1")
for i in A:
    incrStack(i)
    print()
print("Solution2")
for i in A:
    incrStack2(i)
    print()