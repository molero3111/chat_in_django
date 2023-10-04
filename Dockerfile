# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=djangochat.settings

# Set the working directory in the container
WORKDIR /chat_in_django


# Copy the current directory contents into the container at /chat_in_django
COPY . /chat_in_django

# Install needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose a port for the Django development server
EXPOSE 8000

#  run application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
