METER_INCH = 39.37
METER_FEET = 3.281
INCH_FEET = 12
METER_KM = 1000
METER_DM = 10

def convertToUnit (inputValue, inputUnit, outputUnit) :
    upperInputUnit = inputUnit.upper()
    if outputUnit.upper() == "DECIMETER" :
        return(convertToUnit(inputValue * METER_DM, inputUnit,  "METER")) ##culprit of error
    elif upperInputUnit == "METER" :
        return(convertFromMeter(inputValue, outputUnit))  
    elif upperInputUnit == "INCH" : 
        return(convertFrominch(inputValue, outputUnit))
    elif upperInputUnit == "FEET" :
        return(convertFromFeet(inputValue, outputUnit))
    elif upperInputUnit == "KILOMETER" :
        return(convertFromMeter(inputValue * METER_KM, outputUnit))
    elif upperInputUnit == "DECIMETER" : 
        return(convertFromMeter(inputValue / METER_DM, outputUnit))

def convertFromMeter (val, toConvert) :
    if toConvert.upper() == "METER" :
        return(val)
    elif toConvert.upper() == "INCH" : 
        return(val * METER_INCH)
    elif toConvert.upper() == "FEET" :
        return(val * METER_FEET)


def convertFrominch (val, toConvert) :
    if toConvert.upper() == "METER" :
        return(val / METER_INCH)
    elif toConvert.upper() == "INCH" : 
        return(val)
    elif toConvert.upper() == "FEET" :
        return(val / INCH_FEET)



def convertFromFeet (val, toConvert) :
    if toConvert.upper() == "METER" :
        return(val / METER_FEET)
    elif toConvert.upper() == "INCH" : 
        return(val * INCH_FEET)
    elif toConvert.upper() == "FEET" :
        return(val)

##seperateDriver

x  = convertToUnit(10, "meter", "inch")
print(x)