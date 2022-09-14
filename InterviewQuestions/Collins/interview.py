"""
A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8] -n
A2 = [2, 1, 8, 3] -m
Sort A1 by the sequence in A2 and if there are any remaining integers,
add them in ascending order.
Output = [2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9]
"""


def merger(arr1, arr2):
    i = j = 0
    output = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1
    while i < len(arr1):
        output.append(arr1[i])
        i += 1
    while j < len(arr2):
        output.append(arr2[j])
        j += 1
    return output


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    sorted_arr1 = merge_sort(arr[:m])
    sorted_arr2 = merge_sort(arr[m:])
    return merger(sorted_arr1, sorted_arr2)


def map_sorter(map):
    arr = []
    for key in map.keys():
        while map[key] > 0:
            arr.append(key)
            map[key] -= 1
    arr = merge_sort(arr)
    return arr


def solution(a1, a2):
    map = dict()
    output = []
    for i in a1:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
    for i in a2:
        while map[i] > 0:
            output.append(i)
            map[i] -= 1
        del(map[i])
    if map:
        output.extend(map_sorter(map))
    return output


A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2 = [2, 1, 8, 3]

print(solution(A1, A2))