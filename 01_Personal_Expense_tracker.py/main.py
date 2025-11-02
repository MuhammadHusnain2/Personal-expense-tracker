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
 

        choice = int(input("Enter your choice from (1-4): "))

        if(choice == 1):
            print(add_expense())
        elif(choice == 2):
            print(view_expense())
        elif(choice == 3):
            print(delete_expense())
        elif(choice == 4):
            print("Exiting....Thanks for using this app")
            break
        else:
            print("Invalid choice...Try again")

main()

