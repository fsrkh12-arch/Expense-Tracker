# Expense Tracker Application

## Overview
A Flask-based expense tracking web application with user authentication. Users can register, log in, and track their expenses.

## Project Structure
- `app.py` - Main Flask application with routes for authentication and dashboard
- `templates/` - Jinja2 HTML templates
  - `layout.html` - Base template
  - `index.html` - Dashboard page
  - `login.html` - Login page
  - `register.html` - Registration page
- `static/` - Static assets (CSS, JavaScript)
  - `styles.css` - Application styles
  - `script.js` - Client-side JavaScript
- `expenses.db` - SQLite database for user data and expenses

## Technology Stack
- Python 3.11
- Flask (web framework)
- Flask-Session (server-side sessions)
- CS50 SQL library (database access)
- SQLite (database)
- Werkzeug (password hashing)

## Running the Application
The application runs on port 5000 using the Flask development server:
```bash
python app.py
```

## Database
Uses SQLite with a `users` table containing:
- `id` - User ID
- `username` - Unique username
- `hash` - Password hash

## Features
- User registration with password confirmation
- User login with session management
- User logout
- Protected routes requiring authentication
