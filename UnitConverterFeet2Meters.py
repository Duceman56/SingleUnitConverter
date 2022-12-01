print("All purpose linear unit convertor")

len = float(input("Input length: "))
type = str(input("The units? (Ex. Miles, Meters, Inches, etc.): ")).capitalize()
print(type)
con_type = str(input("What units to be outputted?: "))
print("you entered " + str(len) +" "+ str(type))

if type.__eq__("Meter") :
    print(type)
else :
        print("no")
