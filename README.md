# 🗣 Django Contact Form

A lightweight and robust Django application designed for handling user inquiries through a feedback form with a clean Bootstrap-based administrative dashboard.

## ✨ Features

* **Feedback Form:** User-friendly interface for submitting contact requests.
* **Data Management:** A structured Bootstrap table to view and manage records.
* **Validation:** Server-side form validation using Django Forms.
* **Clean UI:** Styled with Bootstrap 5 for a modern look and feel.

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/PolitexProg/django-mohirdev-task-form.git
cd django-mohirdev-task-form

```

### 2. Set up the environment

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

```

### 3. Database setup

```bash
python manage.py migrate

```

### 4. Run the development server

```bash
python manage.py runserver

```

Open [http://127.0.0.1:8000](https://www.google.com/search?q=http://127.0.0.1:8000) in your browser to see the application.

## 🛠 Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, Bootstrap 5
* **Database:** SQLite (default for development)
