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

if __name__ == '__main__':

    # Pass the headers as the parameter to db()
    mydb = db(['id', 'name', 'age'])
    
    # Use .insert(pos, row) to add to the table
    mydb.insert(1, [0, 'Bob', 11])
    mydb.insert(2, [1, 'Sam', 9])
    mydb.insert(3, [2, 'Will', 10])
    
    # Use .display() to show the table
    print('Full table:\n')
    mydb.display()
    print('\n')
    
    # Use .select(query) to select specific rows
    print('Where age >= 10:\n')
    mydb.select('age >= 10').display()
    print('\n')
    
    # Any Python-compilable code can be used
    print('Where len(name) != 4:\n')
    mydb.select('len(name) != 4').display()
    print('\n')
    
    # This returns a db object so you can use
    # methods like .display() on it
    
    # To save the table use .save(filename)
    mydb.save('table')
    
    # To load in a table from a file use load(filename)
    db2 = load('table')
    
    # This returns a db object
    print('Loaded from table.csv:\n')
    db2.display()
