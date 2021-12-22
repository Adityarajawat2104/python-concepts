# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2 - 1.5
# Floor Division: 5 // 2 - 2 (number of times the divisions can be done)
# Exponent (to the power): print(3 ** 2)
# Modulus:        5 % 2 - 1 (remainder after divisions)
# increment / multi/dev/sub num += 1
# is operator check if the variables points to the same object ex a = 2 and b = 2 then a is b is true

# Important note - no matter how many base 2 digits you’re willing to use, the decimal value 0.1 cannot be represented exactly as a base 2 fraction.
# In base 2, 1/10 is the infinitely repeating fraction
# On a typical machine running Python, there are 53 bits of precision available for a Python float,
# so the value stored internally when you enter the decimal number 0.1 is the binary fraction
# 0.00011001100110011001100110011001100110011001100110011010
# Conclusion - fraction values are not stores as it is but in near binary fractions in memory
# decimal module can be used to solve this

num = 5
num += num
print(num)

num1 = '100'
num2 = '200'
# print(round(num))
# print(abs(num2))
print(int(num1) + float(num2)) #casting from str to int

# num *= num
# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2