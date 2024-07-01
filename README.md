# Litestar HTMX MongoDB Example Application

This is a simple CRUD application built with Litestar, HTMX, and MongoDB. It demonstrates how to create a web application with server-side rendering and dynamic updates using HTMX.

## Features

- List, create, read, update, and delete items
- Server-side rendering with Jinja2 templates
- Dynamic updates with HTMX
- MongoDB integration for data persistence

## Prerequisites

- Python 3.7+
- Docker and Docker Compose (for running MongoDB)

## Setup

1. Clone the repository:

git clone https://github.com/yourusername/litestar-htmx-mongodb-example.git
cd litestar-htmx-mongodb-example

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. Install the required packages:

pip install litestar pymongo motor uvicorn

4. Start MongoDB using Docker Compose:

docker-compose up -d

This will start a MongoDB instance using the configuration specified in the `docker-compose.yml` file.

## Running the Application

1. Start the Litestar server using Uvicorn:

uvicorn app.main:app --reload

2. Open your web browser and navigate to `http://localhost:8000`

## Project Structure

- `app/main.py`: Main application file with route handlers and Litestar configuration
- `app/database.py`: MongoDB connection and helper functions
- `app/models.py`: Pydantic models for data validation
- `app/templates/`: Jinja2 templates for HTML rendering
- `static/`: Static files (CSS, JS, etc.)
- `docker-compose.yml`: Docker Compose configuration for MongoDB

## Contributing

Feel free to submit issues or pull requests if you have any improvements or find any bugs.

## License

This project is open-source and available under the MIT License.
