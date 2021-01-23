from datetime import datetime 
from random import randint 

def random_int_list( N: int = 50, min: int = 1, max: int= 100, reverse: int = False ):
    
    arr = []

    for i in range( N ):
        
        arr.append( randint( min, max ) )
    
    arr.sort( reverse=reverse )

    return arr

def clean_repetitions( arr ):

    #using hash set makes it faster to search
    hash_set = set() 

    new_arr = []
    
    for e in arr:
        
        if e in hash_set:
            continue 

        new_arr.append( e )
        hash_set.add( e )

    return new_arr 

def climbingLeaderboard( ranked, player ):

    ranked = clean_repetitions( ranked )

    rank_pointer = len( ranked ) - 1

    player_pointer = 0

    results = [ 1 ] * len( player )

    while True:

        if player_pointer >= len( player ):
            break
        
        if rank_pointer < 0:
            break

        r = ranked[ rank_pointer ]
        p = player[ player_pointer ]
        
        if p < r:
            results[ player_pointer ] = ( rank_pointer + 1 ) + 1
            player_pointer += 1
            continue 
        
        elif p == r:
            results[ player_pointer ] = ( rank_pointer ) + 1
            player_pointer += 1
            continue 
        
        else:
            rank_pointer -= 1

    return results
            
def test_1( ):

    ranked = [ 100, 90, 90, 80 ]

    player = [ 70, 80, 105 ]

    res = climbingLeaderboard( ranked, player )

    print( "res: {0}".format( res ) )

def test_2( ):

    ranked = random_int_list( N = 5, reverse = True )

    player = random_int_list( N = 3 )

    print( "ranked: {0}".format( ranked ) )

    print( "player: {0}".format( player ) )

    res = climbingLeaderboard( ranked, player )

    print( "res: {0}".format( res ) )

    
if __name__ == "__main__":
    test_1()
    test_2( )

