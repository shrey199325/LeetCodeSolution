"""

class inter():
    pass


class B:
    def alpha(self):
        print("B")

class C:
    def alpha(self):
        print("C")

class A(metaclass=inter, B, C):
    def alpha(self):
        super(B, self).alpha()

    @staticmethod
    def stat_method(val):
        return val

    @classmethod
    def class_method(cls):
        pass


A.class_method()
A.stat_method(10)"""


"""
DS:
insert(), find(), del(), get_random()
O(1)
2,6,8,9,9,11,4


arr = [2,6,8,9,11]

i = 5
map_node = {
    2: (0),
    6: (1),
    8: (2),
    9: (3),
    11: 4
}


def del_(val):
    pass
    # add_ = map_node[val]
    # map_node.remove(val)
    # set = {hash(id(2)): id(2)}


# add_set = {id(2), id(6), ...}
"""


"""
m*n
rows and columns are sorted

2  3  4  5  6
7  8  9  10 11
12 13 14 15 16
17 18 19 20 21

m+n





# I1(2,14)  I2(5, 6)  I3 (17, 19), I4 (20,21) I5(2,8)

      I
  I1 I2 I3
"""