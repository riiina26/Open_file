def get_products(filename='recipes.txt'):
    with open(filename, encoding='utf8') as recipes:
        cook_book = {}
        for line in recipes:
            recipe_name = line.strip().lower()
            cook_book[recipe_name] = list()

            ingredients_count = int(recipes.readline().strip())

            for i in range(ingredients_count):
                ingredient = recipes.readline().strip().split(' | ')

                ingredient_name = ingredient[0].lower()
                ingredient_quantity = int(ingredient[1])
                ingredient_measure = ingredient[2]

                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': ingredient_quantity,
                    'measure': ingredient_measure
                }

                cook_book[recipe_name].append(ingredient)

            recipes.readline()

    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)

cook_book = get_products()
create_shop_list(cook_book)



