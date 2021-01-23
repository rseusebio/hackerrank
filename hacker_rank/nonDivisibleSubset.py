from itertools import combinations 
from datetime import datetime
from random import randint

def get_key( e ):
    return len( e[ "v" ])

def get_key2( e: dict ) -> int:
    return len( e[ "k" ] )

def nonDivisibleSubset( k, S ):

    # at most k remains: 0 -- k-1 
    remains = [ 0 ] * k

    result =  0

    for n in S:
        remain = n % k 
        remains[ remain ] += 1
    
    # because you can only add one of them
    if remains[ 0 ] > 0:
        result += 1

    for i in range( 1, len( remains ) , 1 ):

        symmetric = k - i 

        if i == symmetric and remains[ i ] > 0:
            result += 1
        else:
            arr = [ remains[ i ] , remains[ symmetric ] ]
            arr.sort()
            result += arr.pop() 

            remains[ i ] = 0
            remains[ symmetric ] = 0

    return result


# try to work out this idea 
def nonDivisibleSubset_fast( k, S ):

    size = len( S )

    arr = []


    for i in range( size ):
       
        n = S[ i ]
        d = { "k": n, "v": [] }
        
        for j in range( size ):
            # we can improve this by looking back on pasts j 
            # relative to i 
            if j == i:
                continue                 
            
            n2 = S[ j ]

            if ( n2 + n ) % k != 0:
                continue 
            
            d[ "v" ].append( n2 )

        arr.append( d )

    arr.sort( reverse=False, key=get_key )
        
    nice = set()

    not_nice = set()

    for i in range( len( arr ) ):
        
        d = arr[ i ]

        if d["k"] not in not_nice:

            nice.add( d["k"] )

            not_nice = set( list( not_nice ) + d["v"] )

    return len( nice )

def next_smallest( arr, smallest ) -> int:

    holder = None 
    s = None 

    for i in range( len( arr ) ):
        
        d = arr[ i ]

        k = d["k"]
        v = d["v"]

        size = len( v )

        if size == smallest :
            if s == None:
                holder = i
                s = smallest  
        elif size < smallest:
            if size > s or s == None:
                holder = i
                s = size 
    
    return holder 
             
def nonDivisibleSubset_fast2( k, S ):

    size = len( S )
    arr = []

    for i in range( size ):
       
        n = S[ i ]
        d = { "k": n, "v": [] }
        
        for j in range( size ):
            # we can improve this by looking back on pasts j 
            # relative to i 
            if j == i:
                continue                 
            
            n2 = S[ j ]

            if ( n2 + n ) % k != 0:
                continue 
            
            d[ "v" ].append( n2 )

        arr.append( d )
        
    nice = set()

    not_nice = set()

    smallest = 0 

    while len( arr ) > 0:

        index = next_smallest( arr, smallest )

        if index == None:
            smallest += 1
            continue  
        
        d = arr.pop( index )

        if d["k"] not in not_nice:

            nice.add( d["k"] )

            not_nice = set( list( not_nice ) + list( d[ "v" ] ) )
    
    return len( nice )

def isSubsetOk( sub, k ):

    size = len( sub )

    for i in range( size ):
       
        v = sub[ i ]

        for j in range( size ):

            if j == i:
                continue

            n = sub[ j ]

            s = v + sub[ j ]

            if  s % k == 0: 
                return False, n, v 

    return True, None, None

def has_invalid_combinations( invalid_combs, sub ):

    for a, b in invalid_combs:

        if a in sub and b in sub:

            return True 

    return False

def nonDivisibleSubset_slow( k, S ):

    size = len( S )

    invalid_combs = set( )

    for i in range( size, 1, -1 ):

        for c in combinations( S, i ):

            if has_invalid_combinations( invalid_combs, c ):
                continue 

            res, a, b = isSubsetOk( c, k )

            if res:
                return i
            
            _arr = [ a, b ]

            _arr.sort( )

            invalid_comb = tuple( _arr )

            invalid_combs.add( invalid_comb )

    for i in S:
        if i % k == 0:
            return 1 

    return 0

def test( S, k) :

    d = datetime.now() 
    res = nonDivisibleSubset( k, S )
    delta = datetime.now() - d 
    print( "fast:: res: {0} , time: {1}".format( res, delta.total_seconds( ) ) )

    d = datetime.now()
    res = nonDivisibleSubset_fast( k, S )
    delta = datetime.now() - d 
    print( "slow:: res: {0} , time: {1}".format( res, delta.total_seconds( ) ) )


def random_list_of_ints( N ):

    arr = set( )

    for i in range( N ):

        arr.add( randint(1, 10**4) )
    
    return list( arr )

if __name__ == "__main__":

    S = list( map( int, "1 7 4 2 10 20 55 42 43 16 17 19 22".split(" ") ) )
    k = 4

    test( S, k )

    # print( "===============")

    # S = list( map( int, "19 10 12 24 25 22 278 576 496 727 410 124 338 149 209 702 282 718 771 575 436".split(" ") ) )

    # k = 7

    # test( S, k )

    # print( "===============")

    # S = random_list_of_ints( 50)

    # k = 7

    # test( S, k )

    # print( "===============")

    # S = random_list_of_ints( 10 ** 5 )
    # k = 4
    # test( S, k )

    print( "===============")
    S = list( map( int, "1 7 4 2".split(" ") ) )
    k = 3
    test( S, k )



