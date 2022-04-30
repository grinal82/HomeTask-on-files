file_name = 'recipes.txt'

def file_processing(file_name: str, mode = 'r', encoding = 'utf-8', data: str =''):
    cook_book = {}
    temp_list = []
    with open(file_name, mode, encoding = encoding) as file:
        for line in file:
            line = line.strip()
            temp_list.append(line)
            
    for i in range(len(temp_list)):
        if temp_list[i].isdigit():
            item = list()
            key = temp_list[i - 1]
            for j in range(1, int(temp_list[i]) +1):
                added_ingredient = dict()
                ingredient = temp_list[i + j].split(" | ")
                added_ingredient['ingredient_name'] = ingredient[0]
                added_ingredient['quantity'] = int(ingredient[1])
                added_ingredient['measure'] = ingredient[2]
                item.append(added_ingredient)
            cook_book[key] = item
    print(cook_book)
    return cook_book

def take_order():
    dishes = input('Введите через запятую заказываемые блюда в расчете на одного гостя:').split(', ')
    person_count = int(input('Введите количество гостей:'))
    dish_list = get_shop_list_by_dishes(dishes, person_count)

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_needed = {}
    data = file_processing(file_name)
    for dish in dishes:
        for ingredient in data[dish]:
            if ingredient['ingredient_name'] not in ingredients_needed:
                ingredients_needed[ingredient['ingredient_name']] = {'measure':ingredient['measure'],'quantity':ingredient['quantity']*person_count}
            else:
                ingredients_needed[ingredient['ingredient_name']]['quantity'] = {
                    ingredients_needed[ingredient['ingredient_name']]['quantity']
                    +(ingredient['quantity']*person_count)}
    return print(ingredients_needed)

def main():
    take_order()
    

if __name__ == "__main__":
    main()




