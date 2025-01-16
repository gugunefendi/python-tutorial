# string to float

# symbol positive will ignore
# symbol is optional you can use + or -
stringWithSymbol = float('+1.23')
print(stringWithSymbol) # output 1.23


# string with space and newline
# space and newline will ignore
stringWithSpace = float('  -12345\n')
print(stringWithSpace) # output -12345.0


# string with scientific notation or notasi ilmiah
# it's same with 1 x 10 pangkat -3, or 1 / 1000
stringWithNotation = float('1e-003')
print(stringWithNotation) # output 0.001


# string with scientific notaion and with positive symbol
# positive symbol does not affect the number
four = float('+1E6')
print(four) # 1000000.0


# string infinity 
# negative symbol mean infinitive negative
# infinity is bilangan tak terhingga
five = float('-Infinity')
print(five) # output -inf


# numbers to float

# decimal
decimal = float(10)
print(decimal) # output 10.0


# float
floatNumber = float(3.14)
print(floatNumber) # output 3.14


# without argument
noArgument = float()
print(noArgument) # output 0.0


# rule string as argument
'''
1. decimal number can have positive or negative symbol + or - (optional)
2. space in front or back will ignore
3. use e or E for eksponent, sample ('1e-003')
4. use 'inf' or infinity (case-sensitive)
5. use nan for NaN (case-sensitive)
6. grouping numbers. You can insert underscore in beetwen digit 
'''

print(float('  123_456.78'))  # Output: 123456.78
print(float('NaN'))          # Output: nan
print(float('Inf'))          # Output: inf
