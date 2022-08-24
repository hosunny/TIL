for T in range(1, 11):
    N = int(input())
    angry = list(map(int, input().split()))
    i = 1
    print(f'#{N}', end=' ')
    while True:
        angry.append(angry.pop(0) - i)
        i += 1
        if i == 6:
            i = 1
        if angry[-1] <= 0:
            angry[-1] = 0
            break
    for j in angry:
        print(j, end=' ')
    print()