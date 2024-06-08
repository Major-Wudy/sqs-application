#!/bin/sh

# Warte auf die Datenbank, bevor der Server gestartet wird
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Datenbankmigrationen durchführen
python src/manage.py migrate

# Statische Dateien sammeln (falls erforderlich)
python src/manage.py collectstatic --noinput

# Entwicklungsserver starten
exec "$@"
