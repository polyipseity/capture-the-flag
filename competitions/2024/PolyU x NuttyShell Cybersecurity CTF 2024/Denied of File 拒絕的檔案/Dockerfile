# Use the official Ubuntu 22.04 LTS image as the base image
FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /app

# Update the package lists and install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip install flask

# Copy the application code to the container
COPY app.py app.py
copy flag.txt /flag.txt

# Expose the port on which the application will run
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
