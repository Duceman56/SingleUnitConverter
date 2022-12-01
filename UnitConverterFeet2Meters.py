print("Feet to Meter Conversion")
len = float(input("Input object length in feet: "))
print("You entered: " + str(len))

if len >= 0: 
    print("Acceptable number")
    converted_unit = round((len/3.281), 3)
    print(str(converted_unit) + " meters")
else : 
    print("ERROR! Positive value needed!")


print("All purpose linear unit convertor")
type = str(input("What unit will be inputed? (Ex. Miles, Meters, Inches, etc.): "))
len = float(input("Input length: "))
print("you entered " + str(len) +" "+ str(type))
