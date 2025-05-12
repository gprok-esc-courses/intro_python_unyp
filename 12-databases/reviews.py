# The purpose of this program is to keep track of 
# movies, books, events, etc, a user is attending/reading
# along with a grade 1-5

import sqlite3 

db = sqlite3.connect('reviews.db')
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS review (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, title TEXT, eval INTEGER)") 

while True:
    print("1. Add")
    print("2. Categories")
    print("3. View All")
    print("0. EXIT")
    choice = int(input("Choose: "))

    if choice == 1:
        category = input("Category: ")
        title = input("Title: ")
        eval = int(input("Evaluation (1-5): "))
        cursor.execute("INSERT INTO review (category, title, eval) VALUES (?, ?, ?)", (category, title, eval))
        db.commit()
    elif choice == 2:
        result = cursor.execute("SELECT DISTINCT category FROM review")
        rows = result.fetchall()
        counter = 1
        category_list = ['none']
        for row in rows:
            print(counter, row[0])
            category_list.append(row[0])
            counter += 1
        print("O BACK")
        option = int(input("Select: "))
        if option != 0:
            result = cursor.execute("SELECT * FROM review WHERE category=?", (category_list[option],))
            rows = result.fetchall()
            print(rows)
    elif choice == 3:
        result = cursor.execute("SELECT * FROM review")
        rows = result.fetchall()
        for row in rows:
            print("Cat:", row[1], ", Title:", row[2], ", Evaluation:", row[3]) 
    elif choice == 0:
        print("Bye")
        break
    else: 
        print("Wrong choice")
