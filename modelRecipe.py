#ModelRecipe.py

from convertibleElement import *

import re

class ModelRecipe(object):
    origRecipe=""
    parsedRecipe=""
    finalRecipe=""
    scale=1.0
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


    #!!!!!!!!!!!!!!!
    #public methods        
    def parseRecipe (self):
        recipe=""
        recipe = self.getOrigRecipe()

        #regex for value and unit of measurement
        unitEx = re.compile( '''(?:(?:(?:\d*\s*\d+\s*(?:[/.]\s*\d*)?)\s*
                            (?:x\s*\d*\s*\d+\s*(?:[/.]\s*\d*)?)?)\s*
                            
                           (?:ounces?|ozs?|pounds?|lbs?|tablespoons?|teaspoons?
                           |tbsp?|tsp|fluid\s*ounces?|milligrams?|mg
                           |kilograms?|kgs?|grams?|g|fl?\s*oz|milliliters?|ml|liters?|l
                           |inches|inch|in|pints?|pts?|millimeters?|mm|centimeters?
                           |quarts?|qts?|cm|cups?)\s*
                           
                           (?:(?:(?:un)?\s*-?\s*salted)?\s*butter|margarine
                           |all\s*-?\s*purpose\s*-\s*flour|flour
                           |(?:(?:(?:light|dark)?\s*brown)?|(?:granulated)?)\s*sugar)?)
                           
                           |(?:(?:\d+)\s*(?:celsius|ºc|c|degrees\s*(?:celsius|fahrenheit|c|f)|
                           fahrenheit|ºf|f))''', re.IGNORECASE | re.VERBOSE)   
        #creates a list of all substrings matching regex
        celist = re.findall(unitEx, recipe)    
        #print(celist)
        #regex to match first occurence of appropriate alphabetic character
        splitEx = re.compile('[opldcmgkiftº]', re.IGNORECASE)
        #regex to find specific ingredients
        ingEx = re.compile('''(?:(?:un)?\s*-?\s*salted)?\s*butter|margarine
                          |all\s*-?\s*purpose\s*-?\s*flour
                          |(?:(?:(?:light|dark)?\s*brown)?|(?:granulated)?)\s*sugar''', re.IGNORECASE | re.VERBOSE) ##change
        self.createConEl(celist,splitEx,ingEx)
        recipe = self.addTags(celist, recipe)
                    
        self.setParsedRecipe(recipe)
        self.setParseCheck(True)

            #helper methods 
    #each string element in celist gets converted into
    #convertible elements(calls convertible element constructor)
    #and gets modified element and places it in list    
    def createConEl(self, list, r1,r2):
        for ce in list:
            splitCe = re.search(r1,ce)#recognizes where the original string should split
            start = splitCe.start()
            end = ce.__len__()
            strvalue = ce[0:start].strip()# takes double part of string and assigns it to value
            
            unitingred = ce[start:end]#takes string part of the convertible strin and assigns it to unitingred                      
            splitStr = re.search(r2,unitingred)#finds ingredient for the purpose to split unit and ingredient
            #if no ingredient was found, nofbs is assign to ingred
            if(splitStr == None):
                unit = unitingred
                ingred = 'nofbs'
            #if ingredient is found the original string is split
            else:
                begin = splitStr.start()
                unit = unitingred[0:begin]
                ingred = unitingred[begin:end]
            #Deals with numerical part of string
            xpos = strvalue.find('x')
            #if x is found btwn two numerical values, call convertible element constructor for each value
            if(xpos != -1):
                strval1 = strvalue[0:xpos-1].strip()
                strval2 = strvalue[xpos+1:strvalue.__len__()].strip()
                double1 = self.convertValue(strval1)
                double2 = self.convertValue(strval2)
                conEl1 = ConvertibleElement(double1, unit, ingred)
                conEl2 = ConvertibleElement(double2, unit, ingred)
                self.setCElistElement(conEl1)
                self.setCElistElement(conEl2)
            #if no x is found, convertible element constructor is called once
            else:
                double1 = self.convertValue(strvalue)
                conEl1 = ConvertibleElement(double1, unit, ingred)
                self.setCElistElement(conEl1)
                

    #Converts string into double. Returns double   
    def convertValue(self, strvalue):
        #if string contains whole number or decimal. gets converted to double easily
        if(strvalue.find('/')==-1):
            value = int(float(strvalue))
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
     
                #find marker, replace with data from appropriate CE: value+" "+units
                workingstring=re.sub("<"+str(counter)+">", str(self.listCE[counter].getValue())+" "+str(self.listCE[counter].getUnit()), workingstring)
                           
                counter = counter + 1
                
            self.setFinalRecipe(workingstring)
                   
            
        
    
                
                
        
            
