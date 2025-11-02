def add_expense():
    expense = int(input("Expense: "))
    catogary = input("Catogary: ")
    descrip = input("Description: ")

    Items = f"Expense:{expense}\nCatogary:{catogary}\nDescription:{descrip}"

    #For saving all the information
    with open("Expense.txt","w") as f1:
        f1.write(Items)

