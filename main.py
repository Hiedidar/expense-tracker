from expense_tracker import ExpenseTracker
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Export to CSV")
        print("4. Plot by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")
                tracker.add_expense(amount, category, description)
                print("✅Expense added")
            except ValueError:
                print("⚠️ Invalid input for amount.")

        elif choice == "2":
            print(tracker.get_expenses())

        elif choice == "3":
            tracker.export_to_csv()

        elif choice == "4":
            tracker.plot_expenses_by_category()

        elif choice == "5":
            print("Exiting... Goodbye 👋")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()