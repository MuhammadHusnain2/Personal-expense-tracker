def delete_expense():
    with open("Expense.txt","r") as f3:
        delete = f3.readlines()
        for i, line in enumerate(delete):
            print(f"{i}: {line.strip()}")

        choice = int(input("Enter line no that you want to delete: "))
        delete.pop(choice)

        with open("expense.txt","w") as f:
            f.writelines(delete)

