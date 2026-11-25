
print("PERSONAL EXPENSE TRACKER")
print("=" * 30)

expenses = []

while True:
    name = input("\nEnter expense name (or 'done' to finish): ").strip()

    if name.lower() == "done":
        break

    if not name:
        print("Expense name cannot be empty.")
        continue

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        expenses.append({"name": name, "amount": amount})
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number.")

print("\nEXPENSE SUMMARY")
print("=" * 30)

total = 0

for expense in expenses:
    print(f"{expense['name']}: {expense['amount']:.2f}")
    total += expense["amount"]

print("-" * 30)
print(f"TOTAL EXPENSES: {total:.2f}")
print(f"Number of expenses: {len(expenses)}")

print("\nThank you for using the Expense Tracker!")
