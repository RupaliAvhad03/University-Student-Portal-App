import sqlite3
import tkinter as tk
from tkinter import messagebox

def view_students():
    try:
        conn = sqlite3.connect("E:/Student_App.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students")
        results = cursor.fetchall()
        conn.close()

        msg = "\n".join([str(row) for row in results])
        messagebox.showinfo("Student Records", msg)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_student():
    def submit():
        try:
            conn = sqlite3.connect("E:/Student_App.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Students (student_id, first_name, last_name, email, phone_number)
                VALUES (?, ?, ?, ?, ?)
            """, (entry_id.get(), entry_fname.get(), entry_lname.get(), entry_email.get(), entry_phone.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student added successfully!")
            top.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    top = tk.Toplevel(root)
    top.title("Add Student")

    tk.Label(top, text="Student ID").pack()
    entry_id = tk.Entry(top)
    entry_id.pack()

    tk.Label(top, text="First Name").pack()
    entry_fname = tk.Entry(top)
    entry_fname.pack()

    tk.Label(top, text="Last Name").pack()
    entry_lname = tk.Entry(top)
    entry_lname.pack()

    tk.Label(top, text="Email").pack()
    entry_email = tk.Entry(top)
    entry_email.pack()

    tk.Label(top, text="Phone Number").pack()
    entry_phone = tk.Entry(top)
    entry_phone.pack()

    tk.Button(top, text="Submit", command=submit).pack(pady=10)

def delete_student():
    def submit_delete():
        try:
            conn = sqlite3.connect("E:/Student_App.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Students WHERE student_id = ?", (entry_id.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Deleted", "Student deleted successfully!")
            del_top.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    del_top = tk.Toplevel(root)
    del_top.title("Delete Student")

    tk.Label(del_top, text="Enter Student ID to Delete").pack()
    entry_id = tk.Entry(del_top)
    entry_id.pack()
    tk.Button(del_top, text="Delete", command=submit_delete).pack(pady=10)

def update_student():
    def submit_update():
        try:
            conn = sqlite3.connect("E:/Student_App.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Students
                SET first_name = ?, last_name = ?, email = ?, phone_number = ?
                WHERE student_id = ?
            """, (entry_fname.get(), entry_lname.get(), entry_email.get(), entry_phone.get(), entry_id.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Updated", "Student updated successfully!")
            upd_top.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    upd_top = tk.Toplevel(root)
    upd_top.title("Update Student")

    tk.Label(upd_top, text="Student ID").pack()
    entry_id = tk.Entry(upd_top)
    entry_id.pack()

    tk.Label(upd_top, text="New First Name").pack()
    entry_fname = tk.Entry(upd_top)
    entry_fname.pack()

    tk.Label(upd_top, text="New Last Name").pack()
    entry_lname = tk.Entry(upd_top)
    entry_lname.pack()

    tk.Label(upd_top, text="New Email").pack()
    entry_email = tk.Entry(upd_top)
    entry_email.pack()

    tk.Label(upd_top, text="New Phone Number").pack()
    entry_phone = tk.Entry(upd_top)
    entry_phone.pack()

    tk.Button(upd_top, text="Update", command=submit_update).pack(pady=10)

def view_enrollments():
    try:
        conn = sqlite3.connect("E:/Student_App.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.student_id, s.first_name, s.last_name, c.course_name, e.semester
            FROM Students s
            JOIN Enrollment e ON s.student_id = e.student_id
            JOIN Courses c ON e.course_id = c.course_id
        """)
        results = cursor.fetchall()
        conn.close()

        msg = "\n".join([f"{r[0]} | {r[1]} {r[2]} | {r[3]} | {r[4]}" for r in results])
        messagebox.showinfo("Enrollments", msg)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("University Student Portal")
root.geometry("400x500")

# Buttons - added before mainloop
tk.Button(root, text="View Students", command=view_students).pack(pady=5)
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Update Student", command=update_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)
tk.Button(root, text="View Enrollments", command=view_enrollments).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

# ---------- Main Loop ----------
root.mainloop()
