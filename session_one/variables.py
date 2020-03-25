# let's cover literals and variables
"""
Python is a strong dynamic typed language, meaning it keeps true with assigned types,
does type checking and does not perform type coersion.
"""
# declare an int
test = 1234
print(test)
print(type(test))
# declare a float
test = 456.789
print(test)
print(type(test))

#integer division
int_div = 2134 // 24
print(int_div)
print(type(int_div))

remainder = 2134 % 24
print(remainder)
print(type(remainder))

float_div = 2134 / 24
print(float_div)
print(type(float_div))

#float division

float_div = 123.456 / 123.25
print(float_div)
print(type(float_div))

print("==================================")

# declare a boolian
is_it_true = True
is_it_false = False
print(is_it_true)
print(type(is_it_true))
print(is_it_false)
print(type(is_it_false))

print("==================================")
# declare a string
this_is_me = "This is a nice little string wiht stuff."
print(this_is_me)
print(type(this_is_me))
this_is_other = 'This is another one of those.'
print(this_is_other)
print(type(this_is_other))
# Create a type error
print("Let's try to create a type error")

my_string_val = "This is a string and an int "
my_int_val = 1
test = my_string_val + str(my_int_val)
print(test)
# test = "This string and an integer" + 1

# no type error for floats and ints

val_float = 123.456
val_int = 789
test = val_float+val_int
print(test)
print(type(test))

# =========== Q & A ===============
print("remainder of 27 % 3 is " + str(27%3))
print("remainder of 27 % 2 is " + str(27%2))
print()

print(int("123"))
print(int("123.345"))