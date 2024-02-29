import sys
import csv
import calendar


def get_full_month(date_string):
    year, month, day = map(int, date_string.split('-'))
    return calendar.month_name[month].lower()


def generate_report(database_file, month):
    birthday_counts = {}
    anniversary_counts = {}
    total_birthdays = 0
    total_anniversaries = 0

    with open(database_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            department = row["Department"]
            birthday_month = get_full_month(row["Birthday"])
            hiring_month = get_full_month(row["Hiring Date"])

            if birthday_month and birthday_month.lower() == month.lower():
                if department in birthday_counts:
                    birthday_counts[department] += 1
                else:
                    birthday_counts[department] = 1
                total_birthdays += 1
            if hiring_month and hiring_month.lower() == month.lower():
                if department in anniversary_counts:
                    anniversary_counts[department] += 1
                else:
                    anniversary_counts[department] = 1
                total_anniversaries += 1

    print(f"Report for {month.capitalize()} generated")
    print("--- Birthdays ---")
    print(f"Total: {total_birthdays}")
    print("By department:")
    for department, count in birthday_counts.items():
        print(f"- {department}: {count}")
   
    print("--- Anniversaries ---")
    print(f"Total: {total_anniversaries}")
    print("By department:")
    for department, count in anniversary_counts.items():
        print(f"- {department}: {count}")


if len(sys.argv) != 3:
    sys.exit()
else:
    database_file = sys.argv[1]
    month = sys.argv[2]
    generate_report(database_file, month)