import sys
import os
import platform
import urllib.parse
sys.path.append(os.path.dirname(__file__))
from controller import RecipeController



def application(environ, start_response):
	status = '200 OK'
	
	post_input = urllib.parse.parse_qs(environ['wsgi.input'].readline().decode(),True)

	recipeText = post_input.get('recipeText',[''])[0]
	system = post_input.get('system',[''])[0]
	scaling = post_input.get('scaling',[''])[0]

	controller = RecipeController( system,recipeText,scaling )
	output  = controller.getOutput()
	output  = output + "<!-- python-version: " + platform.python_version() + "-->"

	response_headers = [('Content-type', 'text/html'),
		('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	return [output]
