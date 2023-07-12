#Задача 1

cook_book = {}

with open('menu.txt', 'r', encoding='utf-8') as cook:
    text = cook.read()
    lists = text.strip().split('\n\n')

    for lst in lists:
        lines = lst.split('\n')
        dish = lines[0]
        ingredients = []

        for line in lines[2:]:
            ingredient_info = line.split(' | ')
            ingredient_name = ingredient_info[0]
            quantity = int(ingredient_info[1])
            measure = ingredient_info[2]
            ingredient = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients.append(ingredient)

        cook_book[dish] = ingredients

print(cook_book)

#задача 2

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
    return shop_list


kaka = get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2)
print(kaka)

#Задача 3

with open('1.txt', 'r', encoding='utf-8') as txt1:
    i = 0
    for t1, t1_1 in enumerate(txt1):
        i += 1
    print(i)
with open('2.txt', 'r', encoding='utf-8') as txt2:
    g = 0
    for t2, t2_2 in enumerate(txt2):
        g += 1
    print(g)

with open('3.txt', 'w', encoding='utf-8') as yes:
    if t1 > t2:
        yes.write(f'2.txt\n{g}\n{t2_2}\n')
        yes.write(f'1.txt\n{i}\n{t1_1}')

