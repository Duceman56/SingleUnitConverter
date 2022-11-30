print("Feet to Meter Conversion")
x = int(input("Input how long the object is in feet: "))
print("You entered: ")
print(x)
if x >= 0: 
    print("Acceptable number")
else : 
    exit(print("ERROR! Positive value needed!"))

converted_unit = (x/3.281)
converted_round = round(converted_unit, 5)
print(converted_round)