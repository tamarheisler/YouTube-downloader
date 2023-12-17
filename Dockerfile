# Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy app files
COPY app.py .
COPY templates templates/


# Expose port
EXPOSE 5000

# Run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
