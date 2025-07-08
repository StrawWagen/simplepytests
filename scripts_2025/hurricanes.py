#find category from user inputted windspeed
category = 0

print( "Saffir-Simpson Scale calculator" )
windIn = input( "Please enter windspeed: " )
wind = int( windIn )


if wind >= 156:
    category = 5

elif wind >= 131:
    category = 4

elif wind >= 111:
    category = 3

elif wind > 96:
    category = 2

elif wind > 74:
    category = 1

print( "The windspeed indicates a hurricane of category:", category )
