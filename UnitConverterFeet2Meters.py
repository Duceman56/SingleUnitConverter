print("All purpose linear unit convertor")

len = float(input("Input length: "))
type = str(input("The units? (Ex. Miles, Meters, Inches, etc.): "))
con_type = str(input("What units to be outputted?: "))
print("you entered " + str(len) +" "+ str(type))

capitalize(type)

if type.__contains__("m") :
    print("meter")
else :
        print("no")
