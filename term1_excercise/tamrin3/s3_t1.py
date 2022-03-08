
n = int(input())

n= n+1
while True:

    j = 2
    #j<n**0.5
    while j*j<n:
        if n%j==0:
            n+=1
            break
            j+=1
    else:
        print(n)
        break

#time limit exceed! sqrt
