# begin
# Instantiate instant variable of other classes
# Call ViewWindow to create a window
# while TRUE
# 	Created a view ViewUserInput to promp for user input
# 	Retrieve recipe input from user
# 	Use uploadRecipe method with user input
# 	Retrieve chosen conversion choice from user
# 	Retrieve serving size from user
# 	Send information over to ModelRecipe for parsing and converstion
# 	Retrieve new Rececipe
# 	Display with View Output
# End while
# 	
# 
# 	
# **Unsure how to prompt for changes or where prompting for changes occurs
# **Also unsure what classes will specifically handle what job
# 	*ex: Who will handle exit critera
# 	*what class will handle parsing/conversion
# 
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
