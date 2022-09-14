def Solve(N,A):
    # write your code here
    # return your answer
    min_diff, res_dict = None, dict()
    for i in A:
        if i==0:
            return 0
        sign = -1 if i<0 else 1
        min_diff = i*sign if min_diff is None else min(i*sign, min_diff)
        if min_diff==(i*sign):
            if (min_diff) in res_dict:
                res_dict[min_diff] = i if res_dict[min_diff]<i else res_dict[min_diff]
            else:
                res_dict[min_diff] = i
    return res_dict[min_diff]


N = int(input())

A = list(map(int,input().split()))

out_ = Solve(N,A)

print(out_)