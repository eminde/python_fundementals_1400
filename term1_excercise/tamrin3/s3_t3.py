

n = int(input())

i = 0
while i<n:

    c=0
    while c < n-(i+1):
        print(end=' ')
        c+=1

    j = 0
    while j<i+1:

        fact_i = 1
        i_c =1
        while i_c<=i:
            fact_i*=i_c
            i_c+=1

        fact_j = 1
        j_c = 1
        while j_c<j+1:
            fact_j*=j_c
            j_c+=1

        fact_ij=1
        ij_c = 1
        while ij_c<i-j+1:
            fact_ij*=ij_c
            ij_c+=1

        a_ij = fact_i//(fact_j*fact_ij)
        print(a_ij, end=" ")  

        j+=1  

    # for new line
    print()
    i+=1



