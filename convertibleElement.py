#ConvertibleElement.py
class ConvertibleElement(object):
        
    #constructor
    def __init__ (self, givenvalue, givenunit):
        self.value=givenvalue
        self.unit=givenunit

    #accessor methods
    def getValue (self):
        return self.value
    def getUnit (self):
        return self.unit

    #mutator methods
    def setValue (self, givenvalue):
        self.value=givenvalue
    def setUnit (self, givenunit):
        self.unit=givenunit

    def convertElement (self, desiredunits, scale):
        #this is andrew's method
        #return converted element
        pass
