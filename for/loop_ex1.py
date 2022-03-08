


list_nomre = []

while True:
    n = float(input("lotfan nomre nomarat ra vared konid: "))

    if n == -1 :
        break

    list_nomre.append(n)


s = 0
for nomre in list_nomre:
    s+=nomre

print(s/len(list_nomre))