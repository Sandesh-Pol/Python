import tkinter as tk
from tkinter import messagebox
import sqlite3 as lite

class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")

        except Exception:
            print('Unable to create db . . !')

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data)
                return True
        except Exception:
            return False

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False

    def delete_data(self, Id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [Id])
                return True
        except Exception:
            return False

class CourseManagementGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Course Management")
        self.geometry("900x650")

        self.db = DatabaseManage()

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=60, pady=50)

        tk.Label(self.main_frame, text="Course Management", font=('Helvetica', 32)).pack(pady=20, anchor='w')

        tk.Button(self.main_frame, text="Insert a new Course", command=self.show_insert_course, font=('Helvetica', 14)).pack(pady=10, anchor='w')
        tk.Button(self.main_frame, text="Show all courses", command=self.show_all_courses, font=('Helvetica', 14)).pack(pady=10, anchor='w')
        tk.Button(self.main_frame, text="Delete a Course", command=self.show_delete_course, font=('Helvetica', 14)).pack(pady=10, anchor='w')

    def create_back_button(self, parent_frame, callback):
        back_button = tk.Button(parent_frame, text="Back", command=callback, font=('Helvetica', 14))
        back_button.pack(side=tk.LEFT, pady=10, padx=10, anchor='w')
        return back_button

    def switch_frame(self, from_frame, to_frame):
        from_frame.pack_forget()
        to_frame.pack(fill=tk.BOTH, expand=True, padx=60, pady=50)

    def show_insert_course(self):
        self.main_frame.pack_forget()
        insert_frame = tk.Frame(self)
        insert_frame.pack(fill=tk.BOTH, expand=True, padx=60, pady=50)

        tk.Label(insert_frame, text="Insert a new Course", font=('Helvetica', 24)).pack(pady=20, anchor='w')

        tk.Label(insert_frame, text="Enter course name:", font=('Helvetica', 14)).pack(pady=5, anchor='w')
        name_entry = tk.Entry(insert_frame, font=('Helvetica', 14))
        name_entry.pack(pady=5, anchor='w')

        tk.Label(insert_frame, text="Enter course description:", font=('Helvetica', 14)).pack(pady=5, anchor='w')
        description_entry = tk.Text(insert_frame, wrap=tk.WORD, width=50, height=5, font=('Helvetica', 14))
        description_entry.pack(pady=5, anchor='w')

        tk.Label(insert_frame, text="Enter course price:", font=('Helvetica', 14)).pack(pady=5, anchor='w')
        price_entry = tk.Entry(insert_frame, font=('Helvetica', 14))
        price_entry.pack(pady=5, anchor='w')

        tk.Label(insert_frame, text="Is this course private (0/1):", font=('Helvetica', 14)).pack(pady=5, anchor='w')
        is_private_entry = tk.Entry(insert_frame, font=('Helvetica', 14))
        is_private_entry.pack(pady=5, anchor='w')

        self.create_back_button(insert_frame, lambda: self.switch_frame(insert_frame, self.main_frame))

        tk.Button(insert_frame, text="Insert Course", command=lambda: self.perform_insert(
            name_entry.get(),
            description_entry.get("1.0", tk.END),
            price_entry.get(),
            is_private_entry.get()
        ), font=('Helvetica', 14)).pack(pady=10, anchor='w')

    def show_all_courses(self):
        self.main_frame.pack_forget()
        courses_frame = tk.Frame(self)
        courses_frame.pack(fill=tk.BOTH, expand=True, padx=60, pady=50)

        tk.Label(courses_frame, text="Course List", font=('Helvetica', 24)).pack(pady=20, anchor='w')

        courses = self.db.fetch_data()

        if not courses:
            tk.Label(courses_frame, text="No courses available.", font=('Helvetica', 14)).pack(pady=10, anchor='w')
        else:
            for index, item in enumerate(courses):
                tk.Label(courses_frame, text=f"Course {index + 1}:", font=('Helvetica', 14)).pack(anchor='w')
                tk.Label(courses_frame, text=f"Course ID: {item[0]}", font=('Helvetica', 14)).pack(anchor='w')
                tk.Label(courses_frame, text=f"Course Name: {item[1]}", font=('Helvetica', 14)).pack(anchor='w')
                tk.Label(courses_frame, text=f"Course Description: {item[2]}", font=('Helvetica', 14)).pack(anchor='w')
                tk.Label(courses_frame, text=f"Course Price: {item[3]}", font=('Helvetica', 14)).pack(anchor='w')
                is_private = 'Yes' if item[4] else 'No'
                tk.Label(courses_frame, text=f"Is Private: {is_private}", font=('Helvetica', 14)).pack(anchor='w')

        self.create_back_button(courses_frame, lambda: self.switch_frame(courses_frame, self.main_frame))

    def show_delete_course(self):
        delete_frame = tk.Frame(self)
        delete_frame.pack(fill=tk.BOTH, expand=True, padx=60, pady=50)

        tk.Label(delete_frame, text="Delete a Course", font=('Helvetica', 24)).pack(pady=20, anchor='w')

        tk.Label(delete_frame, text="Enter the course ID to delete:", font=('Helvetica', 14)).pack(pady=5, anchor='w')
        record_id_entry = tk.Entry(delete_frame, font=('Helvetica', 14))
        record_id_entry.pack(pady=5, anchor='w')

        self.create_back_button(delete_frame, lambda: self.switch_frame(delete_frame, self.main_frame))

        tk.Button(delete_frame, text="Delete Course", command=lambda: self.perform_delete(record_id_entry.get()), font=('Helvetica', 14)).pack(pady=10, anchor='w')

    def perform_insert(self, name, description, price, is_private):
        if self.db.insert_data([name, description, price, is_private]):
            messagebox.showinfo("Success", "Course was inserted successfully")
        else:
            messagebox.showerror("Error", "OOPS something went wrong")

    def perform_delete(self, record_id):
        if self.db.delete_data(record_id):
            messagebox.showinfo("Success", "Course was deleted successfully!")
        else:
            messagebox.showerror("Error", "Something went wrong!")

if __name__ == "__main__":
    app = CourseManagementGUI()
    app.mainloop()
