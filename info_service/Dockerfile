# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables to prevent Python from writing pyc files and to ensure that Python will output things in UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app/src

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    Django==5.1 \
    channels==4.0.0 \
    django-redis \
    django-redis-sessions 

RUN pip install --no-cache-dir requests

# # Copy the rest of the application code into the container
# COPY src/ . 
# # Expose the port the app runs on
# EXPOSE 8002

# # Command to run the application
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8002"]