
import csv
import pandas as pd
import datetime
import numpy as np

global trac_data
trac_data = pd.DataFrame(columns=['type', 'property', 'amount', 'date'])
# trac_data2 = {'type': 'Expense', 'property': 'Food', 'amount': 100, 'date': '2021-01-01'}
# trac_data = pd.concat([trac_data, pd.DataFrame.from_dict(trac_data2,orient='index').T], ignore_index=True)
# print(trac_data)
def write_to_csv(data : 'pd.DataFrame'):
    data.to_csv('data.csv',index=False)
# print(trac_data)
# write_to_csv(trac_data)

def read_from_csv():
    global trac_data
    trac_data = pd.read_csv('data.csv')

def add_data(data : dict):
    global trac_data
    tempdf = pd.DataFrame.from_dict(data, orient='index').T
    print(tempdf)
    trac_data = pd.concat([trac_data, tempdf], ignore_index=True)



def get_data():
    return trac_data

def add_expense():
    type_ = input("Enter the type of expense: (Expense, Income/E,I): ")
    if type_.lower() == 'exit':
        return
    if type_.lower() not in ['expense', 'income', 'e', 'i']:
        print("Please enter a valid type")
        return
    elif type_.lower() in ['e', 'expense']:
        type_ = 'Expense'
    elif type_.lower() in ['i', 'income']:
        type_ = 'Income'
    prop = input("Enter the property of your expense: ")
    amount = input("Enter the amount: ")
    date = input("Enter the date: (DD/MM/YYYY): ")
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    data = {'type': type_, 'property': prop, 'amount': amount, 'date': date}
    # print(data)
    add_data(data)
    # print(trac_data)

def get_expenses():
    read_from_csv()
    # date = input("Enter the date: (DD/MM/YYYY): ")
    # date = datetime.datetime.strptime(date, "%d/%m/%Y")
    # for index, row in trac_data.iterrows():
    #     if row['date'] == date:
    #         print(row)
    # return
    # print(trac_data)
    # print('--- Summary ---')
    templ = trac_data.groupby('type')
    for name, group in templ:
        # print('Total: ', group['amount'].sum())
        # print('-----------------------')
        print(f'--- {name} Summary ---\nTotal {name}: {group["amount"].sum()}\n')
    print(f"Total: {trac_data['amount'].sum()}\n")


def main(userin : int = 0):
    try:
        if userin == 0:
            userin = int(input("Welcome to Expense Tracker! What would you like to do? \n1. Add Expense \n2. Get Expenses \n3. Exit\n"))
        if userin == 1:
            add_expense()
        elif userin == 2:
            get_expenses()
        elif userin == 3:
            return 'exit'
    except ValueError:
        print("Please enter a valid number")
        return

    return

if __name__ == '__main__':
    read_from_csv()
    numin = 0
    while True:
        if numin == 0:
            numin = int(input("Welcome to Expense Tracker! What would you like to do? \n1. Add Expense \n2. Get Expenses \n3. Exit\n"))
        a = main(numin)
        if a == 'exit':
            break
        cont = input("Would you like to continue? (Y/N): ")
        if cont.lower() == 'n' or cont.lower() == '':
            break
        elif cont.lower() == 'y':
            te = input('Would you like to start over? (Y/N): ')
            if te.lower() == 'y':
                numin = 0
                write_to_csv(trac_data)
            elif te.lower() == 'n':
                pass
            else:
                print("Please enter a valid input")
                break
        else:
            print("Please enter a valid input")
            break
    write_to_csv(trac_data)
    print("Thank you for using Expense Tracker!")
