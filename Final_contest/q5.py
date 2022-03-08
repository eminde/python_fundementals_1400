

f = int(input())
# f_poly = []
# f_line = input().split()
# for zarib in f_line:
#     f_poly.append(int(zarib))

f_poly = list(map(int,input().split()))

g = int(input())
g_poly = []
g_line = input().split()
for zarib in g_line:
    g_poly.append(int(zarib))

x = int(input())

g_x = 0 
for i in range(g+1):
    g_x += g_poly[i]*(x**(g-i))

fg_x = 0
for i in range(f+1):
    fg_x += f_poly[i]*(g_x**(f-i))

f_x = 0
for i in range(f+1):
    f_x += f_poly[i]*(x**(f-i))

gf_x = 0
for i in range(g+1):
    gf_x += g_poly[i]*(f_x**(g-i))

if fg_x>= gf_x :
    print("FOG", fg_x)
else:
    print("GOF", gf_x)