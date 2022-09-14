"""
A = 10
B = 5
C = 2
D = 1

only 2 people
time = 23 (10+1+9+1+2)
2, 1, 10, 2, 2 = 17
"""


map_ = {100: 2, 2: None, 3: 0}
# print(max(map_, key=map_.get, default=10))
# map_ = {k: v for k, v in map_.items() if v is not None}
# common_scg, max_scg = None, None
# min_, max_ = None, None
# for k, v in map_.items():
#     if v is not None:
#         if not max_ or max_ < v:
#             max_scg, max_ = k, v
#         if not min_ or min_ > v:
#             common_scg, min_ = k, v
common_scg = min(map_, key= lambda x: map_[x] if map_[x] is not None else float("inf"))
max_scg = max(map_, key= lambda x: map_[x] if map_[x] is not None else -float("inf"))
print(max_scg, common_scg)