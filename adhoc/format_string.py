

# name = 'ali'
# dars = 'zaban'
# nomre = 20

# print(f'{name} dar {dars} nomre {nomre} ra gereft.')


# x = 4.5 
# print(f'This will print out the variable x: {x}')
# print(f'This will print out the variable x: {x:.3 f}')



# table = ['Sjoerd','Jack','Dcab'] 
# for name in table:
#         print(f'{name:10}') 


# table2 = [4127, 4098,  7678] 

# for num in table2: 

#     print(f'{num:10d}') 



print(f'Number   Square       Cube') 

for x in range(1, 11): 
    x = float(x)
    print(f'{x:<5.2f}       {x*x:>6.2f}          {x*x*x:^8.2f}')