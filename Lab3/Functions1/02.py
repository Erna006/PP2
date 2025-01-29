# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature.
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def to_centigrade(f):
    c = (5 / 9) * (f - 32)
    return c
f = float(input("Enter in a Fahrenheit temperature: "))
print(to_centigrade(f))