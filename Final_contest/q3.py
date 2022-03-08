
n = int(input())

num_books = 0
ali_wallet = 0

for _ in range(n):
    allowance ,book_price = [int(i) for i in input().split()]
    ali_wallet += allowance

    if ali_wallet >= book_price:
        num_books += 1
        ali_wallet -= book_price
    
print(num_books)    