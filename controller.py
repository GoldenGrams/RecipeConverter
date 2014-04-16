#####################
#controller.py
#####################
#
######################

from view import RecipeView
from modelRecipe import ModelRecipe
from decimal import *

class RecipeController:
        system = ""
        recipeText = ""
        strScale = "1"
        scaling = 1
        errorFlag = False
        x = "Invalid input found"
        submitted = False
        
        
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
                elif self.submitted == True:
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
                        #insert some sort of way to handle
                        #empty recipe input or other imputs
                        self.errorOutput(1)
                        self.errorFlag = True

        def setScaling(self, strScale):
                self.strScale = strScale
                try:
                        if Decimal(strScale) > 0 : 
                                self.scaling = Decimal(strScale)
                        else:
                                self.errorOutput(3)
                                self.errorFlag = True
                except:
                        self.strScale = "1"
                        if not strScale:
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
                

        def setSubmit (self, submit):
                self.submitted = True if submit=="submit" else False                
