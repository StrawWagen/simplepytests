def printWelcome():
    """This function welcomes you!"""
    print( "Welcome!" )
    print( "This function does nothing!")
    print( "You're welcome!" )

printWelcome()

def changeValue( value ):
    value = value * 132
    return value

number = 5
number = changeValue( number )
print( "Outside:", number )