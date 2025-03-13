# MovyTech Machine Test

## Overview

This project is a Django-based application developed as part of a machine test for MovyTech.

## Prerequisites

- Python 3.x
- pip
- Virtualenv (recommended)

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nightcoder95/Machine-Test-MovyTech.git
   cd Machine-Test-MovyTech

2. **Create a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate.bat`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create a SuperUser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   - Open your browser and go to: `http://127.0.0.1:8000/bills`
   - Admin panel: `http://127.0.0.1:8000/admin/`

