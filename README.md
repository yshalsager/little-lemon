# Little Lemon Restaurant API

This project is an API built using Django REST Framework for the Little Lemon restaurant. The API handles table bookings and menu items for the restaurant.

The project is built as part of the [Back-End Developer Capstone](https://www.coursera.org/learn/back-end-developer-capstone/) course on Coursera.

## Installation

To run this project, you will need to have Python 3 and MySQL installed on your machine. You can then follow these steps:

1. Clone the repository to your local machine using `git clone`.
2. Install pipenv using pip: `pip install pipenv`.
3. Run `pipenv install` to create a virtual environment and install the required packages.
4. Create a MySQL database and update the `DATABASES` setting in `settings.py` with your database details.
5. Run the migrations using `python manage.py migrate`.
6. Start the development server using `python manage.py runserver`.

## Usage

The API has the following endpoints:

- `/auth/users/`: User registration API
- `/api-token-auth/`: Token authorization API
- `/restaurant/menu/`: Menu items API
- `/restaurant/booking/tables/`: Table booking API

The API supports HTTP requests such as GET, POST, PUT and DELETE. The data is stored in a MySQL database using Django models.

## Testing

The API can be tested using the Insomnia REST client. Unit tests are also included in the project.

## Peer Review

This project will be peer reviewed by two of your peers in the course. The grading criteria include:

- Use of Django to serve static HTML content
- Committing the project to a Git repository
- Connecting the backend to a MySQL database
- Implementation of the menu and table booking APIs
- User registration and authentication
- Unit tests
- Ability to test the API using the Insomnia REST client.
