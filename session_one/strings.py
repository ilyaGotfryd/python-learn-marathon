"""
In this module we are going to be covering strings, string formatting and string manipilation.
This comment is a multiline string.
"""

# Single line string literal
fisrt_string = "This is a simple string."
second_string = 'This is another stirng.'
fist_string = "This isn't important."
second_string = 'This one contains "double" quotes.'
third_string = "Double quotes can be escaped \" Testing"
print(third_string)
fourth_string = " We have new lines here\n Check us out."
print(fourth_string)
# Multiline string literal
multi_line = """
  And we can have as many lines as we want in here.
  This way when we print it - 
  It shows up as we wrote it.
"""
print(multi_line)

# f-string and f-string formatting
# The old way
number_of_ways = 4
print("This is {} way. But there are {} others. Like {}".format("one", "few", number_of_ways))

first_name = "This"
last_name = "Person"
age = 31

print(f"We are looking at: {first_name} {last_name} of age {age} they are {'young' if age < 30 else 'old' }.")

multi_output = f"""
Name: {last_name}, {first_name}
Age: {age}
"""
print(multi_output)

person = {"first_name": "Bob", "last_name": "Sample", "age": 59}
multi_output = f"""
Name: {person["last_name"]}, {person["first_name"]}
Age: {person["age"]}
Is 59: {person["age"] == 59 }
"""
print(multi_output)


# splitting a string
input_string = "Let's test this string with a bunch of words."
result = input_string.split(" ")
print(result[::2])

chat_command = "!alarm This is outragous!!!"
tokens = chat_command.split(" ")
command = tokens[0]
print(command)
# joining a string
print(tokens)
print(tokens[1:])
phrase = " ".join(tokens[1:])
print(phrase)
my_strings = ["OnlyOne"]
print(" ".join(my_strings))
# stripping leading and trailing spaces
sample_str = "   There are some spaces here before and after   "
print(sample_str.strip())
print(sample_str)
# case manipulation
command = tokens[0].upper()
print(command)
print(f"Is command !ALARM :{command == '!ALARM'}")

command = "!HALP".lower()
print(command)
print("=========== ASSIGNMENT ============")
# let's build a random IP address
"127.234.20.129"
import random
value = random.randint(0,255)
print(value)
ip_vals = []
ip_vals.append(str(random.randint(0,255)))
ip_vals.append(str(random.randint(0,255)))
ip_vals.append(str(random.randint(0,255)))
ip_vals.append(str(random.randint(0,255)))
print(".".join(ip_vals))


print(".".join([str(random.randint(0,255)) for _ in range(4)]))
