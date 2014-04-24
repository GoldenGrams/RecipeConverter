import os 

class RecipeView:

	# instance variables
	measurementSystem = ""
	scaling = ""
	originalRecipeText = ""
	convertedRecipeText = ""
	errorText = ""

	def getDocument(self):
		# construct a path to the template file
		template = os.path.dirname(__file__) + os.sep + "view.tpl"
		with open (template, "r") as myfile:
    			text=myfile.read()

		text = text.replace("%measurementsystem%",self.measurementSystem)
		text = text.replace("%originalrecipetext%",self.originalRecipeText)
		text = text.replace("%convertedrecipetext%",self.convertedRecipeText)
		text = text.replace("%errortext%",self.errorText)
		text = text.replace("%imperialchecked%","checked" if self.measurementSystem=="imperial" else "")
		text = text.replace("%metricchecked%","checked" if self.measurementSystem=="metric" else "")
		text = text.replace("%scaling%",self.scaling)
		return text

	def setSystem(self,measurementSystem):
		self.measurementSystem = measurementSystem

	def setScaling(self,scaling):
		self.scaling = scaling

	def setOriginalRecipeText(self,originalRecipeText):
		self.originalRecipeText = originalRecipeText

	def setConvertedRecipeText(self,convertedRecipeText):
		self.convertedRecipeText = convertedRecipeText

	def setErrorText(self,errorText):
		self.errorText = errorText


	def getOutput(self):
		return self.getDocument()
