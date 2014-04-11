import os 

class RecipeView:
	def getDocument(self, measurementSystem, recipeText, scaling):
		template = os.path.dirname(__file__) + "/view.tpl"
		with open (template, "r") as myfile:
    			text=myfile.read()

		text = text.replace("%measurementsystem%",measurementSystem)
		text = text.replace("%recipetext%",recipeText)
		text = text.replace("%imperialchecked%","checked" if measurementSystem=="imperial" else "")
		text = text.replace("%metricchecked%","checked" if measurementSystem=="metric" else "")
		text = text.replace("%scaling%",scaling)
		return text






	def getOutput(self,measurementSystem,recipeText,scaling):
		return self.getDocument(measurementSystem,recipeText,scaling)
