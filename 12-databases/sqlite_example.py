import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)") 

sel = -1

while sel != '0':

    print("1. View Products")
    print("2. Add Product")
    print("3. Change Product Name")
    print("4. Delete Product")
    print("0. EXIT")
    sel = input("Select > ")

    if sel == '1':
        result = cursor.execute("SELECT * FROM products")
        rows = result.fetchall() 

        for row in rows: 
            print("Product", row[0], ":", row[1])
    elif sel == '2':
        pname = input("Product name: ")
        cursor.execute("INSERT INTO products (name) VALUES ('" + pname +"')")
        connection.commit()
    elif sel == '3':
        pid = input("Product ID: ")
        pname = input("Product name: ")
        cursor.execute("UPDATE products SET name=? WHERE id=?", (pname, pid))
        connection.commit()
    elif sel == '4':
        pid = input("Product ID: ")
        cursor.execute("DELETE FROM products WHERE id=?", (pid,))
        connection.commit()