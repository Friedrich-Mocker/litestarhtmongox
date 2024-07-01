# 🚀 Litestar HTMX MongoDB Example Application

Welcome to this exciting example of a modern web application built with cutting-edge technologies! This project showcases a simple yet powerful CRUD application that leverages the strengths of Litestar, HTMX, and MongoDB.

## ✨ Features

- 📋 List, create, read, update, and delete items with ease
- 🖥️ Server-side rendering with Jinja2 templates for blazing-fast initial loads
- ⚡ Dynamic updates powered by HTMX for a smooth user experience
- 🗄️ MongoDB integration for robust and scalable data persistence

## 🛠️ Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.7+
- Docker and Docker Compose (for running MongoDB)

## 🚀 Setup

Follow these steps to get your development environment ready:

1. Clone the repository:

```
git clone https://github.com/yourusername/litestar-htmx-mongodb-example.git
cd litestar-htmx-mongodb-example
```

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```
pip install litestar pymongo motor uvicorn
```

4. Start MongoDB using Docker Compose:

```
docker-compose up -d
```

This will launch a MongoDB instance using the configuration in the `docker-compose.yml` file.

## 🏃‍♂️ Running the Application

1. Start the Litestar server using Uvicorn:

```
uvicorn app.main:app --reload
```

2. Open your web browser and navigate to `http://localhost:8000`

## 📁 Project Structure

Our project is organized as follows:

- `app/main.py`: Main application file with route handlers and Litestar configuration
- `app/database.py`: MongoDB connection and helper functions
- `app/models.py`: Pydantic models for data validation
- `app/templates/`: Jinja2 templates for HTML rendering
- `static/`: Static files (CSS, JS, etc.)
- `docker-compose.yml`: Docker Compose configuration for MongoDB

## 🤝 Contributing

We welcome contributions! Feel free to submit issues or pull requests if you have any improvements or find any bugs. Let's make this project even better together!

## 📄 License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you see fit!

---

Happy coding! 🎉 If you have any questions or need further assistance, don't hesitate to reach out.
