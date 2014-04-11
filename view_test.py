from view import RecipeView

v = RecipeView()
v.setMeasurementSystem("imperial")
v.setRecipeText("sample recipe text")
v.setScaling("1")
print (v.getOutput())
