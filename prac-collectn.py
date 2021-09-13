mylist = ['History','Math','Physics', 'Compsci']
course = ['Art', 'Education']
# slicing
# print(max(mylist)) min max sum len sorted - these have no impact on original
mylist.append('Art') # add item to last
mylist.insert(0, 'Art') # add at specific place
mylist.extend(course) # add individual items of a list to another list
print(mylist.append(course))
# mylist.remove('Art') #removes 1 occurance of the item in list
popped = mylist.pop(-2) # remove last item by default and returns value
# new_list = sorted(mylist, reverse=True) # original is not changed
# mylist.sort() default ascending
# mylist.sort(reverse=True) # original is changed
print(mylist.index('Art')) # returns index of the item
print('Bio' in mylist) # check if the item is present

# for index, item in enumerate(mylist):
#     print(f"Value at {index} is {item}")
for index, item in enumerate(mylist, start=1):
    print(f"Value at {index} is {item}")

print(popped)
print(mylist)

seen = set()