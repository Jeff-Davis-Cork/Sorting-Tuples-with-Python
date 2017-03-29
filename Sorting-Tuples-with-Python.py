def Print(data):
    # Output the list ‘data’ of (name,age) tuples in the
    # form of a headed table, allowing 7 spaces for each
    # name and 3 spaces for each age, with 1 extra space
    # between them.
    print('%-7s %3s' % ('Name','Age'))
    print('------- ---')
    for name, age in data:
        print('%-7s %3s' % (name,age))

def InsertionSort( data, field ) :
    # Sorts the list ‘data’ of (name,age) tuples into
    # ascending order of field ‘field’, which is either
    # the string “name” or “age”, using the Insertion
    # Sort algorithm
    if field=='name':
        index=0
    else:
        index=1
    for i in range(len(data)):
        b = data[i]             # this is the pointer / field
        j = i                     # this is the tuple being looked at
        while j > 0 and b[index] < data[j-1][index]:
            data[j]=data[j-1]         # this moves the tuple left one position
            j-=1                # this moves to the next tuple position
        data[j]=b                # sets the new position of tuple
    # print('data is:',data)
    for i in range(len(data)):
        if data[i][index]==data[i-1][index]:
            if index==0:
                index=1
            else:
                index=0
            b = data[i]             # this is the pointer / field
            j = i                     # this is the tuple being looked at
            while j > 0 and b[index] < data[j-1][index]:
                data[j]=data[j-1]         # this moves the tuple left one position
                j-=1                # this moves to the next tuple position
            data[j]=b                # sets the new position of tuple
    Print(data)

def SelectionSort( data, field ) :
    # Sorts the list ‘data’ of (name,age) tuples into
    # ascending order of field ‘field’, which is either
    # the string “name” or “age”, using the Selection
    # Sort algorithm
    for i in range( len( lst ) ) : # put its ’i’th smallest item into position ’i’ of ’lst’ # set ’imin’ to the position of the smallest item from lst[ i ] onwards imin = i
        for j in range( i + 1, len( lst ) ) :
            if lst[ j ] < lst[ imin ] :
                imin = j           # swap the values in positions ’i’ and ’imin’ of ’lst’
        ( lst[ i ], lst[ imin ] ) = ( lst[ imin ], lst[ i ] )


            
                        
data=[ ('Ann',23),('Tim',18),('Bob',37),('Ned',51),('Sue',18) ]
data2=[ ('Ann',33),('Ann',23),('Tim',18),('Bob',37),('Ned',51),('Sue',18) ]

 
