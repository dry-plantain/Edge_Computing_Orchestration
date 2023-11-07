# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy your application files into the container
COPY . /app

# Install dependencies (Flask, Pillow, etc.)
COPY requirements.txt /app
RUN pip install -r requirements.txt  # If you have a requirements file

# Expose the port your Flask app will run on
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python", "imageProcessing1.py"]
