# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=djangochat.settings

# install system dependencies
RUN apt-get update
RUN apt-get -y install libgdal-dev g++ --no-install-recommends

# Set the working directory in the container
WORKDIR /chat_in_django

# Copy the current directory contents into the container at /chat_in_django
COPY . /chat_in_django

# Install needed packages specified in requirements.txt
RUN pip install -r requirements.txt