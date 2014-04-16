import re
#testable string
recipe = '500 18/6 cups 4.0 sm Acorn squash 0.0 Salt 118.3mlButter or margarine 118.3 ml Honey 453.6 g Whole-berry cranberry sauce'
def parseRecipe(recipe):
    #regex for value and unit of measurement
    unitEx = re.compile( '''(?:(?:\d*\s*\d+(?:/|.)?\d*)\s*(?:ounces?|oz|pounds?|lbs?
                          |fluid\s*ounces?|milligrams?|mg|grams?|g|kilograms?|kg 
                          |fl\s*oz|milliliters?|ml|liters?|l|inches|inch|in|pints?
                          |millimeters?|mm|centimeters?|quarts?|qt|cm|cups?))|
                          (?:(?:\d+)\s*(?:celsius|ºc|c|fahrenheit|ºf|c))''', re.IGNORECASE | re.VERBOSE)
    
    #creates a list of all substrings matching regex
    celist = re.findall(unitEx, recipe)    
    print(celist)
    #regex to match first occurence of appropriate alphabetic character
    Ex = re.compile('[oplcmgkifº]', re.IGNORECASE)
    createConEl(celist,Ex)
    addTags(celist, recipe)
    
#each string element in celist gets converted into
#convertible elements(calls convertible element constructor)
#and gets modified element and places it in list    
def createConEl(list, regex):
    for ce in list:
        m = re.search(regex,ce)#recognizes where the original string should split
        start= m.start()
        end = ce.__len__()
        strvalue = ce[0:start]# takes double part of string and assigns it to value
        print(strvalue)
        double = convertValue(strvalue)
        print(double)                
        unit = ce[start:end]#takes measurement unit part of string and assigns it to unit                      
        if (unit == 'fahrenheit' or'ºf'or'f'):
            unit = 'degrees f'
            print(unit)
        elif (unit == 'celsius' or 'ºc' or 'c'):
            unit = 'degrees c'
            print(unit)
        else:
            print(unit)
##        conEl = ConvertibleElement(value,unit)
##        self.setCElistElement(conEl)

#Converts string into double. Returns double   
def convertValue(strvalue):
    #if string contains whole number or decimal. gets converted easily
    if(strvalue.find('/')==-1):
           value = float(strvalue)
    #converts string containing fraction into double
    else:
        #if string does not contain white space, only deal with fraction
        if(strvalue.find(' ')==-1):
            numden = strvalue.split('/')#holding numerator/denominator
            num = float(numden.pop(0))
            den = float(numden.pop(0))
            value = (num/den)
        #if string contains white space, deal with whole number and fraction
        else:
            white = strvalue.find(' ')
            fnum = strvalue[0:white]
            newstr = strvalue[white:strvalue.__len__()]
            numden = newstr.split('/')
            num = float(numden.pop(0))
            den = float(numden.pop(0))
            value = (float(fnum))+(num/den)
    return value

#Replaces each convertable element with <#>. Returns recipe with tagged elements
def addTags(list,recipe): 
    num = 0
    for ce in list:
        recipe = recipe.replace(ce, '<'+ str(num) + '>',1)
        num = num + 1
    return recipe
    print(recipe)
  
