
a = int(input())
a_poly = list(range(a+1))
for i in range(a+1):
    a_poly[i] = int(input())

b = int(input())
b_poly = list(range(b+1))
for i in range(b+1):
    b_poly[i] = int(input())


if a<b:
    for i in range(-1, -a-2, -1):
        b_poly[i] += a_poly[i]
    print(b_poly)
else:
    for i in range(-1, -b-2, -1):
        a_poly[i] += b_poly[i]
    print(a_poly)