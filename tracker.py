"""Main expense tracker application."""
from expense import Expense
from storage import Storage
from report import Report
from datetime import datetime
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class ExpenseTracker:
    
    def __init__(self, filename: str = "expenses.csv"):
        self.expenses = []
        self.storage = Storage(filename)
        self.expenses = self.storage.load_expenses()
        self._sync_next_id()
    
    def _sync_next_id(self):
        if self.expenses:
            self.next_id = max(exp.id for exp in self.expenses) + 1
        else:
            self.next_id = 1
    
    def add_expense(self):
        print("\n--- Add New Expense ---")
        
        try:
            while True:
                try:
                    amount = float(input("Enter amount spent: ₹"))
                    if amount <= 0:
                        print("Amount must be positive. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            
            category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip()
            if not category:
                category = "Uncategorized"
            
            description = input("Enter description: ").strip()
            if not description:
                description = "No description"
            
            date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if date_input:
                try:
                    date = datetime.strptime(date_input, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Using today's date.")
                    date = datetime.now()
            else:
                date = datetime.now()
            
            expense = Expense(
                expense_id=self.next_id,
                amount=amount,
                date=date,
                category=category,
                description=description
            )
            
            self.expenses.append(expense)
            self.next_id += 1
            self.storage.save_expenses(self.expenses)
            
            print(f"\n✓ Expense added successfully! (ID: {expense.id})")
        
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"\n✗ Error adding expense: {e}")
            logger.error(f"Error in add_expense: {e}")
    
    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        
        print("\n" + "=" * 60)
        print(f"{'YOUR EXPENSES':^60}")
        print("=" * 60)
        
        sorted_expenses = sorted(self.expenses, key=lambda x: x.date, reverse=True)
        
        for exp in sorted_expenses:
            print(exp)
        
        print("=" * 60)
        print(f"Total: ₹{sum(exp.amount for exp in self.expenses):.2f}")
        print()
    
    def delete_expense(self):
        if not self.expenses:
            print("\nNo expenses to delete.")
            return
        
        print("\n--- Delete Expense ---")
        
        print("\nCurrent expenses:")
        for exp in sorted(self.expenses, key=lambda x: x.id):
            print(f"  ID {exp.id}: ₹{exp.amount:.2f} - {exp.category} - {exp.description}")
        
        try:
            delete_id = int(input("\nEnter Expense ID to delete (0 to cancel): "))
            
            if delete_id == 0:
                print("Deletion cancelled.")
                return
            
            for exp in self.expenses:
                if exp.id == delete_id:
                    confirm = input(f"Delete expense: {exp}? (y/n): ").lower()
                    if confirm == 'y':
                        self.expenses.remove(exp)
                        self.storage.save_expenses(self.expenses)
                        print("\n✓ Expense deleted successfully!")
                    else:
                        print("Deletion cancelled.")
                    return
            
            print(f"\n✗ Expense ID {delete_id} not found.")
        
        except ValueError:
            print("\n✗ Invalid ID. Please enter a number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"\n✗ Error deleting expense: {e}")
            logger.error(f"Error in delete_expense: {e}")
    
    def update_expense(self):
        if not self.expenses:
            print("\nNo expenses to update.")
            return
        
        print("\n--- Update Expense ---")
        
        print("\nCurrent expenses:")
        for exp in sorted(self.expenses, key=lambda x: x.id):
            print(f"  ID {exp.id}: ₹{exp.amount:.2f} - {exp.category} - {exp.description}")
        
        try:
            update_id = int(input("\nEnter Expense ID to update (0 to cancel): "))
            
            if update_id == 0:
                print("Update cancelled.")
                return
            
            expense_to_update = None
            for exp in self.expenses:
                if exp.id == update_id:
                    expense_to_update = exp
                    break
            
            if not expense_to_update:
                print(f"\n✗ Expense ID {update_id} not found.")
                return
            
            print(f"\nCurrent expense: {expense_to_update}")
            print("\nLeave field blank to keep current value.")
            
            amount_input = input(f"New amount (current: ₹{expense_to_update.amount:.2f}): ").strip()
            if amount_input:
                try:
                    new_amount = float(amount_input)
                    if new_amount > 0:
                        expense_to_update.amount = new_amount
                except ValueError:
                    print("Invalid amount, keeping current value.")
            
            category_input = input(f"New category (current: {expense_to_update.category}): ").strip()
            if category_input:
                expense_to_update.category = category_input
            
            description_input = input(f"New description (current: {expense_to_update.description}): ").strip()
            if description_input:
                expense_to_update.description = description_input
            
            self.storage.save_expenses(self.expenses)
            print("\n✓ Expense updated successfully!")
            print(f"Updated expense: {expense_to_update}")
        
        except ValueError:
            print("\n✗ Invalid ID. Please enter a number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"\n✗ Error updating expense: {e}")
            logger.error(f"Error in update_expense: {e}")
    
    def search_expenses(self):
        """Search expenses by category or description."""
        if not self.expenses:
            print("\nNo expenses to search.")
            return
        
        print("\n--- Search Expenses ---")
        search_term = input("Enter search term (category or description): ").strip().lower()
        
        if not search_term:
            print("Search cancelled.")
            return
        
        results = [
            exp for exp in self.expenses
            if search_term in exp.category.lower() or search_term in exp.description.lower()
        ]
        
        if not results:
            print(f"\nNo expenses found matching '{search_term}'.")
            return
        
        print(f"\n--- Search Results ({len(results)} found) ---")
        for exp in sorted(results, key=lambda x: x.date, reverse=True):
            print(exp)
        
        total = sum(exp.amount for exp in results)
        print(f"\nTotal for search results: ₹{total:.2f}")
    
    def generate_report(self):
        """Generate and display expense reports."""
        if not self.expenses:
            print("\nNo expenses to report.")
            return
        
        print("\n--- Expense Reports ---")
        print("1. Summary Report")
        print("2. Category Report")
        print("3. Monthly Report")
        print("4. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        report = Report(self.expenses)
        
        if choice == "1":
            report.print_summary()
        
        elif choice == "2":
            categories = set(exp.category for exp in self.expenses)
            print("\nAvailable categories:")
            for cat in sorted(categories):
                print(f"  - {cat}")
            category = input("\nEnter category name: ").strip()
            report.print_category_report(category)
        
        elif choice == "3":
            print("\n--- Monthly Breakdown ---")
            month_totals = report.expenses_by_month()
            for month, total in sorted(month_totals.items()):
                print(f"{month}: ₹{total:.2f}")
        
        elif choice == "4":
            return
        
        else:
            print("Invalid choice.")
    
    def menu(self):
        print("\n" + "=" * 50)
        print("EXPENSE TRACKER".center(50))
        print("=" * 50)
        
        while True:
            print("\n--- Main Menu ---")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Update Expense")
            print("4. Delete Expense")
            print("5. Search Expenses")
            print("6. Generate Reports")
            print("7. Exit")
            
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == "1":
                self.add_expense()
            
            elif choice == "2":
                self.view_expenses()
            
            elif choice == "3":
                self.update_expense()
            
            elif choice == "4":
                self.delete_expense()
            
            elif choice == "5":
                self.search_expenses()
            
            elif choice == "6":
                self.generate_report()
            
            elif choice == "7":
                print("\nThank you for using Expense Tracker!")
                print("Your expenses have been saved.")
                break
            
            else:
                print("\n✗ Invalid choice. Please enter a number between 1 and 7.")