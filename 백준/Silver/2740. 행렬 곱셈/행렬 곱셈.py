A = []
B = []
for i in range(2) :
    N, M = map(int, input().split()) 
    if i == 0 :
        for a in range(N) :
            A.append(list(map(int, input().split())))
    else :
        for b in range(N) :
            B.append(list(map(int, input().split())))
for i in A :
    lst = []
    for j in range(len(B[0])) :
        X = 0
        for i_2 in range(len(i)) :
            X += i[i_2] * B[i_2][j]
        lst.append(X)
    for k in lst :
        if k == lst[-1] :
            print (k)
        else :
            print(k, end = " ")