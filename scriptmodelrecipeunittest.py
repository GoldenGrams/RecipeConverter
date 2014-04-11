#unit test script for ModelRecipe class

from modelRecipe import *
from convertibleElement import *

testrecipe = "This is a derpy little test recipe"

testobject = ModelRecipe(testrecipe)

print (testobject.getOrigRecipe())

testobject.setParsedRecipe("Use <0> of leather and <1> of string")

print(testobject.getParsedRecipe())

firstCE=ConvertibleElement(3, "cm")
testobject.setCElistElement(firstCE)

secondCE=ConvertibleElement(4, "inches")
testobject.setCElistElement(secondCE)

#testobject.convertRecipe("Imperial", 1)

testobject.finalizeRecipe()


print(testobject.getFinalRecipe())

