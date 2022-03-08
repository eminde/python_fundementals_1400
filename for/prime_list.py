
prime_numbers = []

for n in range(2,10000):

    for prime in prime_numbers:
        if n%prime == 0:
            break
    else:
        print(n)
        prime_numbers.append(n)


