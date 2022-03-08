
a,b = 10,20


for i in range(a,b+1):

    for j in range(2,i):
        if i%j ==0:
            k = i//j
            print(i, 'barabar ba', j , '*', k)
            break
        
    else:
        print(i , 'adad avval ast!')