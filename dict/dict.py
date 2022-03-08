# car_titles = ['brand', 'year', 'color']
# car_1 = ['pride', 1398, 'sefid']



from audioop import add

 
#car_1 = {'brand':'saipa','model': 'pride','year':1398, 'color':'sefid'}
# print(car_1)
#print(type(car_1))

# car_1['color'] = 'siah'
# print(car_1['brand'])
# print(car_1['sherkatsazandeh'])

# car_1['sherkatsazandeh'] = 'zamiad'
# print(car_1['sherkatsazandeh'])
# print(car_1)

# print(list(car_1.keys()))

# print(list(car_1.values()))

# print(car_1.keys())
# print(car_1.values())
# print(car_1.items())

# for x in car_1:
#     print(x)

# for key in car_1:
#     print(key, car_1[key])

# for value in car_1.values():
#     print(value)

# for key, value in car_1.items():
#     print(key, value)

# x = car_1.pop('brand')
# print(x)
# print(car_1)

## empty dictionary
# empty_dict = {}
# print(type(empty_dict), empty_dict)


# # dict.clear()
# car_1.clear()
# print(car_1)

# membership 

# print('check brand in car_1: ','brand' in car_1)
# print ('check bimeh in car_1: ','bimeh' in car_1)


# namayeshgah = {
#     'car_1':{'brand':'saipa','model': 'pride','year':1398, 'color':'sefid'},
#     'car_2':{'brand':'irankhodro','model': '405','year':1394, 'color':'metalic'},
#     'car_3':{'brand':'bmw','model': 'i8','year':1398, 'color':'siah'}
# }

# # print(type(namayeshgah))
# # print(namayeshgah)
# # print(namayeshgah.keys())
# # print(namayeshgah.values())

# print(namayeshgah['car_1']['brand'])


# adadha = {
#     'fard':[1,3,5,7,9],
#     'zoj':[2,4,6,8],
#     'avval' : [2,3,5,7]
# }


# print(adadha['fard'][2])


# list_a = [['brand', 'saipa'], ['model', 'pride'], ['color','sefid']]
# dict_a = dict(list_a)
# print(dict_a)



# dict.update()
car_1 = {'brand':'saipa','model': 'pride','year':1398, 'color':'sefid'}

print ( 'befor update: ', car_1)
car_update = {'color':'siah', 'year':1400, 'options':'shishe barghi, zabt'}

car_1.update(car_update)

print('after update', car_1)
