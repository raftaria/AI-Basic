import fah_converter


print("Enter a celcius value: ")
celcius = float(input())

fah = fah_converter.convert_c_to_f(celcius)
print("That's {0} degrees Fahrenheit".format(fah))