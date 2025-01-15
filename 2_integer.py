'''
int() function used to convert float, string, hexadecimal, biner
'''

# float to int
rounding = int(123.45) # output 123
print(rounding)

# string to int
convertStringToInteger = int('123') # output 123
print(convertStringToInteger)

# string to integer
stringToInteger = int('   -12_345\n') # python ignore space
print(stringToInteger)

# hexa to integer
hexaToInteger = int('FACE', 16)
print(hexaToInteger)

secondHexaToIntegerint = int('0xface', 0) # 0 can't in front
print(secondHexaToIntegerint)

# biner basis 2
binerToInteger = int('01110011', base=2)
print(binerToInteger)