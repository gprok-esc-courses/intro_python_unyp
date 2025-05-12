import sqlite3 
from tkinter import Tk, ttk, StringVar, END

class TodoListApp:
    def __init__(self, window):
        self.window = window
        self.db = None 
        self.cursor = None
        self.connect_db()

        # Task Form
        self.form_frame = ttk.LabelFrame(window, text="Task Data")
        self.form_frame.pack(fill='x')
        task_label = ttk.Label(self.form_frame, text="Task: ").grid(row=0, column=0)
        project_label = ttk.Label(self.form_frame, text="Project: ").grid(row=1, column=0)
        self.task_value = StringVar()
        task_field = ttk.Entry(self.form_frame, textvariable=self.task_value, width=30).grid(row=0, column=1)
        self.project_value = StringVar()
        project_field = ttk.Entry(self.form_frame, textvariable=self.project_value, width=30).grid(row=1, column=1)

        # Buttons
        self.button_frame = ttk.Frame(window)
        self.button_frame.pack(fill='x')
        self.add_btn = ttk.Button(self.button_frame, text="Add", command=self.add_new).grid(row=0, column=0)
        self.upd_btn = ttk.Button(self.button_frame, text="Update", command=self.update).grid(row=0, column=1)
        self.compl_btn = ttk.Button(self.button_frame, text="Complete", command=self.complete).grid(row=0, column=2)

        # Tasks List
        self.tasks_frame = ttk.Frame(window) 
        self.tasks_frame.pack(fill="both", expand=True)

        self.list = ttk.Treeview(self.tasks_frame, columns=("ID", "Task", "Project"), show="headings")
        self.list.heading("ID", text="ID")
        self.list.heading("Task", text="Task")
        self.list.heading("Project", text="Project")
        self.list.column("ID", width=30)
        self.list.column("Task", width=220)
        self.list.column("Project", width=130)
        self.list.pack(fill="both", expand=True)

        self.list.bind("<<TreeviewSelect>>", self.item_selected)

        self.selected_id = None

        self.load_tasks()


    def update(self):
        id = self.selected_id
        task = self.task_value.get()
        project = self.project_value.get()
        if len(task) == 0 or len(project) == 0:
            print("Field(s) are empty")
            return 
        self.cursor.execute("UPDATE tasks SET task=?, project=? WHERE id=?", (task, project, id))
        self.db.commit()
        self.load_tasks()


    def complete(self):
        id = self.selected_id
        self.cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (id,))
        self.db.commit()
        self.load_tasks()



    def item_selected(self, event):
        sel = self.list.selection()
        print(sel)
        item = self.list.item(sel[0], "values")
        self.selected_id = (item[0])
        self.task_value.set(item[1])
        self.project_value.set(item[2])


    def load_tasks(self):
        for item in self.list.get_children():
            self.list.delete(item)
        self.cursor.execute("SELECT id, task, project FROM tasks WHERE completed=0")
        tasks = self.cursor.fetchall()
        for task in tasks:
            self.list.insert("", END, values=task)
    
    def add_new(self):
        task = self.task_value.get()
        project = self.project_value.get()
        if len(task) == 0 or len(project) == 0:
            print("Field(s) are empty")
            return 
        self.cursor.execute("INSERT INTO tasks (task, project, completed) VALUES (?, ?, 0)", (task, project))
        self.db.commit()
        self.load_tasks()


    def connect_db(self):
        self.db = sqlite3.connect('todo.db')
        self.cursor = self.db.cursor()
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                task TEXT, 
                                project TEXT, 
                                completed INTEGER
                            )
                            """)
        self.db.commit()



root = Tk()
root.title("Todo List")
root.geometry("700x500")
app = TodoListApp(root)
root.mainloop()