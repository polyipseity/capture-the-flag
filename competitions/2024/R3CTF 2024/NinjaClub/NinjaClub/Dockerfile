FROM python:3.9-slim

WORKDIR /usr/src/app

COPY src /usr/src/app

COPY flag.txt /flag.txt

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["uvicorn", "ninja-club:app", "--host", "0.0.0.0", "--port", "8000"]
