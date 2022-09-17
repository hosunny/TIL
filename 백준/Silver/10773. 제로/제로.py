K = int(input())
lst = [int(input()) for _ in range(K)]
stk = []
for i in lst:
    if i != 0:
        stk.append(i)
    else:
        stk.pop()
print(sum(stk))