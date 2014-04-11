#####################
#controller.py
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
#Call display view and return converted recipe <- still working on
#Will recusively call itself if recieve no variable or incorrect input
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
        x = "Invalid input found"
        
        
        #Method to call the view
        def getOutput(self):
                v = RecipeView()
                if self.errorFlag == False:
                        #finalRecipe = self.processRecipe()
                        finalRecipe = self.recipeText
                        #display final recipe for user
                        #convert scaling back to string
                        #actually don't need to do that
                        #before sending to user
                else:
                        v.setErrorText(self.x)
                        errorFlag = False
                        #return error message and pull up
                        #the view with info for user to enter again.
                        #reset errorFlag before recussion   
                      
                
                v.setSystem(self.system)
                v.setRecipeText(self.recipeText)
                v.setScaling(self.strScale)
                return v.getOutput()

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
        #Return an error message based upon a situation
        def errorOutput(self, errorNum):
                if errorNum == 1:
                        self.x = "Not a valid scale value"
                elif errorNum == 2:
                        self.x = "No recipe found"
                elif errorNum == 3:
                        self.x = "Invalid serving size"
                elif errorNum == 4:
                        self.x = "Empty field found"
                        return 
        
#break down inputCheck
#mutators for inputs
        def setSystem(self, system):
                if system.lower() in ['metric', 'imperial']:
                        self.system = system
                elif not system:
                        self.errorOutput(4)
                        self.errorFlag = True
                else:
                        #insert some sor of way to handle
                        #empty recipe input or other imputs
                        self.errorOutput(1)
                        self.errorFlag = True

        def setScaling(self, strScale):
                if strScale.isdecimal():
                        if Decimal(strScale) > 0 : 
                                self.scaling = Decimal(strScale)
                        else:
                                self.errorOutput(3)
                                self.errorFlag = True
                elif not strScale:
                        self.errorOutput(4)
                        self.errorFlag = True
                        
                else:
                        #insert error input
                        #for none double and
                        #input other than
                        #empty string
                        self.errorOutput(3)
                        self.errorFlag = True
                        
        def setRecipeText (self, recipeText):
                if(recipeText):
                        self.recipeText = recipeText
                        
                elif not recipeText:
                        self.errorOutput(4)
                        self.errorFlag = True        
                else:
                        #insert some sort way to handle
                        #empty recipe input
                        self.errorOutput(2)
                        self.errorFlag  = True
                
                
