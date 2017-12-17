# Use an official Python runtime as a parent image
FROM python:3.6.3

# Set the working directory to /app
WORKDIR /sample-app

# Copy the current directory contents into the container at /app
ADD . /sample-app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8001

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
ENTRYPOINT ["gunicorn", "-b", ":8001", "sample.app:get_app()"]
