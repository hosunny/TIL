num = int(input())
lst = []
for i in range(1, num+1):
    t = list(map(int, input().split()))
    lst.append(t)


for i in range(num):
    A = 1
    for j in range(num):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            A += 1
    print(A, end = ' ')