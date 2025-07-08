whatsIn = input( "Enter string to slice: " )
sliceSrt = input( "Start of slice: " )
sliceEnd = input( "End of slice: " )

sliceSrt = int( sliceSrt )
sliceEnd = int( sliceEnd )

print( whatsIn[sliceSrt:sliceEnd] ) 
