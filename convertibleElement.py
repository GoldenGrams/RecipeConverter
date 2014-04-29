#ConvertibleElement.py

class ConvertibleElement:
    value=0.0
    unit=""
    ingredient=""
    
    #constructor
    def __init__ (self, givenvalue, givenunit, giveningredient):
        self.value=givenvalue
        self.unit=givenunit
        self.ingredient=giveningredient        

    #accessor methods
    def getValue (self):
        return self.value
    def getUnit (self):
        return self.unit
    def getIngredient (self):
        return self.ingredient

    #mutator methods
    def setValue (self, givenvalue):
        self.value=givenvalue
    def setUnit (self, givenunit):
        self.unit=givenunit
    def setIngredient (self, giveningredient):
        self.ingredient=giveningredient

    #!!!!!!!!!!!!!
    # if converting from metric to metric or imperial to imperial, scaling doesnt happen
    def convertElement (self, desiredUnitsSystem, scale):
        #this is andrew's method
        #changes values inside converted element        

        initValue = self.getValue()
        initUnit = self.getUnit().lower()
        self.setIngredient(self.getIngredient().lower()) #assuming ingredient name is not removed from overall string of recipe
        scale = float(scale)
        finalValue=initValue
        formatting=""
        specialingredientflag=0

        
        if (desiredUnitsSystem.lower() == "metric"):

            #density adjustments
            density=1.0
            if (self.getIngredient()=="salted butter"):
                density = (1/0.96)
                specialingredientflag=1
            elif (self.getIngredient()=="unsalted butter" or self.getIngredient()=="butter" or self.getIngredient()=="un salted butter"or self.getIngredient()=="un-salted butter"):
                density = (1/0.91)
                specialingredientflag=1
            elif (self.getIngredient()=="margarine"):
                density = (1/1)
                specialingredientflag=1
            elif (self.getIngredient()=="all-purpose flour" or self.getIngredient()=="all purpose flour"):
                density = (1/0.58)
                specialingredientflag=1
            elif (self.getIngredient()=="flour"):
                density = (1/0.51)
                specialingredientflag=1
            elif (self.getIngredient()=="light brown sugar"):
                density = (1/0.81)
                specialingredientflag=1
            elif (self.getIngredient()=="dark brown sugar"):
                density = (1/0.81)
                specialingredientflag=1
            elif (self.getIngredient()=="brown sugar"):
                density = (1/0.81)
                specialingredientflag=1
            elif (self.getIngredient()=="granulated sugar"):
                density = (1/0.85)
                specialingredientflag=1

            
            #length
            if (initUnit=="in" or initUnit=="inches" or initUnit=="inch"):
                finalValue = (initValue*2.54)
                #x="%.3f" % x
                formatting = "%.2f"
                self.setValue(finalValue)
                #print (finalValue)
                finalUnit = "cm"
                self.setUnit(finalUnit)
                #print(finalUnit)

            #mass
            elif (initUnit=="lbs" or initUnit=="pounds" or initUnit=="lb" or initUnit=="pound"):
                finalValue = (initValue*453.592)
                formatting = "%.1f" 
                self.setValue(finalValue)
                finalUnit= "g"
                self.setUnit(finalUnit)

            elif (initUnit=="oz" or initUnit=="ounces" or initUnit=="ounce" or initUnit=="ozs"):
                finalValue = (initValue*28.3495)
                formatting = "%.1f" 
                self.setValue(finalValue)
                finalUnit = "g"
                self.setUnit(finalUnit)

            #volume
                #& (giveningredient.lower()=="butter" or giveningredient.lower()=="sugar" or giveningredient.lower()=="margarine" or giveningredient.lower()=="flour"):

            elif (initUnit=="qt" or initUnit=="quart" or initUnit=="quarts" or initUnit=="qts") and (specialingredientflag==1):
                finalValue = ((initValue*0.946353)*density)
                formatting = "%.3f" 
                self.setValue(finalValue)
                finalUnit = "g"
                self.setUnit(finalUnit)

            elif (initUnit=="pt" or initUnit=="pint" or initUnit=="pints" or initUnit=="pts")  and (specialingredientflag==1):
                finalValue = ((initValue*473.176)*density)
                formatting = "%.0f"
                self.setValue(finalValue)
                finalUnit = "g"
                self.setUnit(finalUnit)

            elif (initUnit=="cup" or initUnit=="cups")  and (specialingredientflag==1):
                finalValue = ((initValue*236.588)*density)
                formatting = "%.0f" 
                self.setValue(finalValue)
                finalUnit = "g"
                self.setUnit(finalUnit)

            elif (initUnit=="fl oz" or initUnit=="fluid ounces")  and (specialingredientflag==1):
                finalValue = ((initValue*29.5735)*density)
                formatting = "%.0f" 
                self.setValue(finalValue)
                finalUnit = "g"
                self.setUnit(finalUnit)

            elif (initUnit.lower()=="tablespoons" or initUnit.lower()=="tbsp")  and (specialingredientflag==1):
                finalValue = ((initValue*14.7868)*density)
                formatting = "%.0f" 
                self.setValue(finalValue)
                finalUnit = "g"
                self.setUnit(finalUnit)

            elif (initUnit.lower()=="teaspoons" or initUnit.lower()=="tsp")  and (specialingredientflag==1):
                finalValue = ((initValue*4.92892)*density)
                formatting = "%.0f"
                self.setValue(finalValue)
                finalUnit = "g"
                self.setUnit(finalUnit)
            ####
                
            elif (initUnit=="qt" or initUnit=="quart" or initUnit=="quarts" or initUnit=="qts"):
                finalValue = (initValue*0.946353)
                formatting = "%.3f"
                self.setValue(finalValue)
                finalUnit = "L"
                self.setUnit(finalUnit)

            elif (initUnit=="pt" or initUnit=="pint" or initUnit=="pints" or initUnit=="pts" ):
                finalValue = (initValue*473.176)
                formatting = "%.0f"
                self.setValue(finalValue)
                finalUnit = "mL"
                self.setUnit(finalUnit)

            elif (initUnit=="cup" or initUnit=="cups"):
                finalValue = (initValue*236.588)
                formatting = "%.0f"
                self.setValue(finalValue)
                finalUnit = "mL"
                self.setUnit(finalUnit)

            elif (initUnit=="fl oz" or initUnit=="fluid ounces"):
                finalValue = (initValue*29.5735)
                formatting = "%.0f"
                self.setValue(finalValue)
                finalUnit = "mL"
                self.setUnit(finalUnit)

            elif (initUnit.lower()=="tablespoons" or initUnit.lower()=="tbsp" or initUnit.lower()=="tbs"):
                finalValue = (initValue*14.7868)
                formatting = "%.0f"
                self.setValue(finalValue)
                finalUnit = "g"
                self.setUnit(finalUnit)

            elif (initUnit.lower()=="teaspoons" or initUnit.lower()=="tsp"):
                finalValue = (initValue*4.92892)
                formatting = "%.0f"
                self.setValue(finalValue)
                finalUnit = "g"
                self.setUnit(finalUnit)

            #finalValue=finalValue*scale
           # finalValue=formatting.format(finalValue)
           #set final value after scaling


            #temperature
            if (initUnit=="degrees f" or initUnit=="degrees fahrenheit" or initUnit=="f" or initUnit=="fahrenheit" or initUnit=="ºf"):
                finalValue = ((initValue-32.0)/9.0)*5.0
                finalValue = "%.0f" % finalValue
                self.setValue(finalValue)
                finalUnit = "degrees Celsius"
                self.setUnit(finalUnit)


        if (desiredUnitsSystem.lower() == "imperial"):

            #density adjustments
            density=1.0
            if (self.getIngredient()=="salted butter"):
                density = 0.96
                specialingredientflag=1
            elif (self.getIngredient()=="unsalted butter" or self.getIngredient()=="butter" or self.getIngredient()=="un salted butter"or self.getIngredient()=="un-salted butter"):
                density = 0.916
                specialingredientflag=1
            elif (self.getIngredient()=="margarine"):
                density = 1.0
                specialingredientflag=1
            elif (self.getIngredient()=="all-purpose flour" or self.getIngredient()=="all purpose flour"):
                density = 0.58
                specialingredientflag=1
            elif (self.getIngredient()=="flour"):
                density = 0.51
                specialingredientflag=1
            elif (self.getIngredient()=="light brown sugar"):
                density = 0.81
                specialingredientflag=1
            elif (self.getIngredient()=="dark brown sugar"):
                density = 0.81
                specialingredientflag=1
            elif (self.getIngredient()=="brown sugar"):
                density = 0.81
                specialingredientflag=1
            elif (self.getIngredient()=="granulated sugar"):
                density = 0.85
                specialingredientflag=1
            elif (self.getIngredient()=="sugar"):
                density = 0.85
                specialingredientflag=1
            
            #length
            if (initUnit=="cm" or initUnit=="centimeters" or initUnit=="centimeter"):
                finalValue = (initValue*0.39)
                formatting = "%.3f"
                self.setValue(finalValue)
                finalUnit = "in"
                self.setUnit(finalUnit)

            #mass
            elif (initUnit=="kg" or initUnit=="kilograms" or initUnit=="kilogram" or initUnit=="kgs") and (specialingredientflag==1):
                finalValue = ((initValue*2.2046)*density)
                formatting = "%.3f"
                self.setValue(finalValue)
                finalUnit = "cups"
                self.setUnit(finalUnit)
                
            elif (initUnit=="g" or initUnit=="grams" or initUnit=="gram") and (specialingredientflag==1):
                finalValue = ((initValue*0.035274)*density)
                formatting = "%.2f"
                self.setValue(finalValue)
                finalUnit = "Tbsp"
                self.setUnit(finalUnit)

            elif (initUnit=="kg" or initUnit=="kilograms" or initUnit=="kilogram" or initUnit=="kgs"):
                finalValue = (initValue*2.2046)*density
                formatting = "%.3f"
                self.setValue(finalValue)
                finalUnit = "lbs"
                self.setUnit(finalUnit)

            elif (initUnit=="g" or initUnit=="grams" or initUnit=="gram"):
                finalValue = (initValue*0.035274)*density
                formatting = "%.2f"
                self.setValue(finalValue)
                finalUnit = "oz"
                self.setUnit(finalUnit)

            #Volume
            elif (initUnit=="l" or initUnit=="liter" or initUnit=="liters" or initUnit=="litres"):
                finalValue = (initValue*4.22675)
                formatting = "%.3f"
                self.setValue(finalValue)
                finalUnit = "cups"
                self.setUnit(finalUnit)

            elif (initUnit=="ml" or initUnit=="milliliter" or initUnit=="milliliters"):
                finalValue = (initValue*0.00422675)
                formatting = "%.3f"
                self.setValue(finalValue)
                finalUnit = "cups"
                self.setUnit(finalUnit)

         #   finalValue=finalValue*scale
      #      finalValue=formatting.format(finalValue)
      #set final value again after scaling
    

            #temperature
            if (initUnit=="degrees c" or initUnit=="degrees celsius" or initUnit=="c" or initUnit=="celsius" or initUnit=="ºc"):
                finalValue = ((initValue*9.0)/5.0)+32
                finalValue = "%.0f" % finalValue
                self.setValue(finalValue)
                finalUnit = "degrees Fahrenheit"
                self.setUnit(finalUnit)
