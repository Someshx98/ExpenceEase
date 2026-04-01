# Expense Tracker

A command-line expense tracking application built with Python. Track your spending, categorize expenses, and generate insightful reports.

## Features

- ✅ **Add Expenses**: Record expenses with amount, category, description, and date
- 📊 **View Expenses**: Display all expenses sorted by date
- ✏️ **Update Expenses**: Modify existing expense entries
- 🗑️ **Delete Expenses**: Remove unwanted expense records
- 🔍 **Search**: Find expenses by category or description
- 📈 **Reports**: Generate comprehensive spending reports
  - Summary report with totals and averages
  - Category-wise breakdown with percentages
  - Monthly spending trends
  - Top expenses analysis

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup
1. Clone or download this repository
2. Navigate to the project directory
3. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Running the Application
```bash
python main.py
```

### Main Menu Options

1. **Add Expense**
   - Enter the amount spent
   - Specify a category (e.g., Food, Transport, Entertainment)
   - Add a description
   - Optionally set a custom date (defaults to today)

2. **View All Expenses**
   - Displays all recorded expenses sorted by date
   - Shows total spending

3. **Update Expense**
   - Select an expense by ID
   - Update amount, category, or description
   - Leave fields blank to keep current values

4. **Delete Expense**
   - Select an expense by ID
   - Confirm deletion
   - Expense is permanently removed

5. **Search Expenses**
   - Search by category or description keywords
   - View matching expenses and their total

6. **Generate Reports**
   - **Summary Report**: Overall statistics, category breakdown, monthly trends, and top expenses
   - **Category Report**: Detailed analysis of a specific category
   - **Monthly Report**: Month-by-month spending breakdown

7. **Exit**
   - Safely close the application
   - All data is automatically saved

## File Structure

```
expense-tracker/
│
├── main.py           # Application entry point
├── tracker.py        # Main ExpenseTracker class
├── expense.py        # Expense model class
├── storage.py        # File storage management
├── report.py         # Report generation
├── expenses.csv      # Data file (auto-generated)
└── expense_tracker.log  # Log file (auto-generated)
```

## Data Storage

- Expenses are stored in `expenses.csv` in the same directory
- CSV format ensures easy backup and portability
- Data persists between sessions
- Automatic file creation on first run

## Example Usage

```
--- Main Menu ---
1. Add Expense
2. View All Expenses
3. Update Expense
4. Delete Expense
5. Search Expenses
6. Generate Reports
7. Exit

Enter your choice (1-7): 1

--- Add New Expense ---
Enter amount spent: ₹500
Enter category (e.g., Food, Transport, Entertainment): Food
Enter description: Lunch at restaurant
Enter date (YYYY-MM-DD) or press Enter for today: 

✓ Expense added successfully! (ID: 1)
```

## Report Example

```
==================================================
EXPENSE SUMMARY REPORT
==================================================

Total Expenses: ₹15,450.00
Number of Transactions: 23
Average Expense: ₹671.74

--- Expenses by Category ---
Food                : ₹  5,200.00 ( 33.7%)
Transport           : ₹  4,100.00 ( 26.5%)
Entertainment       : ₹  3,150.00 ( 20.4%)
Bills               : ₹  3,000.00 ( 19.4%)

--- Top 5 Expenses ---
1. ₹2,500.00 - Bills - Electricity bill
2. ₹1,800.00 - Entertainment - Concert tickets
3. ₹1,200.00 - Food - Grocery shopping
```

## Error Handling

- Input validation for amounts (must be positive numbers)
- Date format validation
- File I/O error handling
- Graceful handling of corrupted data
- Logging of errors to `expense_tracker.log`

## Key Improvements from Original Code

### Code Quality
- ✅ Fixed typo: `Expence` → `Expense`
- ✅ Added type hints for better code clarity
- ✅ Comprehensive error handling
- ✅ Logging system for debugging
- ✅ Proper class documentation

### Functionality
- ✅ Added update expense feature
- ✅ Added search functionality
- ✅ Comprehensive reporting system
- ✅ Category and monthly analysis
- ✅ Date validation and custom date input
- ✅ Confirmation prompts for deletions

### User Experience
- ✅ Better formatted output
- ✅ Input validation with helpful error messages
- ✅ Visual separators and emojis
- ✅ Sorted displays (by date, amount, etc.)
- ✅ More intuitive menu system

### Data Integrity
- ✅ UTF-8 encoding support
- ✅ Automatic file creation
- ✅ Better CSV parsing with error recovery
- ✅ ID synchronization on load
- ✅ Backup capability

## Future Enhancements

Potential features for future versions:
- Budget tracking and alerts
- Export to PDF/Excel
- Data visualization (charts/graphs)
- Multiple currency support
- Recurring expenses
- Tags/labels for expenses
- Data import from bank statements
- Mobile app companion

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the project repository.

---

**Happy Tracking! 💰**