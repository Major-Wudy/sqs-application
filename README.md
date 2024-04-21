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
| 1 | Zuverlässigkeit | Das System führt Funktionen unter den festgelegten Bedingungen und Umgebungen aus. Geringe "meantime zo recovery" und niedrige Anzahl an Ausfällen. | 
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
| Auth0 | https://auth0.com/ | Verwendung der API nach Vorgaben des Anbieters |

  

# Randbedingungen

Technischer Art:
- Deployment und Entwicklung mit Docker (damit verbundenes OS in Docker ist Linux - Ubuntu)
- Programmiersprache des Backends ist Python
- Framework: ?
- Frontend: HTML und Bootstrap 5
- Datenbank: MongoDB
- Externes Systeme: https://docs.carboninterface.com/#/, Auth0 https://auth0.com/
- API-Dokumentation mit Swagger für pyhton

Organisatorischer Art:
- Zeit: xx.06.24 Ende Sommersemester 2024
- Budget: kein finanzielles Interesse
- Dokumente und Unterlage aus der Vorlesung SQS beeinflussen die Entwicklung
- 
  

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

  

# Bausteinsicht

  

## Whitebox Gesamtsystem

  

***\<Übersichtsdiagramm>***

  

Begründung  

*\<Erläuternder Text>*

  

Enthaltene Bausteine  

*\<Beschreibung der enthaltenen Bausteine (Blackboxen)>*

  

Wichtige Schnittstellen  

*\<Beschreibung wichtiger Schnittstellen>*

  

### \<Name Blackbox 1>

  

*\<Zweck/Verantwortung>*

  

*\<Schnittstelle(n)>*

  

*\<(Optional) Qualitäts-/Leistungsmerkmale>*

  

*\<(Optional) Ablageort/Datei(en)>*

  

*\<(Optional) Erfüllte Anforderungen>*

  

*\<(optional) Offene Punkte/Probleme/Risiken>*

  

### \<Name Blackbox 2>

  

*\<Blackbox-Template>*

  

### \<Name Blackbox n>

  

*\<Blackbox-Template>*

  

### \<Name Schnittstelle 1>

  

…

  

### \<Name Schnittstelle m>

  

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
| Titel | Architektur der Anwendung |
| Kontext | In welchem Architektur Modell soll die Anwendung entwickelt werden? Layer oder Oinion |
| Entscheidung | Onion architecture | 
| Status | accepted | 
| Konsequenzen | Die Anwendung wird aufgrund der angestrebten Wartbarkeit in der onion Architektur entwickelt. |

| **Kategorie** | **Bemerkung** |
|-----------------|-------------------|
| Titel | Deployment der Anwendung |
| Kontext | Auf welche Art soll die Anwendung deployed werden? |
| Entscheidung | Docker | 
| Status | proposed | 
| Konsequenzen | tbd |

# Qualitätsanforderungen

  

## Qualitätsbaum

| **Qualitätskategorie** | **Qualität** | **Beschreibung** | **Qualitätsszenario** |
|-----------------|-------------------|-------------------|-------------------|
| Zuverlässigkeit (1) | Robustheit | Das System soll zuverlässig unter den angegebenen Laufzeitumgebung laufen. | |
| | Geringe meantime to recovery | Das System soll nach einem Ausfall schnellstmöglich wieder verfügbar sein. | |
| | Ausfallsicherheit | Das System soll multiinstanzfähig sein. | |
| | Verfügbarkeit | Bei nicht vorhanden sein der externen Schnittstellen soll das System den Anwender über die eingeschränkte Funktionalität informieren. | 
| | Tests | Das System soll eine Codecoverage von >= 80% aufweisen. | |
| Wartbarkeit (2) | Wartung | Es sollen außerhalb des fachlichen Kerns der Anwendung Komponenten ausgetauscht werden können, ohne die Fachlichkeit der Anwendung zu beeinflussen. | |
| | Verbesserung | Es sollen Verbesserungen für die Anwendung implementiert werden können, die die bestehende Fachlichkeit erweitern ohne diese zu verändern. | | 
| | Reparatur | Bei einem Ausfall soll die Anwendung einen Recovery und Backup Plan verfolgen für sachgerechtes wiederaufsetzen des Systems | |
| Benutzerfreundlichkeit (3) | einfache Handhabung | Einfache Handhabung für umweltbewusste Personen, speziell bezogen auf eine kurze Zeit zur Eingabe der Daten und bis zum Ergebnis. | | 
| | einfaches Erlernen | Die Oberfläche der Anwendung ist selbsterklärend und Funktionen, die komplexer sind, sind Hilfestellungen für den Anwender leicht einsehbar und ersichtlich | |
| | Effizienz | Die Anwendung soll in zufriedenstellender Zeit eine Antowrt auf die Eingaben des Anwenders liefern. | |
| | Rechtschreibung | Die Oberflächen sollen keine Rechtschreibfehler enthalten. | |
| | Grammatik | Die Oberflächen sollen keine Grammatikfehler enthalten. | |
| Übertragbarkeit (4) | Betriebssystem unabhängig | Das System soll unabhängig vom Betriebssystem lauffähig sein. | |
| | Übertragbar | Das System soll leicht von einem System auf ein anderes überführt werden können. | |
| Sicherheit | Abgesichert | Anfragen sollen nur von authentifizierten Anwendern getätigt werden können. | |
| | Datensicherheit | Bei einem Ausfall sollen die Daten gesichert und persistent verfügbar sein. | |  
| Kulturell und Regional | Mehrsprachig | Die Benutzeroberflächen der Anwendung sollen in deutscher und englischer Sprache verfügbar sein. | | 

## Qualitätsszenarien

| **ID** | **Beschreibung** |
|-----------------|-------------------|
| 1 | tbd | 
  

# Risiken und technische Schulden

  

# Glossar

  

| Begriff        | Definition        |

|----------------|-------------------|

| *\<Begriff-1>* | *\<Definition-1>* |

| *\<Begriff-2*  | *\<Definition-2>* |


