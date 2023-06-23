N = int(input())
fact = 1
i = 1

while i <= N:
    fact *= i
    i += 1
    print(fact)

fact = 1
s = ""
i = 1

while i <= N:
    fact *= i
    s += str(fact) + " "
    i += 1

print(s)
