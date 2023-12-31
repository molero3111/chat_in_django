# Room-Based Chat App

Welcome to the Room-Based Chat App! This web application allows users to join chat rooms and engage in real-time
conversations with others.

## Features

- Join chat rooms.
- Real-time messaging using WebSocket connections.

## Technologies Used

- **Django**: The web framework for the backend.
- **Channels**: Extends Django to handle WebSocket connections and real-time events.
- **Daphne**: An ASGI (Asynchronous Server Gateway Interface) server for serving Django Channels applications.
- **Bootstrap**: Used for styling the frontend.
- **SQLite**: The database for storing user data and chat messages.

## Getting Started

To run this project locally, follow these steps:

## 1. Clone this repository to your local machine:

    git clone https://github.com/molero3111/chat_in_django.git
    cd chat_in_django

## 2. Create environment.py in djangochat app from environment.example.py file

## 3. Create environment

## 3.1 Using venv

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt

## 3.2 Using conda

    conda env create -f environment.yml
    conda activate chat_in_django_env

## 4. Apply database migrations

    python manage.py migrate

## 5. Load room fixtures

    python manage.py loaddata fixtures/rooms_fixture.json
    # NOTE: In case you get error that room table is not found, 
    # execute 'python manage.py makemigrations room' command, then
    # 'python manage.py migrate' again.

## 6. Run local server

    python manage.py runserver

## Usage

    Create an account or log in if you already have one.
    Browse available chat rooms and join the ones that interest you.
    Start chatting with other users in real-time.




