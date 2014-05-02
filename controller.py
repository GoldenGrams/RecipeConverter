#####################
#controller.py      #    
##############################################################################
#Recives input from user through view, and pass it on to Model recipe if all #
#fields are filled. Otherwise will send view an error message to display to  #
#users.                                                                      #   
#Calls ModelRecipe to convert the recipe and pass on the finalized recipe    #
#to the view along with the scaling and system used.                         #   
##############################################################################


from view import RecipeView
from modelRecipe import ModelRecipe
from decimal import *

class RecipeController:
        system = ""
        originalRecipeText = ""
        strScale = "1"
        scaling = 1
        errorFlag = False
        x = "Invalid input found"
        submitted = False
        
        
        #Method to call the view
        def getOutput(self):
                v = RecipeView()
                convertedRecipeText = ""
                #checks if user entered information in all fields
                #and that the input is valid
                #Convert the recipe if they are
                if self.errorFlag == False:
                        convertedRecipeText = self.processRecipe()
                elif self.submitted == True:
                        v.setErrorText(self.x)
                        errorFlag = False
                        #return error message and pull up
                        #reset errorFlag before recussion   
                      
                #display final recipe for user
                v.setSystem(self.system)
                v.setOriginalRecipeText(self.originalRecipeText)
                v.setConvertedRecipeText(convertedRecipeText)
                v.setScaling(self.strScale)
                return v.getOutput()

        #Step through the process of converting the recipe
        #Create a ModelRecipe object, and calls methods from ModelRecipe
        #Return the altered recipe
        def processRecipe(self):
                recipeMod = ModelRecipe(self.originalRecipeText)
                recipeMod.parseRecipe()
                recipeMod.convertRecipe(self.system, self.scaling)
                recipeMod.finalizeRecipe()
                finalRecipe = recipeMod.getFinalRecipe()
                return finalRecipe

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
        
        #mutator for system type
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

        #mutator for scaling
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

        #mutator for recipe text  
        def setRecipeText (self, recipeText):
                if(recipeText):
                        self.originalRecipeText = recipeText
                        
                elif not recipeText:
                        self.errorOutput(4)
                        self.errorFlag = True        
                else:
                        #insert some sort way to handle
                        #empty recipe input
                        self.errorOutput(2)
                        self.errorFlag  = True
                
        #Listener for submit button
        def setSubmit (self, submit):
                self.submitted = True if submit=="submit" else False                
