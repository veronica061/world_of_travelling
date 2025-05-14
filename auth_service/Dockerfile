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

