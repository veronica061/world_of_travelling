# Use the official Python image from the Docker Hub
FROM python:3.10-alpine

# Set environment variables to prevent Python from writing pyc files and to ensure that Python will output things in UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app/src

# Install system dependencies
RUN apk add --no-cache --virtual \
    build-essential \
    libpq-dev \
    && rm -rf /var/cache/apk/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    Django==5.1 \
    channels==4.0.0 \
    django-redis \
    django-redis-sessions

RUN pip install --no-cache-dir requests

RUN pip install --no-cache-dir daphne==4.0.0 

# # Copy the rest of the application code into the container
# COPY src/ . 
# # Expose the port the app runs on
# EXPOSE 8000

# RUN python manage.py makemigrations
# RUN python manage.py migrate

# # Command to run the application
# CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "my_site.asgi:application"]
