#unit test script for ModelRecipe class

from modelRecipe import *
from convertibleElement import *

testrecipe = "This is a derpy little test recipe"

testobject = ModelRecipe(testrecipe)

print (testobject.getOrigRecipe())

testobject.setParsedRecipe("<0> is a <1>")

print(testobject.getParsedRecipe())

firstCE=ConvertibleElement(3, "feet")
testobject.setCElistElement(firstCE)

secondCE=ConvertibleElement(4, "meters")
testobject.setCElistElement(secondCE)


testobject.setConvertCheck(True)
testobject.finalizeRecipe()


print(testobject.getFinalRecipe())

