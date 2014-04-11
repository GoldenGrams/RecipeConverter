def convertElement(desiredUnitsSystem, scale):
    givenValue = self.getValue()
    givenUnit = self.getUnit(self)

    if (desiredUnitsSystem == "Metric"):
        #length
        if (initUnit=="in" or initUnit=="inches"):
            finalValue = (initValue*2.54)*scale
            self.setValue(finalValue)
            #print (finalValue)
            finalUnit = "cm"
            self.setUnit(finalUnit)
            #print(finalUnit)

        #temperature
        elif (initUnit=="degrees F" or initUnit=="degrees Fahrenheit"):
            finalValue = ((initValue-32.0)/9.0)*5.0
            self.setValue(finalValue)
            finalUnit = "Celsius"
            self.setUnit(finalUnit)

        #mass
        elif (initUnit=="lbs" or initUnit=="pounds" or initUnit=="pound"):
            finalValue = (initValue*453.592)*scale
            self.setValue(finalValue)
            finalUnit= "g"
            self.setUnit(finalUnit)

        elif (intUnit=="oz" or initUnit=="ounces"):
            finalValue = (initValue*28.3495)*scale
            self.setValue(finalValue)
            finalUnit = "g"
            self.setUnit(finalUnit)

        #volume
        elif (initUnit=="qt" or initUnit=="quart" or initUnit=="quarts"):
            finalValue = (initValue*0.946353)*scale
            self.setValue(finalValue)
            finalUnit = "L"
            self.setUnit(finalUnit)

        elif (initUnit=="pt" or initUnit=="pint" or initUnit=="pints"):
            finalValue = (initValue*473.176)*scale
            self.setValue(finalValue)
            finalUnit = "mL"
            self.setUnit(finalUnit)

        elif (initUnit=="cup" or initUnit=="cups"):
            finalValue = (initValue*236.588)*scale
            self.setValue(finalValue)
            finalUnit = "mL"
            self.setUnit(finalUnit)

        elif (initUnit=="oz" or initUnit=="ounces"):
            finalValue = (initValue*29.5735)*scale
            self.setValue(finalValue)
            finalUnit = "mL"
            self.setUnit(finalUnit)

    if (desiredUnitsSystem == "Imperial"):
        #length
        if (initUnit=="cm" or initUnit=="centitmeters" or initUnit=="centimetres"):
            finalValue = (initvalue*0.39)*scale
            self.setValue(finalValue)
            finalUnit = "in"
            self.setUnit(finalUnit)

        #temperature
        elif (initUnit=="degrees C" or initUnit=="degrees Celsius"):
            finalValue = ((initValue*9.0)/5.0)+32
            self.setValue(finalValue)
            finalUnit = "Fahrenheit"
            self.setUnit(finalUnit)

        #mass
        elif (initUnit=="kg" or initUnit=="kilograms" or initUnit=="kgs"):
            finalValue = (initValue*2.2046)*scale
            self.setValue(finalValue)
            finalUnit = "lbs"
            self.setUnit(finalUnit)

        elif (initUnit=="g" or initUnit=="grams"):
            finalValue = (initValue*0.035274)*scale
            self.setValue(finalValue)
            finalUnit = "oz"
            self.setUnit(finalUnit)

        #Volume
        elif (initUnit=="L" or initUnit=="liter" or initUnit=="liters"):
            finalValue = (initValue*4.22675)*scale
            self.setValue(finalValue)
            finalUnit = "cups"
            self.setUnit(finalUnit)

        elif (initUnit=="mL" or initUnit=="milliliter" or initUnit=="milliliters"):
            finalValue = (initValue*0.00422675)*scale
            self.setValue(finalValue)
            finalUnit = "cups"
            self.setUnit(finalUnit)
