FROM python:3.9

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 9000

CMD ["fastapi", "run", "main.py", "--port", "9000"]