t = [
    ["inch", (1 / 39.3701)],
    ["foot", (1 / 3.28084)],
    ["kilometer", (1000)],
    ["anyUnit", 42069]
]

def convertToUnit(inputValue, inputUnit, outputUnit) :
    if inputUnit == "meter" :
        return(meterToUnit(inputValue, outputUnit))

    else :
        toMeterFactor = getToMeterFac(inputUnit)
        convertedValue = inputValue * toMeterFactor
        return(meterToUnit(convertedValue, outputUnit))


#precondition inputValue is guarentieed to be in meters
def meterToUnit(inputValue, outputUnit) :
    return(inputValue / getToMeterFac(outputUnit))

def getToMeterFac(stringUnit) :
     for row in t :
        row[0]
        if row[0] == stringUnit:
            return(row[1])


z = convertToUnit(1, "kilometer", "inch")
print(z)