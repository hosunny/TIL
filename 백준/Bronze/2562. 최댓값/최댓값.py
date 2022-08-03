i = 0
lst = []
while i < 9 :
    num = int(input())
    lst.append(num)
    i += 1
A = max(lst)
B = lst.index(max(lst))
print(A)
print(B + 1)