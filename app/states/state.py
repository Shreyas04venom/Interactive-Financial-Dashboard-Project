import reflex as rx
from typing import TypedDict


class NetWorthData(TypedDict):
    month: str
    value: int


class PortfolioData(TypedDict):
    name: str
    value: float


class TransactionData(TypedDict):
    date: str
    description: str
    amount: float
    type: str


class State(rx.State):
    """The main state for the financial dashboard app."""

    net_worth_data: list[NetWorthData] = [
        {"month": "Jan", "value": 100000},
        {"month": "Feb", "value": 105000},
        {"month": "Mar", "value": 110000},
        {"month": "Apr", "value": 112000},
        {"month": "May", "value": 118000},
        {"month": "Jun", "value": 125000},
    ]
    portfolio_data: list[PortfolioData] = [
        {"name": "Stocks", "value": 50000},
        {"name": "Bonds", "value": 25000},
        {"name": "Real Estate", "value": 35000},
        {"name": "Cash", "value": 15000},
    ]
    transactions_data: list[TransactionData] = [
        {
            "date": "2024-07-01",
            "description": "Salary Deposit",
            "amount": 5000,
            "type": "income",
        },
        {
            "date": "2024-07-02",
            "description": "Groceries",
            "amount": -150,
            "type": "expense",
        },
        {
            "date": "2024-07-03",
            "description": "Stock Purchase (AAPL)",
            "amount": -1000,
            "type": "investment",
        },
        {
            "date": "2024-07-05",
            "description": "Rent",
            "amount": -2000,
            "type": "expense",
        },
        {
            "date": "2024-07-10",
            "description": "Dividend Income",
            "amount": 200,
            "type": "income",
        },
    ]