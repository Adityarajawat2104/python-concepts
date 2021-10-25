# Strings prac
# message = 'hello world'
# message.replace("world", "universe") #string are immutable
# new_message = message.replace("world", "universe") #string are immutable
# print(len(message))
# print(message[0])
# print(message[0:5]) [start:stop:step] step skip number of characters
# print(message[:5])
# print(message.count("l"))
# print(message[message.find('world'):])
# print(message[message.index('world'):])
# print(new_message.upper())
# print(new_message.lower())
# print(new_message.startswith("Hello"))
# print(new_message.endswith("asdfasdfasdf"))
# print(new_message.split("asdfasdfasdf"))

s = "Hey there! what should this string be?"
# # Length should be 20
# print("Length of s = {0}".format(len(s)))
# print(f"Length of s = {len(s)}")
# print(s[0:10:3])

print("Hey" in s) # in operator is used to check if substr exist in string (Case sensitive)

# print(s.index("z")) # give index of 1st occurence of the char/str, throws value error if not present
# print(s.find("z")) # give index of 1st occurence of the char/str, returns -1 if not present
# print(s.count("z")) # give number of occurence of the char/str, returns 0 if not present

str1 = "hello"
str2 = "world"
# message = "{}, {}".format(str1, str2)
message = f"{str1}, {str2}"
# print(str1 + ", " + str2)
# print(message)

print(message.split(" "))

my_message = "Hello World"

print(my_message[::-1])

s1 = "Aditya"
s2 = s1.encode().decode() #define str with same value but different location in memory

print(s1 == s2) #True
print(s1 is s2) #False

s3 = '-'.join(['a','b','c'])
print(s3)


sentence = "It was a stormy night\nThe house creeked\nThe wind blew."
sentence.splitlines()
#=> ['It was a stormy night', 'The house creeked', 'The wind blew.']

print('One1'.isalpha())
print('One'.isalpha())

print('1'.isalnum())
print('hey1'.isalnum())

print('1'.isnumeric())
print('hey1'.isnumeric())

# string.lstrip() #=> 'string of whitespace    '
# string.rstrip() #=> '  string of whitespace'
# string.strip() #=> 'string of whitespace'

print('florida dolphins'.capitalize())
print('florida dolphins'.title())

sentence = "If you want to be a ninja want to be jinja"
print(sentence.partition(' want '))



