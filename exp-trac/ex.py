import csv
import datetime
global trac_data
trac_data = {}
def write_to_csv(type_ : str, data : dict):
    with open('data.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([type_, data])

def read_from_csv():
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            trac_data[row[0]] = row[1]

def add_data(type_ : str, data : dict):
    trac_data[type_] = data
    write_to_csv(type_, data)

def get_data(type : str):
    return trac_data[type]

def add_expense():
    type_ = input("Enter the type of expense: ")

def main():
    read_from_csv()
    try:
        userin = int(input("Welcome to Expense Tracker! What would you like to do? \n1. Add Expense \n2. Get Expenses \n3. Exit\n"))
    except ValueError:
        print("Please enter a valid number")
        return

