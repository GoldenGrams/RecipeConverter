#unit test script for ModelRecipe class

from modelRecipe import *
from convertibleElement import *

testrecipe = "4 1/2 cups5 ºf 22 c 4.0 sm Acorn squash 0.0 Salt 118.3mlButter or margarine 118.3 ml Honey 453.6 g Whole-berry cranberry sauce"

testobject = ModelRecipe(testrecipe)

print (testobject.getOrigRecipe())

testobject.parseRecipe()

print(testobject.getParsedRecipe())

print(testobject.getCE(0))

#firstCE=ConvertibleElement(3, "cm")
#testobject.setCElistElement(firstCE)

#secondCE=ConvertibleElement(4, "inches")
#testobject.setCElistElement(secondCE)

#testobject.convertRecipe("Imperial", 1)

testobject.finalizeRecipe()


print(testobject.getFinalRecipe())

