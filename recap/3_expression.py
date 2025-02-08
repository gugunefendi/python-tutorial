# Documentation url https://docs.python.org/3/reference/expressions.html

# Expression
# Expression is a combination from value, variable, operator or function that evaluated to be a single value.

# Arithmetic Conversions
# Pyhton automatically convert a numeric value to make sure operation runs correctly

# If either argument is a complex number, the other is converted to complex
x = 3 + 4j + 2 # 
print(x) # Output: (5+4j)

# if either argument is a floating-point number, the other is converted to float point
y = 1.2 + 2
print(y) # Output: 3.2

# if all numbers is intger. no one to convert
z = 3 + 5
print(z) # Output: 8


# Expression Literal
# Literals is fixed value whic was written directly, no need to count or recount
# Python support string and bytes literals and various numeric literals

# String literals
# stringliteral ::= [stringprefix](shortstring | longstring)

# stringprefix ::= "r" | "u" | "R" | "U" | "f" | "F" | "fr" | "Fr" | "fR" | "FR" | "rf" | "rF" | "Rf" | "RF"
# Prefix	        Fungsi
# r / R	            Raw string: Escape sequence (\n, \t) considered a normal character
# u / U	            Unicode string (Python 2, no need in Python 3).
# f / F	            F-string: String with expression which can be evaluated.
# fr / rf / Fr / RF	Combination F-string and Raw string.

# short string can use '' or ""
# long string can use '''long string'''
short_string1 = 'Hello' # short string
short_string2 = "Pyhton" # short string
long_string = '''Hello Pyhton
these are 
the long string
''' # long string
print(short_string1)
print(short_string2)
print(long_string)


raw_str = r"C:\Users\NewFolder"  # normal character considered a normal character
print(raw_str)  # C:\Users\NewFolder

formatted_str = f"Nilai: {10 + 5}"
print(formatted_str)  # Nilai: 15

combined_str = fr"Path: {10}\n"
print(combined_str)  # Path: 10\n (raw string ignore \n)
