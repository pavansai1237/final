# Use the official Python image.
# It automatically sets up the environment.
FROM python:3.12-slim

# Install Tesseract dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    tesseract-ocr-eng \
    tesseract-ocr-hin

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available for Streamlit
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py"]
