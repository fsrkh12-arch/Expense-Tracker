# Expense Tracker

I built Expense Tracker as a follow-up to my CS50 project, expanding it as a simple personal tool for understanding my income and spending over time. I made it for fun, and using it helped me see more clearly where my money was going. A few friends also tested the tool for me.

The repository contains a Flask application and a separate browser-only demo. Their features and storage differ, as described below.

## Try it

[Open the browser demo](https://fsrkh12-arch.github.io/Expense-Tracker/)

The demo stores expenses and budgets in the current browser. It does not use the Flask application's accounts or database, and its data does not sync across devices.

## Flask application

The Flask version supports registration and login, adding and deleting expenses, setting a monthly budget, and viewing totals and a monthly average. Expenses are associated with the signed-in user; passwords are hashed with Werkzeug. The backend uses SQLite through the CS50 SQL library and Flask-Session for sessions. The repository currently includes the database file the app uses.

To run it locally, install Python and run these commands from the repository directory:

```sh
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app run
```

Open the address printed by Flask. The app is a learning project: its direct Python entry point enables debug mode, and it should not be treated as a production finance service without further security and deployment work.
