
#t = 0,
#n_rev =5432


n = int(input())

n_rev = 0

t = n
while t:
    r = t%10
    n_rev*=10
    n_rev += r
    
    t = t//10

    # if t !=0:
    #     n_rev*=10

if n == n_rev:
    print('YES')
else:
    print('NO')