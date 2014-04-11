import os 

class RecipeView:

	# instance variables
	measurementSystem = ""
	scaling = ""
	recipeText = ""

	def getDocument(self, measurementSystem, recipeText, scaling):
		# construct a path to the template file
		template = os.path.dirname(__file__) + "/view.tpl"
		with open (template, "r") as myfile:
    			text=myfile.read()

		text = text.replace("%measurementsystem%",measurementSystem)
		text = text.replace("%recipetext%",recipeText)
		text = text.replace("%imperialchecked%","checked" if measurementSystem=="imperial" else "")
		text = text.replace("%metricchecked%","checked" if measurementSystem=="metric" else "")
		text = text.replace("%scaling%",scaling)
		return text

	def setSystem(self,measurementSystem):
		self.measurementSystem = measurementSystem

	def setScaling(self,scaling):
		self.scaling = scaling

	def setRecipeText(self,recipeText):
		self.recipeText = recipeText




	def getOutput(self):
		return self.getDocument(self.measurementSystem,self.recipeText,self.scaling)
