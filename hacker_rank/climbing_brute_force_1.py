from datetime import datetime 

def remove_rep( arr ):

    new_arr = [] 

    for e in arr:

        if e in new_arr:
             continue 

        new_arr.append( e )
    
    return new_arr

def climbingLeaderboard( ranked, player ):

    ranked = remove_rep( ranked )

    result = [ None ] * len( player ) 

    for i in range( len( player ) ):

        p = player[ i ]

        for j in range( len( ranked ) ):
            
            r = ranked[ j ]

            if p > r: 

                    ranked = ranked[ 0 : j ] + [ p ] + ranked[ j : len( ranked ) ]

                    result[ i ] = j + 1
                    
                    break

            elif p == r:

                result[ i ] = j + 1

                break 

        if result[ i ] == None:
            
            result[ i ] = len( ranked ) + 1

            ranked.append( p )

    return result

def test_1():

    ranked = [ 100, 90, 90, 80, 75, 60 ]

    player = [ 50, 65, 77, 90, 102 ]

    d = datetime.now() 
    result = climbingLeaderboard( ranked, player )
    delta = datetime.now() - d 

    print( "result: {0}, time: {1}".format( result, delta.total_seconds() ) )

def test_2():

    ranked = [ 100, 100, 50, 40, 40, 20, 10 ]

    player = [ 5, 25, 50, 120 ]

    d = datetime.now() 
    result = climbingLeaderboard( ranked, player )
    delta = datetime.now() - d 

    print( "result: {0}, time: {1}".format( result, delta.total_seconds() ) )

def test_3():

    ranked = [ 100, 90, 90, 80 ]

    player = [ 70, 80, 105 ]

    d = datetime.now() 
    result = climbingLeaderboard( ranked, player )
    delta = datetime.now() - d 

    print( "result: {0}, time: {1}".format( result, delta.total_seconds() ) )
    
if __name__ == "__main__":
    test_3()

