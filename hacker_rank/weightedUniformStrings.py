from string import ascii_lowercase

def test_ascii_func():

    for c in ascii_lowercase:
        k = ord( c ) - 96
        print( "{0} - {1}".format( c, k ) )

def weightedUniformStrings( s: str, queries ):
    
    hs = set( s )
    arr = []

    for c in hs:
        qnt = s.count( c )
        v = ord( c ) - 96
        arr += list( range( v, v* (qnt + 1), v  ) )

    arr = set( arr )

    r = [ "No" ] * len( queries )
    
    for i in range( len( queries ) ):
        q = queries[ i ]
        if q in arr:
            r[i] = "Yes"
    
    return r

def weightedUniformStrings_1( s: str, queries ):

    d = { }

    for c in s:
        k = ord( c ) - 96
        if k in d:
            d[ k ] += 1
        else:
            d[ k ] = 1
    
    hs = set( ) 
    for k, v in d.items():
        for i in range( 1 , v + 1 ):
            hs.add( k * i )
    
    result = []
    for q in queries:
        v = queries[ i ]
        if q in hs:
            result.append( "Yes" )
        else:
            result.append( "No" )
    
    return result

def test():

    txt = "./output.txt"
    fptr = open(txt, 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

def test_1():

    s = "abccddde"
    q = [  1, 3, 12, 5, 9, 10 ]

    r = weightedUniformStrings( s, q )

    print( "result: {0}\n".format( r ) )

def find_wrong( ):

    f1 = open( "./output.txt", "r" )

    f2 = open( "./expected.txt", "r" )

    counter = 1 

    lines = [] 

    while True:
        counter += 1
        l1 = f1.readline()
        l2 = f2.readline() 

        if not l1 or not l2:
            print( "finishing at line {0} {1} {2}".format( counter, l1, l2 ) )
            break

        if l1 != l2:
            lines.append( counter )
    
    print(lines)




if __name__ == "__main__":
    test_1( )