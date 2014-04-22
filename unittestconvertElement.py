#unit test script for ModelRecipe class

from modelRecipe import *
from convertibleElement import *
from convertElement import *

#testrecipe = "This is a derpy little test recipe"
#cElem1 = "3 inches"
#cElem2 = "10 cm"
#cElem3 = "2 cups"
#testobject = ModelRecipe(testrecipe)

#Testing "Metric"

#cETest001 = ConvertibleElement(4 1/2, "cups")
#cETest002 = ConvertibleElement(5, "ºf")
cETest003 = ConvertibleElement(22, "degrees C")
'''
                               4.0 sm Acorn squash
                               0.0 Salt
                               118.3mlButter or margarine
                               118.3 ml Honey
                               453.6 g Whole-berry cranberry sauce
'''
'''
cETest1 = ConvertibleElement(3,"inches")
cETest2 = ConvertibleElement(1, "in")
cETest3 = ConvertibleElement(2, "inch")
cETest4 = ConvertibleElement(212, "degrees F")
cETest5 = ConvertibleElement(68, "degrees Fahrenheit")
cETest6 = ConvertibleElement(2, "lbs")
cETest7 = ConvertibleElement(2, "pounds")
cETest8 = ConvertibleElement(1, "pound")
cETest9 = ConvertibleElement(1, "oz")
cETest10 = ConvertibleElement(4, "ounces")
cETest11 = ConvertibleElement(1, "ounce")
cETest12 = ConvertibleElement(1, "qt")
cETest13 = ConvertibleElement(1, "quart")
cETest14 = ConvertibleElement(2, "quarts")
cETest15 = ConvertibleElement(1, "pt")
cETest16 = ConvertibleElement(1, "pint")
cETest17 = ConvertibleElement(4, "pints")
cETest18 = ConvertibleElement(1, "cup")
cETest19 = ConvertibleElement(3, "cups")
cETest20 = ConvertibleElement(6, "fluid ounces")
cETest21 = ConvertibleElement(5, "fl oz")
#Testing "Imperial"
cETest22 = ConvertibleElement(1, "cm")
cETest23 = ConvertibleElement(5, "centimeters")
cETest24 = ConvertibleElement(1, "centimeter")
cETest25 = ConvertibleElement(20, "degrees C")
cETest26 = ConvertibleElement(0, "degrees Celsius")
cETest27 = ConvertibleElement(1, "kilogram")
cETest28 = ConvertibleElement(1, "kg")
cETest29 = ConvertibleElement(2, "kilograms")
cETest30 = ConvertibleElement(1, "g")
cETest31 = ConvertibleElement(1, "gram")
cETest32 = ConvertibleElement(28, "grams")
cETest33 = ConvertibleElement(1, "L")
cETest34 = ConvertibleElement(1, "liter")
cETest35 = ConvertibleElement(1, "liters")
cETest36 = ConvertibleElement(1, "mL")
cETest37 = ConvertibleElement(473, "milliliters")
cETest38 = ConvertibleElement(1, "milliliter")

cETest39 = ConvertibleElement(33.8, "degrees Fahrenheit")
cETest40 = ConvertibleElement(1.5, "cups")
cETest41 = ConvertibleElement(0.5, "L")
'''
'''
cETest5 = ConvertibleElement(1, "pound")
cETest5 = ConvertibleElement(1, "pound")
cETest5 = ConvertibleElement(1, "pound")
'''



#print (testobject.getOrigRecipe())
#print (cETest1.getValue() + cETest1.getUnit())
#print (cETest1.getUnit())
#print (cETest2.getValue())
#print (cETest2.getUnit())
#print (cETest3.getValue())
#print (cETest3.getUnit())

#testobject.setParsedRecipe("Use <0> of leather and <1> of string")
#cETest1.convertElement("Metric",1)
#print(testobject.getParsedRecipe())
#print (cETest1.getValue()+cETest1.getUnit())
#print (cETest1.getUnit())

#firstCE=ConvertibleElement(3, "feet")
#testobject.setCElistElement(firstCE)

#secondCE=ConvertibleElement(4, "meters")
#testobject.setCElistElement(secondCE)


#testobject.setConvertCheck(True)
#testobject.finalizeRecipe()


#print(testobject.getFinalRecipe())

'''

print (str(cETest1.getValue()) + cETest1.getUnit())
cETest1.convertElement("Metric",2)
print (str(cETest1.getValue())+cETest1.getUnit())

print (str(cETest2.getValue()) + cETest2.getUnit())
cETest2.convertElement("Metric",1)
print (str(cETest2.getValue())+cETest2.getUnit())

print (str(cETest3.getValue()) + cETest3.getUnit())
cETest3.convertElement("Metric",1)
print (str(cETest3.getValue())+cETest3.getUnit())

print (str(cETest4.getValue()) + cETest4.getUnit())
cETest4.convertElement("Metric", 1)
print (str(cETest4.getValue()) + cETest4.getUnit())

print (str(cETest5.getValue()) + cETest5.getUnit())
cETest5.convertElement("Metric", 1)
print (str(cETest5.getValue()) + cETest5.getUnit())

print (str(cETest6.getValue()) + cETest6.getUnit())
cETest6.convertElement("Metric", 1)
print (str(cETest6.getValue()) + cETest6.getUnit())

print (str(cETest7.getValue()) + cETest7.getUnit())
cETest7.convertElement("Metric", 1)
print (str(cETest7.getValue()) + cETest7.getUnit())

print (str(cETest8.getValue()) + cETest8.getUnit())
cETest8.convertElement("Metric", 1)
print (str(cETest8.getValue()) + cETest8.getUnit())

print (str(cETest9.getValue()) + cETest9.getUnit())
cETest9.convertElement("Metric", 1)
print (str(cETest9.getValue()) + cETest9.getUnit())

print (str(cETest10.getValue()) + cETest10.getUnit())
cETest10.convertElement("Metric", 1)
print (str(cETest10.getValue()) + cETest10.getUnit())

print (str(cETest11.getValue()) + cETest11.getUnit())
cETest11.convertElement("Metric", 1)
print (str(cETest11.getValue()) + cETest11.getUnit())

print (str(cETest12.getValue()) + cETest12.getUnit())
cETest12.convertElement("Metric", 1)
print (str(cETest12.getValue()) + cETest12.getUnit())

print (str(cETest13.getValue()) + cETest13.getUnit())
cETest13.convertElement("Metric", 1)
print (str(cETest13.getValue()) + cETest13.getUnit())

print (str(cETest14.getValue()) + cETest14.getUnit())
cETest14.convertElement("Metric", 1)
print (str(cETest14.getValue()) + cETest14.getUnit())

print (str(cETest15.getValue()) + cETest15.getUnit())
cETest15.convertElement("Metric", 1)
print (str(cETest15.getValue()) + cETest15.getUnit())

print (str(cETest16.getValue()) + cETest16.getUnit())
cETest16.convertElement("Metric", 1)
print (str(cETest16.getValue()) + cETest16.getUnit())

print (str(cETest17.getValue()) + cETest17.getUnit())
cETest17.convertElement("Metric", 1)
print (str(cETest17.getValue()) + cETest17.getUnit())

print (str(cETest18.getValue()) + cETest18.getUnit())
cETest18.convertElement("Metric", 1)
print (str(cETest18.getValue()) + cETest18.getUnit())

print (str(cETest19.getValue()) + cETest19.getUnit())
cETest19.convertElement("Metric", 1)
print (str(cETest19.getValue()) + cETest19.getUnit())

print (str(cETest20.getValue()) + cETest20.getUnit())
cETest20.convertElement("Metric", 1)
print (str(cETest20.getValue()) + cETest20.getUnit())

print (str(cETest21.getValue()) + cETest21.getUnit())
cETest21.convertElement("Metric", 1)
print (str(cETest21.getValue()) + cETest21.getUnit())

print (str(cETest22.getValue()) + cETest22.getUnit())
cETest22.convertElement("Imperial", 1)
print (str(cETest22.getValue()) + cETest22.getUnit())

print (str(cETest23.getValue()) + cETest23.getUnit())
cETest23.convertElement("Imperial", 1)
print (str(cETest23.getValue()) + cETest23.getUnit())

print (str(cETest24.getValue()) + cETest24.getUnit())
cETest24.convertElement("Imperial", 1)
print (str(cETest24.getValue()) + cETest24.getUnit())

print (str(cETest25.getValue()) + cETest25.getUnit())
cETest25.convertElement("Imperial", 1)
print (str(cETest25.getValue()) + cETest25.getUnit())

print (str(cETest26.getValue()) + cETest26.getUnit())
cETest26.convertElement("Imperial", 1)
print (str(cETest26.getValue()) + cETest26.getUnit())

print (str(cETest27.getValue()) + cETest27.getUnit())
cETest27.convertElement("Imperial", 1)
print (str(cETest27.getValue()) + cETest27.getUnit())

print (str(cETest28.getValue()) + cETest28.getUnit())
cETest28.convertElement("Imperial", 1)
print (str(cETest28.getValue()) + cETest28.getUnit())

print (str(cETest29.getValue()) + cETest29.getUnit())
cETest29.convertElement("Imperial", 1)
print (str(cETest29.getValue()) + cETest29.getUnit())

print (str(cETest30.getValue()) + cETest30.getUnit())
cETest30.convertElement("imperial", 1)
print (str(cETest30.getValue()) + cETest30.getUnit())

print (str(cETest31.getValue()) + cETest31.getUnit())
cETest31.convertElement("Imperial", 1)
print (str(cETest31.getValue()) + cETest31.getUnit())

print (str(cETest32.getValue()) + cETest32.getUnit())
cETest32.convertElement("Imperial", 1)
print (str(cETest32.getValue()) + cETest32.getUnit())

print (str(cETest33.getValue()) + cETest33.getUnit())
cETest33.convertElement("Imperial", 1)
print (str(cETest33.getValue()) + cETest33.getUnit())

print (str(cETest34.getValue()) + cETest34.getUnit())
cETest34.convertElement("Imperial", 1)
print (str(cETest34.getValue()) + cETest34.getUnit())

print (str(cETest35.getValue()) + cETest35.getUnit())
cETest35.convertElement("Imperial", 1)
print (str(cETest35.getValue()) + cETest35.getUnit())

print (str(cETest36.getValue()) + cETest36.getUnit())
cETest36.convertElement("Imperial", 1)
print (str(cETest36.getValue()) + cETest36.getUnit())

print (str(cETest37.getValue()) + cETest37.getUnit())
cETest37.convertElement("Imperial", 1)
print (str(cETest37.getValue()) + cETest37.getUnit())

print (str(cETest38.getValue()) + cETest38.getUnit())
cETest38.convertElement("Imperial", 1)
print (str(cETest38.getValue()) + cETest38.getUnit())

print (str(cETest39.getValue()) + cETest39.getUnit())
cETest39.convertElement("Metric", 1)
print (str(cETest39.getValue()) + cETest39.getUnit())

print (str(cETest40.getValue()) + cETest40.getUnit())
cETest40.convertElement("Metric", 1)
print (str(cETest40.getValue()) + cETest40.getUnit())

print (str(cETest41.getValue()) + cETest41.getUnit())
cETest41.convertElement("Imperial", 1)
print (str(cETest41.getValue()) + cETest41.getUnit())
'''

print (str(cETest003.getValue()) + cETest003.getUnit())
cETest003.convertElement("Imperial", 1)
print (str(cETest003.getValue()) + cETest003.getUnit())
