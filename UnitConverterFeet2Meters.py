print("All purpose linear unit convertor")

len = float(input("Input length: "))
type = str(input("The units? (Ex. Miles, Meters, Inches, etc.): ")).capitalize()
con_type = str(input("What units to be outputted?: ")).capitalize()
#print("you entered " + str(len) +" "+ str(type))

if type.__eq__("Meter") and con_type.__contains__("Inc"):
    print(str(round(len*39.37, 3)) + " Inches")
else :
        print("Not Today boi")
