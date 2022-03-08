
n =22
avvali = False
j = 2
while j*j<n:
    if n%j==0:
        break
    j+=1
    print(j)
else:
    avvali = True

print(n , avvali)