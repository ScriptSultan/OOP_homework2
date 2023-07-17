# #Задача 1
#
# cook_book = {}
#
# with open('menu.txt', 'r', encoding='utf-8') as cook:
#     text = cook.read()
#     lists = text.strip().split('\n\n')
#
#     for lst in lists:
#         lines = lst.split('\n')
#         dish = lines[0]
#         ingredients = []
#
#         for line in lines[2:]:
#             ingredient_info = line.split(' | ')
#             ingredient_name = ingredient_info[0]
#             quantity = int(ingredient_info[1])
#             measure = ingredient_info[2]
#             ingredient = {
#                 'ingredient_name': ingredient_name,
#                 'quantity': quantity,
#                 'measure': measure
#             }
#             ingredients.append(ingredient)
#
#         cook_book[dish] = ingredients
#
# print(cook_book)
#
# #задача 2
#
# cook_book = {
#     'Омлет': [
#         {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#     'Утка по-пекински': [
#         {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#         {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#         {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#         {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#     'Запеченный картофель': [
#         {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#         {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#         {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
# }
#
#
# def get_shop_list_by_dishes(dishes, person_count):
#     shop_list = {}
#     for dish in dishes:
#         if dish in cook_book:
#             for ingredient in cook_book[dish]:
#                 ingredient_name = ingredient['ingredient_name']
#                 quantity = ingredient['quantity'] * person_count
#                 measure = ingredient['measure']
#                 if ingredient_name in shop_list:
#                     shop_list[ingredient_name]['quantity'] += quantity
#                 else:
#                     shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
#     return shop_list
#
#
# kaka = get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2)
# print(kaka)

#Задача 3

files = ['1.txt', '2.txt']

da = []
net = []

for od_file in files:
    with open(od_file, encoding='utf-8') as f:
        net.append(od_file)
        da.append(f.read().split('\n'))
# с помощью этого FOR сделаем словарь dict_files
dict_files = dict(zip(net, da))

#Далее я сделал сортировку по количеству строк
dada = []

for dd in dict_files.items():
    dada.append(dd)
gaga = sorted(dada, key=lambda dlina: len(dlina[1]))

#Затем я создал новый файл и сделал запись как того требовали в задании.
with open('file.txt', 'w', encoding='utf-8') as res:
    for gege in gaga:
        ga = gege[0]
        napishi_1 = res.write(f'{ga}\n')
        napishi_2 = res.write(f'{len(gege[1])}\n')
        for v_strokah in gege[1]:
            napishi_3 = res.write(f'{ge}\n')

#Эта программа будет работать с любым количеством файлов, если их запишем в список FILES

