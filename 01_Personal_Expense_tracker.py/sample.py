from Write_expense import add_expense
from show_expense import view_expense
from Delete_expense import delete_expense

def main():
    while True:
        print("\n Expense tracker tool")
        print("1.Add Expense")
        print("2.View Expense")
        print("3.Delete Expense")
        print("4.Exit")

        try:
            choice = int(input("Enter your choice from (1-4): "))
        except ValueError:
            print("Invalid value.Kindly enter choice in numbers")
            continue

        if(choice == 1):
            add_expense
        elif(choice == 2):
            view_expense
        elif(choice == 3):
            delete_expense
        elif(choice == 4):
            print("Exiting....Thanks for using this app")
            break
        else:
            print("Invalid choice...Try again")

main()