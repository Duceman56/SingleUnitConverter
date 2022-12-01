print("Feet to Meter Conversion")
len = float(input("Input object length in feet: "))
print("You entered: " + str(len))

if len >= 0: 
    print("Acceptable number")
    converted_unit = round((len/3.281), 3)
    print(str(converted_unit) + " meters")
else : 
    exit(print("ERROR! Positive value needed!"))