# Part 1 - server
from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
    return header, data

def filter_by_month_and_department(data, target_month, target_department):
    filtered_data = []
    for row in data:
        employee_id = row[0]
        hiring_date = datetime.strptime(row[1], '%Y-%m-%d')

        # Check if the ID is a valid integer
        try:
            employee_id = int(employee_id)
        except ValueError:
            # Handle the case where ID is not a valid integer
            employee_id = None

        if employee_id is not None and hiring_date.month == target_month and row[2] == target_department:
            filtered_data.append({"id": employee_id, "name": row[3], "birthday": hiring_date.strftime('%b %d')})
    return filtered_data

@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    target_month = int(request.args.get('month', 1))
    target_department = request.args.get('department', 'HR')
    header, data = read_csv('database.csv')
    filtered_data = filter_by_month_and_department(data, target_month, target_department)
    
    response_data = {
        "total": len(filtered_data),
        "employees": filtered_data
    }

    return jsonify(response_data)

@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    target_month = int(request.args.get('month', 1))
    target_department = request.args.get('department', 'HR')
    header, data = read_csv('database.csv')
    filtered_data = filter_by_month_and_department(data, target_month, target_department)
    
    response_data = {
        "total": len(filtered_data),
        "employees": filtered_data
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
