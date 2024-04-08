FROM python:3.8.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--port", "8000"]