
# iterables are data types which can be looped over like str, list, dict etc
mylist = [1, 2, 3]
for item in mylist:
    print(item)

# to check whether variable is iterable dir(variable_name) should have __item__() method
print(dir(mylist))

# iterators are datatypes which remembers where they ie it ie have an state and can get next value and have __next__ method
# iterables with __iter__() / iter() returns iterators
# iterators can only go forward

i_mylist = iter(mylist)
print(i_mylist)
print(dir(i_mylist))