# Use an official Python runtime
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy project files and install dependencies
COPY . .
RUN pip install -r requirements.txt

# Expose the port Flask and Dash run on
EXPOSE 5000

# Run the app
CMD ["python", "app/main.py"]
