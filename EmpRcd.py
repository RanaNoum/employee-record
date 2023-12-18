import tkinter as tk
from tkinter import messagebox
import mysql.connector

class EmployeeManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")

        # Create labels and entry fields
        self.label_name = tk.Label(root, text="Employee Name:")
        self.entry_name = tk.Entry(root)
        self.label_salary = tk.Label(root, text="Employee Salary:")
        self.entry_salary = tk.Entry(root)

        # Create buttons
        self.add_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.remove_button = tk.Button(root, text="Remove Employee", command=self.remove_employee)
        self.show_all_button = tk.Button(root, text="Show All Records", command=self.display_all_employees)

        # Grid layout
        self.label_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        self.label_salary.grid(row=1, column=0)
        self.entry_salary.grid(row=1, column=1)
        self.add_button.grid(row=2, column=0, columnspan=2)
        self.remove_button.grid(row=3, column=0, columnspan=2)
        self.show_all_button.grid(row=4, column=0, columnspan=2)

        # Initialize database connection
        self.db_connection = self.connect_to_database()

    def connect_to_database(self):
        db_connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database_name"
        )
        #hello this will return 
        return db_connection

    def add_employee(self):
        emp_name = self.entry_name.get()
        emp_salary = self.entry_salary.get()

        try:
            db_cursor = self.db_connection.cursor()
            db_cursor.execute("CREATE TABLE IF NOT EXISTS employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary DECIMAL(10, 2))")

            employee_sql_query = "INSERT INTO employee (name, salary) VALUES (%s, %s)"
            employee_values = (emp_name, emp_salary)
            db_cursor.execute(employee_sql_query, employee_values)
            self.db_connection.commit()

            last_inserted_id = db_cursor.lastrowid
            print(f"Employee {emp_name} added successfully! (ID: {last_inserted_id})")
        except Exception as e:
            messagebox.showerror("Error", f"Error while adding employee: {e}")

    def remove_employee(self):
        # Implement the removal logic (similar to previous example)
        pass

    def display_all_employees(self):
        # Implement the display logic (similar to previous example)
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementGUI(root)
    root.mainloop()
