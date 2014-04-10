#####################
#####Variables#######
#-orgRecipe - string
#-parsedRecipe
#-NewRecipe - string
#-desiredUnits - string 
#-scale - double
#####################
# Controller Class:
# Class begins with calling view to ask for user input
# After recieving user input, Controller would create a recipie object.
# TBC
#
#####################
#pass string that will state either imperial or metric
#Call upon view to create view prompting user for input
#Recieve user inputs from view
#create a Recipe object
#ModelRecipe.parseRecipe
#ModelRecipe.convertRecipe(desiredUnit, scale)
#ModelRecipe.getFinalRecipe()
#Calls upon the OutputView and display the recipe

#######################
#Controller gain user input from view.
#Call display view and return 
#How view passes on inputs is still undecided
#
#######################
# Food for thought.
# FInd a way to exit the program.
#
#
#
######################


#####
#get output 
#
#setmethod for variable
#######
#Write a constructor that handles scaling, recipe, and desired units
#
#
#######

from view import RecipeView
class RecipeController:
        system = ""
        recipeText = ""
        scaling = ""
        def __init__(self,system,recipeText,scaling):
                self.system = system
                self.recipeText = recipeText
                self.scaling = scaling
                return

        def getOutput(self):
                v = RecipeView()
                return v.getOutput(self.system, self.recipeText)
