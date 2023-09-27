import json
from termcolor import colored
# json_data to be stored through the program

def savefile(json_data):
    json_string= json.dumps(json_data)
    with open("../expenses.txt", "w") as file:
        file.write(json_string)

def addExpenses(json_data):
    category = input("Please enter the catagory of your item: ")
    price = input("Please enter the price Ex 406.55, 12: ")
    description = input("Please write description for teh expense: ")
    try:
        price = int(price)
    except:
        return "FAIL"
    value = list(json_data.get(category, []))
    if value != []:
        json_data[category] = [price + value[0], description]
    else:
        json_data[category] = [price, description]
    return "SUCCESS"

def deleteExpenses(json_data):
    category = input("Please enter the catagory of your item: ")
    value = list(json_data.get(category))[0]
    if value == []:
        return "FAIL"
    del json_data[category]
    return "SUCCESS"

def calculateTotal(json_data):
    values = list(json_data.values())
    sum = 0
    for value in values:
        sum += value[0]
    return sum

def listExpenses(json_data):
    expenseList = "\n"

    if len(json_data.keys()) == 0:
        return "EMPTY"
    for key in json_data:
        expenseList += f"{key} - {json_data[key][0]} - {json_data[key][1]}\n"
    return expenseList

def main():
    with open("../expenses.txt", "r") as file:
        json_data = json.load(file)
    while True:
        line1 = "Welcome to Expenses Tracker App"
        line2 = "Commands are \nadd - adds expenses\ndelete - delete expenses\ntotal - total expenses\n" \
                "list - lists all the expenses by catagory and price\n" \
                "quit - exit application\n" \
                "Enter Command: "
        command = input(f'{line1}\n{line2}').strip().lower()
        if command == "add":
            string = addExpenses(json_data)
            if string == "SUCCESS":
                print(colored("\nExpense added!\n", "green"))
                savefile(json_data)
            else:
                print(colored("\nPrice is not valid\n", "red"))
        if command == "delete":
            string = deleteExpenses(json_data)
            if string == "SUCCESS":
                print(colored("\nExpense deleted!\n", "green"))
                savefile(json_data)
            else:
                print(colored("\nExpense doesn't exist\n", "red"))
        if command == "total":
            total = calculateTotal(json_data)
            print(f"\nTotal Expense is \033[1m{total}\033[0m!\n")
        if command == "list":
            expenseList = listExpenses(json_data)
            if expenseList == "EMPTY":
                print(f'\nNo Expenses in Document!\n')
            else:
                print(expenseList)
        if command == "quit":
            print("\nExited Program\n")
            exit(0)

if __name__ == "__main__":
    main()