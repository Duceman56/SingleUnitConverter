print("Feet to Meter Conversion")
x = int(input("Input object length in feet: "))
print("You entered: " + str(x))

if x >= 0: 
    print("Acceptable number")
else : 
    exit(print("ERROR! Positive value needed!"))

converted_unit = round((x/3.281), 3)
print(converted_unit)