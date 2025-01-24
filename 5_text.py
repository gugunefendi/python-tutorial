# manipulate string with str(), str called string
username = str(input('Input your name: '))
print(username)

# digit and numerals enclosed in quotes are also string
print('90')

# quote inside quote
print('doesn\'t') # output doesn't
# or
print("doesn't") # output doesn't

# if you want character that start with \ represented as special character
# you can use raw string by adding an 'r' before the first quote
print("C:\\directory\name")     # output C:\directory
                                # ame
print(r"C:\\directory\name") # output C:\\directory\name

# concatenation
# you can use '+' symbol for cancatenation strings
# and '*' for repeat the string
print('Hello' + 'World') # output HelloWorld
print( 3 * 'Yes') # output YesYesYes
print(3 * 'Ok' + 'Good') # output OkOkOkGood

# two or more string literal that enclosed between quotes next to each other are automaticly concatenated
print('Py' 'thon') # output Python


# string can be indexed (subscripted), with the first character having index 0. There is separate character type;
# a character is simply a string of size one
word = 'Python'
print(word[0]) # output 'P' character in position 0
print(word[5]) # output 'n' character in position 5

# indices may also be negative number, to start counting from the right
# negative number start from -1
print(word[-1]) # output 'n' last character
print(word[-2]) # output 'o' second last character
print(word[-6]) # output 'P'

# slicing string
print(word[0:2]) # output Py; character from position 0 (included) to 2 (exclude)
print(word[2:5]) # output tho; character from position 2 (included) to 5 (exclude)
print(word[:2])  # output Py; character from the beginning to position 2 (excluded)
print(word[4:])   # output on; characters from position 4 (included) to the end
print(word[-2:])  # output on; characters from the second-last (included) to the end

# count length of string
randomtext = 'asdanfkfhiue[[wf*&52sdnc.znvlksaghliufdag'
print(len(randomtext))