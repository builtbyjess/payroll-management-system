# UNIVERSITY PAYROLL MANAGEMENT SYSTEM

# Preload employee records
employees = [
    {
        "id": "UNU001",
        "name": "Andreson James",
        "position": "Dean of Faculty",
        "department": "Computing",
        "hourly_wage": 5500
    },
    {
        "id": "UNU002",
        "name": "Makayla Okafor ",
        "position": "Computer Science Lecturer ",
        "department": "Computer Science ",
        "hourly_wage": 3500
    },
    {
        "id": "UNU003",
        "name": "Daniel Briggs",
        "position": "GST Lecturer ",
        "department": "General Studies",
        "hourly_wage": 2840
    },
    {
        "id": "UNU004",
        "name": "Richard Oluwabayode",
        "position": "Deputy Registrar ",
        "department": "Registry ",
        "hourly_wage": 4000
    },
    {
        "id": "UNU005",
        "name": "Charlotte Din",
        "position": "Clinic Matron ",
        "department": "University Clinic ",
        "hourly_wage": 2000
    },
    {
        "id": "UNU006",
        "name": "Fedora Clarke",
        "position": "Network Administrator ",
        "department": "ICT Department ",
        "hourly_wage": 3200
    },
    {
        "id": "UNU007",
        "name": "Ellie Thompson",
        "position": "Faculty Secretary ",
        "department": "Faculty Administration ",
        "hourly_wage": 2000
    },
    {
        "id": "UNU008",
        "name": "Naomi Bello",
        "position": "Laboratory Technician ",
        "department": "Science Laboratory ",
        "hourly_wage": 2000
    },
    {
        "id": "UNU009",
        "name": "Steven Peters",
        "position": "Security Officer",
        "department": "Security Unit",
        "hourly_wage": 1500
    },
    {
        "id": "UNU010",
        "name": "Edward Adams ",
        "position": "Maintenance Officer ",
        "department": "Works and Maintenance ",
        "hourly_wage": 1800
    }
]


def view_all_employees():
    print("\nUNIVERSITY EMPLOYEE RECORDS")
    print("-" * 90)
    print(f"{'ID':<10} {'NAME':<25} {'POSITION':<28} {'HOURLY WAGE':<12}")

    for employee in employees:
        print(
            f"{employee['id']:<10}"
            f"{employee['name']:<25}"
            f"{employee['position']:<28}"
            f"₦{employee['hourly_wage']:<12,}"
        )
    print("-" * 90)


def calculate_total_payroll():
    total_payroll = 0
    for employee in employees:
        monthly_salary = employee["hourly_wage"] * 160
        total_payroll = total_payroll + monthly_salary

    print("\nTOTAL MONTHLY UNIVERSITY PAYROLL")
    print(f"₦{total_payroll:,}")


def view_individual_records():
    while True:
        employee_id = input("\nEnter Employee ID (or type EXIT to stop): ")

        if employee_id.upper() == "EXIT":
            break

        found = False
        for employee in employees:
            if employee["id"] == employee_id:
                found = True
                print("\n--- INDIVIDUAL STAFF RECORD: ---")
                print("Full Name:", employee["name"])
                print("Position:", employee["position"])
                print("Department:", employee["department"])
                print(f"Hourly Wage: ₦ {employee['hourly_wage']:,}")

                hours_worked = int(input("Enter hours worked this week: "))
                hourly_wage = employee["hourly_wage"]
                regular_hours = min(hours_worked, 40)
                overtime_hours = max(hours_worked - 40, 0)

                overtime_rate = hourly_wage * 1.5
                regular_pay = regular_hours * hourly_wage
                overtime_pay = overtime_hours * overtime_rate
                weekly_salary = regular_pay + overtime_pay
                monthly_salary = weekly_salary * 4

                print(f"Regular Hours: {regular_hours}")
                print(f"Overtime Hours: {overtime_hours}")
                print(f"Regular pay: ₦ {regular_pay:,}")
                print(f"Overtime Pay: ₦ {overtime_pay:,}")
                print(f"Weekly Salary: ₦ {weekly_salary:,}")
                print(f"Estimated Monthly Salary: ₦ {monthly_salary:,}")
                break

        if not found:
            print("Employee ID not found.")


def main_menu():
    print("MAIN MENU IS STARTING")

    while True:
        print("\n" + "=" * 40)
        print("UNIVERSITY")
        print("PAYROLL MANAGEMENT SYSTEM")
        print("EMPLOYEE MANAGEMENT PORTAL")
        print("=" * 40)
        print("\nMAIN MENU")
        print("1. View Total University Payroll")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")
        if choice == "1":
            calculate_total_payroll()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            view_individual_records()
        elif choice == "4":
            print("\nThank you for using the University Payroll Management System.")
            break
        else:
            print("\nInvalid choice. Please select a number from 1 to 4.")


if __name__ == "__main__":
    main_menu()
