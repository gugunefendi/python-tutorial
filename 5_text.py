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

# string method
print( str.capitalize( "hello WOrLd" ) ) # capitalize
greeting = 'Good Morning'
print( greeting.count( 'o' )) # count
print( greeting.find( 'd' ) ) # find
print( greeting.index( 'r' ) ) # like find but return error if substring not found
# space
print( " ".isspace() ) # true
print( "\t\t".isspace() ) # true because all character is tab
print( "\n".isspace() ) # true because all character is new line
print( "  a ".isspace() ) # false because have character 'a'
print( "".isspace() ) # false
# UPPER
print( "banana".isupper() ) # false
print( "BANANA".isupper() ) # true
print( "banANa".isupper() ) # false
# join
# str.join(iterable); join string in iterable
fruitlists = ['apple', 'banana', 'mango']
print( " ".join(fruitlists) )
# a type error will be raised if there are any non string values in iterable
dataSample = ['apple', 20, 'banana'] 
# print( " ".join(dataSample) ) # raised type error because there are any int, all value must string
# solution, change int to string
print( " ".join( map( str, dataSample ) ))

# string replace
# change all substring
dataSampleTwo = "Hello world, world is beautiful"
result = dataSampleTwo.replace("world", "Python") # output: Hello Python, Python is beautiful
print(result)

dataSampleThree = "apple apple apple"
result = dataSampleThree.replace("apple", "mango", 2) # if count is given, only the first count occurences are replaced.
print(result) # output: mango mango apple

dataSampleFour = 'hello world'
print( dataSampleFour.split(" "))

# f string
# with f string we can insert expression with placed inside {}
# sample
employee_name   = 'Gunawan'
employee_age    = 33
# with f string we are no need add '+' or format() for concatenation strings
print(f"my name {employee_name} and I am {employee_age} years old")

employee_salary = 50000000
employee_tax    = 5000000
print(f"Your salary: {employee_salary} and tax {employee_tax}. Salary neet { employee_salary - employee_tax }")

# use method
print(f"Employee name: {employee_name.upper()}")

# use date
from datetime import datetime
date_now = datetime.now()
print(f"Now is: { date_now:%d-%m-%Y %H:%M:%S }")