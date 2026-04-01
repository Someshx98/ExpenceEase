from expense import Expense
from typing import List, Dict
from datetime import datetime, timedelta
from collections import defaultdict


class Report:
    
    def __init__(self, expenses: List[Expense]):
        self.expenses = expenses
    
    def total_expenses(self) -> float:
        return sum(exp.amount for exp in self.expenses)
    
    def expenses_by_category(self) -> Dict[str, float]:
        category_totals = defaultdict(float)
        for exp in self.expenses:
            category_totals[exp.category] += exp.amount
        return dict(category_totals)
    
    def expenses_by_month(self) -> Dict[str, float]:
        month_totals = defaultdict(float)
        for exp in self.expenses:
            month_key = exp.date.strftime('%Y-%m')
            month_totals[month_key] += exp.amount
        return dict(month_totals)
    
    def expenses_in_date_range(self, start_date: datetime, end_date: datetime) -> List[Expense]:
        return [
            exp for exp in self.expenses
            if start_date <= exp.date <= end_date
        ]
    
    def top_expenses(self, n: int = 5) -> List[Expense]:
        return sorted(self.expenses, key=lambda x: x.amount, reverse=True)[:n]
    
    def average_expense(self) -> float:
        if not self.expenses:
            return 0.0
        return self.total_expenses() / len(self.expenses)
    
    def print_summary(self):
        if not self.expenses:
            print("\nNo expenses to report.")
            return
        
        print("\n" + "=" * 50)
        print("EXPENSE SUMMARY REPORT")
        print("=" * 50)
        
        print(f"\nTotal Expenses: ₹{self.total_expenses():.2f}")
        print(f"Number of Transactions: {len(self.expenses)}")
        print(f"Average Expense: ₹{self.average_expense():.2f}")
        
        print("\n--- Expenses by Category ---")
        category_totals = self.expenses_by_category()
        for category, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (total / self.total_expenses()) * 100
            print(f"{category:20s}: ₹{total:10.2f} ({percentage:5.1f}%)")
        
        print("\n--- Expenses by Month ---")
        month_totals = self.expenses_by_month()
        for month, total in sorted(month_totals.items()):
            print(f"{month}: ₹{total:.2f}")
        
        # Top expenses
        print("\n--- Top 5 Expenses ---")
        for i, exp in enumerate(self.top_expenses(5), 1):
            print(f"{i}. ₹{exp.amount:.2f} - {exp.category} - {exp.description}")
        
        print("\n" + "=" * 50)
    
    def print_category_report(self, category: str):
        category_expenses = [exp for exp in self.expenses if exp.category == category]
        
        if not category_expenses:
            print(f"\nNo expenses found for category: {category}")
            return
        
        print(f"\n--- {category} Expenses ---")
        total = sum(exp.amount for exp in category_expenses)
        print(f"Total: ₹{total:.2f}")
        print(f"Count: {len(category_expenses)}")
        print(f"Average: ₹{total/len(category_expenses):.2f}")
        print("\nTransactions:")
        for exp in sorted(category_expenses, key=lambda x: x.date):
            print(f"  {exp.date.strftime('%Y-%m-%d')}: ₹{exp.amount:.2f} - {exp.description}")