
p = [0, 4, 8, 6, 2, 10, 100000000]
s=[]
d = {}
rem=10

for i in p:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in range(0,rem/2+1):
    if i in d:
        pair = [i, rem-i]
        if pair[0]==pair[1] and d[i]>=2:
            s.append(pair)
        elif pair[1] in d:
            s.append(pair)
print(s)

#######################################################################################
#######################################################################################

rem55 = set()
golden_val = 10 # The diff we want
result = set()
for ele in p:
    if ele in rem55:
        result.add((ele, golden_val-ele))
    rem55.add(golden_val-ele)

print(result)
