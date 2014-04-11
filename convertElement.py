def convertElement(desiredUnitsSystem, scale):
    #variable(s)
    '''
    float initValue
    Str initUnit
    Str desiredUnitsSystem
    float finalValue
    Str finalUnit
    int scale
    '''

    def __init__ (self, initValue, initUnit, desiredUnitsSystem, finalValue, finalUnit, scale):
        #pass
        self.initValue = initValue
        self.initUnit = initUnit
        self.desiredUnitsSystem = desiredUnitsSystem
        self.finalValue = finalValue
        self.finalUnit = finalUnit
        self.scale = scale

        #getValue
    def getValue(self, initValue): return self.initValue
        
        #getUnit
    def getUnit(self, initUnit): return self.initUnit

        #If desiredUnitsSystem is Metric
    if (desiredUnitsSystem == "Metric"):
        #length
        if (initUnit=="in" or initUnit=="inches"):
            finalValue = (initValue*2.54)*scale
            return finalValue
            finalUnit = "cm"
            return finalUnit

        #temperature
        elif (initUnit=="degrees F" or initUnit=="degrees Fahrenheit"):
            finalValue = ((initValue-32.0)/9.0)*5.0
            return finalValue
            finalUnit = "Celsius"
            return finalUnit

        #mass
        elif (initUnit=="lbs" or initUnit=="pounds" or initUnit=="pound"):
            finalValue = (initValue*453.592)*scale
            return finalValue
            finalUnit= "g"
            return finalUnit

        elif (intUnit=="oz" or initUnit=="ounces"):
            finalValue = (initValue*28.3495)*scale
            return finalValue
            finalUnit = "g"
            return finalUnit

        #volume
        elif (initUnit=="qt" or initUnit=="quart" or initUnit=="quarts"):
            finalValue = (initValue*0.946353)*scale
            return finalValue
            finalUnit = "L"
            return finalUnit

        elif (initUnit=="pt" or initUnit=="pint" or initUnit=="pints"):
            finalValue = (initValue*473.176)*scale
            return finalValue
            finalUnit = "mL"
            return finalUnit

        elif (initUnit=="cup" or initUnit=="cups"):
            finalValue = (initValue*236.588)*scale
            return finalValue
            finalUnit = "mL"
            return finalUnit

        elif (initUnit=="oz" or initUnit=="ounces"):
            finalValue = (initValue*29.5735)*scale
            return finalValue
            finalUnit = "mL"
            return finalUnit

    if (desiredUnitsSystem == "Imperial"):
        #length
        if (initUnit=="cm" or initUnit=="centitmeters" or initUnit=="centimetres"):
            finalValue = (initvalue*0.39)*scale
            return finalValue
            finalUnit = "in"
            return finalUnit

        #temperature
        elif (initUnit=="degrees C" or initUnit=="degrees Celsius"):
            finalValue = ((initValue*9.0)/5.0)+32
            return finalValue
            finalUnit = "Fahrenheit"
            return finalUnit

        #mass
        elif (initUnit=="kg" or initUnit=="kilograms" or initUnit=="kgs"):
            finalValue = (initValue*2.2046)*scale
            return finalValue
            finalUnit = "lbs"
            return finalUnit

        elif (initUnit=="g" or initUnit=="grams"):
            finalValue = (initValue*0.035274)*scale
            return finalValue
            finalUnit = "oz"
            return finalUnit

        #Volume
        elif (initUnit=="L" or initUnit=="liter" or initUnit=="liters"):
            finalValue = (initValue*4.22675)*scale
            return finalValue
            finalUnit = "cups"
            return finalUnit

        elif (initUnit=="mL" or initUnit=="milliliter" or initUnit=="milliliters"):
            finalValue = (initValue*0.00422675)*scale
            return finalValue
            finalUnit = "cups"
            return finalUnit
