# Converter
# 
# Description
# The Converter takes in data that has already been parsed into a quantity and a unit.
# The quantity's units are compared with a list of English and Metric measurements to determine which conversion ratio is necessary to use.
# The quantity is then modified according to the conversion ratio (multiplication, division, etc.).
# The Converter returns the correct conversion of the quantity and the applicable unit.
# The Converter may also multiply the quantities by the serving size given by the user.
# 
# List of convertible units: Units intended to be converted
# weight: pounds, ounces, grams, kilograms
# liquid: Tablespoons, teaspoons, fluid ounces, cups, pints, quarts, gallons, milliliters, liters
# temperature: Fahrenheit, Celsius
# length: inches, centimeters
# 
# Pseudocode
# 03/25/14
# while input is parsed
# if there is a unit to convert AND a unit to be converted to (Can this conversion be made?)
# 		do the necessary conversion
# 		modify based on serving size
# 		return correct quantity and unit
# 	else if
# repeat as above for other units of measure (It might not be the first item I list, but it   might be further down the list.)
# 	else error message
# 	end if
# end while
# 
# 03/27/14
# precondition: array of un-converted convertible elements
# if converter recognizes tagged convertible units
# 	if converter recognizes current unit and future unit
# 		-- (a list of conversions between Imperial and Metric units, and vice versa)
# 		do the necessary conversion (mostly multiplication or division)
# 		return correct quantity and unit
# else cannot convert
# end if
# else cannot convert
# end if
