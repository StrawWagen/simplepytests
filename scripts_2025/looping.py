# looping test

import string

number = 1
answer = "y"
while answer == "y":
    print( number )
    answer = input( "Do you want the next number ( Y/N )").lower()
    number = number + 1

print( "goodbye!" )
