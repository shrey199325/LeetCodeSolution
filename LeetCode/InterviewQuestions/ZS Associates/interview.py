"""
Technical round

arr1 = ["apple", "mango", "mango" "grapes"] -> n
arr2 = ["mango", "papaya", "papaya"] -> m

output -> ["apple", "mango", "mango", "grapes", "papaya"]
"""


def solution(arr1, arr2):
    solution_set1 = set()
    solution_set1.update(arr1)  # O(n)
    sol_set2 = []
    for elem in arr2:              # O(m)
        if elem not in solution_set1:  # O(1)
            sol_set2.append(elem)  # O(1) / s: O(m)
    return arr1 + sol_set2     # O(n+m) / s: O(m+n)


def solution2(arr1, arr2):
    sol_dict = dict() # {"apple": 1}
    for elem in arr1:
        if elem in sol_dict:
            sol_dict[elem] += 1
        else:
            sol_dict[elem] = 1
    for elem in arr2:
        if elem not in sol_dict:
            if elem in sol_dict:
                sol_dict[elem] += 1
            else:
                sol_dict[elem] = 1
    return sol_dict


arr1 = ["apple", "mango", "mango" "grapes"]
arr2 = ["mango", "papaya", "papaya"]
sol = solution2(arr1, arr2)
sol = sorted(sol.items(), key=lambda x: x[1], reverse=True)