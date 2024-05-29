# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

ENV FLASK_APP=api/api.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run api.py when the container launches
CMD ["flask", "run"]
