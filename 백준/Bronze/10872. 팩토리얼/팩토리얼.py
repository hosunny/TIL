num = int(input())
if num == 0 :
    print(1)
else:
    ans = 1
    for i in range(1, num+1) :
        ans *= i

    print(ans)