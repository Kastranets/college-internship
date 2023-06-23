A, B = map(int, input().split())
S = 0
for i in range (A, B+1):
    S += i
print(S)

A = float(input())
N = int(input())
p = 1
for i in range(1, N+1):
    p *= A
    print(p)