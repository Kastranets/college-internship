N = int(input())
fact = 1
for i in range(1, N+1):
    fact *= i
    i += 1
    print(fact)

fact = 1
s = ""
for i in range(1, N+1):
    fact *= i
    s += str(fact) + " "
    i += 1
print(s)