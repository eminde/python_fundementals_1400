

n = 100
while n<10000:

    t=n 
    s = 0
    while t:
        s+= (t%10)**3
        t = t//10

    if s==n:
        print(n)

    n+=1
