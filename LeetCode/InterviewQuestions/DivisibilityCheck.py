def Solve(N, A):
    count = 0
    already_checked = set()
    for j in range(len(A)):
        i = A[j]
        if i not in already_checked:
            for k in range(j+1, len(A)):
                if i % A[k] == 0:
                    count += 1
                    already_checked.add(i)
                if A[k] not in already_checked and A[k] % i == 0:
                    already_checked.add(A[k])
        else:
            count+=1
    print(already_checked)
    return count


N = int(input())

A = list(map(int, input().split()))

out_ = Solve(N, A)

print(out_)
