#ConvertibleElement.py

class ConvertibleElement:
    value=0
    unit=""
    #constructor
    def __init__ (self, givenvalue, givenunit):
        self.value=givenvalue
        self.unit=givenunit

    #accessor methods
    def getValue (self):
        return self.value
    def getUnit (self):
        return self.unit

    #mutator methods
    def setValue (self, givenvalue):
        self.value=givenvalue
    def setUnit (self, givenunit):
        self.unit=givenunit

    def convertElement (self, desiredUnitsSystem, scale):
        #this is andrew's method
        #changes values inside converted element        

        initValue = self.getValue()
        initUnit = self.getUnit()
        initUnit = initUnit.lower()
        scale = float(scale)

        
        if (desiredUnitsSystem.lower() == "metric"):
            #length
            if (initUnit=="in" or initUnit=="inches" or initUnit=="inch"):
                finalValue = (initValue*2.54)*scale
                self.setValue(finalValue)
                #print (finalValue)
                finalUnit = "cm"
                self.setUnit(finalUnit)
                #print(finalUnit)

            #temperature
            elif (initUnit=="degrees f" or initUnit=="degrees F" or initUnit=="degrees Fahrenheit"):
                finalValue = ((initValue-32.0)/9.0)*5.0
                self.setValue(finalValue)
                finalUnit = "degrees Celsius"
                self.setUnit(finalUnit)

            #mass
            elif (initUnit=="lbs" or initUnit=="pounds" or initUnit=="lb" or initUnit=="pound"):
                finalValue = (initValue*453.592)*scale
                self.setValue(finalValue)
                finalUnit= "g"
                self.setUnit(finalUnit)

            elif (initUnit=="oz" or initUnit=="ounces" or initUnit=="ounce"):
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

            elif (initUnit=="fl oz" or initUnit=="fluid ounces"):
                finalValue = (initValue*29.5735)*scale
                self.setValue(finalValue)
                finalUnit = "mL"
                self.setUnit(finalUnit)

        if (desiredUnitsSystem.lower() == "imperial"):
            #length
            if (initUnit=="cm" or initUnit=="centimeters" or initUnit=="centimeter"):
                finalValue = (initValue*0.39)*scale
                self.setValue(finalValue)
                finalUnit = "in"
                self.setUnit(finalUnit)

            #temperature
            elif (initUnit=="degrees c" or initUnit=="degrees C" or initUnit=="degrees Celsius"):
                finalValue = ((initValue*9.0)/5.0)+32
                self.setValue(finalValue)
                finalUnit = "degrees Fahrenheit"
                self.setUnit(finalUnit)

            #mass
            elif (initUnit=="kg" or initUnit=="kilograms" or initUnit=="kilogram"):
                finalValue = (initValue*2.2046)*scale
                self.setValue(finalValue)
                finalUnit = "lbs"
                self.setUnit(finalUnit)

            elif (initUnit=="g" or initUnit=="grams" or initUnit=="gram"):
                finalValue = (initValue*0.035274)*scale
                self.setValue(finalValue)
                finalUnit = "oz"
                self.setUnit(finalUnit)

            #Volume
            elif (initUnit=="l" or initUnit=="liter" or initUnit=="liters"):
                finalValue = (initValue*4.22675)*scale
                self.setValue(finalValue)
                finalUnit = "cups"
                self.setUnit(finalUnit)

            elif (initUnit=="ml" or initUnit=="milliliter" or initUnit=="milliliters"):
                finalValue = (initValue*0.00422675)*scale
                self.setValue(finalValue)
                finalUnit = "cups"
                self.setUnit(finalUnit)
