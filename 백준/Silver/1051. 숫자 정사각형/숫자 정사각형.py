N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
mm = min(N, M)
MM = max(N, M)
if mm == M:
    lst = list(map(list, zip(*lst)))
result = 1
for j in range(0, mm - 1):
    for k in range(j + 1):
        for x in range(MM - (mm - 1 - j)):
            if lst[k][x] == lst[k + (mm - 1 - j)][x] == lst[k][x + (mm - 1 - j)] == lst[k + (mm - 1 - j)][x + (mm - 1 - j)]:
                result = mm - j
                break
        if result != 1:
            break
    if result != 1:
        break
print(result * result)