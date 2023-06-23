A, B = map(int, input().split())
S = 0
i = A
while i <= B:
    S += i
    i += 1
print(S)

A = float(input())
N = int(input())
p = 1
i = 1
while i <= N:
    p *= A
    print(p)
    i += 1
