# manipulate string with str(), str called string
name = str(input('Input your name: '))
print(name)

# digit and numerals enclosed in quotes are also string
print('90')

# quote inside quote
print('doesn\'t') # output doesn't
# or
print("doesn't") # output doesn't

# if you want character that start with \ represented as special character
# you can use raw string by adding an 'r' before the first quote
print('C:\some\name')   # output C:\some
                        # ame
print(r'C:\some\name') # output C:\some\name

# concatenation
# you can use '+' symbol for cancatenation strings
# and '*' for repeat the string
print('Hello' + 'World') # output HelloWorld
print( 3 * 'Yes') # outpur YesYesYes

print('Py' 'thon')
