FROM public.ecr.aws/docker/library/python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "application.py"]
