# Task Management RESTful API

This project implements a RESTful API for task management using Django REST framework. Users can create, update, and delete tasks, set task priorities, due dates, and reminders. User authentication and authorization have been implemented to ensure secure access to tasks.

## Features

- User Registration and Authentication
- Create, Read, Update, and Delete Tasks
- Task Prioritization
- Due Dates 
- Permission System: Users can only view, update, and delete their own tasks

## Technologies Used

- Django
- Django REST Framework
- SQLite (or your chosen database)
  

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AsmaaMHadir/Django-Resftul-Tasks-API.git
cd project-directory
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the project dependencies:
   
```bash

pip install django djangorestframework

```

4. Apply migrations and create a superuser:

```bash

python manage.py migrate
python manage.py createsuperuser

```

5. Run the development server:
   
```bash
python manage.py runserver
```

# Usage
Register a new user through the registration endpoint.
login with your newly created user on the login endpoint and start creating tasks and assigning them a priority level. Tasks will be displayed according to the priority level through an internal numerical mapping.

# Contributing
Contributions are welcome! Feel free to submit issues and pull requests.


# Contact
For any inquiries, please contact asmaahadir11@gmail.com.







