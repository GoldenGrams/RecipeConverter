import re

def parseTheRecipe(recipe):
    #regex for value and unit of measurement    
    unitEx = re.compile('''(?:(?:(?:\d*\s*\d+\s*(?:[/.]\s*\d+)?)\s*

                            (?:x\s*\d*\s*\d+\s*(?:[/.]\s*\d*)?)?)\s*
                            
                           (?:ounces?|ozs?|pounds?|lbs?|tablespoons?|teaspoons?
                           |tbsp?|tsp|fluid\s*ounces?|milligrams?|mg|grams?|g
                           |kilograms?|kgs?|fl?\s*oz|milliliters?|ml|liters?|l
                           |inches|inch|in|pints?|pts?|millimeters?|mm|centimeters?
                           |quarts?|qt|cm|cups?)\s*
                           
                           (?:(?:(?:un)?\s*-?\s*salted)?\s*butter|margarine
                           |all\s*-?\s*purpose\s*-\s*flour|flour
                           |(?:(?:(?:light|dark)?\s*brown)?|(?:granulated)?)\s*sugar)?)
                           
                           |(?:(?:\d+)\s*(?:celsius|ºc|c|degrees\s*(?:celsius|fahrenheit|c|f)|
                           fahrenheit|ºf|f))''', re.IGNORECASE | re.VERBOSE)
    #creates a list of all substrings matching regex
    celist = re.findall(unitEx, recipe)    
    #print(celist)
    #regex to match first occurence of appropriate alphabetic character
    splitEx = re.compile('[oplcdmgkiftº]', re.IGNORECASE)
    #regex to find specific ingredients
    ingEx = re.compile('''(?:(?:un)?\s*-?\s*salted)?\s*butter|margarine
                          |all\s*-?\s*purpose\s*-?\s*flour
                          |(?:(?:(?:light|dark)?\s*brown)?|(?:granulated)?)\s*sugar'''
                           , re.IGNORECASE | re.VERBOSE)
    print(celist)
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
        strvalue = ce[0:start].strip()# takes double part of string and assigns it to value/removes white space
               
        unitingred = ce[start:end]#takes measurement unit and ingredient(if exist) part of string and assigns it to unitingre      
        splitStr = re.search(r2,unitingred)
      
        #Assigns unitingred to unit if no special ingredient is found
        if(splitStr == None):
            unit = unitingred
            ingred = 'nofbs'
        else:
            begin = splitStr.start()
            unit = unitingred[0:begin]
            ingred = unitingred[begin:end]
  
        #Deals with value numerical part of string
        xpos = strvalue.find('x')
        if(xpos != -1):
            strval1 = strvalue[0:xpos-1].strip()
            strval2 = strvalue[xpos+1:strvalue.__len__()].strip()
            double1 = convertValue(strval1)
            double2 = convertValue(strval2)
            print(str(double1) +' unit: '+ unit + ' ing: ' + ingred)
            print(str(double2) +' unit: '+ unit + ' ing: ' + ingred)
##            conEl1 = ConvertibleElement(double1,unit,ingred)
##            conEl2 = ConvertibleElement(double2,unit,ingred)
##            self.setElistElement(conEl1)
##            self.setElistElement(conEl2)
        else:
            double1 = convertValue(strvalue)
            print(str(double1) +' unit: '+ unit + ' ing: ' + ingred)
##            conEl1 = ConvertibleElement(double1, unit, ingred)
##            self.setElistElement(conEl1)

#Converts string into double. Returns double   
def convertValue(strvalue):
    #if string contains whole number or decimal. gets converted to double easily
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
            print(fnum)
            newstr = strvalue[white:strvalue.__len__()]
            print(newstr)
            numden = newstr.split('/')
            num = float(numden.pop(0))
            den = float(numden.pop(0))
            value = (float(fnum))+(num/den)
    return value

#Replaces each convertable element with <#>. Returns recipe with tagged elements
def addTags(list,recipe): 
    num = 0
    for ce in list:
        if(ce.find('x') != -1):
            dimension = [] 
            dimension = ce.split('x')
            firdim = dimension[0]
            recipe = recipe.replace(firdim, '<' + str(num) + '>',1)
            num = num + 1
            secdim = dimension[1]
            recipe = recipe.replace(secdim, '<' + str(num) + '>',1)
            num = num + 1
        else:        
            recipe = recipe.replace(ce, '<'+ str(num) + '>',1)
            num = num + 1
    #print(recipe)
    return recipe
    
  


