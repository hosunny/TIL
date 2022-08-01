t = int(input()) # T를 받고
for i in range(t): # A, B를 받고
    a, b = map(int, input().split())
    # 최소공배수는 A와 B를 곱한 값을 A와 B의 최대공약수로 나눈 값이다.
    for j in range(1, min(a, b)+1):
        if a % j == 0 and b % j == 0:
            l = j
    
    print ((a * b) // l)