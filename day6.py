# Slicing Tuples 
"""tpl= ('mango', 'orange', 'grapes', 'apple')
all_items=tpl[1:3]
print(all_items)"""


""""fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)
print(orange_mango)"""

# Syntax
"""tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
print(middle_two_items)
print(all_items)"""

#Exercises: Level 1

#1)Create an empty tuple
tp=()
print(tp)

#2)Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sister=('Sita','Gita')
brother=('Shyam','Hari')
print(sister)
print(brother)

#3Join brothers and sisters tuples and assign it to siblings
siblings=sister + brother
print(siblings)

#4)How many siblings do you have?
print('The count of siblings:',len(siblings))

#5)Modify the siblings tuple and add the name of your father and mother and assign it to family_members
tpl_to_list=list(siblings)
father="Romio"
mother="Juliet"
tpl_to_list.append(father)
tpl_to_list.append(mother)
print('Converting sibling tuples to list',tpl_to_list)
family_member=tuple(tpl_to_list)
print(family_member)


#Exercises: Level 2

#1)Unpack siblings and parents from family_members  (look)
siblings = family_member[:-2]
parents = family_member[-2:]

print("Siblings:", siblings)
print("Parents:", parents)

#2)Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('apple', 'grapes', 'mango', 'banana')
vegetables=('cauliflower', 'onion', 'cabbage', 'radish')
animal_products=('chicken','mutton','fish')
food_stuff_tp= fruits + vegetables + animal_products
print(food_stuff_tp)

#3)Change the about food_stuff_tp tuple to a food_stuff_lt list.
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

#4)Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list. (look)
middle_item_slicing=food_stuff_tp[-6:-5]
print(middle_item_slicing)

#5)Slice out the first three items and the last three items from food_stuff_lt list.
# First 3 items
first_three = food_stuff_tp[:3]

# Last 3 items
last_three = food_stuff_tp[-3:]

print("First three items:", first_three)
print("Last three items:", last_three)

#6)Delete the food_stuff_tp tuple completely.
del(food_stuff_tp)

#8)Check if 'Estonia' is a nordic country.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
checking='Estonia' in nordic_countries
print(checking)

"""9)Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')"""