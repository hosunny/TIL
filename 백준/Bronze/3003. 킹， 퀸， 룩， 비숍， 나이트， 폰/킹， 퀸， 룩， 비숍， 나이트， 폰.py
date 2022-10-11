white = list(map(int, input().split()))

# 원래 말의 개수 list
black = [1,1,2,2,2,8]

for i in range(6):
    x = black[i] - white[i]
    print(x, end = ' ')