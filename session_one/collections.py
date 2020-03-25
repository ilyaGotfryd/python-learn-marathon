# Let's cover collections and all the wonderful things we can do with them
# While pandas and numpy do wonders and havevery potent c based paralellized code underneeth them
# Python's native collectinons are quite magnificent and performance optimized themselves.
# We will play with basics of the underlying language and see the power of what we can do right here

## TUPLE
# declare - empty full
first_one = tuple()
print(type(first_one))
one_element = (123,)
print(one_element)
print(type(one_element))
# unrol tuple into coma delimited values
multi_type_tup = ("string here", 123, False, 345.0)
print(multi_type_tup)
my_string, this_int, is_it_though, a_float = multi_type_tup
print(my_string)
print(this_int)
print(is_it_though)
print(a_float)
# access elements
print("==========================")
print(multi_type_tup[2])
# try changing values
# multi_type_tup[3] = "Crazy stuff" - this throws a TypeError exception
multi_type_tup = (123,False, "Yay")
print(multi_type_tup)

print("="*50)
## LIST
# declare - empty, full
empty_list = []
print(empty_list)
print(type(empty_list))
a_list = [1,2,3,4,5,]
print(a_list)
# create using '*' operator
small_list = [0]*20
print(small_list)
small_list = [1,2,3]*10
print(small_list)
matrix = [[1,2,3,4,5]]*5

from pprint import pprint
pprint(matrix)
# access
print('+'*50)
print(small_list[5])
# mutate
alter_me = [2,3,4,5,6]
print(alter_me)
alter_me[3] = "Testing Testing"
print(alter_me)
# pile on different types
alter_me[4] = True
print(alter_me)
# splice - get some from the end, some from the begining, everyother one, etc.
print("="*20 + "SPLICING" + "="*20)
big_list = [i for i in range(100)]
print(big_list)
print(big_list[-1])
print(big_list[-5:])
print(big_list[95:])
print(big_list[:20])
print(big_list[10:20])
print(big_list[10:-10])
print(big_list[::2])
print("qwertyuiopasdfghjklzxcvbnm"[::2])
print(big_list[1::2])
# add lists, append item to list
print("-"*20+"APPENDING LIST" + "-"*20)
small_list = [i for i in range(10)]
small_list.append("A")
print(small_list)
small_list.insert(5, 'B')
print(small_list)
print(dir(small_list))
small_list.reverse()

# print(list_one - list_two) - NOT SUPPORTED

print(small_list)
# randomly select a value out of a list - choices
import random
rnd_val = random.choices(["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"])
print(rnd_val)
# shuffle contents of the list - shuffle
random.shuffle(small_list)
print(small_list)

print("#"*20 + " SET " + "#"*20)
## SET
# declare - empty, full
first_set = set()
print(type(first_set))
second_set = {1,2,3,4,5,5,5}
print(second_set)
print(type(second_set))
# feed a list of repeating elements to a set
list_one = [i for i in range(10)]
list_two = [i for i in range(5,15)]
list_all = list_one + list_two
print(list_all)
print(set(list_all))
print("="*50)
# set math - & | ^
print(list_one)
print(list_two)

print(set(list_one) - set(list_two))
print(set(list_two) - set(list_one))
# print(set(list_one) + set(list_two)) - `+` not supported
print(set(list_one) | set(list_two)) # this is a way to add to sets together
print(set(list_one) & set(list_two))
print(set(list_one) ^ set(list_two))
#access 
# print(dir(set(list_one)))
set_one = set(list_one)
one_val = set_one.pop()
set_one.add(5)
set_one.add(-1)
print(one_val)
print(set_one)
two_val = set_one.pop()
print(two_val)
print(set_one)


## DICTIONARY

# declare - empty, full
first_dict = {}
print(first_dict)
print(type(first_dict))
second_dict = {"first": 123.0, "second": True, "Third": "Some String here"}
print(second_dict)
third_dict = {123.4: "test", "something else": 456}
print(third_dict)

# key, value - is it hashable (try declareing with list)
crazy_dict = {(123, "2020-02-23"): "Some value here", (124, "2020-03-23"): "something else here as well"}
print(crazy_dict)
nice_dict = {"weight": 211.5, "height" : 72, "first_name": "This", "last_name": "Person"}
# bad_dict = {[1,"a"]:"value"} - list is not hashable


#let's try hashing
print("Hashing a string 'Let's see what this does' ")
print(hash("Let's see what this does"))

# access
print(nice_dict["height"])
print(crazy_dict[(124, "2020-03-23")])


# add
pprint(nice_dict)
nice_dict["Middle Name"] = "Wolfgang"
nice_dict["last_temp_reads"] = [98.6, 99.1, 97.8]
pprint(nice_dict)
nice_dict["first_name"] = "DonkeyLobster"
pprint(nice_dict)
# join lists - update
nice_dict.update(crazy_dict)
pprint(nice_dict)


# we will cover comprehansion once we go over loops