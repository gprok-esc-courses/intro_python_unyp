import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    user='sample', 
    password='sample',
    database='python_products'
)

cursor = connection.cursor()

sel = -1

while sel != '0':

    print("1. View Products")
    print("2. Add Product")
    print("3. Change Product Name")
    print("4. Delete Product")
    print("0. EXIT")
    sel = input("Select > ")

    if sel == '1':
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall() 

        for row in rows: 
            print("Product", row[0], ":", row[1])
    elif sel == '2':
        pname = input("Product name: ")
        cursor.execute("INSERT INTO products (name) VALUES ('" + pname +"')")
        connection.commit()
    elif sel == '3':
        pid = input("Product ID: ")
        pname = input("Product name: ")
        query = "UPDATE products SET name=%s WHERE id=%s"
        values = (pname, pid)
        cursor.execute(query, values)
        connection.commit()
    elif sel == '4':
        pid = input("Product ID: ")
        cursor.execute("DELETE FROM products WHERE id=%s", (pid,))
        connection.commit()