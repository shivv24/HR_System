class Employee:
    def __init__(self, name, emp_id, department, position):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.position = position

class HRSystem:
    def __init__(self):
        self.emps = []
        self.attendance = {}
        self.leave_rem = {}

    def add_employee(self, employee):
        self.emps.append(employee)
        self.leave_rem[employee.emp_id] = 0

    def mark_attendance(self, date, *employee_ids):
        if date not in self.attendance:
            self.attendance[date] = []
        for emp_id in employee_ids:
            self.attendance[date].append(emp_id)

    def apply_for_leave(self, emp_id, leave_days):
        if emp_id in self.leave_rem and self.leave_rem[emp_id] >= leave_days:
            self.leave_rem[emp_id] -= leave_days
            return True
        return False

    def approve_leave(self, emp_id, leave_days):
        if emp_id in self.leave_rem:
            self.leave_rem[emp_id] += leave_days

    def generate_report(self):
        print("Employee Attendance:")
        for date, employees in self.attendance.items():
            print(f"Date: {date}, Employees: {', '.join(str(emp_id) for emp_id in employees)}")

        print("\nLeave Balance:")
        for emp_id, balance in self.leave_rem.items():
            print(f"Employee ID {emp_id}: {balance} days")


if __name__ == "__main__":
    hr_system = HRSystem()

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. Apply for Leave")
        print("4. Approve Leave")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            department = input("Enter department: ")
            position = input("Enter position: ")
            hr_system.add_employee(Employee(name, emp_id, department, position))
            print("Employee added successfully.")

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            employee_ids = input("Enter employee IDs separated by spaces: ").split()
            hr_system.mark_attendance(date, *employee_ids)
            print("Attendance marked successfully.")

        elif choice == "3":
            emp_id = input("Enter employee ID: ")
            leave_days = int(input("Enter number of leave days: "))
            if hr_system.apply_for_leave(emp_id, leave_days):
                print("Leave applied successfully.")
            else:
                print("Insufficient leave balance.")

        elif choice == "4":
            emp_id = input("Enter employee ID: ")
            leave_days = int(input("Enter number of leave days: "))
            hr_system.approve_leave(emp_id, leave_days)
            print("Leave approved successfully.")

        elif choice == "5":
            hr_system.generate_report()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
