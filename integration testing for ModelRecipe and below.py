#ModelRecipe unit test complete
#ConvertibleElement unit test complete
#josie's parser's component testing complete
#andrew's converter's component testing complete
#testing parser's integration into ModelRecipe
#testing converter's integration into ConvertibleElement

from modelRecipe import *

testrecipe = "4 1/2 cups 5 f 22 c 4.0 sm Acorn squash 0.0 Salt 118.3ml Butter or margarine 118.3 ml Honey 453.6 g Whole-berry cranberry sauce"

testobject = ModelRecipe(testrecipe)

print(testobject.getOrigRecipe())

testobject.parseRecipe()

print(testobject.getParsedRecipe())

testobject.convertRecipe("Imperial", 1)

print(testobject.getCE(2).getValue())

testobject.finalizeRecipe()

print(testobject.getFinalRecipe())
