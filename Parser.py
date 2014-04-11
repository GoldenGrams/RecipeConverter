import re
recipe = ''

def parse(recipe):
    recipeFile = open("rec1.txt", "r") #recipeFile gets file object
    recipe = recipeFile.read() #recipe gets string object
    unitEx = re.compile('(?:\d+(?:\|/|.)?\d+)\s*(?:ounces?|oz|pounds?|lbs?| \
                    milligrams?|mg|grams?|g|kilograms?|kg| \
                    milliliters?|ml|liters?|inches|inch|in| \
                    millimeters?|mm|centimeters?|cm)', re.IGNORECASE)
    #creates a list of all substrings matching regex               
    conElist = re.findall(unitEx, recipe)
 

    print(conElist)
    #Replaces each convertable element with <#>
    num = 0
    for ce in conElist:
        recipe = recipe.replace(ce, '<'+ str(num) + '>',1)
        num = num + 1
    print(recipe)
    

    
