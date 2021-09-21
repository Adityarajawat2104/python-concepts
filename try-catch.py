
a = 5
b = 0

try:
    print(a / b)
except:
    print("Invalid value for B")

 # Why finally is required
try:
    print(a / b)
    with open("test.txt", 'r') as f:
        pass
except FileNotFoundError as e:
    print(e)
finally:
    print("Invalid value for B from finally")

print("Invalid value for B")