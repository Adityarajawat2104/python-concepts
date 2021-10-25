# Quite same as string
courses = ['Maths', 'Bio', 'Chemistry', 'Physics']
            # 1       2         3          4
            #-4      -3        -2         -1
# slicing [begin:end:step] end is exclusive like str
print(courses[0:2])
print(courses[0:-2])

# courses.sort() # sorts the same list, similarly .reversed() reverses the same list
# sorted_courses = sorted(courses) # sorts and returns a new list, similarly reversed(list) returns new list in yields
# reversed_couses = reversed(sorted_courses)


courses.append("Arts") # add at the end
courses.insert(2, "CompSc") # adds at certain index

courses.pop() # remove last element
courses.remove("CompSc") # removes certain element

print(courses.index("Bio")) # returns index of element, value error if not present
print(courses.count("Arts")) # returns count of element, 0 if not present

# print(courses.clear()) clear all elements of the string
# print(courses.extend(courses)) # merge 2 strings and do not remove duplicates

# courses_new = courses.copy() # makes a different copy of the list otherwise same location is refered by both variables
# courses_new.append("Arts")
# print(courses_new)
# print(courses)

# deep copy is used when there are objects inside the list like below

new_courses = ["Arts", "CompSc"]
courses.append(new_courses)
import copy
courses1 = copy.deepcopy(courses)
courses1[-1].append("IT")

print(courses)
print(courses1)

