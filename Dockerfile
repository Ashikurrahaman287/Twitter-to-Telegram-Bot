# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
C:\Users\Ashik\PycharmProjects\tweetsender
# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "main.py"]
