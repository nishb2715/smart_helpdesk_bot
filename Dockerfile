FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for some langchain tools)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .


# Run the main app
CMD ["python", "app.py"]
