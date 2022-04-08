# badsql
This is a file-based version of SQL.



Pass the headers as the parameter to `db()`

```python
mydb = db(['id', 'name', 'age'])
```

Use `.insert(pos, row)` to add to the table

```python
mydb.insert(1, [0, 'Bob', 11])
mydb.insert(2, [1, 'Sam', 9])
mydb.insert(3, [2, 'Will', 10])
```

Use `.display()` to show the table

```python
print('Full table:\n')
mydb.display()
print('\n')
```

Use `.select(query)` to select specific rows

```python
print('Where age >= 10:\n')
mydb.select('age >= 10').display()
print('\n')
```

Any Python-compilable code can be used

```python
print('Where len(name) != 4:\n')
mydb.select('len(name) != 4').display()
print('\n')
```

The `.select()` method returns a db object

To save the table use `.save(filename)`

```python
mydb.save('table')
```

To load in a table from a file use `load(filename)`

```python
db2 = load('table')
```

This returns a db object

```python
print('Loaded from table.csv:\n')
db2.display()
```

Note:

for `.save()` and `load()`, '.csv' is appended at the end of the filename

Other methods:

This removes the first instance of \[2, 'Will', 10]

```python
mydb.remove([2, 'Will', 10])
```

Similarly `mydb.remove_all([2, 'Will', 10])` removes all the instances of \[2, 'Will', 10]

This removes the row in position 1

```python
mydb.delete(1)
```

### Changes

#### 7th April 2022

v0.1 - Initial release

v0.2 - Bug fix in \__init__.py

v0.3 - Added README.md

v1.0.1 - Bug fix in setup.py

v1.1 - All bugs fixed, available for use with `pip install badsql`

#### 8th April 2022

v1.2 - Added `.remove()` and `.remove_all()` methods
