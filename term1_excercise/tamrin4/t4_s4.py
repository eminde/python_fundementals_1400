

a = int(input())
a_poly = list(range(a+1))
for i in range(a+1):
    a_poly[i] = int(input())

b = int(input())
b_poly = list(range(b+1))
for i in range(b+1):
    b_poly[i] = int(input())


c_poly = list(range(a+b+1))

for i in range(len(c_poly)):
    c_poly[i] = 0

for i in range(a+1):
    for j in range(b+1):
        c_poly[i+j] += a_poly[i] * b_poly[j]

print(c_poly)

# a = [1,3,5]
# b = [2,4,6,9]
# c = [0,0,0,0,0,0]
