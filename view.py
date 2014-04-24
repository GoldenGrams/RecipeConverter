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

		# set converted recipe to display if it exists, otherwise display the original for input
		text = text.replace("%originalrecipecontentinnerstyledisplay%","block" if self.convertedRecipeText == "" else "none")
		text = text.replace("%convertedrecipecontentinnerstyledisplay%","none" if self.convertedRecipeText == "" else "block")
		text = text.replace("%originalbuttonstyle%","font-weight:bold" if self.convertedRecipeText == "" else "font-weight:none")
		text = text.replace("%convertedbuttonstyle%","font-weight:normal" if self.convertedRecipeText == "" else "font-weight:bold")

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
