import tkinter as tk
from tkinter import messagebox
import mysql.connector

class EmployeeManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")

        # Create labels and entry fields
        self.label_id = tk.Label(root, text="Employee ID:")
        self.entry_id = tk.Entry(root)
        self.label_name = tk.Label(root, text="Employee Name:")
        self.entry_name = tk.Entry(root)
        self.label_salary = tk.Label(root, text="Employee Salary:")
        self.entry_salary = tk.Entry(root)

        # Create buttons
        self.add_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.remove_button = tk.Button(root, text="Remove Employee", command=self.remove_employee)
        self.show_all_button = tk.Button(root, text="Show All Records", command=self.display_all_employees)

        # Grid layout
        self.label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)
        self.label_name.grid(row=1, column=0)
        self.entry_name.grid(row=1, column=1)
        self.label_salary.grid(row=2, column=0)
        self.entry_salary.grid(row=2, column=1)
        self.add_button.grid(row=3, column=0, columnspan=2)
        self.remove_button.grid(row=4, column=0, columnspan=2)
        self.show_all_button.grid(row=5, column=0, columnspan=2)

        # Initialize database connection
        self.db_connection = self.connect_to_database()

    def connect_to_database(self):
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="nomi12345",
            database="my_first_db"
        )
        return db_connection

    def add_employee(self):
        emp_id = self.entry_id.get()
        emp_name = self.entry_name.get()
        emp_salary = self.entry_salary.get()

        try:
            db_cursor = self.db_connection.cursor()
            db_cursor.execute("CREATE TABLE IF NOT EXISTS employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary DECIMAL(10, 2))")

            employee_sql_query = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
            employee_values = (emp_id, emp_name, emp_salary)
            db_cursor.execute(employee_sql_query, employee_values)
            self.db_connection.commit()

            messagebox.showinfo("Employee Added", f"Employee {emp_name} added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error while adding employee: {e}")

    def remove_employee(self):
        emp_id = self.entry_id.get()

        try:
            db_cursor = self.db_connection.cursor()
            delete_sql_query = "DELETE FROM employee WHERE id = %s"
            delete_values = (emp_id,)
            db_cursor.execute(delete_sql_query, delete_values)
            self.db_connection.commit()

            messagebox.showinfo("Employee Removed", f"Employee with ID {emp_id} removed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error while removing employee: {e}")

    def display_all_employees(self):
        try:
            db_cursor = self.db_connection.cursor()
            db_cursor.execute("SELECT * FROM employee")
            records = db_cursor.fetchall()

            for record in records:
                print(f"ID: {record[0]}, Name: {record[1]}, Salary: {record[2]}")
        except Exception as e:
            messagebox.showerror("Error", f"Error while fetching records: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementGUI(root)
    root.mainloop()
