class db:
    
    def __init__(self, headers):
        if not isinstance(headers, list):
            raise (
                ValueError('headers argument must be a list, not ' + str(type(headers)))
            )
        self.table = [headers]
        
    def insert(self, pos, row):
        
        if not isinstance(row, list):
            raise (
                ValueError('row argument must be a list, not ' + str(type(row)))
            )
            
        if len(row) != len(self.table[0]):
            raise (
                ValueError('wrong length of row: expecting ' + \
                           str(len(self.table[0])) + ', got ' + str(len(row)))
            )
            
        if not isinstance(pos, int):
            raise (
                ValueError('pos argument must be an integer, not ' + str(type(pos)))
            )

        if pos <= 0 or pos > len(self.table):
            raise (
                ValueError('pos out of range: expecting 1 to ' + str(len(self.table[0])))
            )

        self.table.insert(pos, row)

    def delete(self, ind):
        
        if not isinstance(ind, int):
            raise (
                ValueError('ind argument must be an integer, not ' + str(type(ind)))
            )
            
        if ind <= 0 or ind >= len(self.table):
            raise (
                ValueError('ind out of range: expecting 1 to ' + str(len(self.table)))
            )

        self.table.pop(ind)

    def remove(self, row):

        if not isinstance(row, list):
            raise (
                ValueError('row argument must be an list, not ' + str(type(row)))
            )

        if row not in self.table:
            raise (
                ValueError('row not in table, cannot remove')
            )

        self.table.remove(row)

    def remove_all(self, row):

        if not isinstance(row, list):
            raise (
                ValueError('row argument must be an list, not ' + str(type(row)))
            )

        while row in self.table:
            self.table.remove(row)

    def display(self):

        row_size = len(self.table[0])
        col_size = len(self.table)
        max_lens = [0 for x in range(row_size)]
        
        for i in range(col_size):
            for j in range(row_size):
                if len(str(self.table[i][j])) > max_lens[j]: 
                    max_lens[j] = len(str(self.table[i][j]))

        for y in range(col_size):
            print(end='| ')
            for z in range(row_size):
                item = str(self.table[y][z])
                print(item, (max_lens[z] - len(item)) * ' ', end='| ')
            print('')
            if y == 0:
                print(end='| ')
                for a in max_lens:
                    print(a * '-', end = ' | ')
                print('')

    def select(self, query):

        if not isinstance(query, str):
            raise (
                ValueError('query argument must be a string, not ' + str(type(query)))
            )
        
        headers = self.table[0]
        ret = db(headers)
        
        for row in range(1, len(self.table)):
            vars = {}
            for x in range(len(headers)):
                vars[headers[x]] = self.table[row][x]
            try:
                if eval(query, vars):
                    ret.insert(len(ret.table), self.table[row])
            except:
                raise (
                    ValueError('query could not be understood')
                )

        return ret

    def save(self, filename):

        if not isinstance(filename, str):
            raise (
                ValueError('filename argument must be a string, not ' + str(type(filename)))
            )

        if filename == '':
            raise (
                ValueError('filename argument was empty')
            )

        f = open(filename + '.csv', 'w')
        for row in self.table:
            new_row = [repr(x) for x in row]
            f.write(', '.join(new_row) + '\n')
        f.close()

def load(filename):

    if not isinstance(filename, str):
        raise (
            ValueError('filename argument must be a string, not ' + str(type(filename)))
        )

    try:
        f = open(filename + '.csv', 'r')
    except:
        raise (
            ValueError('file \'' + filename + '.csv\' not found')
        )

    text = f.read().split('\n')
    f.close()

    lst = []
    
    for line in text:
        if line != '':
            lst.append([])
            x = line.split(', ')
            for y in x:
                lst[-1].append(eval(y))

    mydb = db(lst[0])
    for i in range(1, len(lst)):
        mydb.insert(len(mydb.table), lst[i])

    return mydb
