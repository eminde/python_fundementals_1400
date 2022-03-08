
n = int(input())

lines = []
saf = []
flag = True
count = 0
for _ in range(n):
    row = input().split()
    if row[1] == '-':
        saf.append(row[0])
        saf.append(row[2])
    if row[2] == '-':
        count+=1
    lines.append(row)

if len(saf)==0:
    flag = False
    print('Impossible')
if count != 1: 
    flag = False
    print('Impossible')

if flag:
    for i in range(n-2):
        for row  in lines:
            if row [0] == saf[-1]:
                if row[2] == '-':
                    break
                if row[1] == saf[-2]:
                    saf.append(row[2])
                else:
                    flag = False
                    
if flag:
    print(saf)