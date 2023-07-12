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


