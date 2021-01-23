def round_grade( grade ):

    if grade < 38:
        return grade
    
    m = grade % 5 
    
    next_multiple = grade + 5 - m

    if next_multiple - grade < 3:
        return next_multiple
    else:
        return grade
    
def gradingStudents( grades ):

    output = []

    for i in range( len( grades ) ):
        output.append( round_grade( grades[ i ] ) )
        
    return output 


if __name__ == "__main__":

    grades = [ 73, 67, 38, 33 ]

    output = gradingStudents( grades )

    for i in output:
        print( i )