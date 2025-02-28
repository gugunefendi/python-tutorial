# Binding or parenthesized expression, list display, dictionary display, set display

# ( expressions... )
# [ expressions... ], { key: value... }
# { expressions }

# binding expression
a = ( 1 + 2 ) * 3 
print( a )

# list display
numbers = [ 10, 12, 15, 18 ]
print( numbers )

# dictionary display
user = { 'name': 'Gunawan' } # key: value
print( user[ 'name' ] )

# set display
score = { 23, 87, 99 }
print( score )


# await expression
# await x


# Exponentiation
# **
exponentiation = 2**3 # it same with 2 * 2 = 4 * 2 = 8 
print( exponentiation )

# Positive, negative, bitwise NOT
# +x, -x, ~x
number = 5
positive_number = +number # 5
negative_number = -number # -5
bitwise_not = ~number # -6
print( positive_number )
print( negative_number )
print( bitwise_not )


# Multiplication, matrix multiplication, division, floor division, remainder
# *, @, /, //, %
# multiplication
print( 4 * 2) # output 8

# matrix multiplication
import numpy as np

matrix1 = np.array([[ 1, 2 ], [ 3, 4 ]])
matrix2 = np.array([[ 5, 6 ], [ 7, 8 ]])
result_matrix_multiplication = matrix1 @ matrix2
print( result_matrix_multiplication ) # result [[ 19 22 ] [ 43 50 ]]

# division
print( 7 / 2 ) # output 3.5

# floor division
print( 7 // 2 ) # output 3 // round to bottom

# remainder or modulus
print( 7 % 2 ) # output 1

# Addition and subtraction
# +, -

# addition
print( 5 + 5 ) # output 10

# subtraction
print( 6 - 2 ) # output 4


# Shifts # Bit manipulation in binner
# <<, >>
originalNumber = 8
left_shift = originalNumber << 2 # geser 2 bit ke kiri
# 00001000 << 2 menjadi 00100000 (setara dengan 8 * 2^2 = 32)
print( left_shift ) # output 32

right_shift = originalNumber >> 2 # geser 2 bit ke kanan
# 00001000 >> 2 menjadi 00000010 (setara dengan 8 // 2^2 = 2)
print( right_shift ) # output 2


# Bitwise AND
# &
print( 6 & 3 ) # output 2
# 6 in biner: 0100
# 3 in biner: 0011
# 0100 & 0011 = 0010 (in decimal 2)

# Bitwise XOR
# ^
print( 6 ^ 3 ) # output 5


# Bitwise OR
# |
print( 6 | 3 ) # output 7


# Comparisons, including membership tests and identity tests
# in, not in, is, is not, <, <=, >, >=, !=, ==

# sample in lists
fruits = [ 'apple', 'banana', 'cherry' ]
print('apple' in fruits) # output True
print('grape' not in fruits) # output True

# sample in string
text = 'Hello world'
print('Hello' in text) # output True
print('Python' not in text) # output True

# Identity Tests. is, is not ( use to check is two object has same object in memory (not only same value) )
# sample with number
a = 10
b = 10
print( a is b ) # output: True because number is immutable in python

# sample with lists
list1 = [ 1, 2, 3 ]
list2 = [ 1, 2, 3 ]
print( list1 == list2 ) # output True ( vlue is same )
print( list1 is list2 ) # output False ( object in different memory )

# use 'is not'
print(a is not b)  # Output: False
print(list1 is not list2)  # Output: True

number1 = 10
number2 = 20

# Kurang dari dan lebih dari
print(number1 < number2)   # Output: True
print(number1 > number2)   # Output: False

# Kurang dari atau sama dengan, lebih dari atau sama dengan
print(number1 <= 10)  # Output: True
print(number2 >= 15)  # Output: True

# Tidak sama dengan
print(number1 != number2)  # Output: True

# Sama dengan
print(number1 == 10)  # Output: True


# Boolean NOT
# not x
registered = True
haveAccount = False
print( not registered )
print( not haveAccount )

isRegistered = False
print( not isRegistered )

# Boolean AND
# and
man = True
woman = False
print( man, woman )

# Boolean OR
# or
software_engineer = True
hardware_engineer = False
position = software_engineer or hardware_engineer
print( position ) # output true because software_engineer is true


# Conditional expression
#if - else
inputName = str(input('Please enter your name: '))
if inputName == 'Christiano Ronaldo':
    print('You are amazing!')
else:
    print(f'Hello {inputName}') # concatenation string recommended use f string for python 3.6+


# if - elif - else
inputNumber = int(input('Please enter an integer: '))
if inputNumber < 0:
    inputNumber = 0
    print( 'Negative change to zero' )
elif inputNumber == 0:
    print( 'Zero' )
elif inputNumber == 1:
    print( 'Single' )
else:
    print( 'More' )


# lambda expression
# lambda expression is anonym function or without name and can be write in single line
# usually use to simple operation

# syntax
# lambda argument: expression

# example
add = lambda x, y: x + y
print(add(12, 12)) 

# lambda with function map and filter
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# Assignment Expression
# :=
# assignment expression or walrus operation use to assignment value to variable as part from expression
# this fitur introduced in python 3.8
# syntax: variable := expression

# sample reduce repitition
if (n := len('Python')) > 5:
    print(f'Panjang string lebih dari 5: {n}')

# use in loop
fruits = ['apple', 'banana', 'cherry']
while (item := fruits.pop(0)) != 'cherry':
    print(f'Mengambil item: {item}')