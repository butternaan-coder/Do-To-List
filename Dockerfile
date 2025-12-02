FROM python:3.13.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render will assign $PORT automatically
EXPOSE $PORT

# Use python -m streamlit (Fixes: "streamlit: command not found")
CMD ["bash", "-c", "python -m streamlit run main.py --server.address=0.0.0.0 --server.port=$PORT"]
