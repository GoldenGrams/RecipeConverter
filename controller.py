#####################
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
#Call display view and return: <- still working on
#
# Food for thought.
# FInd a way to exit the program.
#
#
#
######################

from view import RecipeView
from modelRecipe import ModelRecipe
from decimal import *

class RecipeController:
        system = ""
        recipeText = ""
        strScale = ""
        scaling = 1
        errorFlag = False
        
        
        #Constructor
        #check for empty string
        #check for imperial and metric inputs
        def __init__(self,system,recipeText,strScale):
                self.inputCheck(system, recipeText, strScale)
                if self.errorFlag == False:
                        #finalRecipe = self.processRecipe()
                        print (self.system, self.scaling, self.recipeText)
                        #display final recipe for user
                        #convert scaling back to string
                        #before sending to user
                else:
                        #return error message and pull up
                        #the view with info for user to enter again.
                        return
        
        #Method to call the view
        def getOutput(self):
                v = RecipeView()
                return v.getOutput(self.system, self.recipeText, self.strScale)

        #Step through the process of converting the recipe
        #Return the altered recipe
        def processRecipe(self):
                recipeMod = ModelRecipe(self.recipeText)
                recipeMod.parseRecipe()
                recipeMod.convertRecipe(self.system, self.scaling)
                recipeMod.finalizedRecipe()
                finalRecipe = recipeMod.getFinalRecipe()
                return self.finalRecipe

        #Error Message method
        #Display an error message for the view
        def errorOutput(errorNum):
                if errorNum == 1:
                        x = "Not a valid scale value"
                elif errorNum == 2:
                        x = "No recipe found"
                elif errorNum == 3:
                        x = "Invlid serving size"
                        return x
                        
        #check input for empty or error strings
        def inputCheck(self, system, recipeText, strScale):
                if system.lower() in ['metric', 'imperial']:
                        self.system = system
                else:
                        #insert some sor of way to handle
                        #empty recipe input or other imputs
                        self.errorFlag = True
                if(recipeText):
                        self.recipeText = recipeText
                else:
                        #insert some sort way to handle
                        #empty recipe input
                        self.errorFlag  = True
                if strScale.isdecimal():
                        if Decimal(strScale) > 0 : 
                                self.scaling = Decimal(strScale)
                        else:
                                self.errorFlag = True
                elif (strScale):
                        #insert error input
                        #for none double and
                        #input other than
                        #empty string
                        self.errorFlag = True
                return
                
