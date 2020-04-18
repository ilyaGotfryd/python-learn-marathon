"""
There is a variety of ways to evaluate truthiness of something.
"""

# basic truthiness of values
# int
print(f"Value 0 is {bool(0)}")
print(f"Value 1 is {bool(1)}")
print(f"Value -1 is {bool(-1)}")
val = 20
if val:
  print("val is True")
# float
print(f"Value 0.0 is {bool(0.0)}")
print(f"Value 0.1 is {bool(0.1)}")
# collection
print(f"Empty list is {bool([])}")
print(f"List with one element is {bool(['Test'])}")
print(f"List with one element is {bool([0])}")
print(f"List with one element is {bool([False])}") #list is not empty

print(f"Empty Dict is {bool({})}")
print(f"Dict with an element is {bool({0:False})}") # dict is not empty
# None
val = None
print(f"A variable with value None is {bool(val)}")
print(f"Is val equal to None {val is None}")
# string
print(f"Empty string is {bool('')}")
print(f"String with one char is {bool(' ')}")
print(f"String with one char is {bool('0')}")
# undefined
# print(f"A nonexistant varaible is {bool(nemo)}") # does not exist

# comparison - < > == != <= >=

print(f"Aa > Ba string {'Aa' > 'Ba'}")
print(f"is 5 == 5.0 {5 == 5.0}")
print(f"is 5 != '5' {5 != '5'}")

# operator 'and' 'or'

val = 5
print(f"is val {val} between 3 and 7 {val >=3 and val <=7}")
print(f"is val {val} outside of [4..6] {val < 4 or val > 6}")

# in operator
# value in collection
characters = ['a','b','c','d','e', 1, 2, 3]
print(f"is z in the list {'z' in characters}")
print(f"is d in the list {'d' in characters}")
print(f"is 3 in the list {3 in characters}")
# substring in string
print(f" is 'lo' in 'Hello World' {'lo' in 'Hello World'}")
# key in dictionarry
person = {"fname": "John", "lname": "lobster", "age":23}
print(f"does person have age {'age' in person}")

# describe a condition where value is either None or is outside of an interval right value inclusive
val = None
result = val or 'Defaults'

print(f"1)result assigned to {result}")

val = 1
result = val or 'Defaults'

print(f"2)result assigned to {result}")

