import sys
import os
import platform
import cgi
import urllib.request
import re
# determine the location of the current file and add it to the system path.
# this will allow us to load local modules
sys.path.append(os.path.dirname(__file__))
from controller import RecipeController

# built-in definition specified by mod_wsgi and apache2
def application(environ, start_response):
	status = '200 OK'
	
        # get the post input from the environment that has been passed
	post_input = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ, keep_blank_values=True)

	# get individual form input
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

	# hack to get file upload input.  move this to a file model class later
	try:
		if( post_input['fileuploadinput'].value ):
			recipeText =  post_input['fileuploadinput'].file.read().decode("utf-8")
	except:
		pass
	# hack to get url upload input.  move this to a url model class later
	try:
		if( post_input['urluploadinput'].value):
			recipeText = urllib.request.urlopen(post_input['urluploadinput'].value).read().decode("utf-8")
			#sanitize the html so we can view it in a div
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



	#load the controller
	controller = RecipeController()
	
	#pass data to the controller
	controller.setSystem( system )
	controller.setRecipeText( recipeText )
	controller.setScaling( scaling )
	controller.setSubmit( submit )



	#get output back from the controller
	output  = controller.getOutput().encode()
	#output  = output + "<!-- python-version: " + platform.python_version() + "-->"

	#build the response to the browser using the output from the controller
	response_headers = [('Content-type', 'text/html'),
		('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	#return the output to mod_wsgi/apache
	return [output]
