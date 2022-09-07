T = int(input())

for H in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(sum(lst))