def square( num ):
    return num * num

def askAndSquare():
    print( "Squares stuff in a range!" )
    rStart = int( input( "Enter range start:" ) ) 
    rEnd = int( input( "Enter range end:" ) )

    for i in range( rStart, rEnd ):
        print( square( i ) )

askAndSquare()