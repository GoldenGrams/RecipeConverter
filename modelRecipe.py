#ModelRecipe.py

from convertibleElement import *

import re

class ModelRecipe(object):
    origRecipe=""
    parsedRecipe=""
    finalRecipe=""
    scale=1
    didParse=False
    didConvert=False
    listCE=[]
    #constructor (set privacy?)
    def __init__ (self, givenrecipe):
        self.origRecipe=givenrecipe
        self.parsedRecipe
        self.finalRecipe
        self.scale
        self.didParse
        self.didConvert
        self.listCE=[]
        
        
    #accessor methods (privacy?)
    def getOrigRecipe (self):
        return self.origRecipe
    def getParsedRecipe (self):
        return self.parsedRecipe
    def getScale (self):
        return self.scale
    def getParseCheck (self):
        return self.didParse
    def getConvertCheck (self):
        return self.didConvert
    def getList (self):
        return self.listCE
    def getCE (self, index):
        return self.listCE[index]
    def getFinalRecipe (self):
        return self.finalRecipe
	

    #mutator methods (privacy?)
    def setOrigRecipe (self, givenstring):
        self.origRecipe=givenstring
    def setParsedRecipe (self, givenstring):
        self.parsedRecipe=givenstring
    def setFinalRecipe (self, givenstring):
        self.finalRecipe=givenstring
    def setScale (self, givenscale):
        self.scale=givenscale
    def setParseCheck (self, givenboolean):
        self.didParse=givenboolean
    def setConvertCheck (self, givenboolean):
        self.didConvert=givenboolean
    def setCElistElement (self, givenCE):
        self.listCE.append(givenCE)

    #helper methods
    #each string element in celist gets converted into
    #convertible elements(calls convertible element constructor)
    #and gets modified element and places it in list    
    def createConEl(self, list, regex):
        for ce in list:
            splitCe = re.search(regex,ce)#recognizes where the original string should split
            start = splitCe.start()
            end = ce.__len__()
            strvalue = ce[0:start].strip()# takes double part of string and assigns it to value
            double = self.convertValue(strvalue)                
            unit = ce[start:end]#takes measurement unit part of string and assigns it to unit                      
            #changes degree unit to degrees f or degrees c
            if ((unit == 'fahrenheit') or (unit == 'ºf') or (unit == 'f')):
                unit = 'degrees f'
            elif ((unit == 'celsius') or (unit == 'ºc') or (unit == 'c')):
                unit = 'degrees c'
            else:
                unit = unit
            #print(double)
            #print(unit)
            conEl = ConvertibleElement(double,unit)
            self.setCElistElement(conEl)
            
            

    #Converts string into double. Returns double   
    def convertValue(self, strvalue):
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
                newstr = strvalue[white:strvalue.__len__()]
                numden = newstr.split('/')
                num = float(numden.pop(0))
                den = float(numden.pop(0))
                value = (float(fnum))+(num/den)
        return value

    #Replaces each convertable element with <#>. Returns recipe with tagged elements
    def addTags(self,list,recipe): 
        num = 0
        for ce in list:
            recipe = recipe.replace(ce, '<'+ str(num) + '>',1)
            num = num + 1
        #print(recipe)
        return recipe


    #!!!!!!!!!!!!!!!
    #public methods        
    def parseRecipe (self):
        recipe=""
        recipe = self.getOrigRecipe()

        #regex for value and unit of measurement
        unitEx = re.compile( '''(?:(?:\d*\s*\d+(?:/|.)?\d*)\s*(?:ounces?|oz|pounds?|lbs?
                              |fluid\s*ounces?|milligrams?|mg|grams?|g|kilograms?|kg 
                              |fl\s*oz|milliliters?|ml|liters?|l|inches|inch|in|pints?
                              |millimeters?|mm|centimeters?|quarts?|qt|cm|cups?))|
                              (?:(?:\d+)\s*(?:celsius|ºc|c|fahrenheit|ºf|f))''', re.IGNORECASE | re.VERBOSE)   
        #creates a list of all substrings matching regex
        celist = re.findall(unitEx, recipe)    
        #print(celist)
        #regex to match first occurence of appropriate alphabetic character
        splitEx = re.compile('[oplcmgkifº]', re.IGNORECASE)
        self.createConEl(celist,splitEx)
        recipe = self.addTags(celist, recipe)
                
    
        self.setParsedRecipe(recipe)
        self.setParseCheck(True)

        # pass workingString to parser (josie's method)
        # set result of parsing to workingString
        #self.parseTheRecipe(workingString)

        
    def convertRecipe (self, desiredsystem, scaling):
        workingCE = None
        if self.getParseCheck():
            counter = 0
            while len(self.getList()) > counter:
                workingCE=self.getCE(counter)
                
                #andrew's method
                workingCE.convertElement(desiredsystem, scaling)

                counter = counter + 1
        self.setConvertCheck(True)
        
    def finalizeRecipe (self):
        workingstring=""
        if self.getConvertCheck():
            workingstring=self.getParsedRecipe()
                        
            counter=0
            while len(self.getList()) > counter:
                x=self.listCE[counter].getValue()
                x="%.3f" % x
                #find marker, replace with data from appropriate CE: value+" "+units
                workingstring=re.sub("<"+str(counter)+">", " "+ str(x)+" "+str(self.listCE[counter].getUnit())+" ", workingstring)
                           
                counter = counter + 1
                
            self.setFinalRecipe(workingstring)
                   
            
        
    
                
                
        
            
