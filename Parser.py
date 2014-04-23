import re

#testable string
recipe = '''1 tbs dark brown sugar, 4 tablespoon 30 x 23 cm
            1/8 lbs7.5cm 5 ºf 22 ºc 4.0 sm Acorn squash 0.0 Salt
            118.3ml Butter or margarine 118.3 ml Honey
            453.6 g Whole-berry cranberry sauce'''

def parseTheRecipe(recipe):
    #regex for value and unit of measurement
    unitEx = re.compile( '''(?:(?:\d*\s*\d+\s*(?:x|/|.)?\s*\d*)\s*(?:ounces?|oz|pounds?|lbs?
                          |tablespoons?|teaspoons?|tbs|tsp
                          |fluid\s*ounces?|milligrams?|mg|grams?|g|kilograms?|kg 
                          |fl\s*oz|milliliters?|ml|liters?|l|inches|inch|in|pints?
                          |millimeters?|mm|centimeters?|quarts?|qt|cm|cups?)\s*                          
                          (?:butter|margarine|all\s*purpose\s*flour
                          |(?:(?:(?:light|dark)?\s*brown)?|(?:granulated)?)\s*sugar)?)                          
                          |(?:(?:\d+)\s*(?:celsius|ºc|c|degrees\s*(?:celsius|fahrenheit|c|f)|
                          fahrenheit|ºf|f))''', re.IGNORECASE | re.VERBOSE)   
    #creates a list of all substrings matching regex
    celist = re.findall(unitEx, recipe)    
    print(celist)
    #regex to match first occurence of appropriate alphabetic character
    splitEx = re.compile('[oplcdmgkiftº]', re.IGNORECASE)
    ingEx = re.compile('''butter|margarine|all\s*purpose\s*flour|
                          (?:(?:(?:light|dark)?\s*brown)?|
                          (?:granulated)?\s*sugar)''', re.IGNORECASE | re.VERBOSE) 
    createConEl(celist,splitEx,ingEx)
    return addTags(celist, recipe)
    
#each string element in celist gets converted into
#convertible elements(calls convertible element constructor)
#and gets modified element and places it in list    
def createConEl(list, r1, r2):
    for ce in list:
        splitCe = re.search(r1,ce)#recognizes where the original string should split
        start = splitCe.start()
        end = ce.__len__()
        strvalue = ce[0:start].strip()# takes double part of string and assigns it to value
        double = convertValue(strvalue)
        unitingred = ce[start:end]#takes measurement unit part of string and assigns it to unit      
        splitStr = re.search(r2,unitingred)
        if(splitStr == None):
            unit = unitingred
            ingred = 'nofbs'
            #changes degree unit to degrees f or degrees c
            if ((unit == 'fahrenheit') or (unit == 'ºf') or (unit == 'f')):
                unit = 'degrees f'
            elif ((unit == 'celsius') or (unit == 'ºc') or (unit == 'c')):
                unit = 'degrees c'
            else:
                unit = unit
        else:
            splitStr = splitStr##change
            begin = splitStr.start()
            unit = unitingred[0:begin]
            ingred = unitingred[begin:end]
        print(str(double) + unit + ingred)
                   
##        conEl = ConvertibleElement(double,unit,ingred) 
##        self.setElistElement(conEl)

#Converts string into double. Returns double   
def convertValue(strvalue):
    #if string contains whole number or decimal. gets converted to double easily
    if(strvalue.find('/')==-1):##change
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
    #print(recipe)
    return recipe
    
  
