josie's pseudocode

#PARSER
 
//recipe is stored in the variable recipe
  Recipe = recipe string object
//pattern object is created for all possible convertible elements that will be found in a recipe
  unitRegularExpression = re.compile(‘(\d+) (unit?)’)
//Recipe is analyzed.
  An array is created containing all substrings/convertible elements matching the regex.
  array = findall(unitRegularExpression, recipe)
  for convertible element in array:
      call convertible element constructor 
      element gets converted and placed back into array
//iterate through array
  for converted element in list:
      setElement() //replaces unconverted element with converted element    
    
//creates another recipe object. will contain new recipe with tagged elements
  taggedrecipe = recipe
  for item in list:
      each convertible element in recipe will be replaced with convertible
      element in btwn angle brackets(ex. 1ml  will be <1ml>)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~

convertible element pseduocode
# Converter
# 
# Description
# The Converter takes in data that has already been parsed into a quantity and a unit.
# The quantity's units are compared with a list of English and Metric measurements to determine which conversion ratio is necessary to use.
# The quantity is then modified according to the conversion ratio (multiplication, division, etc.).
# The Converter returns the correct conversion of the quantity and the applicable unit.
# The Converter may also multiply the quantities by the serving size given by the user.
# 
# List of convertible units: Units intended to be converted
# weight: pounds, ounces, grams, kilograms
# liquid: Tablespoons, teaspoons, fluid ounces, cups, pints, quarts, gallons, milliliters, liters
# temperature: Fahrenheit, Celsius
# length: inches, centimeters
# 
# Pseudocode
# 03/25/14
# while input is parsed
# if there is a unit to convert AND a unit to be converted to (Can this conversion be made?)
# 		do the necessary conversion
# 		modify based on serving size
# 		return correct quantity and unit
# 	else if
# repeat as above for other units of measure (It might not be the first item I list, but it   might be further down the list.)
# 	else error message
# 	end if
# end while
# 
# 03/27/14
# precondition: array of un-converted convertible elements
# if converter recognizes tagged convertible units
# 	if converter recognizes current unit and future unit
# 		-- (a list of conversions between Imperial and Metric units, and vice versa)
# 		do the necessary conversion (mostly multiplication or division)
# 		return correct quantity and unit
# else cannot convert
# end if
# else cannot convert
# end if

#~~~~~~~~~~~~~~
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

    #get methods
    def getInitValue(self): return self.initValue
    def getFinalValue(self): return self.finalValue
    
    def getInitUnit(self): return self.initUnit
    def getFinalUnit(self): return self.finalUnit

    #set methods
    def setInitValue(self, givenvalue):
        self.initValue = givenvalue
    def setInitUnit(self, givenunit):
        self.initUnit = givenunit

    def setFinalValue(self, finalvalue):
        self.finalValue = finalvalue
    def setFinalUnit(self, finalunit):
        self.finalUnit = finalunit
        

        #If desiredUnitsSystem is Metric
    if (desiredUnitsSystem == "Metric"):
        #length
        if (initUnit=="in" or initUnit=="inches"):
            finalValue = (initValue*2.54)*scale
            setFinalValue(finalValue)
            getFinalValue()
            #print (finalValue)
            finalUnit = "cm"
            setFinalUnit(finalUnit)
            getFinalUnit()
            #return finalUnit
            #print(finalUnit)

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
