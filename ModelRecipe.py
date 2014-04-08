PARSER
 
//recipe is stored in the variable recipe
  Recipe = recipe string object
//pattern object is created for all possible convertible elements that will be found in a recipe
  unitRegularExpression = re.compile(‘(\d+) (unit?)’)
//Recipe is analyzed.
  An array is created containing all substrings/convertible elements matching the regex.
  array = findall(unitRegularExpression, recipe)
  for convertible element in array:
      call convertible element constructor 
      element gets converted and placed back into array
//iterate through array
  for converted element in list:
      setElement() //replaces unconverted element with converted element    
    
//creates another recipe object. will contain new recipe with tagged elements
  taggedrecipe = recipe
  for item in list:
      each convertible element in recipe will be replaced with convertible
      element in btwn angle brackets(ex. 1ml  will be <1ml>)
    
