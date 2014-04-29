import sys
import os
import platform
import urllib.parse
sys.path.append(os.path.dirname(__file__))
from controller import RecipeController



#def application(environ, start_response):
def application(post_input):
        status = '200 OK'

        #post_input = urllib.parse.parse_qs(environ['wsgi.input'].readline().decode(),True)

        recipeText = post_input.get('recipeText',[''])[0]
        system = post_input.get('system',[''])[0]
        scaling = post_input.get('scaling',[''])[0]
        submit = post_input.get('submit',[''])[0]


#        controller = RecipeController( system,recipeText,scaling )

        controller = RecipeController()
        controller.setSystem( system )
        controller.setRecipeText( recipeText )
        controller.setScaling( scaling )
        controller.setSubmit( submit )
        output  = controller.getOutput()
        output  = output + "<!-- python-version: " + platform.python_version() + "-->"

        response_headers = [('Content-type', 'text/html'),
                ('Content-Length', str(len(output)))]
        #start_response(status, response_headers)
        return [output]


def test():
	system = "imperial"
	scaling = "1"
	recipeText = "118.3 ml  453.6 g Whole-berry cranberry sauce"
	submit = "submit"

	formdata = {'recipeText':{0:recipeText}, 'system':{0:system}, 'scaling':{0:scaling}, 'submit':{0:submit}}
	#formdata = {}

	print (application(formdata)[0])

test()
input("press enter to exit")
