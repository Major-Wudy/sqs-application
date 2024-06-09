# Verwende ein Basis-Image mit Java
FROM adoptopenjdk:11-jre-hotspot

# Arbeitsverzeichnis erstellen und setzen
WORKDIR /karate

# Karate JAR-Datei herunterladen
RUN curl -L -o karate.jar https://github.com/karatelabs/karate/releases/download/v1.4.0/karate-1.4.0.jar

# Kopiere die Karate-Tests in das Image
COPY tests /karate/tests

# Setze den Klassenpfad
ENV CLASSPATH=/karate

# Standard-Kommando für die Ausführung der Karate-Tests
CMD ["java", "-jar", "karate.jar", "tests"]