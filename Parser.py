import re
recipe = '4.0 sm Acorn squash 0.0 Salt 118.3mlButter or margarine 118.3 ml Honey 453.6 g Whole-berry cranberry sauce'

def parseRecipe(recipe):
    #regex for value and unit of measurement
    unitEx = re.compile('(?:(?:\d+(?:\|/|.)?\d+)\s*(?:ounces?|oz|pounds?|lbs?|' 
                    + 'milligrams?|mg|grams?|g|kilograms?|kg|'
                    + 'milliliters?|ml|liters?|inches|inch|in|' 
                    + 'millimeters?|mm|centimeters?|cm))|(?:(?:\d+)\s*(?:celsius|c|' 
                    + 'fahrenheit|f))', re.IGNORECASE)
    #creates a list of all substrings matching regex
    celist = re.findall(unitEx, recipe)    
    print(celist)
    #regex to match first occurence of appropriate alphabetic character
    Ex = re.compile('[oplcmgkif]', re.IGNORECASE)
    #each string element in celist gets converted into
    #convertible elements(calls convertible element constructor)
    #and gets modified element and places it in list
    for ce in celist:        
        m = re.search(Ex,ce)#recognizes where the original string should split
        start= m.start()
        end = ce.__len__()
        value = float(ce[0:start])# takes double part of string and assigns it to value
        unit = ce[start:end]#takes measurement unit par of string and assigns it to unit
##        conEl = ConvertibleElement(value,unit)
##        self.setCElistElement(conEl)

        
    # setParsedRecipe(recipe):   
    #Replaces each convertable element with <#>
    num = 0
    for ce in celist:
        recipe = recipe.replace(ce, '<'+ str(num) + '>',1)
        num = num + 1
    print(recipe)
  
