from view import RecipeView

v = RecipeView()
v.setSystem("imperial")
v.setRecipeText("sample recipe text")
v.setScaling("1")
print (v.getOutput())
