squares = [ 1, 4, 6, 8, 10 ]
print(squares[0]) # output 1
print(squares[-1]) # output 10
#slicing return new list
print(squares[-3:]) # output [6, 8, 10]

# concatenation 
print( squares + [ 12, 14, 16 ] ) # output 1, 4, 6, 8, 10, 12, 14, 16

# assignment reference
# Simple assignment in Python never copies data. When you assign a list to a variable, 
# #the variable refers to the existing list. Any changes you make to the list 
# through one variable will be seen through all other variables that refer to it.:
rgb = ["red", "green", "blue"]
rgba = rgb
print( id(rgb) == id(rgba) ) # output True
rgba.append("alph")
print(rgb) # output red, green, blue, alph

# slicing element in list
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters) # output [ a b c d e f ]
# slicing 2 - 5
letters[2:5] = ['C', 'D', 'E']
print(letters) # output [ a b C D E f ]
# remove element in list
letters[2:5] = []
print(letters) # output [ a b f ]
# clear all element by replacing all the element with an empty list
letters[:] = []
print(letters) # output []

# length all list
letters_second = ['a', 'b', 'c', 'd']
print(len(letters_second)) # output 4

# nest list
fruits = ['apple', 'banana', 'grape']
vegetables = ['carrot', 'tomato', 'pumpkin']
fruit_and_vegetables = [fruits, vegetables]
print(fruit_and_vegetables) # output [['apple', 'banana', 'grape'], ['carrot', 'tomato', 'pumpkin']]
