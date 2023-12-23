import Matrix as mx
import Gauss as gx

def split_last_column(m:mx.Matrix):
    if m.col == 1:
        return None
    
    I = mx.identity(m.col) - mx.identity(m.col - 1)

    return m - (m*I), m*I

def rg(m:mx.Matrix):
    rng = 0
    r = gx.reduce_left(m)
    for c in range(1, m.row + 1):
        if r.coefficents[(c, c)] == 1:
            rng += 1
    return rng

def resolve(m:mx.Matrix):
    m_omo, coeff = split_last_column(m)
    if rg(m_omo) != rg(m):
        return None
    
    return gx.reduce_left(m)

M = mx.Matrix(((1,2,3),(2,4,6)))


print(resolve(M))
#
#print(rg(M))
#
#print(gx.reduce_left(M))
#
#m = mx.Matrix(((1,9),(6,8),(7,5),(12,9)))
#
#
#print(gx.reduce_left(split_last_column(m)[0]))
#
#print(split_last_column(m)[0], split_last_column(m)[1])