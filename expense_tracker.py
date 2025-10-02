import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class ExpenseTracker:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        description TEXT
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_expense(self, amount, category, description=""):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        query = "INSERT INTO EXPENSES (amount, category, date, description) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (amount, category, date, description))
        self.conn.commit()

    def get_expenses(self):
        return pd.read_sql_query("SELECT * FROM EXPENSES", self.conn)

    def export_to_csv(self, filename="expenses.csv"):
        df = self.get_expenses()
        df.to_csv(filename, index=False)
        print(f"Data exported to {filename}")

    def plot_expenses_by_category(self):
        df = self.get_expenses()
        if df.empty:
            print("No expenses yet.")
            return
        df.groupby("category")["amount"].sum().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Expenses by category")
        plt.show()