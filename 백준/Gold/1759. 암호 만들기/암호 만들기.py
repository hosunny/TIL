from itertools import combinations

L, C = map(int, input().split())
alpha = input().split()
alpha.sort()
aeiou = {'a', 'e', 'i', 'o', 'u'}
for i in combinations(alpha, L):
    if 2 <= len(set(i) - aeiou) < L:
        print("".join(i))