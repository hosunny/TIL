i = int(input()) 
for j in range(1, i + 1)  :
    x, y = map(int, input().split()) 
    print(f'Case #{j}: {x} + {y} = {x + y}')