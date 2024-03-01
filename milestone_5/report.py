import csv
from datetime import datetime

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  
        data = [row for row in reader]
    return header, data

def filter_by_month(data, target_month):
    filtered_data = []
    for row in data:
        hiring_date = datetime.strptime(row[1], '%Y-%m-%d')
        if hiring_date.month == target_month:
            filtered_data.append(row)
    return filtered_data

def generate_report(file_path, target_month):
    header, data = read_csv(file_path)
    filtered_data = filter_by_month(data, target_month)

    birthdays_by_department = {}
    anniversaries_by_department = {}

    for row in filtered_data:
        department = row[2]
        if department not in birthdays_by_department:
            birthdays_by_department[department] = 0
        birthdays_by_department[department] += 1

        if department not in anniversaries_by_department:
            anniversaries_by_department[department] = 0
        anniversaries_by_department[department] += 1

    print(f"Report for {target_month}:")
    print("--- Birthdays ---")
    print(f"Total: {len(filtered_data)}")
    print("By department:")
    for department, count in birthdays_by_department.items():
        print(f"- {department}: {count}")

    print("--- Anniversaries ---")
    print(f"Total: {len(filtered_data)}")
    print("By department:")
    for department, count in anniversaries_by_department.items():
        print(f"- {department}: {count}")

generate_report('database.csv', 4)  