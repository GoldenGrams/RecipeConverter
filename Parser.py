import re
#testable string
recipe = '1/2 cup 4.0 sm Acorn squash 0.0 Salt 118.3mlButter or margarine 118.3 ml Honey 453.6 g Whole-berry cranberry sauce 5.5 liters'
def parseRecipe(recipe):
    #regex for value and unit of measurement
    unitEx = re.compile( '''(?:(?:\d+(?:\|/|.)?\d*)\s*(?:ounces?|oz|pounds?|lbs?
                          |fluid\s*ounces?|milligrams?|mg|grams?|g|kilograms?|kg 
                          |fl\s*oz|milliliters?|ml|liters?|l|inches|inch|in|pints?
                          |millimeters?|mm|centimeters?|quarts?|qt|cm|cups?))|
                          (?:(?:\d+)\s*(?:celsius|ºc|c|fahrenheit|ºf|c))''', re.IGNORECASE | re.VERBOSE)
    
    #creates a list of all substrings matching regex
    celist = re.findall(unitEx, recipe)    
    print(celist)
    #regex to match first occurence of appropriate alphabetic character
    Ex = re.compile('[oplcmgkif]', re.IGNORECASE)
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
        value = float(ce[0:start])# takes double part of string and assigns it to value
        unit = ce[start:end]#takes measurement unit par of string and assigns it to unit            
##        conEl = ConvertibleElement(value,unit)
##        self.setCElistElement(conEl)

#Replaces each convertable element with <#>
def addTags(list,recipe): 
    num = 0
    for ce in list:
        recipe = recipe.replace(ce, '<'+ str(num) + '>',1)
        num = num + 1
    print(recipe)
  
