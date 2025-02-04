# in python numbers divide to 5:
# 1. int
# 2. float
# 3. decimal
# 4. fraction
# 5. complex number

# int (Integer) is whole number that do not have a decimal point. Ex: 10, 30, 100, 234
# float (Floating point) is decimal number or fractions. Ex: 14.5, 3.2, 5.06
# decimal is decimal number with high precision, good for financial calculation. Ex: 10.500, 12.240, 210.987
# fraction is fractional number represented a numerator and denominator. Ex: f = Fraction(3, 4) it same with 3/4
# complex number is numbers that have a real part and imaginary part. Ex: c = 2 + 3j

# int
age = 33
house_of_number = 12
product_quantity = 100
print(f"Age \t\t\t: {age}")
print(f"House of Number \t: {house_of_number}")
print(f"Product Quantity \t: {product_quantity}")



# float
price = 12.500
temperature = 36.6
height = 178.2
print(f"Price \t\t: {price}")
print(f"Temperature \t: {temperature}")
print(f"Height \t\t: {height}")



# decimal
from decimal import Decimal
balance = Decimal('10.500')
interest_rate = Decimal('12.240')
amount_due = Decimal('210.987')
print(f"Balance \t: {balance}")
print(f"Interest Rate \t: {interest_rate}")
print(f"Amount Due \t: {amount_due}")



# fraction
from fractions import Fraction
fraction1 = Fraction(3, 4)  # 3/4
fraction2 = Fraction(5, 6)  # 5/6
fraction3 = Fraction(7, 10)  # 7/10
print(f"Fraction 1 \t: {fraction1}")
print(f"Fraction 2 \t: {fraction2}")
print(f"Fraction 3 \t: {fraction3}")


# complex number
complex_number1 = 2 + 3j
complex_number2 = 1 - 4j
complex_number3 = -3 + 2j
print(f"Complec Number 1 \t: {complex_number1}")
print(f"Complec Number 2 \t: {complex_number2}")
print(f"Complec Number 3 \t: {complex_number3}")



# we can also convert from string, float, and hexadecimal base 16 to integer

# convert from string to int
price_string = '12500'
price_integer = int(price_string)
print(price_integer)

# second sample convert from string to int
random_string = '   -34_535\n'
random_string_to_integer = int(random_string)
print(random_string_to_integer)
# python will ignore white space and ( _ ) underscore read by python like read ( . ) dot

# convert from float to integer
temperature_float = 30.3
temperature_integer = int(temperature_float)
print(temperature_integer)

# convert from hexadecimal base 16 to integer
hexa_decimal_1 = 'A'
hexa_to_int_1 = int(hexa_decimal_1, 16)
print(hexa_to_int_1)

hexa_decimal_2 = 'FACE'
hexa_to_int_2 = int(hexa_decimal_2, 16)
print(hexa_to_int_2)