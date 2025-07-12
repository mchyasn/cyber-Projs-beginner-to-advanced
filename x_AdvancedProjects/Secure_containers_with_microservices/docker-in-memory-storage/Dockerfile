# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Ensure the directory exists
RUN mkdir -p /app/tmp

# Run the application and keep the container running
CMD ["sh", "-c", "python3 microservice.py && tail -f /dev/null"]
