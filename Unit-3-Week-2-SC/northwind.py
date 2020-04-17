import sqlite3


# Using `sqlite3`, connect to the given `northwind_small.sqlite3` database.

DB_FILEPATH= 'northwind_small.sqlite3'
connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

#What are the ten most expensive items (per unit price) in the database?
query1 = '''
    SELECT
        DISTINCT ProductId
    FROM OrderDetail
    ORDER BY UnitPrice DESC
    LIMIT 10;
    '''

cursor.execute(query1)
first_result = cursor.fetchall()
print('Top 10 expensive items:', first_result)

#What is the average age of an employee at the time of their hiring?
query2= '''
    SELECT
	avg(age) as AverageAge
FROM (
	SELECT 
		HireDate - BirthDate as age
	FROM Employee
	);
    '''

result2 = cursor.execute(query2).fetchall()
print('Average Age of employee at tiem of hire:', result2)

# What are the ten most expensive items (per unit price) in the database *and*
# their suppliers?
query3='''
    SELECT
        DISTINCT ProductId,
                SupplierId
    FROM OrderDetail
    JOIN Product ON OrderDetail.ProductId = Product.Id
    ORDER BY OrderDetail.UnitPrice DESC
    LIMIT 10;
    '''
result3= cursor.execute(query3).fetchall()
print('Top 10 most expensive items and their suppliers:', result3)

# What is the largest category (by number of unique products in it)?

query4='''
    SELECT
	count(Product.Id),
	CategoryName
    FROM Category
    JOIN Product ON Category.Id = Product.CategoryId
    GROUP BY Category.Id
    ORDER BY count(Product.Id) DESC 
    LIMIT 1;
    '''
result4 = cursor.execute(query4).fetchall()
print('Largest category:', result4)

#Check challenge.md for answers to part 4 