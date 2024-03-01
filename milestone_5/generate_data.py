from faker import Faker
import csv

fake = Faker()

# generate employees data
def employee_generator(num):
    employees = []
    fake.unique.clear()  # Clear the unique names cache
    for _ in range(num):
        name = fake.unique.first_name()
        hiring_date = fake.date_between(start_date='-3y', end_date='today')
        department = fake.random_element(elements=('HR', 'Finance', 'Engineering'))
        birthday_date = fake.date_of_birth(minimum_age=21, maximum_age=75)
        employees.append({'Name': name, 'Hiring Date': hiring_date, 'Department': department, 'Birthday Date': birthday_date})
    return employees

# export employees data to csv
def export_csv(employees, filename='database.csv'):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Name', 'Hiring Date', 'Department', 'Birthday Date']
        writer = csv.writer(file)

        # Write header
        writer.writerow(fieldnames)
        
        # Write data
        for employee in employees:
            writer.writerow(employee.values())  # Use employee.values() to get the values in the correct order

# Example usage
export_csv(employee_generator(50))
