# diplay a massage
print('hello world')

#Quotes Inside Quotes
print("What's your name")
print('My name is "Joaquim"')

#Assign String to a Variable
name = "Joaquim"
print(name)

#Multiline Strings
msg = """
    Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

print(msg)

#Strings are Arrays
first_name = "Joaquim"
print(first_name[0:3])

#Looping Through a String
fruts = "Banana"
list = []
for x in fruts:
    list.append(x)
print(list)

#String Length
full_name = "Joaquim Adriano Manhoca"
name_lenght = len(full_name)
print(name_lenght)

#Check String
text = "The best things in life are free"
print("free" in text)

if "free" in text:
    print('Yes "Free" is present.')

#Check if NOT
print("expensive" not in text)

if "expensive" not in text:
    print("expensive is not in text")