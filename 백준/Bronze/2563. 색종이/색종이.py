n = int(input())

lst = []
for i in range(n) :
    P = list(map(int, input().split()))
    lst.append(P)

f_lst = []
for i in lst :
    for j in range(i[0], i[0] + 10) :
        for k in range(i[1], i[1] + 10) :
            f_lst.append((j, k))
s_lst = set(f_lst)

print(len(s_lst))