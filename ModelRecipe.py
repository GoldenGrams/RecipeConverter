# PARSER
#  
# //recipe is stored in the variable recipe
# Recipe = recipe string object
# //pattern objects are created for all units used in recipes
# unitRegularExpression = re.compile(‘(\d+) (unit?)’)
# //Recipe is analyzed.
# If(user inputs imperial to metric)
# If(text matches ‘# unit’) //should match imperial units only
#             	ListOfPositions = the start and end positions of where ‘# unit’ has matched
#                         For(every position in ListOfPositions)
#             		Value= actual number matched
#             		Unit = unit matched
#             	            Converter object uses unit and value to properly convert it to metric.
#             	            Once converted text is returned, Original text is replaced with converted
#             	            Text.
#                             	//ConvertedRecipe will be returned back to Model Recipe     	
#                             	ConvertedRecipe = recipe with all units converted 
#             Else  if//no matches were round
#             	no text was matched
#                         some sort of error message is thrown  
# else if(user inputs metric to imperial)
# If(text matches ‘# unit’) //should match metric units only
#             	ListOfPositions = the start and end positions of where ‘# unit’ has matched
#                         For(every position in ListOfPositions)
#                         	Value = actual number matched
#                             	Unit = unit matched
#                             	 Converter object uses unit and value to properly convert it to imperial.
#                             	 Once converted text is returned, Original text is replaced with converted
#                             	 Text.
#                             	//ConvertedRecipe will be returned back to recipe
#                             	ConvertedRecipe = recipe with all units converted
#             	Else if //no matches were round
#                             	No text was matched
#             	            	some sort of error message is thrown
# 
# 
