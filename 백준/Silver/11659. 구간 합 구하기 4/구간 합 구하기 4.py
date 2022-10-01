import sys


N, M = map(int, sys.stdin.readline().split())
lst = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(N):
    lst[i + 1] += lst[i]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    print(lst[B] - lst[A - 1])