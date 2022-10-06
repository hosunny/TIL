import sys
input = sys.stdin.readline

x=int(input())
n=int(input())

sum=0 #1
for i in range(n):
    a, b = map(int, input().split())
    sum+=(a*b) #2

if x==sum: #3
    print("Yes")
else:
    print("No")

