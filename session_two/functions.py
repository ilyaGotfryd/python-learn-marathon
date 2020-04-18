"""
One of very powerful common constructs in modern languages is function.
It gives you an ability to logically group the code, redistribute and reuse it.
"""

# let's build a greeting function
# 1) print Greetings to you from Python
# 2) pull "Python" out into a variable
# 3) wrap both lines into a function without a parameter - discuss scope
# 4) run code and see that function is not executed
# 5) call declared function
# 6) turn variable with value "Python" into parameter and pass literal to the function
# 7) use formatting from within print to create a greeting and return it, print returned value outside
# import ipdb; ipdb.set_trace()
def greetings_from(name):
  formatted_str = f"Greetings to you from {name}"
  return formatted_str

donkey_lobster = "Python"
result = greetings_from(donkey_lobster)
print(result)
print(greetings_from)
print(type(greetings_from))
#revisit scope

print("---- POsitional Params --------")
# passing positional parameters in
# import ipdb; ipdb.set_trace()
def display_pos_params(first, second, third):
  print(f"first:{first}, second:{second}, third:{third}")

test = "This will work"
display_pos_params(9, test, False)

print("========== KWARGS ============")
# passing in key word arguments
def display_kwargs(one, two, k_one=1, k_two="two", k_three=None, k_four="some val"):
  print(f"one: {one}, two:{two}, k_one:{k_one}, k_two:{k_two}, k_three: {k_three}, k_four:{k_four}")

display_kwargs("first", 2)
display_kwargs(1, "second", k_three="Other then None")
# default values

# beware of mutable default values
def crazy_stuff(dont_mutate_me=[]):
  for i in range(5):
    dont_mutate_me.append(i)
  return dont_mutate_me

print(crazy_stuff(dont_mutate_me=[1,2]))
print(crazy_stuff())
print(crazy_stuff())
print(crazy_stuff())

def less_crazy_stuff(dont_mutate_me=None):
  dont_mutate_me = dont_mutate_me or []
  for i in range(5):
    dont_mutate_me.append(i)
  return dont_mutate_me

print(less_crazy_stuff())
print(less_crazy_stuff())
print(less_crazy_stuff())

def change_arg_value(test_changed):
  test_changed.append("new string value")

value = ["original"]
print(value)
change_arg_value(value)
print(value)
# creating and accessing optional positional parameters and keyword arguments 

# unrolling dictionarry into parameters
print("========== unrolling stuff =============")
kparams_dict = {"one": 1, "three": False, "two": 2.34}

def sample_kwargs(one=0, two=1.0, three=True):
  print(f"one:{one} two:{two} three:{three}")

sample_kwargs()
sample_kwargs(**kparams_dict)

# import ipdb; ipdb.set_trace()
# passing kwargs through without reusing them
def special_function(value, url="", header={}):
  print(f"sending stuff({value}) to {url} with header {header}")

def format_send(one, two, **kwarg):
  fmt_str = f"First:{one}, Second:{two}"
  # print(fmt_str)
  special_function(fmt_str, **kwarg)


format_send("Donkey", "Lobster", url="http://google.com")

print("=========  ALL KWARGS =============")

def all_kwargs(**kwargs):
  for k,v in kwargs.items():
    print(f"k({k}): v:({v})")

all_kwargs(sill="One", donkey="Lobster", truthy=False)

print('========== ALL POSITIONAL ========')
def all_pos_params(*args):
  print(args)

all_pos_params("one", 2, 3.0, False)
# returning multiple values and unrolling them into a tuple

def return_a_tuple():
  return "first", 2, 3.01

one, two, three = return_a_tuple()
print(f"one:{one}  two:{two}  three:{three}")

single = return_a_tuple()
print(single)
# type hints - simple types

# type hints - collection

# yield key word and generators

# switch case using dictionarry and functions (add, sbutract, multiply, divide)

# lambda

# same switch case with lambdas

# closure in lambda - using variable from external scope




