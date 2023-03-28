# Family Tree Project

This is a family tree project created with Python, Django Rest Framework, and Postgresql database. The project allows users to apply their family members and access information related to their family tree.

## Requirements

To run this project, you'll need the following:

- Python 3.8 or later
- Django 3.1 or later
- Django Rest Framework 3.12 or later
- Postgresql 12 or later

## Installation

1. Clone the repository to your local machine:


https://github.com/mohamedsamiromar/family-tree/

2. Create a virtual environment and activate it:

python3 -m venv env
source env/bin/activate


3. Install the project requirements:

pip install -r requirements.txt


4. Create a database in Postgresql and update the database settings in `family_tree/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': 'your_database_port',
    }
}


5. Run database migrations:
python manage.py migrate

6. Create a superuser:
python manage.py createsuperuser


7. Start the development server:
python manage.py runserver



Usage
Once you have the project up and running, you can access the API by visiting http://localhost:8000/api/ in your web browser. You can use the API to apply family members and access information related to your family tree.

Authentication
Some API endpoints require authentication. To authenticate, you can use the Django Rest Framework's built-in token authentication. To get an authentication token, you'll need to log in to the Django admin panel and create a token for your user.

1. Log in to the Django admin panel at http://localhost:8000/admin/.
2. Click on the "Tokens" link under the "Authentication and Authorization" section.
3. Click on the "Add token" button.
4. Select your user from the dropdown list.
5. Click on the "Save" button.
6. Copy the token that is displayed.
You can now use this token to authenticate with the API by including it in the Authorization header of your API requests:
Authorization: Token YOUR_TOKEN_HERE


Endpoints
The following API endpoints are available:

GET /api/persons/
Returns a list of all persons in the family tree.

POST /api/persons/
Adds a new person to the family tree.

Request Body
{
    "name": "John Smith",
    "gender": "male",
    "father": null,
    "mother": null,
    "spouse": null,
    "children": []
}


. name (required): The name of the person.
. gender (required): The gender of the person (male or female).
. father: The ID of the person's father (if known).
. mother: The ID of the person's mother (if known).
. spouse: The ID of the person's spouse (if known).
. children: A list of IDs of the person's children (if any).
. GET /api/persons/{person_id}/
. Returns information about a specific person in the family tree.

PUT /api/persons/{person


We welcome any developer who wants to contribute to the Family Tree Project! Here are some ways you can help:

. Add new features to the project.
. Improve the existing codebase.
. Fix bugs and issues reported by users.
. Write tests to improve the project's reliability.
. Improve the project's documentation.
. To get started, you can fork the project and make your changes. Once you've made your changes, create a pull request and we'll review your changes.

Before submitting your pull request, make sure your code follows our coding standards and has been thoroughly tested. We appreciate all contributions to the project and look forward to working with you!



