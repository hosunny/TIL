S = input()
for ans in 'abcdefghijklmnopqrstuvwxyz' :
    if ans in S :
        print(S.find(ans))
    else :
        print(-1)