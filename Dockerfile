# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run migrations and then start the application
RUN python inventory/manage.py makemigrations
RUN python inventory/manage.py migrate

# Set the working directory to the Django project directory
WORKDIR /inventory

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
