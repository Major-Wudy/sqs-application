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


  

## Qualitätsziele
Die Anwendung soll folgende Qualitätsziele (QZ) erreichen:

| Priorität    | Qualitätsziel  | Szenatio          |
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
![image](https://github.com/Major-Wudy/sqs-application/assets/47253607/39575ab4-e20c-4277-8b23-7fc9c3855d0f)

CarbonScore ist das zu entwicklende System und implementiert die Schnittstellen CarbonInterface zur Berechnung der CO²-Emissionen einer Aktivität, Auth0 als Authentifizierungsmöglichkeit und eine Datenbank als persistenten Datenspeicher. Die Anwendung stellt dem User eine Benutzeroberfläche als Webanwendung zur Verfügung.

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
| 3 | Database | <ul> <li>Verbindet sich per Verbindungsstring mit der Anwendung</li> <li>Tauscht über einen Connector SQL Queries mit der Anwendung aus</li> </ul> |
| 4 | CarbonScore | <ul> <li>Stellt dem User eine Oberfläche zur Verfügung, welche über den Browser mit http angesprochen werden kann</li> </ul> |
| 5 | API | <ul> <li>Erhält Anfragen als JSON über http</li> <li>Sendet Antworten als JSON über http</li> </ul> | 

 

**Erläuterung der externen fachlichen Schnittstellen**

| ID | Schnittstelle | Beschreibung |
|--------------|----------------|-------------------|
| 1 | CarbonInterface | <ul> <li>Der Schnittstelle müssen Details zur Aktivität zur Verfügung gestellt werden, die CO² abgeben</li> <li>Verwendet die präziseste Methodik im Bereich zur Berechnung der geschätzten CO² Emission</li> <li>Sendet eine Antwort, zur Verwendung im System</li> </ul> |
  

## Technischer Kontext


![technisches Kontextdiagramm](https://github.com/Major-Wudy/sqs-application/assets/47253607/2cee32e4-49d2-4d28-aaf9-be901545418a)

  

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

![Scope_and_context](https://github.com/Major-Wudy/sqs-application/assets/47253607/d9373f73-9433-4c38-9253-29d401b7f284)

![level1-whitebox](https://github.com/Major-Wudy/sqs-application/assets/47253607/d8d6e085-7c93-4fe6-a994-18bd491c9edc)



*Begründung:*  

Die Applikation wird in eine persistente Datenhaltung, eine externe API zur Berechnung der geschätzten CO² Emissionen und der Geschäftslogik unterteilt.
- Die Applikation ist kein Datebnakmanagementsystem, daher wird für die persistente Datenhaltung ein Nachbarsystem benötigt
- Die Applikation hat keine Möglichkeit zur Eigenberechnung der geschätzen CO² Emissionen, daher wird eine 3rd Party API zur Berechnung benötigt
  

*Enthaltene Bausteine:*
- Carbonscore: Bearbeitet Nutzeranfragen und bereitet diese für das jeweilige Nachbarsystem vor und verarbeitet die zurückgemeldeten Anworten der Systeme für Anwender
- Datenbank: Sopeichert notwendige persistene Daten
- Carboninterface API: Errechnet die geschätzen CO² Emissionen für die übermittelten Werte
  

Wichtige Schnittstellen  

| **Name**        | **Verantwortung** |
|-----------------|-------------------|
| Carboninterface API | Zur Errechnung der geschätzen CO² Emissionen einer Aktivität. |
| Datenbank | Speicherung von Daten der Anwendung über die Laufzeit einer Session hinweg. |
| Infrastructure Service Interface | Zugriff auf die Datenbank ist über dieses Interface möglich.| |
| Domain Service Interface | Zugriff auf die Geschäftslogik in den Domain Services über dieses Interface möglich.|

  

### Carboninterface
*Zweck*

Die Applikation hat selbst keine Möglichkeiten zur Berechnung von CO² Emissionen und nutzt daher diese 3rd Party API zur Berechnung dieser. Die Carboninterface API liefert anhand übermittelter Daten die geschätze CO² Emission für die Aktivität. Dabei werden Die Daten als JSON bereitgestellt und enthalten ermittelten Werte in gm kg, lb und mt.

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
- Rückgabe der CO² Emissionen bei Übergabe einer Aktivität 

*Probleme*
- Im freien Plan sind nur 200 Calls pro Monat möglich, mehr muss finanziell per ABo gelöst werden


### Datenbank
*Zweck*

Speichern der Token zur Kommunikation mit der eigenen API, Zwischenspeicherung der gesendeten Request, damit bei Systemabsturz eine Queue zum Abarbeiten entsteht, Speichern der CO² Emissionen für einen User.

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

## Ebene 2

  

### Whitebox *\<Baustein 1>*

  

*\<Whitebox-Template>*

  

### Whitebox *\<Baustein 2>*

  

*\<Whitebox-Template>*

  

…

  

### Whitebox *\<Baustein m>*

  

*\<Whitebox-Template>*

  

## Ebene 3

  

### Whitebox \<\_Baustein x.1\_\>

  

*\<Whitebox-Template>*

  

### Whitebox \<\_Baustein x.2\_\>

  

*\<Whitebox-Template>*

  

### Whitebox \<\_Baustein y.1\_\>

  

*\<Whitebox-Template>*

  

# Laufzeitsicht

  

## *\<Bezeichnung Laufzeitszenario 1>*

  

-   \<hier Laufzeitdiagramm oder Ablaufbeschreibung einfügen>

### Ablaufbeschreibung
1. gewünschte Aktivität über die UI auswählen (Electricity, Flight, Shipping, Fuel)
1. Daten der ausgewählten Aktivität in die UI nach vorgegebenem Schema (JSON) eingeben
1. Über die UI den HTTP POST Request mit den gewünschten Daten absenden
1. Auf Rückmeldung des Systems warten

  

-   \<hier Besonderheiten bei dem Zusammenspiel der Bausteine in diesem

    Szenario erläutern>

  

## *\<Bezeichnung Laufzeitszenario 2>*

  

…

  

## *\<Bezeichnung Laufzeitszenario n>*

  

…

  

# Verteilungssicht

  

## Infrastruktur Ebene 1

  

***\<Übersichtsdiagramm>***

  

Begründung  

*\<Erläuternder Text>*

  

Qualitäts- und/oder Leistungsmerkmale  

*\<Erläuternder Text>*

  

Zuordnung von Bausteinen zu Infrastruktur  

*\<Beschreibung der Zuordnung>*

  

## Infrastruktur Ebene 2

  

### *\<Infrastrukturelement 1>*

  

*\<Diagramm + Erläuterungen>*

  

### *\<Infrastrukturelement 2>*

  

*\<Diagramm + Erläuterungen>*

  

…

  

### *\<Infrastrukturelement n>*

  

*\<Diagramm + Erläuterungen>*

  

# Querschnittliche Konzepte

  

## *\<Konzept 1>*

  

*\<Erklärung>*

  

## *\<Konzept 2>*

  

*\<Erklärung>*

  

…

  

## *\<Konzept n>*

  

*\<Erklärung>*

  

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
| 2 | Bei Systemabsturz soll sich die selbst neustarten. Dies soll die Anwendung 5x veruschen, bevor es in einen dauerhaften Fehlerzustand übergeht. |
| 3 | Beim Ausfall einer Instanz der Anwendung soll die Möglichkeit besitzen, den Trafiic der ausgefallenen Instanz auf andere Instanzen weiterzugeben. |
| 4 | Ist eine externe Schnittstelle nicht verfügbar, soll das System einen Hinweis darauf liefern und weiterlaufen. |
| 5 | Die Logik des Systems ist durch Unittests getestet und kann durch ein Tool ausgewertet werden. Die Auswertung der Testabdeckung muss dabei >= 80% sein. |
| 6 | Wird eine ander Datenbank oder ein andere Schnittstelle zur Berechnung des CarbonScores verwendet, kann diese ohne Anpassung der Fachlichkeit ausgetauscht und implementiert werden. |
| 7 | Eine Funktion soll leicht verständlich sein und damit eine kognitiven Last von <= 15 sein. Diese soll über ein externes Tool geprüft werden. |
| 8 | Bei Verbesserungen oder neuen Funktionen sollen diese in das Sytem implementiert werden können, ohne dass der Fachliche Kern der Anwendung angepasst werden muss. Beispiel: Hinzufügen eines Benutzerprofils für das Speicher der gesendeten Anfragen pro Benutzer |
| 9 | Ein Anwender kann ohne weitere Dokumentation zur Verwendung der Anwendung die Anwendung erfolgreich bedienen. |
| 10 | Die Anwendung soll innerhalb einer Sekunde eine Anwort an den Anwender senden. |
| 11 | Egal ob Windwos, Mac oder Linux: Die Anwendung ist unter allen Betriebssystemen ausführbar. |
| 12 | Die Anwendung kann von einem System auf das andere portiert werden. Beispiel: Virtualisierte Anwendung als Docker Container. |
| 13 | Anfragen an die Software können nur mit Token, die von der Anwendung ausgestellt sind erfolgen. Beispiel Auth mit Bearer Token für die API. |
  

# Risiken und technische Schulden

  

# Glossar

  

| Begriff        | Definition        |

|----------------|-------------------|

| *\<Begriff-1>* | *\<Definition-1>* |

| *\<Begriff-2*  | *\<Definition-2>* |


