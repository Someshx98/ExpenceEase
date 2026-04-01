from expense import Expense
import csv
import os
from datetime import datetime
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Storage:
    
    def __init__(self, filename: str = "expenses.csv"):
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        if not os.path.exists(self.filename):
            try:
                with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Amount", "Date", "Category", "Description"])
                logger.info(f"Created new expense file: {self.filename}")
            except IOError as e:
                logger.error(f"Failed to create file: {e}")
                raise
    
    def load_expenses(self) -> List[Expense]:
        expenses = []
        
        if not os.path.exists(self.filename):
            logger.warning(f"File {self.filename} does not exist")
            return expenses
        
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)

                try:
                    next(reader)
                except StopIteration:
                    logger.info("Empty expense file")
                    return expenses
                
                # Read expenses
                for line_num, row in enumerate(reader, start=2):
                    try:
                        if len(row) != 5:
                            logger.warning(f"Line {line_num}: Invalid row length, skipping")
                            continue
                        
                        expense = Expense(
                            expense_id=int(row[0]),
                            amount=float(row[1]),
                            date=datetime.strptime(row[2], '%Y-%m-%d'),
                            category=row[3],
                            description=row[4]
                        )
                        expenses.append(expense)
                    
                    except (ValueError, IndexError) as e:
                        logger.warning(f"Line {line_num}: Error parsing expense - {e}")
                        continue
            
            logger.info(f"Loaded {len(expenses)} expenses from {self.filename}")
            return expenses
        
        except IOError as e:
            logger.error(f"Failed to read file: {e}")
            raise
    
    def save_expenses(self, expenses: List[Expense]):
        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                # Write header
                writer.writerow(["ID", "Amount", "Date", "Category", "Description"])
                
                # Write expenses
                for exp in expenses:
                    writer.writerow([
                        exp.id,
                        f"{exp.amount:.2f}",
                        exp.date.strftime('%Y-%m-%d'),
                        exp.category,
                        exp.description
                    ])
            
            logger.info(f"Saved {len(expenses)} expenses to {self.filename}")
        
        except IOError as e:
            logger.error(f"Failed to save expenses: {e}")
            raise
    
    def backup_file(self, backup_path: str = None):
        if not os.path.exists(self.filename):
            logger.warning("No file to backup")
            return
        
        if backup_path is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = f"{self.filename}.backup_{timestamp}"
        
        try:
            import shutil
            shutil.copy2(self.filename, backup_path)
            logger.info(f"Backup created: {backup_path}")
        except IOError as e:
            logger.error(f"Failed to create backup: {e}")
            raise