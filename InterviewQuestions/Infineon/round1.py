"""
2 log files
correct input
errors
Log1 -- n
INFO: pwd/a1.py: Here is a log -- 1
ERROR: pwd/a1.py: Here is an error1
ERROR: pwd/a1.py: Here is an error1 -- 2
ERROR: pwd/a1.py: Here is an error4 -- 1
Log2 -- m
INFO: pwd/a1.py: Here is a log
ERROR: pwd/a1.py: Here is an error1
ERROR: pwd/a1.py: Here is an error2
ERROR: pwd/a1.py: Here is an error3
ERROR: pwd/a1.py: Here is an error4
"""


def solution(log1, log2):
    log1_map = dict()
    log2_map = dict()
    log1_arr, log2_arr = log1.split("\n"), log2.split("\n")
    ans_log1, ans_log2 = dict(), dict()
    for line in log1_arr:
        log1_map[line] = 1 + log1_map.get(line, 0)
    for line in log2_arr:
        log2_map[line] = 1 + log2_map.get(line, 0)
    for key in log1_map.keys():
        tmp = log1_map[key] - log2_map.get(key, 0)
        if tmp > 0:
            ans_log2[key] = tmp
        elif tmp < 0:
            ans_log1[key] = tmp
        if key in log2_map:
            log2_map.pop(key)
    for key in log2_map.keys():
        ans_log1[key] = key
    return {
        "missing_log1": ans_log1,
        "missing_log2": ans_log2
    }


if __name__ == "__main__":
    log1_dir = "./log1"
    log2_dir = "./log2"
    log1_str, log2_str = "", ""
    log1_map = dict()
    log2_map = dict()
    with open(log1_dir, "r") as f1:
        for line in f1.readlines():
            log1_map[line] = 1 + log1_map.get(line, 0)
    with open(log2_dir, "r") as f2:
        for l in f2.read():
            log2_str += l
    answer = solution(log1_str, log2_str)
    print(answer)
