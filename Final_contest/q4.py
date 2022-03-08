
l ,r = [int(i) for i in input().split()]


############Solution 1 #############

prime_nums = []

for i in range(l,r+1):
    n=i
    j = 2
    while j*j<=n:
        if n%j==0:
            break
        j+=1
    else:
        prime_nums.append(i)

if len(prime_nums)<2:
    print("NO")
else:
    for i in range(len(prime_nums)-1):
        if prime_nums[i+1]-prime_nums[i]<=2:
            print("YES")
            break
    else:
        print("NO")  


############ Solution 2 #############
# end = False

# for i in range(l,r+1):

#     avvali = False

#     n=i
#     j = 2
#     while j*j<=n:
#         if n%j==0:
#             break
#         j+=1
        
#     else:
#         avvali = True

#     # print(i , avvali)

#     if avvali:
#         for k in range(2):
#             n= i+k+1
#             j = 2
#             # print(n)
#             while j*j<=n:
#                 if n%j==0:
#                     break
#                 j+=1
#             else:
#                 if end == False:
#                     # print(i,n)
#                     print('YES')
#                     end = True
#                     break

# if end == False:
#     print('NO')
    
