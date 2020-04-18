"""
Another very essential part of logic flow is ability to loop. Looping is used in a variety of scenarios:
 - progress over a collection of items
 - repeatedly perform an action until condition is met
 - perform action a set ammount of time
 - create a forever loop that will keep a given program alive, breaking for sleep event, user input, os input
"""

# while loop
# import random
# test = 0
# while test != 10:
#   test = random.randint(0,20)
#   print(f"Test is {test}")

# for loop
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# loop over items in a collection
for day in days:
  print(f"This day is {day}")
  print("What's the next day?")

print("="*20)
# loop over items in a dictionarry
sample_dict = {"one": "first", "two": 2, "three": True, "four": 4.321}
for key, my_val in sample_dict.items():
  print(f"We got key:{key} my_val:{my_val}")
  print(f"my_val type is {type(my_val)}")
  my_val = 1234
print(sample_dict)
print(sample_dict.items())

print("="*20)
another_dict = {"sample": "donkey", "name": "lobster", "age": 24, "married": True, "children": None}
# k, v = ("this", "test")
# import ipdb; ipdb.set_trace()
for k, v in another_dict.items():
  print(f"k: {k} of type {type(k)}")
  print(f"v: {v} of type {type(v)}")
  print("-"*10)
# loop over range - range is a generator

print("+"*20)
items_list = ["1","2","3","four","five"] 
for i in range(5):
  print(f"{i}) {items_list[i]}")

print("+"*20)
for index, val in enumerate(items_list):
  print(f"val:{val} index: {index}")

"""
Python has a very powerful optimized ability to iterate over lists of items and manipulate the output if needed.
It's called comptrehansion
"""
print("+"*20)
#list comprehansion
# convert all the strings with numbers into list of ints
list_of_nums = ["12","73","3","33","42","5"]
result_list = []
for val in list_of_nums:
  new_val = int(val)
  result_list.append(new_val)
print(list_of_nums)
print(result_list)
print('-'*20)
new_list = [int(list_val) for list_val in list_of_nums]
print(new_list)
print('$'*20)
odd_list = [int(list_val) for list_val in list_of_nums if int(list_val)%2 != 0 ]
print(odd_list)

print("------------- DICTIONARRY COMPREHANSION ----------")
#dictionarry comprehansion
# convert dictionarry with nuber strings for values to integers for values
inventory = {"football": "23", "baseball bat": "15", "tent": "5", "soccer shoe": "13", "first aid kit": "75"}
new_inventory = {}
for k,v in inventory.items():
  new_inventory[k] = int(v)

print(inventory)
print(new_inventory)

# get all items in multiples of 5
new_inv = {key.upper():int(value) for key, value in inventory.items() if int(value)%5 == 0 }
print(new_inv)
print(inventory)

print("--------- zip -----------")
# zip generator
# take input list that has keys and values interleaving, use zip and list accessors to convert it to normal dict
inventory_reply = [
  "football",
  "23",
  "baseball bat",
  "15",
  "tent",
  "5",
  "soccer shoe",
  "13",
  "first aid kit",
  "75"
]

items = inventory_reply[::2]
counts = inventory_reply[1::2]
print(items)
print(counts)
print([i for i in zip(items, counts)])
inventory = {k:int(v) for k,v in zip(items, counts)}
print(inventory)
goofy = {v: k for k, v in zip(items, counts)}
print(goofy)
"""
In process of comprehansion it is possible to not only format output, but also filter out the output that is not needed.
"""

# create a list of values divisible by 3 from range

values_by_three = [i for i in range(1,100) if i%3==0]
print(values_by_three)

vals_by_three = []
for i in range(1,100):
  if i%3==0:
    vals_by_three.append(i)

print(vals_by_three)

pract_list = [1,2,3,4,5,6,7,8,12,13,14,15,16]
listdiv3 = [k for k in pract_list if k%3 == 0]
print(listdiv3)
