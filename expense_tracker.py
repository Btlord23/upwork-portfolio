
import csv
import os

FILE_NAME = "expenses.csv"


def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    expenses.append({
                        "name": row["name"],
                        "amount": float(row["amount"])
                    })
        except (ValueError, KeyError, OSError) as error:
            print(f"Could not load expenses: {error}")

    return expenses


def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["name", "amount"]
            )
            writer.writeheader()
            writer.writerows(expenses)

        print("Expenses saved successfully!")

    except OSError as error:
        print(f"Could not save expenses: {error}")


def show_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\nYOUR EXPENSES")
    print("-" * 40)

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['name']} - "
            f"{expense['amount']:.2f}"
        )

    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)

    print("-" * 40)
    print(f"Total expenses: {total:.2f}")
    print(f"Average expense: {average:.2f}")


def main():
    expenses = load_expenses()

    print("=" * 40)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 40)

    while True:
        print("\n1. Add expense")
        print("2. View expenses")
        print("3. Save expenses")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            name = input("Enter expense name: ").strip()

            if not name:
                print("Expense name cannot be empty.")
                continue

            try:
                amount = float(input("Enter amount: "))

                if not 0 < amount < float("inf"):
                    print("Enter a valid positive amount.")
                    continue

                expenses.append({
                    "name": name,
                    "amount": amount
                })

                print("Expense added successfully!")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            save_expenses(expenses)

        elif choice == "4":
            save_expenses(expenses)
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
