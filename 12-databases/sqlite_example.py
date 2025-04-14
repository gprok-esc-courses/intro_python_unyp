import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)") 

print("1. View Products")
print("2. Add Product")
sel = input("Select > ")

if sel == '1':
    result = cursor.execute("SELECT * FROM products")
    rows = result.fetchall() 

    for row in rows: 
        print("Product Name:", row[1])
elif sel == '2':
    pname = input("Product name: ")
    cursor.execute("INSERT INTO products (name) VALUES ('" + pname +"')")
    connection.commit()