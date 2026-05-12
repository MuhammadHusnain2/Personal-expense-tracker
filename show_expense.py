#For showing information of "Expense.txt" to user
def view_expense():
    with open("Expense.txt","r") as f2:
        Read = (f2.readlines())
        for line in Read:
            print(line.strip())