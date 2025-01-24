
# Prerequisites to Run the Project

Before running this project, ensure you have the following installed and configured on your system:

## 1. Python

- Python **3.8+** is required.
- [Download Python](https://www.python.org/downloads/) and ensure it’s added to your PATH.

Verify the Python version:

```bash
python --version
```

## 2. Virtual Environment

Create and activate a virtual environment to manage dependencies.

- **macOS/Linux**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows (Command Prompt)**:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **Windows (PowerShell)**:

  ```bash
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

## 3. Install Dependencies

After activating the virtual environment, install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 4. Database Setup

- This project uses **SQLite** by default (no additional setup required).
- If you're using a different database (e.g., PostgreSQL), ensure the database is set up and accessible. Update the database settings in the `settings.py` file.

## 5. Apply Migrations

Run the following commands to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Static Files (Optional)

Collect static files (if applicable):

```bash
python manage.py collectstatic
```

## 7. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

---

If you encounter any issues or need further assistance, feel free to reach out.
