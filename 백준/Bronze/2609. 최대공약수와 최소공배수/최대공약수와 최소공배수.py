A, B = map(int, input().split())
C = min(A, B)
D = max(A, B)
for i in range(C, 0, -1) :
    if D % i == 0 and C % i == 0 :
        print(i)
        print(int(A * B / i))
        break