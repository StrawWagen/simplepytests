"""

breaker = "~" * 4

for i in range( 1, 20 ):
    print( breaker, i, breaker )

    for j in range( 1, 20 ):
        print( i*j, " ", end = "" )

print( "alldone!" )

"""

import math

contextWindow = 3

print( "Letter finder!" )
haystack = input( "Enter a haystack: " )
needle = input( "Enter what to find: " )
length = len( haystack )

print( "Searching for... " + needle )

for i in range( 1, length ):
    curr = haystack[i]
    if curr == needle:
        print( "Found \"" + needle + "\" at index; " + str( i ) )
        
        contextMin = i + -contextWindow
        contextMin = max( 0, contextMin )
        contextMax = i + contextWindow
        contextMax = min( contextMax, length )
        window = haystack[ contextMin:contextMax ]
        window = str.replace( window, needle, f'"{needle}"' )

        print( "Context " + window )
        break 
    
else:
    print( "Could not find " + needle )