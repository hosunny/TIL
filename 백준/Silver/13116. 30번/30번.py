T = int(input())
for H in range(1, T + 1):
    a, b = map(int, input().split())
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
    print(a * 10)