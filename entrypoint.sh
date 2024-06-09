#!/bin/sh
# Datenbankmigrationen durchführen
python src/manage.py migrate

# Statische Dateien sammeln (falls erforderlich)
python src/manage.py collectstatic --noinput

# Entwicklungsserver starten
exec "$@"
