#

  

**Über arc42**

  

arc42, das Template zur Dokumentation von Software- und

Systemarchitekturen.

  

Template Version 8.2 DE. (basiert auf AsciiDoc Version), Januar 2023

  

Created, maintained and © by Dr. Peter Hruschka, Dr. Gernot Starke and

contributors. Siehe <https://arc42.org>.

  

# Einführung und Ziele

  

## Aufgabenstellung
Im Sommersemester 2024 des Masterstudium INF-M SSE (Fachrichtung Software- und Systemsengineeing) muss in der Vorlesung Softwarequalitätssicherung (SQS) eine kleine eigenständige Anwendung programmiert werden. Diese Anwendung besteht aus der Anwendung selbst mit einer Verbindung zu einer Datenbank, ist an ein externes (fremdgehostetes) System angebunden und verfügt über eine eigene API, die über eine HTML-Testseite angesprochen werden kann. 

Die Anwendung ermöglicht es einem Anwender seinen Co²-Abdruck zu ermitteln, indem man auf sich zugeschnitten Co² austoßende Aktivitäten über die Anwendung anlegen kann. Diese eingegeben Daten werden einer API übergeben, welche die CO²-Emissionen dieser Aktivität berechnet und zurück liefert. Die Anwendung dient als Management und Historie der eingetragenen Aktivitäten und zeigt in der Übersicht den aktuellen Carbon Score des Monats an basieren auf den eingegebenen Aktivitäten einer Person.

Die Anwendung wird von mir im Rahmen der Vorlesung entwickelt und danach nicht mehr weiter verfolgt. 
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)


## Neben dieser Readme Datei finden sich weitere Beschreibungen im Wiki
Biespiel: [Test Setup](https://github.com/Major-Wudy/sqs-application/wiki/Test-Setup), [IaC](https://github.com/Major-Wudy/sqs-application/wiki/Infrastructure-as-code-(Iac)-mit-Docker), [Statische Code Analyse](https://github.com/Major-Wudy/sqs-application/wiki/Statische-Analysen) etc. 
  

## Qualitätsziele
Die Anwendung soll folgende Qualitätsziele (QZ) erreichen:

| Priorität    | Qualitätsziel  | Szenario          |
|--------------|----------------|-------------------|
| 1 | Zuverlässigkeit | Das System führt Funktionen unter den festgelegten Bedingungen und Umgebungen aus. Geringe "meantime to recovery" und niedrige Anzahl an Ausfällen. | 
| 2 | Wartbarkeit | Das System kann modifiziert werden, um es zu verbessern, korrigieren oder an geänderte Bedürfnisse anpassen. Übernimmt ein anderer Entwickler das System können eigene Funktionalitäten und Verbesserungen in das System eingearbeitet werden |
| 3 | Benutzerfreundlichkeit | Das System kann verstanden, erlent und verwendet werden und ist attraktiv für Benutzende. Ein Anwender soll die Anwendung ohne Einführung in das System verwenden können. Die Oberflächen und Funktionen sollen selbsterklärend sein oder direkte Hilfestellungen anbieten |
| 4 | Übertragbarkeit | Das System kann auf verschiedene Umgebungen übertragen werden. Das System soll unteranderem Betriebssystem unabhängig sein. |
  

## Stakeholder

  

| Rolle        | Kontakt        | Erwartungshaltung |
|--------------|----------------|-------------------|
| Dozent | Leander Reimer  | Eine funktionierende Anwendungen mit Einhaltung der angegebenen Qualitätszielen und weiteren SQS-Aspekten  |
| Student/Entwickler | Raphael Wudy | Hoher Lerneffekte im Bereich SQS und Python und eine funktionierene Anwendung mit den angegebenen QZs  |
| Anwender | - | Das System funktioniert, ist benutzerfreundlich und erfüllt die Erwartung, die der Anwender vom System hat |
| zukünftige Entwickler/Maintainer | - | Das System ist wartbar, modizifierbar und lässt sich luaffähig aufsetzen |
| CarbonInterface API | https://www.carboninterface.com/ | Verwendung der API nach Vorgaben des Anbieters |
  

# Randbedingungen

Technischer Art:
- Entwicklung mit Docker (damit verbundenes OS in Docker ist Linux - Ubuntu)
- Programmiersprache des Backends ist Python
- Framework: Django
- Datenbank: MySQL
- Externes Systeme: https://docs.carboninterface.com/#/
- API-Dokumentation nach OpenAPI Standard und Swagger als UI

Organisatorischer Art:
- Zeit: 23.06.24 Abgabetermin Software
- Budget: kein finanzielles Interesse
- Dokumente und Unterlage aus der Vorlesung SQS beeinflussen die Entwicklung
  

# Kontextabgrenzung

## Fachlicher Kontext
![Kontextdiagramm](https://github.com/Major-Wudy/sqs-application/assets/47253607/983fbaf1-6cce-4781-87eb-1e85762ee353)


CarbonScore ist das zu entwicklende System und implementiert die Schnittstellen CarbonInterface zur Berechnung der CO²-Emissionen einer Aktivität und eine Datenbank als persistenten Datenspeicher. Die Anwendung stellt dem User eine Benutzeroberfläche als Webanwendung zur Verfügung.

Liste von Nachbaren zum System und deren Beschreibung:
| ID           | Nachbar        | Beschreibung |
|--------------|----------------|-------------------|
| 1 | User | Hier wird der Input für die Anwendung generiert. Benutzt die Schnittstellen CarbonInterface indirekt. Greift direkt auf das System CarbonScore zu. |
| 2 | CarbonInterface | Ist eine API zur Berechnung der CO²-Emissionen einer Aktivität. CarbonScore verwendet das CarbonInterface direkt und ist über einen API-Key angebunden.|
| 3 | Database | CarbonScore speichert die Daten der Anfragen von Usern und den CarbonScore in der Datenbank für persistente Datenhaltung.|
| 4 | API | CarbonScore stelle eine eigene API zur Verfügung gegen welche entwickelt werden kann. |

*Risiko: Aufgrund der Vielfältigkeit des Internets und der unterschiedlichen Browser und Infrastrukturen der Anwender kann es bei diesen Systemen durch die Fernverbindung zu Netzwerk- und Latenzproblemen kommen. Die Absicherung und Robustheit der Schnittstelle muss daher speziell betrachtet werden.


Liste der Kommunikationsbeziehungen:

| ID           | Nachbar | Kommunikationsbeziehung/Schnittstelle |
|--------------|----------------|-------------------|
| 1 | User |  <ul> <li>Liefert Inputdaten zu einer CO²-Emissionsaktivität</li> <li>Liefert Eingaben für die Anwendung über ein Userinterface (UI)</li> </ul>  |
| 2 | CarbonInterface | <ul> <li>Erhält über https und Api-Key eine JSON Anfrage mit Details zu einer CO²-Emissionsaktivität</li> <li>Gibt als Antwort ein JSON über http zurück</li> </ul> | 
| 3 | Database | <ul> <li>Verbindet sich per Verbindungsstring mit der Anwendung</li> <li>Tauscht über einen Connector SQL Abfragen mit der Anwendung aus</li> </ul> |
| 4 | CarbonScore | <ul> <li>Stellt dem User eine Oberfläche zur Verfügung, welche über den Browser mit http angesprochen werden kann</li> </ul> |
| 5 | API | <ul> <li>Erhält Anfragen als JSON über http</li> <li>Sendet Antworten als JSON über http</li> </ul> | 

 

**Erläuterung der externen fachlichen Schnittstellen**

| ID | Schnittstelle | Beschreibung |
|--------------|----------------|-------------------|
| 1 | CarbonInterface | <ul> <li>Der Schnittstelle müssen Details zur Aktivität zur Verfügung gestellt werden, die CO² abgeben</li> <li>Verwendet die präziseste Methodik im Bereich zur Berechnung der geschätzten CO² Emission</li> <li>Sendet eine Antwort, zur Verwendung im System</li> </ul> |
  

## Technischer Kontext
![technisches Kontextdiagramm](https://github.com/Major-Wudy/sqs-application/assets/47253607/58fddbbf-9e89-4b19-bc29-63e1241c9152)


**Erläuterung der externen technischen Schnittstellen**

| ID | Schnittstelle | Beschreibung |
|--------------|----------------|-------------------|
| 1 | CarbonInterface | <ul><li>Authorisierung über ein Bearer Token</li> <li>Input als JSON mit Content-Type application/json</li> <li>Sendet JSON als Antwort</li></ul> |
  

**Mapping fachliche auf technische Schnittstellen**

| ID | Schnittstelle | Mapping |
|--------------|----------------|-------------------|
| 1 | CarbonInterface | <ul><li>Authentifizierung einer Anfrage über CarbonScore per Bearer Token</li><li>Stellt die Daten der CO²-Emissionsaktivität als JSON für die CarbonInterface API zur Verfügung</li> <li>CarbonScore erhält von CarbonInterface eine JSON Antwort zur Weiterverarbeitung </li></ul> |

# Lösungsstrategie

| Qualitätsziel | Lösungsansatz | Link zu Details |
|--------------|----------------|-------------------|
| Robustheit | Über Infrastructure as Code (Iac) in einem Dockerfile läuft die Anwendung in der vorgegebenen lauffähigen Umgebung unter denselben Bedingungen. | |
| Meantime to recovery | Angabe einer Anzahl von Versuchen an Neustarts wenn der Dockercontainer auf einen Fehler läuft. | [Docker Dokumentation](https://docs.docker.com/config/containers/start-containers-automatically/) | 
| Ausfallsicherheit| Docker-Container sind multiinstanzfähig und können über die docker-compose gesteuert werden. Damit die Ausfallsicherheit gegeben ist, werden mind. 2 Container für die Anwendung erstellt. In Entwicklung nicht notwendig. | [Docker Dokumentation](https://docs.docker.com/compose/compose-file/deploy/#replicas) |
| Verfügbarkeit| Es wird bei einem fehlerhaftem Request gegen die 3rd Party Schnittstelle eine Meldung an den Anwender herausgegeben, wenn die 3rd Party Schnittstelle nicht erreicht werden kann. ||
| Tests| Die Fachlichkeiten der Anwendungen werden mit Unittests geprüft und mit einem Tool zur Code Coverage gemessen. Die Ergebnisse werden auch an ein Statisches Analyse Tool übergeben | [Coverage](https://coverage.readthedocs.io/en/7.5.3/), [unittests](https://docs.python.org/3/library/unittest.html), [Statische Code Analyse](https://docs.sonarsource.com/sonarqube/latest/?_gl=1*gpc57o*_up*MQ..&gclid=EAIaIQobChMI8p6F85LWhgMVJmxBAh3mkglcEAAYASAAEgIvvPD_BwE) |
| Wartung| ||
| Kognitive Last| Die kognitive Last der Funktionen wird mit einem Analyse-Tool geprüft. | [Statische Code Analyse](https://docs.sonarsource.com/sonarqube/latest/?_gl=1*gpc57o*_up*MQ..&gclid=EAIaIQobChMI8p6F85LWhgMVJmxBAh3mkglcEAAYASAAEgIvvPD_BwE) |
| Verbesserung | Durch den Onion Architecture Ansatz sollen Verbesserungen ohne Anpassungen der Fachlichkeit möglich sein. | [Onion Architekture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/) |
| einfache Handhabung| Das Userinterface für Admins soll dem OpenAPI Standard folgen für einfache und einheitliche Handhabung. Daher wird Swagger mit OpenAPI Standard 3.0 für die Admin UI im API Bereich verwendet | [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/readme.html) |
| Effizienz|  |
| Betriebssystem unabhängig| Um die unterschiedliche Hardware der Entwickler und Anwender in de Griff zu bekommen, wir die Anwendung mit Docker entwickelt. Damit wird im Container die richtige Laufzeitumgebung für die Anwendung definiert und die Plattform des Entwicklers ist egal. Außerdem wird die Anwendung als Webanwendung entwickelt und ist damit mit einem Browser für Anwendung zugänglich. | [Docker Dokumentation](https://docs.docker.com/) |
| Übertragbar | Damit die Anwendung von einer Umgebung in eine andere übertragbar ist, wird die Anwendung mit Docker entwickelt. Container an Stelle A herunterfahren ohne Änderungen an Stelle B hochfahren |  |
| Abgesichert | Alle Abfragen an das System über die API sind mit einem Bearer Token abgesichert. | [Django Restframework Auth](https://www.django-rest-framework.org/api-guide/authentication/) |

# Bausteinsicht

  

## Whitebox Gesamtsystem
*Scope und Kontext*

![Scope_and_context](https://github.com/Major-Wudy/sqs-application/assets/47253607/588a28de-8b90-481c-a17d-74babca3972f)

![level1-whitebox](https://github.com/Major-Wudy/sqs-application/assets/47253607/88fd3ef7-442f-4eb7-a8d0-b4a1e64143d8)


*Begründung:*  

Die Applikation wird in eine persistente Datenhaltung, eine externe API zur Berechnung der geschätzten CO²-Emissionen und der Geschäftslogik unterteilt.
- Die Applikation ist kein Datenbankmanagementsystem, daher wird für die persistente Datenhaltung ein Nachbarsystem benötigt
- Die Applikation hat keine Möglichkeit zur Eigenberechnung der geschätzten CO²-Emissionen, daher wird eine 3rd Party API zur Berechnung benötigt
  

*Enthaltene Bausteine:*
- Datenbank: Speichert notwendige persistene Daten
- Carboninterface API: Errechnet die geschätzten CO²-Emissionen für die übermittelten Werte
- UI: Ist die grafische Schnittstelle der Anwendungslogik zu einem Administrator, späteren Maintainer oder anderen Entwickler
- Infrastructure Service API: Bearbeitet alle API-Calls der eigenen API ab und stellt diese zur Verwendung bereit
- Infrastructure Service carboninterface API: Übernimmt die Anfragen von Infrastructure Service API und bereitet diese zur Abfrage der Carboninterface API vor.
- Infrastructure Service Interface: Ein Interface der Anwendung zur Kommunikation mit der Datenbank über einen vorgeschalteten Datenbank Service
- Database Service: Baut die Verbindung zur Datenbank auf und führt Abfragen aus
- Domain Service Interface: Implementiert die Domain Services und bietet anderen Komponenten ein Interface zur Kommunikation mit der Geschäftslogik
- Domain Services: Beinhaltet die Geschäftslogik
- Domain Models: Beinhaltet die Datenmodelle und Entitäten
- Administrator: Verwendet die Applikation
  

Wichtige Schnittstellen  

| **Name**        | **Verantwortung** |
|-----------------|-------------------|
| Carboninterface API | Zur Errechnung der geschätzten CO²-Emissionen einer Aktivität. |
| Datenbank | Speicherung von Daten der Anwendung über die Laufzeit einer Session hinweg. |
| Infrastructure Service Interface | Zugriff auf die Datenbank ist über dieses Interface möglich.| |
| Domain Service Interface | Zugriff auf die Geschäftslogik in den Domain Services über dieses Interface möglich.|
| UI | Grafische Schnittstelle zum Administator, Anwender der Anwendung |

  

### Carboninterface
*Zweck*

Die Applikation hat selbst keine Möglichkeiten zur Berechnung von CO²-Emissionen und nutzt daher diese 3rd Party API zur Berechnung dieser. Die Carboninterface API liefert anhand übermittelter Daten die geschätze CO² Emission für die Aktivität. Dabei werden Die Daten als JSON bereitgestellt und enthalten ermittelten Werte in gm kg, lb und mt.

*Schnittstelle*
[Beschreibung der Schnittstelle](https://docs.carboninterface.com/#/?id=estimates-api
  

*Dokumentation*
- [Dokumentation der API](https://docs.carboninterface.com/#/)
- [Postman Collection](https://docs.carboninterface.com/#/?id=postman)
- [Authentifizierung](https://docs.carboninterface.com/#/?id=authentication)

*Erfüllte Anforderungen*
- Open Source
- Einfache Verwendung durch JSON Datenübermittlung
- Authentifizierung mit Bearer Token
- Rückgabe der CO²-Emissionen bei Übergabe einer Aktivität 

*Probleme*
- Im freien Plan sind nur 200 Calls pro Monat möglich, mehr muss finanziell per ABo gelöst werden


### Datenbank
*Zweck*

Speichern der Token zur Kommunikation mit der eigenen API, Zwischenspeicherung der gesendeten Request, damit bei Systemabsturz eine Queue zum Abarbeiten entsteht, Speichern der CO²-Emissionen für einen User.

*Schnittstelle*

ODBC-Verbindung mit der MySQL-Datenbank, die über das Framework [Django](https://www.djangoproject.com/) implementiert wird. 

*Dokumentation*

- [django.db](https://docs.djangoproject.com/en/5.0/ref/databases/)
- [mysqlclient für Python](https://pypi.org/project/mysqlclient/)

*Erfüllte Anforderung*
- Know-how über die Verwendung
- Dockerfähig
- Mit Django und Python kompatibel

*Risiken*
- Zu starke Einbindung der Datenbank in die API, schmälter die Geschwindigkeit der API

### Infrastructure Service Interface
*Zweck*
Kommuniziert mit dem Datavase Service zur Erstellung von Abfragen und Datenbereinigung vor Übergabe dieser an den Database Service. Ist ein Interface zur Kapselung der Datenbank in der Anwendung. Einfachere Wartung und Austausch der Datebnak möglich.

*Schnittstelle*

Ein Interface, welches die abstrakte Methoden des Database Services implementiert. Stellt Funktionen in der Anwendung zur Verwendung der Datebank bereit.

*Erfüllte Anforderungen*
- einfache Handhabung der Datenbankinteraktion in der Anwendung
- Wartbarkeit
- leichter Austausch der Datenbank möglich

### Domain Service Interface
*Zweck* 

Kapselung der Geschäftslogik als eigenständige Einheit. Stellt der restlichen Anwendung einen Single Point of Contact zur Verfügung.

*Schnittstelle*

Ein Interface, welches die Funktionalität der Geschäftslogik zur Verfügung stellt.

*Erfüllte Anforderungen*
- einfache Handhabung zur Verwendung der Geschäftslogik
- Wartbarkeit
- Austausch der Geschäftslogik / ERgänzung möglich

### UI
*Zweck*

Kommunikation mit der Anwendung über eine grafische Oberfläche zur einfachen und schnellen Einarbeitung in die Verwendung der Anwendung. 

*Schnittstelle*
- grafische Oberfläche

*Erfüllte Anforderungen*
- schnelle und einfache Bedienung der Anwendung ohne "anprogrammieren" der Anwendung
- Testen der Ergebnisse und Funktionsweise der Anwendung
- Dokumentation der API


## Ebene 2 - Domain
### Domain Service Interface
![level2-whitebox-ds-interface](https://github.com/Major-Wudy/sqs-application/assets/47253607/400eb443-b931-443f-864f-9be34203cea4)


*Zweck*

Dient zur Kapselung der Geschäftslogik vom restlichen Teil der Anwendung. Erhöht die Warbarkeit der Anwendung. 

*Enthaltene Bausteine* 
- Domain Services: Implementiert diese und stellt deren Funktionen bereit

*Schnittstellen*
- Infrastructure Service API: Stellt als Single Point of Contact Funktionen der Domain Services bereit
- Infrastructure Service carboninterface API: Stellt als Single Point of Contact Funktionen der Domain Services bereit

*Erfüllte Anforderungen*
- Kapselung der Geschäftslogik
- Wartbarkeit der Anwendung
- Austauschfähige Geschäftslogik

### Domain Services
![level2-whitebox-ds-domain](https://github.com/Major-Wudy/sqs-application/assets/47253607/07d9a6c4-2a63-4735-99df-f3552f29a8a7)


*Zweck* 

Beinhaltet die einzelnen Services für die Bearbeitung der Geschäftslogik

*Enthaltene Bausteine*
- Flight Service: Stellt Funktionen zur Erstellung einer Flug-Aktivität bereit
- Electricity Service: Stellt Funktionen zur Erstellung eines Stromverbrauchs bereit
- Shipping Service: Stellt Funktionen zur Erstellung von Versendungen (Pakete, Briefe etc.) bereit
- Fuel Service: Stellt Funktionen zum Verbrauch von Brennstoff bereit
- Distance Service: Gibt die möglichen Distanzeinheiten wieder
- Weight Service: Gibt die möglichen Gewichtseinheiten wieder
- Transport Service: Gibt mögliche Transportmöglichkeiten wieder

*Schnitstellen* 
- Domain Models: Implementiert die Entitäten der Geschäftslogik
- Domain Service Interface: Stellt für die Funktionen des Domain Services Bereit


### Domain Models
![level2-whitebox-domain-service](https://github.com/Major-Wudy/sqs-application/assets/47253607/f596900d-d103-49d4-b206-5c024b064f33)


*Zweck*

Stellt die Entitäten der Geschfätslogik dar.

*Enthaltene Bausteine*
- Activity: gibt die möglichen Aktivitättstypen wieder
- electricity: Enthlält die Objektdefinition für Stromverbrauch
- flight: Enthält die Objektdefinition für Flüge
- shipping: Enthält die Objektdefinition für das Versenden von Paketen
- carbon: Enthält die Objektdefinitionen für CO² Emission
- distance: Enthält die Objektdefinition für Distanzobjekte
- fuel: Enthält die Objektdefinition für Brennstoffe
- weights: Enthält die Objektdefinition für Gewichtseinheiten

*Schnittstelle*
- Domain Services: Nutzt die Models zur Bereitstellung der Geschäftslogik
  

### Infrastructure API Service
![level2-whitebox-is-api](https://github.com/Major-Wudy/sqs-application/assets/47253607/1a3bbb1e-bd90-44d3-90a1-898ae63b9534)

*Zweck*

Bereitstellung einer API zur Verwendung der Geschäftslogik und Interaktion zwischen zwei Systemen

*Enthaltene Bausteine*
- API URLs: Stellt die URLs für die API zur Verfügung und verbindet diese mit den API Views
- API-Views: Stellt die Views für die OpenAPI Swagger Oberfläche bereit und verbindet diese mit dem genutzten API Service
- Infrastructure Service API: Implementiert die Logik der API und nutzt dazu Domain Service Interface und Database Servcie Interface (Infrastructure Service Interface), sowie Infrastructure Service carboninterface API

*Schnittstellen* 
- Domain Service Interface: Single Point of Contact zur Geschäftslogik
- Database Service Interface: Single Point of Contact zur Datenbank
- Infrastructure Service carboninterface API: Kommunikation mit dem externen System Carboninterface API 

  

# Laufzeitsicht
  ![runtime](https://github.com/Major-Wudy/sqs-application/assets/47253607/449b9f03-790b-41d0-b220-e124d068027a)


## Laufzeitszenario 1: Erstellen einer (CO²) Aktivität
### Ablaufbeschreibung
|Schritt|Beschreibung|Akteur/Baustein|
|-----|-----|-----|
| Erstellen einer Aktivität | Eingabe von Details einer Aktivität über das Userinterface | Anwender/Webbrowser |
||Authentifizierung des Users | Api |
||Validierung des Requets | Api |
||Speichern des Request in der Datenbank | Databse Service Interface |
|| Request verarbeiten | Domain Service Interface|
|| Erstellen der Aktivität | Domain Service |
|| Entität zur Aktivität erstellen | Domain Model |
|| Response vorbereiten mit Aktivitätsdaten | Domain Service |
|| Response weitergeben | Domain Service Interface |
|| Request aus der Datenbank löschen, da verarbeitet | Database Service Interface |
|| Response an den Webbrowser zurückgeben | Api |

Besonderheiten
- Fehler die während der Laufzeit auftreten werden in eine Log-Datei geschrieben
- Der Request des Anwenders wird in der Datenbank gespeichert. Sollte das System abstürzen, sind die noch nicht verarbeiteten Requests in der Datenbank vorhanden

  

## Laufzeitszenario 2: Errechnen der geschätzen CO² Emissionen einer Aktivität
### Ablaufbeschreibung
|Schritt|Beschreibung|Akteur/Baustein|
|-----|-----|-----|
| Ermitteln der geschätzten CO² Emissionen | Eingabe einer Aktivität aus Laufzeitszenario 1 einer Aktivität über das Userinterface | Anwender/Webbrowser |
||Authentifizierung des Users | Api |
||Validierung des Requets | Api |
||Speichern des Request in der Datenbank | Databse Service Interface |
|| Request verarbeiten | 3rd Party API |
|| Errechnen der CO² Emission | 3rd Party API |
|| Response verarbeiten | Api |
|CO² Emissoin speichern | CO² Emissions Enität verarbeiten | Domain Service Interface |
|| CO² Enität erstlelen | Domain Service |
|| Entität erstellen | Domain Models |
|| Entität weiterleiten | Domain Service Interface |
|| Entität speichern | Database Service Interface |
|| Request aus der Datenbank löschen, da verarbeitet | Database Service Interface |
|| Response an den Webbrowser zurückgeben | Api |

Besonderheiten
- Fehler die während der Laufzeit auftreten werden in eine Log-Datei geschrieben
- Der Request des Anwenders wird in der Datenbank gespeichert. Sollte das System abstürzen, sind die noch nicht verarbeiteten Requests in der Datenbank vorhanden



## Laufzeitszenario 3: CO² Emissionen errechnene für einen User
### Ablaufbeschreibung
|Schritt|Beschreibung|Akteur/Baustein|
|-----|-----|-----|
| CO² Emission für einen User errechnen anhand der Aktivitäten | Eingabe der Einheit der CO² Emission über das Userinterface | Anwender/Webbrowser |
||Authentifizierung des Users | Api |
||Validierung des Requets | Api |
|| Request verarbeiten | Domain Service Interface|
|| Aufsummieren der CO² Emission über die Datanbank | Database Service Interface |
|| Erstellen der CO³ Emissoin | Domain Service |
|| Entität zur CO² Emission erstellen | Domain Model |
|| Response vorbereiten mit CO² Emission | Domain Service |
|| Response weitergeben | Domain Service Interface |
|| Response an den Webbrowser zurückgeben | Api |

Besonderheiten
- Fehler die während der Laufzeit auftreten werden in eine Log-Datei geschrieben
- Die Berechnung der CO² Emission soll über die Datenbank per SQL erfolgen


## Laufzeitszenario 4: Löschen der CO² Emissionen eines Users 
### Ablaufbeschreibung
|Schritt|Beschreibung|Akteur/Baustein|
|-----|-----|-----|
| CO² Emission für einen User errechnen anhand der Aktivitäten | Eingabe der Einheit der CO² Emission über das Userinterface | Anwender/Webbrowser |
||Authentifizierung des Users | Api |
||Validierung des Requets | Api |
|| Request verarbeiten | Domain Service Interface|
|| Löschen aller CO² Emission über die Datanbank | Database Service Interface |
|| Response an den Webbrowser zurückgeben | Api |

Besonderheiten
- Fehler die während der Laufzeit auftreten werden in eine Log-Datei geschrieben

# Verteilungssicht

  

## Infrastruktur Ebene 1
![Verteilungsdiagramm](https://github.com/Major-Wudy/sqs-application/assets/47253607/6a6aff80-f81a-4886-9781-3aa3f4e16602)

Begründung  

Die Infrastruktur der Applikation wurde virtualisiert und mit Docker-Containern realisiert. Dies erleichtert es Maintainern oder anderen Entwicklern das Projekt Plattform unabhängig aufzusetzen und zu warten. Des Weiteren sind Sicherheitsaspekte durch Infrastructure as Code (Dockerfiles) abgebildet. Auch ist eine Skalierung der Applikation mit dieser Infrastructur möglich. Kommt ein Container an seine Grenzen, können mehr Ressourcen zugewiesen oder ein neuer Container gespawned werden. Außerdem ist die Ausfallsicherheit höher. Mit Docker-Containern können mehrere Applikationen im selben Netzt liegen und auf Userinpuit warten. 

Qualitäts- und/oder Leistungsmerkmale  
- Ausfallsicherheit: Mehrere Container der Applikation können gespawned werden und somit die Last im Ausfall übernehmen. Die Applikation bleibt online
- Skalierbar: Der Applikations Container kann dupliziert werden und im selben Netz betrieben werden. Die Container agieren unabhängig voneinander
- Wartbarkeit: Die Applikation kann im Huntergrund migriert werden, während die Applikation noch läuft. Erst nach Abschluss der Wartung werden die Container nacheinander neu gestartet. Somit für den Anwender nicht bemerkbar
  

Zuordnung von Bausteinen zu Infrastruktur  
- Application Container kommuniziert über eine native Datenbank Verbindung mit dem Database Container über die Komponente Database Connection API
- Application Container kummuniziert über das docker network mit dem 3rd Party API Container Wiremock über die Komponente API Connection
- Users Computer kommuniziert per http über das Internet mit dem Application Container über einen Webbrowser
- Load Performance Container kommuniziert über  das docker network mit dem Application Container
- ATDD Container kommuniziert über das docker network mit dem Application Container
  

# Querschnittliche Konzepte
![crosscutting_framework](https://github.com/Major-Wudy/sqs-application/assets/47253607/703cabde-7a2f-4bbb-a0cb-068f729af33d)


## Logging
Fehler und besondere Ereignisse sollen über alle Komponenten hinweg in Log-Dateien geschrieben werden. Dabei wäre es sinnvoll bei Fehlermeldungen die Messeges von den Exceptions mit zu loggen.

## Error Handling Try-Catch
Kritische Funktionen müssen über alle Komponenten hinweg in Try-Catch Blöcken umschlossen sein, damit error handling betrieben werden kann und die Anwendung in keine undefinierten Zustände verfällt und nicht abstürzt.

## Django Framework
Funktionen aus dem Django Framework (Database Connection, Views, Session handling) werden in den äußersten Schichten der Applikation integriert. UI, API  und Infrastruktur Datenbank

## Database Service Interface
Zur Kapselung der Datenbank und die deren Implementierung wird ein Interface für andere Komponenten der Applikation zur Verfügung gestellt. Damit soll die Wartbarkeit, Austauschbarkeit und Kapselung gesteigert werden

## Domain Serivce Interface
Zur Kapselung der Geschäftslogik von der restlichen Applikation wird ein Interface implementiert und für andere Komponenten zur Verfüung gestellt. Damit soll die Wartbarkeit, Erweiterung, Verbesserung und Kapselung der Geschäftslogik erreicht werden.
  

# Architekturentscheidungen

| **Kategorie** | **Bemerkung** |
|-----------------|-------------------|
| Titel | Programmiersprache der Anwendung |
| Kontext | In welcher Programmiersprache soll die Anwendung entwickelt werden? Zur Auswahl stehen Java, .Net oder python* |
| Entscheidung | python | 
| Status | accepted | 
| Konsequenzen | Die Anwendung wird in der Programmiersprache Python programmiert. |

*Liste der Pro und Cons für jede Programmiersprache:
Java:
| Pro                                           | Con                                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------ |
| Skills aus dem Bachelorstudium                | Letzte Erfahrung 7 Jahre her                                                   |
| Java basierte Sprache Groovy Skills vorhanden | Nur Basics keine weiterführenden Skills notwendig bei aktueller Groovy Nutzung |
| easy to learn                                 | nicht hard to master aber definitv langer Zeitraum                             |
| gut für leistungsintensive Anwendungen        |                                                                                |

.Net:
| Pro | Con                                        |
| --- | ------------------------------------------ |
|     | Keine Erfahrungen                          |
|     | Kein persönliches Interesse in der Sprache |

python:
| Pro                                                                         | Con               |
| --------------------------------------------------------------------------- | ----------------- |
| leicht zu erlernende Sprache                                                | Keine Erfahrungen |
| Weitverbreitete Sprache im wissenschaftlichen Bereich                       |                   |
| für web programming                                                         |                   |
| gut für Geschwindigkeit, Einfachheit bei der Entwicklung                    |                   |
| Rückgriff auf Tutoren im python Bereich mit persönlicher Erfahrung möglich |                   |

| **Kategorie** | **Bemerkung** |
|-----------------|-------------------|
| Titel | Framework der Anwendung |
| Kontext | In welchem Framework soll die Anwendung programmiert werden. Einschränkungen: Programmiersprache Python |
| Entscheidung | Django | 
| Status | accepted | 
| Konsequenzen | Die Anwendung wird mit dem Framework Django entwickelt. |

| **Kategorie** | **Bemerkung** |
|-----------------|-------------------|
| Titel | Architektur der Anwendung |
| Kontext | In welchem Architektur Modell soll die Anwendung entwickelt werden? Layer oder Oinion |
| Entscheidung | onion architecture | 
| Status | accepted | 
| Konsequenzen | Die Anwendung wird aufgrund der angestrebten Wartbarkeit in der onion Architektur entwickelt. |

| **Kategorie** | **Bemerkung** |
|-----------------|-------------------|
| Titel | Deployment der Anwendung und Entwicklungsumgebung |
| Kontext | Auf welche Art soll die Anwendung deployed werden? |
| Entscheidung | Docker | 
| Status | accepted | 
| Konsequenzen | Die Anwendung wird aufgrund der angestrebten Wartbarkeit und Plattformunabhängigkeit in Docker entwickelt und deployed werden. |

| **Kategorie** | **Bemerkung** |
|-----------------|-------------------|
| Titel | Datenbank der Anwendung |
| Kontext | In welchem Datenbanksystem sollen Daten gespeichert werden. |
| Entscheidung | MyxSQL | 
| Status | accepted | 
| Konsequenzen | Da bereits Erfahrungen mit Docker in Verbindung mit MySQL vorhanden sind, wird MySQL als Datenbank verwendet. |

# Qualitätsanforderungen

  

## Qualitätsbaum

| **Qualitätskategorie** | **Qualität** | **Beschreibung** | **Qualitätsszenario** |
|-----------------|-------------------|-------------------|-------------------|
| Zuverlässigkeit (1) | Robustheit | Das System soll zuverlässig unter den angegebenen Laufzeitumgebung laufen. | 1 |
| | Geringe meantime to recovery | Das System soll nach einem Ausfall schnellstmöglich wieder verfügbar sein. | 2 |
| | Ausfallsicherheit | Das System soll multiinstanzfähig sein. | 3 |
| | Verfügbarkeit | Bei nicht vorhanden sein der externen Schnittstellen soll das System den Anwender über die eingeschränkte Funktionalität informieren. | 4 |
| | Tests | Das System soll eine Codecoverage von >= 80% aufweisen. | 5 |
| Wartbarkeit (2) | Wartung | Es sollen außerhalb des fachlichen Kerns der Anwendung Komponenten ausgetauscht werden können, ohne die Fachlichkeit der Anwendung zu beeinflussen.| 6 |
| | Kognitive Last | Die kognitive Komplexität von Funktionen soll <= 15 sein. | 7 |
| | Verbesserung | Es sollen Verbesserungen für die Anwendung implementiert werden können, die die bestehende Fachlichkeit erweitern ohne diese zu verändern. | 8 | 
| Benutzerfreundlichkeit (3) | einfache Handhabung | Einfache Handhabung für umweltbewusste Personen, speziell bezogen auf die Verwendung der Anwendung. | 9 | 
| | Effizienz | Die Anwendung soll in zufriedenstellender Zeit eine Antowrt auf die Eingaben des Anwenders liefern. | 10 |
| Übertragbarkeit (4) | Betriebssystem unabhängig | Das System soll unabhängig vom Betriebssystem lauffähig sein. | 11 |
| | Übertragbar | Das System soll leicht von einem System auf ein anderes überführt werden können. | 12 |
| Sicherheit | Abgesichert | Anfragen sollen nur von authentifizierten Anwendern getätigt werden können. | 13 |

## Qualitätsszenarien

| **ID** | **Beschreibung** |
|-----------------|-------------------|
| 1 | Über 20 Minuten hinweg soll das System einer Last von 100 Usern mit ca. 50 Requests pro Sekunde standhalten. |
| 2 | Bei Systemabsturz soll sich die selbst neustarten. Dies soll die Anwendung 3x veruschen, bevor es in einen dauerhaften Fehlerzustand übergeht. |
| 3 | Beim Ausfall einer Instanz der Anwendung soll die Möglichkeit besitzen, den Trafiic der ausgefallenen Instanz auf andere Instanzen weiterzugeben. |
| 4 | Ist eine externe Schnittstelle nicht verfügbar, soll das System einen Hinweis darauf liefern und weiterlaufen. |
| 5 | Die Logik des Systems ist durch Unittests getestet und kann durch ein Tool ausgewertet werden. Die Auswertung der Testabdeckung muss dabei >= 80% sein. |
| 6 | Wird eine ander Datenbank oder ein andere Schnittstelle zur Berechnung des CarbonScores verwendet, kann diese ohne Anpassung der Fachlichkeit ausgetauscht und implementiert werden. |
| 7 | Eine Funktion soll leicht verständlich sein und damit eine kognitive Last von <= 15 sein. Diese soll über ein externes Tool geprüft werden. |
| 8 | Verbesserungen oder neuen Funktionen sollen in das Sytem implementiert werden können, ohne dass der Fachliche Kern der Anwendung angepasst werden muss. Beispiel: Hinzufügen eines Benutzerprofils für das Speicher der gesendeten Anfragen pro Benutzer |
| 9 | Ein Anwender kann ohne weitere Dokumentation zur Verwendung der Anwendung die Anwendung erfolgreich bedienen. |
| 10 | Die Anwendung soll innerhalb einer Sekunde eine Anwort an den Anwender senden. |
| 11 | Egal ob Windwos, Mac oder Linux: Die Anwendung ist unter allen genannten Betriebssystemen ausführbar. |
| 12 | Die Anwendung kann von einem System auf das andere portiert werden. Beispiel: Virtualisierte Anwendung als Docker Container. |
| 13 | Anfragen an die Software können nur mit Token, die von der Anwendung ausgestellt sind erfolgen. Beispiel Auth mit Bearer Token für die API. |
  

# Risiken und technische Schulden
|Risiko | Beschreibung |
|-----|-----|
|Django Rest Framework | Bie dieser Integration einer API kann es zu Performance Problemen kommen. Mögliche Lösungen hierfür sind Rate Limiting, Caching, Asynchrone Aufgaben. |

# Glossar

  
| **Begriff**                            | **Beschreibung**                                                                                     |
|----------------------------------------|------------------------------------------------------------------------------------------------------|
| **SQS**                                | Softwarequalitätssicherung, eine Disziplin im Software Engineering, die sich auf die Sicherstellung der Qualität von Softwareprodukten konzentriert. |
| **Carbon Score**                       | Eine Kennzahl, die den CO₂-Ausstoß einer Person basierend auf deren Aktivitäten darstellt. |
| **Anwender**                           | In erster Linie wird hier als Anwender ein Administrator, der die Anwendung wartet oder weiterentwickelt, verstanden. |
| **CarbonInterface**                    | Eine API zur Berechnung der CO₂-Emissionen basierend auf übermittelten Aktivitätsdaten. |
| **OpenAPI Standard**                   | Ein Standard für die Erstellung von API-Dokumentationen, der die Spezifikation von RESTful APIs beschreibt. |
| **Swagger**                            | Ein Open-Source-Framework, das zur Beschreibung, Erstellung, Dokumentation und Nutzung von RESTful Webdiensten verwendet wird. |
| **Infrastructure as Code (IaC)**       | Ein Ansatz zur Verwaltung und Bereitstellung von Rechenzentren durch maschinenlesbare Definitionsdateien, anstatt physische Hardware-Konfigurations- oder interaktive Konfigurationswerkzeuge zu verwenden. |
| **Onion Architecture**                 | Ein Architekturansatz, der die Trennung von Bedenken fördert und die Entwicklung flexibler und testbarer Systeme unterstützt. |
| **Statische Code Analyse**             | Eine Methode zur Analyse von Quellcode, ohne ihn auszuführen, um potenzielle Fehler oder Verbesserungsmöglichkeiten zu identifizieren. |
| **Whitebox Gesamtsystem**              | Eine Darstellung der inneren Struktur des Systems, einschließlich aller internen Komponenten und deren Beziehungen. |
| **Scope und Kontext**                  | Der Umfang und der Kontext einer Anwendung, einschließlich der Grenzen, Ziele und relevanten externen Systeme. |
| **Infrastructure Service API**         | Eine API, die alle Anfragen der eigenen API verarbeitet und zur Verwendung bereitstellt. |
| **Database Service**                   | Ein Service, der die Verbindung zur Datenbank aufbaut und SQL-Abfragen ausführt. |
| **Domain Service Interface**           | Ein Interface, das die Geschäftslogik implementiert und anderen Komponenten zur Verfügung stellt. |
| **Domain Services**                    | Enthält die Geschäftslogik der Anwendung. |
| **Domain Models**                      | Beinhaltet die Datenmodelle und Entitäten, die in der Geschäftslogik verwendet werden. |
| **Postman Collection**                 | Eine Sammlung von API-Anfragen, die in Postman zum Testen und Dokumentieren von APIs verwendet wird. |
| **Flight Service**                     | Ein Service zur Verwaltung und Erstellung von Flugaktivitäten innerhalb der Geschäftslogik. |
| **Electricity Service**                | Ein Service zur Verwaltung und Erstellung von Stromverbrauchsaktivitäten. |
| **Shipping Service**                   | Ein Service zur Verwaltung und Erstellung von Versandaktivitäten (Pakete, Briefe, etc.). |
| **Fuel Service**                       | Ein Service zur Verwaltung und Erstellung von Brennstoffverbrauchsaktivitäten. |
| **Distance Service**                   | Ein Service zur Verwaltung und Bereitstellung von Distanzinformationen. |
| **Weight Service**                     | Ein Service zur Verwaltung und Bereitstellung von Gewichtsinformationen. |
| **Transport Service**                  | Ein Service zur Verwaltung und Bereitstellung von Transportinformationen. |
| **Activity**                           | Ein Datenmodell, das mögliche Aktivitätstypen repräsentiert. |
| **Aktivität**                          | Eine Aktivität, die CO²-Emissionen verursacht. |
| **Infrastructure Service carboninterface API** | Verarbeitet Anfragen von der Infrastructure Service API und bereitet sie für die Carboninterface API vor. |
| **Database Connection API**            | Die Komponente, die die native Datenbankverbindung im Anwendungskontainer verwaltet. |
| **Wiremock**                           | Ein Tool zum Mocking und Stubbing von APIs für Testzwecke. |
| **ATDD (Acceptance Test-Driven Development)** | Eine Methode, bei der Akzeptanztests vor der Entwicklung geschrieben werden, um sicherzustellen, dass die Anforderungen erfüllt werden. |
| **Crosscutting Framework**             | Ein Rahmenwerk für Querschnittskonzepte, die in allen Teilen einer Softwarearchitektur relevant sind, wie Logging und Fehlerbehandlung. |
| **Logging**                            | Das Schreiben von Fehlern und besonderen Ereignissen in Log-Dateien zur Überwachung und Fehleranalyse der Anwendung. |
| **Error Handling**                     | Der Umgang mit Fehlern in der Software durch Try-Catch-Blöcke, um die Anwendung vor Abstürzen und undefinierten Zuständen zu schützen. |
| **Database Service Interface**         | Ein Interface zur Kapselung der Datenbank und deren Implementierung, das anderen Komponenten der Applikation zur Verfügung gestellt wird. |
| **Domain Service Interface**           | Ein Interface zur Kapselung der Geschäftslogik von der restlichen Applikation, das anderen Komponenten zur Verfügung gestellt wird. |




