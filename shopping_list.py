from pprint import pprint
cook_book = {}
with open ("recepies.txt", "r", encoding="utf-8") as f:
  for line in f:
    dish_name = line.strip()
    number = int(f.readline().strip())
    ingredient_list = list()
    for i in range(number):
      ingredients = {}
      ingredient = f.readline().strip()
      ingredients["name"], ingredients["quantity"], ingredients["measure"] = ingredient.split("|")
      ingredients ["quantity"] = int(ingredients["quantity"])
      ingredient_list.append(ingredients)
    f.readline()
    cook_book[dish_name] = ingredient_list

def get_shop_list_by_dishes(dishes, person_count):
  result = {}
  for i in dishes:
    for j in cook_book[i]:
      result[j['name']] = {'measure':j['measure'],'quantity': int(j['quantity']*person_count)}
  pprint(result)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

