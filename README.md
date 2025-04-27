# Hello World Django App

This is a simple Django web application that responds with:

- JSON Message: {"Message": "Hello World!"}
- (Optional) HTML page showing "Hello World!" in bold.

## How to Run the App

1. Create a virtual environment (if not already created):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install Django:
    ```bash
    pip install django
    ```

3. Start the Django server:
    ```bash
    python3 manage.py runserver
    ```

4. Access the application in your browser:

- JSON response: [http://127.0.0.1:8000/json/](http://127.0.0.1:8000/json/)
- HTML page: [http://127.0.0.1:8000/html/](http://127.0.0.1:8000/html/)

## Project Structure

- `helloworldproject/` — Main Django project settings
- `helloapp/` — Django app with views for JSON and HTML
- `manage.py` — Django management script

## Notes

- Make sure the server is running (`python3 manage.py runserver`).
- Keep the terminal open while testing.
- Don't use for production; this is for learning/demo purposes only.

---


