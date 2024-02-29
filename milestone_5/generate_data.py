import random
import datetime
import csv


names = ['John Snow', 'Mary Smith', 'Patricia Jackson', 'Ada Williams', 'Fabian Brown', 'Thomas Moore', 'Lilia Thompson', 'Harry Johnson', 'Samuel Adamson', 'Ivan Prantenko', 'George Wilson', 'Amelia King', 'Scarlett Young', 'Isabella Lewis', 'Olivia Walker', 'Kateryna Shevchenko', 'Jessica Harris', 'Isla Taylor', 'Peter Parson', 'Olga Aldrige', 'Daryna Holumbievska', 'Peter Evans', 'Olivia Flatcher', 'Mary Adamson', 'Lilia Kapitan', 'Ben Wilson', 'Jane Gilbert', 'Monika Doe', 'Elizabeth Evans', 'Berta Walker', 'Sam Ellington', 'Gabriela Lewis', 'Kevin Joe', 'Adam Smith', 'Alexander Miller', 'Maria Tarasenko', 'Anastasia Konoval', 'Ihor Demydenko', 'John Adamson', 'Kevin Miller']
departments = ['HR', 'Production', 'Sales', 'Marketing', 'Finance', 'IT']
start_date = datetime.datetime(2010, 3, 12)
end_date = datetime.datetime(2023, 12, 31)


def generate_random_employee():
    name = random.choice(names)
    department = random.choice(departments)
    hire_date = datetime.datetime(random.randint(2010, 2023), random.randint(1, 12), random.randint(1, 28))
    birthday = datetime.datetime(random.randint(1965, 2006), random.randint(1, 12), random.randint(1, 28))
    return {"Name": name, "Hiring Date": hire_date.strftime("%Y-%m-%d"), "Department": department, "Birthday": birthday.strftime("%Y-%m-%d")}


def write_csv(filename, data):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Hiring Date", "Department", "Birthday"])

        for employee in data:
            writer.writerow([employee["Name"], employee["Hiring Date"], employee["Department"], employee["Birthday"]])

           
def generate_amount(num_employees):
    employee_data = [generate_random_employee() for _ in range(num_employees)]
    write_csv(r"C:\Users\Irina\OneDrive\Рабочий стол\Python\Lesson 5\database.csv", employee_data)
    
    print("Data has been written to database.csv")


num_employees = int(input("Enter the amount of employees: "))
generate_amount(num_employees)