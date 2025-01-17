# Budget Tracker Application

## Overview
The Budget Tracker is a Flask-based web application that helps users track their expenses. It allows users to add, update, view, and delete expense records while maintaining a summary of their total spending.

---

## Features
- **Add Expense**: Record new expenses with details like category, description, amount, and date.
- **View Expenses**: Display a list of all recorded expenses with the total amount spent.
- **Update Expense**: Modify existing expense details.
- **Delete Expense**: Remove an expense from the tracker.

---

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (via SQLAlchemy ORM)

---

## Setup and Installation
### Prerequisites
- Python 3.x

### Project Structure

project/
│
├── budget.py                 # Main application file
├── dbcreate.py               # Script to initialize the database
├── templates/
│   ├── bdtracker/
│       ├── add_expense.html  # Form to add a new expense
│       ├── index.html        # Homepage displaying expenses
│       ├── update_expense.html # Form to update an expense
│
├── static/
│   ├── bdadd.css             # Styles for Add Expense page
│   ├── bdindex.css           # Styles for Index page
│   ├── bdupdate.css          # Styles for Update Expense page
│
└── tracker.db                # SQLite database file (auto-generated)
