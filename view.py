import os 

class RecipeView:

	# instance variables
	measurementSystem = ""
	scaling = ""
	recipeText = ""
	errorText = ""

	def getDocument(self):
		# construct a path to the template file
		template = os.path.dirname(__file__) + os.sep + "view.tpl"
		with open (template, "r") as myfile:
    			text=myfile.read()

		text = text.replace("%measurementsystem%",self.measurementSystem)
		text = text.replace("%recipetext%",self.recipeText)
		text = text.replace("%errortext%",self.errorText)
		text = text.replace("%imperialchecked%","checked" if self.measurementSystem=="imperial" else "")
		text = text.replace("%metricchecked%","checked" if self.measurementSystem=="metric" else "")
		text = text.replace("%scaling%",self.scaling)
		return text

	def setSystem(self,measurementSystem):
		self.measurementSystem = measurementSystem

	def setScaling(self,scaling):
		self.scaling = scaling

	def setRecipeText(self,recipeText):
		self.recipeText = recipeText

	def setErrorText(self,errorText):
		self.errorText = errorText


	def getOutput(self):
		return self.getDocument()
