
n = int(input("lotfan tedad nomarat ra vared konid: "))

list_nomre = list(range(n))

for i in range(n):
    list_nomre[i] = int(input())


s = 0
for nomre in list_nomre:
    s+=nomre

print(s/n)