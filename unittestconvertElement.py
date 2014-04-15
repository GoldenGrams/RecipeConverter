#unit test script for ModelRecipe class

from modelRecipe import *
from convertibleElement import *
from convertElement import *

#testrecipe = "This is a derpy little test recipe"
#cElem1 = "3 inches"
#cElem2 = "10 cm"
#cElem3 = "2 cups"
#testobject = ModelRecipe(testrecipe)
cETest1 = ConvertibleElement(3,"inches")
cETest2 = ConvertibleElement(10, "cm")
cETest3 = ConvertibleElement(2, "cups")
#print (testobject.getOrigRecipe())
#print (cETest1.getValue() + cETest1.getUnit())
#print (cETest1.getUnit())
#print (cETest2.getValue())
#print (cETest2.getUnit())
#print (cETest3.getValue())
#print (cETest3.getUnit())

#testobject.setParsedRecipe("Use <0> of leather and <1> of string")
#cETest1.convertElement("Metric",1)
#print(testobject.getParsedRecipe())
#print (cETest1.getValue()+cETest1.getUnit())
#print (cETest1.getUnit())

#firstCE=ConvertibleElement(3, "feet")
#testobject.setCElistElement(firstCE)

#secondCE=ConvertibleElement(4, "meters")
#testobject.setCElistElement(secondCE)


#testobject.setConvertCheck(True)
#testobject.finalizeRecipe()


#print(testobject.getFinalRecipe())

print (str(cETest1.getValue()) + cETest1.getUnit())
cETest1.convertElement("Metric",1)
print (str(cETest1.getValue())+cETest1.getUnit())

print (str(cETest2.getValue()) + cETest2.getUnit())
cETest2.convertElement("Metric",1)
print (str(cETest2.getValue())+cETest2.getUnit())

print (str(cETest3.getValue()) + cETest3.getUnit())
cETest3.convertElement("Metric",1)
print (str(cETest3.getValue())+cETest3.getUnit())
