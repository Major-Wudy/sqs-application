# Basis-Image mit Python
FROM python:3.10-slim

# Umgebungsvariablen setzen
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Arbeitsverzeichnis erstellen und setzen
WORKDIR /app

# Systemabhängigkeiten installieren
RUN apt-get update \
    && apt-get --no-install-recommends install -y \ 
       python3-dev \
       default-libmysqlclient-dev \
       build-essential \
       pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Abhängigkeiten installieren
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# locust file integrieren
COPY locustfile.py /app/

# Quellcode kopieren
COPY src /app/src
COPY entrypoint.sh /app/

RUN chmod +x /app/entrypoint.sh

# Eintragspunkt für das Startskript setzen
ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
