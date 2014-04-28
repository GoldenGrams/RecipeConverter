import sys
import os
import platform
import cgi
sys.path.append(os.path.dirname(__file__))
from controller import RecipeController



def application(environ, start_response):
	status = '200 OK'
	
	post_input = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ, keep_blank_values=True)

	try:
		recipeText = post_input['recipeText'].value
	except:
		recipeText = ""

	try:
		system=post_input['system'].value
	except:
		system=''

	try:
		scaling=post_input['scaling'].value
	except:
		scaling=''

	try:
		submit=post_input['submit'].value
	except:
		submit=''


	try:
		if( post_input['fileuploadinput'].value ):
			recipeText =  post_input['fileuploadinput'].file.read().decode("utf-8")
	except:
		pass




	controller = RecipeController()
	controller.setSystem( system )
	controller.setRecipeText( recipeText )
	controller.setScaling( scaling )
	controller.setSubmit( submit )



	output  = controller.getOutput()
	output  = output + "<!-- python-version: " + platform.python_version() + "-->"

	response_headers = [('Content-type', 'text/html'),
		('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	return [output]
