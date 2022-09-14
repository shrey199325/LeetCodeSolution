"""


char_set = (‘a’, ‘b’, ‘c’, ‘d’, …) with N distinct characters

example of tuples of size 1 : (‘a’), (‘b’), (‘c’),
example of tuples of size 2 : (‘a’, ‘b’), (‘a’, ‘c’), (‘b’, ‘c’), (‘b’, ‘a’),
example of tuples of size 3 : (‘a’, ‘b’, ‘c’), (‘a’, ‘b’, ‘d’), (‘a’, ‘c’, ‘d’),

where a tuple is an ordered permutation of unique character sequence.

Q1: Write a program to produce all the possible tuples of size K given char_set of N characters, where K <= N

a  + fn(list_[1:], num)
"""


from typing import List, Dict, Any


# Row table:
records = [
    { 'name': 'John', 'age': 50, 'gender': 'M', 'weight': 160, 'height': 180 },
    { 'name': 'Mary', 'age': 26, 'gender': 'F', 'weight': 110, 'height': 160 },
    { 'name': 'Phil', 'age': 35, 'gender': 'M', 'weight': 200, 'height': 185 },
    { 'name': 'George', 'age': 17, 'gender': 'M', 'weight': 150, 'height': 100 },
    { 'name': 'Alison', 'age': 65, 'gender': 'F', 'weight': 90, 'height': 155 },
    { 'name': 'Steve', 'age': 44, 'gender': 'M', 'weight': 182, 'height': 175 }
]


# Column table:
attrs = {
'gender': ['M', 'F', 'M', 'M', 'F', 'M'],
'age': [50, 26, 35, 17, 65, 44],
'name': ['John', 'Mary', 'Phil', 'George', 'Alison', 'Steve'],
'weight': [160, 110, 200, 150, 90, 182],
'height': [180, 160, 185, 100, 155, 175]
}


def solution(records: List[Dict[Any, Any]]) -> Dict[str, List[Any]]:
    attrs = dict()
    for index, elem in enumerate(records):
        for key, val in elem.items():
            if key not in attrs and index == 0:
                attrs[key] = [val]
            elif index > 0 and key not in attrs:
                attrs[key] = [None] * (index + 1)
                attrs[key].append(val)
            else:
                attrs[key].append(val)
    return attrs


# print(solution(records))


def solution_rev(attrs: Dict[str, List[Any]]) -> List[Dict[Any, Any]]:
    records = []
    for key, val in attrs.items():
        if len(records) == 0:
            for elem in val:
                records.append({key: elem})
        else:
            for index, elem in enumerate(val):
                records[index][key] = elem
    return records


# print(solution_rev(attrs))

