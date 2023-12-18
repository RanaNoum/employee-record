import tkinter as tk
from tkinter import messagebox

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
        self.show_all_button = tk.Button(root, text="Show All Records", command=self.show_all_records)

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

    def add_employee(self):
        # Get input values
        emp_id = self.entry_id.get()
        emp_name = self.entry_name.get()
        emp_salary = self.entry_salary.get()

        # Add employee logic (you can replace this with your existing logic)
        # For demonstration purposes, we'll just display a message
        messagebox.showinfo("Employee Added", f"Employee {emp_name} added successfully!")

    def remove_employee(self):
        # Get input value (employee ID)
        emp_id = self.entry_id.get()

        # Remove employee logic (you can replace this with your existing logic)
        # For demonstration purposes, we'll just display a message
        messagebox.showinfo("Employee Removed", f"Employee with ID {emp_id} removed successfully!")

    def show_all_records(self):
        # Retrieve all employee records from the database
        # Replace this with your actual database query
        # For demonstration purposes, we'll just display a message
        all_records = [
            {"id": 1, "name": "John Doe", "salary": 5000},
            {"id": 2, "name": "Jane Smith", "salary": 4500},
            # Add more records here...
        ]

        # Create a new window to display all records
        self.show_records_window(all_records)

    def show_records_window(self, records):
        # Create a new window
        records_window = tk.Toplevel(self.root)
        records_window.title("All Employee Records")

        # Create a text widget to display records
        text_widget = tk.Text(records_window, height=10, width=40)
        text_widget.pack()

        # Insert records into the text widget
        for record in records:
            text_widget.insert(tk.END, f"ID: {record['id']}\nName: {record['name']}\nSalary: {record['salary']}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementGUI(root)
    root.mainloop()
