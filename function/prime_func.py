
def is_prime(n):
    j = 2
    while j*j<=n:
        if n%j==0:
            return False
        j+=1

    # True or False 
    return True


def solve(l,r):
    for i in range(l,r+1):
        if is_prime(i):
            for k in range(i+1,i+3):
                if is_prime(k):
                    return 'Yes'
    return 'No'



l,r = 100, 110
print(solve(l,r))