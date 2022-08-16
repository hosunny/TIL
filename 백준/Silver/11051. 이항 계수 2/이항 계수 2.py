A, B = map(int, input().split())

AA = 1
BB = 1
for i in range(1, B + 1):
    AA *= A + 1 - i
    BB *= B + 1 - i

print((AA // BB) % 10007)