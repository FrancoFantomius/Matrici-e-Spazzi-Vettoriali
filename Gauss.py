from Matrix import Matrix, identity

def rows_first_op(m:Matrix, row_1:int, row_2:int):
    '''Changes the position of the two rows specified'''
    if row_1 in range(m.row + 1) and row_2 in range(m.row + 1):
        
        i = identity(m.row)

        i.coefficents[(row_1, row_1)] = 0
        i.coefficents[(row_2, row_2)] = 0
        i.coefficents[(row_1, row_2)] = 1
        i.coefficents[(row_2, row_1)] = 1
       
        return i * m

def rows_second_op(m:Matrix, row_1:int, row_2:int, alpha = 1):
    '''Adds a row to another one, the second row is multiplied by a constant'''
    if not(row_1 in range(m.row + 1) and row_2 in range(m.row + 1)):
        return None

    i = identity(m.row)

    i.coefficents[(row_1, row_2)] = alpha

    return i * m

def rows_third_op(m:Matrix, row:int, alpha):
    '''Multiplies the selected row for a non-zero constant'''
    if (not row in range(m.row + 1)) or alpha == 0:
        return None
    
    i = identity(m.row)
    i.coefficents[(row, row)] = alpha

    return i * m

def columns_first_op(m:Matrix, col_1:int, col_2:int):
    '''Changes the position of the two columns specified'''
    if col_1 in range(m.col + 1) and col_2 in range(m.col + 1):
        
        i = identity(m.col)

        i.coefficents[(col_1, col_1)] = 0
        i.coefficents[(col_2, col_2)] = 0
        i.coefficents[(col_1, col_2)] = 1
        i.coefficents[(col_2, col_1)] = 1
       
        return m * i

def columns_second_op(m:Matrix, col_1:int, col_2:int, alpha = 1):
    '''Adds a col to another one, the second col is multiplied by a constant'''
    if not(col_1 in range(m.col + 1) and col_2 in range(m.col + 1)):
        return None

    i = identity(m.col)

    i.coefficents[(col_2, col_1)] = alpha

    return m * i

def columns_third_op(m:Matrix, col:int, alpha):
    '''Multiplies the selected col for a non-zero constant'''
    if (not col in range(m.col + 1)) or alpha == 0:
        return None
    
    i = identity(m.col)
    i.coefficents[(col, col)] = alpha

    return m * i

def pivot(m:Matrix, start:int, column:int):
    for line in range(start, m.row + 1):
        if m.coefficents[(line, column)] != 0:
            return (line, column)
    return (start, column)

def reduce_left(m:Matrix):
    f = m
    c = 1

    while c <= m.row and c <= m.col:
        piv = pivot(m, c, c)
        f = rows_first_op(f, c, piv[0])

        if f.coefficents[(c, c)] != 0 and f.coefficents[(c, c)] != 1:
            f = rows_third_op(f, c, 1/f.coefficents[(c, c)])
        
        for rows_up in range(1, c):
            if f.coefficents[(rows_up, c)] != 0:
                f = rows_second_op(f, rows_up, c, - f.coefficents[(rows_up, c)])
        
        for rows_down in range(c + 1, m.row + 1):
            if f.coefficents[(rows_down, c)] != 0:
                f = rows_second_op(f, rows_down, c, - f.coefficents[(rows_down, c)])
        
        c += 1
        
    return f

def det_reduce(m:Matrix):
    f = m
    c = 1

    while c <= m.row and c <= m.col:
        piv = pivot(m, c, c)
        f = rows_first_op(f, c, piv[0])

        if f.coefficents[(c, c)] != 0 and f.coefficents[(c, c)] != 1:
            f = rows_third_op(f, c, 1/f.coefficents[(c, c)])
        
        for rows_up in range(1, c):
            if f.coefficents[(rows_up, c)] != 0:
                f = rows_second_op(f, rows_up, c, - f.coefficents[(rows_up, c)])
        
        for rows_down in range(c + 1, m.row + 1):
            if f.coefficents[(rows_down, c)] != 0:
                f = rows_second_op(f, rows_down, c, - f.coefficents[(rows_down, c)])
        
        c += 1
        
    return f


#a = Matrix(((1,2,3,4),(5, 6, 7, 8)))
#b = a.transpose()
#print(rows_first_op(a, 1, 1))
#print(columns_second_op(a,1,2,-1))
#print(columns_third_op(a,1,2))
#
#c = reduce_left(b)
#
#print(reduce_left(a))
#
#print(c.transpose())