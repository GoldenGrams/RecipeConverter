from mod_python import apache
from mod_python import util
from controller import RecipeController

def safeGetFormdata( formdata, fieldname ):
        try:
                field = formdata[fieldname]
        except:
                field = ""
        return field



def handler(req):

	req.content_type="text/html"
	formdata = util.FieldStorage(req)
	system = safeGetFormdata( formdata, "system" )
	recipeText = safeGetFormdata( formdata, "recipeText" )
	scaling = safeGetFormdata( formdata, "scaling" )
	controller = RecipeController( system,recipeText,scaling )
	req.write(controller.getOutput())

	return apache.OK
