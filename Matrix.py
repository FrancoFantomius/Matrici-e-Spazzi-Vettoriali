

class Matrix():
    def __init__(self, coefficents) -> None:
        '''
        Creates a new matrix, it supposes that the coefficents of the matrix is a tuple.
        To create a matrix with multiple lines,
        the coefficents must be put like:
        ((•), (•), ..., (•)) with every (•) is a line with all the coefficents
        '''
        self.coefficents = {}

        self.col = 0
        self.row = 0

        if type(coefficents[0]) == type(coefficents):
            for line in range(len(coefficents)):
                
                self.row = max(self.row, line + 1)

                for column in range(len(coefficents[line])):
                    
                    self.col = max(self.col, column + 1)
                    
                    self.coefficents[(line + 1, column + 1)] = coefficents[line][column]
        
            coords = tuple(self.coefficents.keys())
            for l in range(self.row):
                for c in range(self.col):
                    if not ((l + 1, c + 1) in coords):
                        self.coefficents[(l + 1, c + 1)] = 0
            

        else:
            self.row = 1
            self.col = len(coefficents)
            for element in range(len(coefficents)):
                self.coefficents[(1, element + 1)] = coefficents[element]

    def __str__(self) -> str:
        rows = {}
        for r in range(1, self.row + 1):
            column = {}
            for c in range(1, self.col + 1):
                column[(r, c)] = self.coefficents[(r,c)]
            
            rows[r] = tuple(column.values())
        
        return str(tuple(rows.values()))
    
    def __repr__(self) -> str:
        return "%sx%s"%(self.row, self.col)

    def __neg__(self):
        lines = {}
        for r in range(1, self.row + 1):
            columns = {}
            for c in range(1, self.col + 1):
                columns[(r, c)] = - self.coefficents[(r, c)]
            
            lines[r] = tuple(columns.values())
        
        return Matrix(tuple(lines.values()))

    def __eq__(self, value) -> bool:
        if self.coefficents == value.coefficents:
            return True
        return False

    def __ne__(self, other: object) -> bool:
        return not(self == other)
    
    def __len__(self) -> int:
        return self.row * self.col
    
    def __add__(self, other):
        max_row = max(self.row, other.row)
        max_col = max(self.col, other.col)
        
        s_coord = tuple(self.coefficents.keys())
        o_coord = tuple(other.coefficents.keys())

        lines = {}


        for l in range(1, max_row + 1):
            coeff = {}
            
            for c in range(1, max_col + 1):
                if (l, c) in s_coord and (l, c) in o_coord:
                    coeff[(l, c)] = self.coefficents[(l, c)] + other.coefficents[(l, c)]
                elif (l , c ) in s_coord and not ((l , c ) in o_coord):
                    coeff[(l , c )] = self.coefficents[(l, c)]
                elif not((l , c ) in s_coord) and (l, c) in o_coord:
                    coeff[(l , c )] = other.coefficents[(l , c )]
                else:
                    coeff[(l , c )] = 0

            lines[l] = tuple(coeff.values())

        return Matrix(tuple(lines.values()))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if type(other) != Matrix:
            i = identity(self.row)
            for r in range(1, self.row + 1):
                i.coefficents[(r,r)] = other
            return i * self

        if self.col != other.row:
            return None
        
        rows = {}

        for r in range(1, self.row + 1):
            cols = {}
            for o_c in range(1, other.col + 1):
                cols[(r, o_c)] = 0
                for c in range(1, self.col + 1):
                    cols[(r, o_c)] += self.coefficents[(r, c)]*other.coefficents[(c, o_c)]

            rows[r] = tuple(cols.values())
        
        return Matrix(tuple(rows.values()))

    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        if self.col != self.row:
            return None
        if other == 1:
            return self
        elif other < 1:
            return None
        return self * (self**(other - 1))

    def transpose(self):
        coefficents = {}

        for coords in tuple(self.coefficents.keys()):
            coefficents[coords[::-1]] = self.coefficents[coords]

        rows = {}
        for r in range(1, self.col + 1):
            column = {}
            for c in range(1, self.row + 1):
                column[(r, c)] = coefficents[(r,c)]
            
            rows[r] = tuple(column.values())
        
        return Matrix(tuple(rows.values()))

def identity(n:int):
    lines = {}
    for g in range(1, n + 1):
        column = {}
        for h in range(1, n + 1):
            if g == h:
                column[(g, h)] = 1
            else:
                column[(g, h)] = 0
        lines[g] = tuple(column.values())
    
    return Matrix(tuple(lines.values()))



#M = Matrix(((1,2,3,4),(7,6,4)))
#m = Matrix(((1,0),(6,8)))
#
#M -= m
#
#print(M)