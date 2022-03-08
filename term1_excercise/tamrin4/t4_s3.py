
a = int(input())
a_poly = list(range(a+1))
for i in range(a+1):
    a_poly[i] = int(input())

x = int(input())

sum = 0 
for i in range(a+1):
    sum += a_poly[i]*(x**(a-i))

print(sum)

# 0 x**3 + 1 x**2 + 2 x**1 + 3 x**0

# 0*(2**3) + 1*(2**2) + 2(2**1) + 3