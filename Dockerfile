# Use official Python  image
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy project files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Spacy model
RUN python -m spacy download en_core_web_sm

# Expose FastAPI's port
EXPOSE 8000

# Command to run FastAPI when container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
