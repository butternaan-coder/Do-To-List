# Use official Python image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app (main.py, etc.)
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]
