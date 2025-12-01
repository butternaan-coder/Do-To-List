FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE $PORT

CMD ["bash", "-c", "streamlit run main.py --server.address=0.0.0.0 --server.port=$PORT"]
