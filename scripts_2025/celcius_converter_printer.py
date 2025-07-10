
#doesn't work with 61st, etc
#but this is a silly test
def prettyTextAfterNum( num ):
    text = ""
    numAbs = abs( num )
    if numAbs >= 4: 
        text = "th"
    
    elif numAbs >= 3:
        text = "rd"

    elif numAbs >= 2:
        text = "nd"

    elif numAbs >= 1:
        text = "st"

    return text
        

def celciusToFarenheit( celcius ):
    return 9.0/5.0 * celcius + 32 #love magic numbers


def printConversionTable( rangeStart = 0, rangeEnd = 100, stepSize = 10 ):
    print( "Printing temperature conversion table from " + str( rangeStart ) + "*C to " + str( rangeEnd ) + "*F" )

    if stepSize != 1: #this print doesn't make sense with stepsize 1
        print( "Only converting every " + str( stepSize ) + prettyTextAfterNum( stepSize ) + " degree" )

    #actually print the table
    for celcius in range( rangeStart, rangeEnd + 1, stepSize ):
        asFarenheit = celciusToFarenheit( celcius )

        print( str( celcius ) + "*C\t| " + str( round( asFarenheit ) ) + "*F" )

    print( "All Done!")

printConversionTable( stepSize = 1 )