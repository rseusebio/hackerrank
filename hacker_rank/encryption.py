from math import sqrt, floor, ceil

def increment_columns( s: str, columns ):

    for i in range( len( s ) ):

        columns[ i ] += s[ i ]

def encryption( s: str ):

    s = s.replace( " ", "" )

    L = len( s )

    c = ceil( sqrt( L ) )

    r = floor( sqrt( L ) )

    s_pointer = 0
    
    e_pointer = c

    columns = [ "" ] * c

    while True:

        if e_pointer >= L:

            epointer = L 

            sub_s = s[ s_pointer : e_pointer ] 

            increment_columns( sub_s , columns )

            break
        else:
            
            sub_s = s[ s_pointer : e_pointer ] 

            increment_columns( sub_s , columns )

            s_pointer = e_pointer

            e_pointer += c

    return " ".join( columns )
    
if __name__ == "__main__":

    s = "haveaniceday"
    print( encryption( s ) )
