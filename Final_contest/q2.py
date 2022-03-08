
x1, y1, x2, y2 = [int(i) for i in input().split()]

x, y = [int(i) for i in input().split()]


# if x1<x2 and y1<y2:
#     if x2>x>x1 and y2>y>y1:
#         print("YES")  
#     else:
#         print("NO")
# else:
#     if x>x1 and y1>y and x2>x and y2<y:
#         print("YES")
#     else:
#         print("NO")

if(x1 < x < x2 or x2 < x < x1) and (y1 < y < y2 or y2 < y < y1):
    print('YES')
else:
    print("np")


