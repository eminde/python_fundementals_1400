
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())

n = 0

if a1>b1:
    n+= a1 # n = n+a1
else:
    n+= b1

if a2>b2:
    n+=a2
else:
    n+=b2

if a3>b3:
    n+=a3
else:
    n+=b3

print(n)