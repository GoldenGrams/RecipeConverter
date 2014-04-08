from controller import RecipeController

def safeGetFormdata( formdata, fieldname ):
        try:
                field = formdata[fieldname]
        except:
                field = ""
        return field



def handler():

	formdata = {}

	formdata["system"] = "imperial"
	formdata["recipeText"] = "sample recipe text"
	formdata["scaling"] = "1"
	
	system = safeGetFormdata( formdata, "system" )
	recipeText = safeGetFormdata( formdata, "recipeText" )
	scaling = safeGetFormdata( formdata, "scaling" )
	controller = RecipeController( system,recipeText,scaling )
	print controller.getOutput()

	return 0

handler()
