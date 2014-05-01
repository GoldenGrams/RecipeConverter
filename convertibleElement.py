#ConvertibleElement.py

# an instantiation of the ConvertibleElement class is the specific number, unit, and sometimes ingredient
# that are manipulated by the program


class ConvertibleElement:

    #instance variables
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

    def convertElement (self, desiredUnitsSystem, scale):
        # This method takes in a desired unit system and a scale as a parameter.
        # The method uses a convertible element (quantity, unit, and in some cases an ingredient.)
        # The ingredient is checked against certain ingredients whose measurements are in mass in
        # metric and volume in Imperial. If such an ingredient is of the special type, the
        # measure of density is modified; otherwise, the density is 1.0.
        # The unit of the convertible element is then checked a list of applicable units of measure.
        # If the ingredient and an item on the list match, the quantity is modified, based on
        # conversion factors. The unit is changed to an applicable unit of measure in the
        # desired unit system.
        
        #local variables
        initValue = self.getValue() #working value within method
        initUnit = self.getUnit().lower() #working unit within method 
        self.setIngredient(self.getIngredient().lower()) #assuming ingredient name is not removed from overall string of recipe
        scale = float(scale)
        finalValue=initValue #the converted quantity
        formatting="" #format converted values
        specialingredientflag=0 #flag to recognize special ingredients

        # Determine if the desired unit system is metric.
        # If it is, check the ingredient. 
        if (desiredUnitsSystem.lower() == "metric"):

            # Density is assumed to be 1.0 unless the convertible element's ingredient is one of the ingredients listed below.
            # Density is modified to the correct number if ingredient is "special". If not, density remains 1.0.
            # The local variable specialingredientflag is changed to 1 when a special ingredient is detected.
            density=1.0
            if (self.getIngredient()=="salted butter"):
                density = 0.96
                specialingredientflag=1
            elif (self.getIngredient()=="unsalted butter" or self.getIngredient()=="butter" or self.getIngredient()=="un salted butter"or self.getIngredient()=="un-salted butter"):
                density = 0.91
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

            # The following series of if...elif blocks check to see whether the conversion can be made.
            # The abbreviations, singular spelling, and plural spellings of unit measures are checked.
            # If there is a unit that can be converted, the conversion is made. 
            
            #Converts units of length (from inches to centimeters)
            # Check to see if the convertible element's unit is "in", "inch" or "inches"
            if (initUnit=="in" or initUnit=="inches" or initUnit=="inch"):
                #The final value (converted quantity) is the initial unit multiplied by 2.54, since there
                #are 2.54 cm per 1 inch.
                finalValue = (initValue*2.54)
                #The following lines shows the set up for formatting.
                #x="%.3f" % x
                formatting = "%.2f"
                #Set the final value to the converted quantity with proper formatting.
                self.setValue(finalValue)
                #print (finalValue)
                finalUnit = "cm"
                #Set the final unit to a comparable unit of measure in the desired measurement system.
                self.setUnit(finalUnit)
                #print(finalUnit)

            #The prior descriptions of what is occuring in the block is applicable to all of
            #the following blocks of code.

            #Convert units of mass
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

            #Convert measurements of special ingredients  
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

            #Convert measures of volume for non-special volumes    
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
            
            # Maintain temperature so that temperature does not get scaled
            if (initUnit=="degrees c" or initUnit=="degrees celsius" or initUnit=="c" or initUnit=="celsius" or initUnit=="ºc"):
                self.setValue(finalValue)
            # Scale and set value when scaled
            else:
                finalValue=self.getValue()*scale
                self.setValue(finalValue)

            #finalValue=formatting.format(finalValue)
            #finalValue=formatting % finalValue
            
            #Conversion of temperature
            if (initUnit=="degrees f" or initUnit=="degrees fahrenheit" or initUnit=="f" or initUnit=="fahrenheit" or initUnit=="ºf"):
                finalValue = ((initValue-32.0)/9.0)*5.0
                #finalValue = "%.0f" % finalValue
                self.setValue(finalValue)
                finalUnit = "degrees Celsius"
                self.setUnit(finalUnit)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Determine if the desired unit system is imperial
        # If it is, check the ingredient. 
        if (desiredUnitsSystem.lower() == "imperial"):

            # Density adjustments
            # Density is assumed to be 1.0 unless the convertible element's ingredient is one of the ingredients listed below.
            # Density is modified to the correct number if ingredient is "special". If not, density remains 1.0.
            # The local variable specialingredientflag is changed to 1 when a special ingredient is detected.
            density=1.0
            if (self.getIngredient()=="salted butter"):
                density = 1/0.96
                specialingredientflag=1
            elif (self.getIngredient()=="unsalted butter" or self.getIngredient()=="butter" or self.getIngredient()=="un salted butter"or self.getIngredient()=="un-salted butter"):
                density = 1/0.916
                specialingredientflag=1
            elif (self.getIngredient()=="margarine"):
                density = 1/1.0
                specialingredientflag=1
            elif (self.getIngredient()=="all-purpose flour" or self.getIngredient()=="all purpose flour"):
                density = 1/0.58
                specialingredientflag=1
            elif (self.getIngredient()=="flour"):
                density = 1/0.51
                specialingredientflag=1
            elif (self.getIngredient()=="light brown sugar"):
                density = 1/0.81
                specialingredientflag=1
            elif (self.getIngredient()=="dark brown sugar"):
                density = 1/0.81
                specialingredientflag=1
            elif (self.getIngredient()=="brown sugar"):
                density = 1/0.81
                specialingredientflag=1
            elif (self.getIngredient()=="granulated sugar"):
                density = 1/0.85
                specialingredientflag=1
            elif (self.getIngredient()=="sugar"):
                density = 1/0.85
                specialingredientflag=1

            # The following series of if...elif blocks check to see whether the conversion can be made.
            # The abbreviations, singular spelling, and plural spellings of unit measures are checked.
            # If there is a unit that can be converted, the conversion is made. 
            
            #Converts units of length (from centimeters to inches)
            # Check to see if the convertible element's unit is "in", "inch" or "inches"
            if (initUnit=="cm" or initUnit=="centimeters" or initUnit=="centimeter"):
                #The final value (converted quantity) is the initial unit multiplied by 2.54, since there
                #are 2.54 cm per 1 inch.
                finalValue = (initValue*0.39)
                formatting = "{0:.3f}"
                #Set the final value to the converted quantity with proper formatting.
                self.setValue(finalValue)
                finalUnit = "in"
                #Set the final unit to a comparable unit of measure in the desired measurement system.
                self.setUnit(finalUnit)

            #The prior descriptions of what is occuring in the block is applicable to all of
            #the following blocks of code.

            #Convert measures of mass for special masses  
            elif (initUnit=="kg" or initUnit=="kilograms" or initUnit=="kilogram" or initUnit=="kgs") and (specialingredientflag==1):
                finalValue = ((initValue*2.2046)*density)
                formatting = "{0:.3f}"
                self.setValue(finalValue)
                finalUnit = "cups"
                self.setUnit(finalUnit)
                
            elif (initUnit=="g" or initUnit=="grams" or initUnit=="gram") and (specialingredientflag==1):
                finalValue = ((initValue*0.035274)*density)
                formatting = "{0:.2f}"
                self.setValue(finalValue)
                finalUnit = "Tbsp"
                self.setUnit(finalUnit)
            
            #Convert units of mass for non-special masses
            elif (initUnit=="kg" or initUnit=="kilograms" or initUnit=="kilogram" or initUnit=="kgs"):
                finalValue = (initValue*2.2046)*density
                formatting = "{0:.3f}"
                self.setValue(finalValue)
                finalUnit = "lbs"
                self.setUnit(finalUnit)

            elif (initUnit=="g" or initUnit=="grams" or initUnit=="gram"):
                finalValue = (initValue*0.035274)*density
                formatting = "{0:.2f}"
                self.setValue(finalValue)
                finalUnit = "oz"
                self.setUnit(finalUnit)

            #Convert units of volume
            elif (initUnit=="l" or initUnit=="liter" or initUnit=="liters" or initUnit=="litres"):
                finalValue = (initValue*4.22675)
                formatting = "{0:.3f}"
                self.setValue(finalValue)
                finalUnit = "cups"
                self.setUnit(finalUnit)

            elif (initUnit=="ml" or initUnit=="milliliter" or initUnit=="milliliters"):
                finalValue = (initValue*0.2029)
                formatting = "{0:.3f}"
                self.setValue(finalValue)
                finalUnit = "tsp"
                self.setUnit(finalUnit)

            #Maintain temperature so that it does not get scaled
            if (initUnit=="degrees f" or initUnit=="degrees fahrenheit" or initUnit=="f" or initUnit=="fahrenheit" or initUnit=="ºf"):
                self.setValue(finalValue)
            #Scaling and set value after scaling
            else:
                finalValue=self.getValue()*scale
                self.setValue(finalValue)
                
            #not working #finalValue=formatting.format(finalValue)
            # not working #finalValue=formatting % finalValue
            
            #Convert the temperature
            if (initUnit=="degrees c" or initUnit=="degrees celsius" or initUnit=="c" or initUnit=="celsius" or initUnit=="ºc"):
                finalValue = ((initValue*9.0)/5.0)+32
                finalValue = "%.0f" % finalValue
                self.setValue(finalValue)
                finalUnit = "degrees Fahrenheit"
                self.setUnit(finalUnit)
