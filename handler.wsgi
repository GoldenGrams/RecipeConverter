import sys
import os
import platform
import cgi
import urllib.request
import re

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

	try:
		if( post_input['urluploadinput'].value):
			recipeText = urllib.request.urlopen(post_input['urluploadinput'].value).read().decode("utf-8")
			#remove all of the newlines
			recipeText = recipeText.replace(" ","!space!")
			recipeText = "".join(recipeText.split())
			recipeText = recipeText.replace("!space!"," ")
			recipeText = re.sub("^.*<\/head>","",recipeText)
			recipeText = re.sub("<script[^>]*\/>","",recipeText)
			recipeText = re.sub("<script.*?<\/script>","",recipeText)
			recipeText = re.sub("</[^>]*>","\n",recipeText)
			recipeText = re.sub("<[^>]*>","",recipeText)
			recipeText = re.sub("^[\s]*","",recipeText,flags=re.MULTILINE)
			recipeText = re.sub("^$","",recipeText)
	except:
		pass




	controller = RecipeController()
	controller.setSystem( system )
	controller.setRecipeText( recipeText )
	controller.setScaling( scaling )
	controller.setSubmit( submit )



	output  = controller.getOutput().encode()
	#output  = output + "<!-- python-version: " + platform.python_version() + "-->"

	response_headers = [('Content-type', 'text/html'),
		('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	return [output]
