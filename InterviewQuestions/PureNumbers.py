def Solve (N):
    # your code goes here
    arr, i, start = ["44","55"], 2, 1
    if i>=N:
        return arr[N-1]
    while i<N:
        start = i
        temp = ["4" + a + "4" for a in arr]
        if i+len(temp)>=N:
            arr=temp
            break
        temp += ["5" + a + "5" for a in arr]
        i += len(temp)
        arr = temp
    return arr[N-start-1]


T = input()
for _ in range(T):
    N = input()

    out_ = Solve(N)
    print(out_)