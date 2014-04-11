#ModelRecipe.py
class ModelRecipe(object):
    #constructor (set privacy?)
    def __init__ (self, givenrecipe):
        self.origRecipe=givenrecipe
        self.parsedRecipe=""
        self.finalRecipe=""
        self.scale=1
        self.didParse=False
        self.didConvert=False
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
        self.didConver=givenboolean
    def setCElistElement (self, givenCE):
        self.listCE.append(givenCE)

    #public methods
        
    def parseRecipe (self):
        workingString=""
        workingString = self.getOrigRecipe(self)
        # pass workingString to parser (josie's method)
        # set result of parsing to workingString
        workingString.parse(workingString)
        self.setParsedRecipe(workingString)
        self.setParseCheck(True)
        
    def convertRecipe (desiredsystem, scaling):
        workingCE=null
        if self.getParseCheck():
            counter = 0
            while len(listCE) > counter:
                workingCE=getConvertibleElement(counter)
                workingCE.convertElement(desiredsystem, scaling)
                counter = counter + 1
        self.setConvertCheck(True)
        
    def finalizeRecipe (self):
        workingstring=""
        if self.getConvertCheck():
            workingstring=self.getParsedRecipe
            counter=0
            while len(listCE) > counter:
                #replace denoter with listCE(counter)
                counter = counter + 1
                workingstring.replace("<"+counter+">",type(listCE[counter]))
                
            # self.setFinalRecipe(workingstring)
                pass
            pass
        pass
    
                
                
        
            
