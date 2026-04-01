"""Expense model class for tracking individual expenses."""
from datetime import datetime
from typing import Optional


class Expense:
    
    def __init__(
        self,
        expense_id: int,
        amount: float,
        date: datetime,
        category: str,
        description: str
    ):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        self.id = expense_id
        self.amount = amount
        self.date = date
        self.category = category.strip()
        self.description = description.strip()
    
    def __str__(self) -> str:
        return (
            f"ID: {self.id} | "
            f"Amount: ₹{self.amount:.2f} | "
            f"Date: {self.date.strftime('%Y-%m-%d')} | "
            f"Category: {self.category} | "
            f"Description: {self.description}"
        )
    
    def __repr__(self) -> str:
        return (
            f"Expense(id={self.id}, amount={self.amount}, "
            f"date={self.date}, category='{self.category}', "
            f"description='{self.description}')"
        )
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'amount': self.amount,
            'date': self.date.strftime('%Y-%m-%d'),
            'category': self.category,
            'description': self.description
        }