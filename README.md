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
| 1 | User | Hier wird der Input für die Anwendung generiert. Benutzt die Schnittstellen CarbonInterface indirekt und die Schnittstelle Auth0 direkt zur Anmeldung am System. Greift direkt auf das System CarbonScore zu. |
| 2 | CarbonInterface | Ist eine API zur Berechnung der CO²-Emissionen einer Aktivität. CarbonScore verwendet das CarbonInterface direkt und ist über einen API-Key angebunden.|
| 3 | Auth0 Interface | Ist eine API, welche die Userauthentifizierung übernimmt und nur über Auth0 authentifizierte User in die Anwendung lässt. CarbonScore verwenden Auth0 direkt als Authentifizierungsmöglichkeit. |
| 4 | Database | CarbonScore speichert die Daten der User in der Datenbank für persistente Datenhaltung.|
| 5 | API | CarbonScore stelle eine eigene API zur Verfügung gegen welche entwickelt werden kann. |

*Risiko: Aufgrund der Vielfältigkeit des Internets und der unterschiedlichen Browser und Infrastrukturen der Anwender kann es bei diesen Systemen durch die Fernverbindung zu Netzwerk- und Latenzproblemen kommen. Die Absicherung und Robustheit der Schnittstelle muss daher speziell betrachtet werden.


Liste der Kommunikationsbeziehungen:
| ID           | Nachbar | Kommunikationsbeziehung/Schnittstelle |
|--------------|----------------|-------------------|
| 1 | User | - Liefert Inputdaten zu einer CO²-Emissionsaktivität - Erhält CO²-Emissionen zur eingegeben Aktivität und einen montalichen CO²-Emissionen Score - Liefert Eingaben für die Anwendung über ein Userinterface (UI)  |
| 2 | CarbonInterface | - Erhält über https und Api-Key eine JSON Anfrage mit Details zu einer CO²-Emissionsaktivität - Gibt als Antwort ein JSON über http zurück | 
| 3 | Auth0 | - Erhält über http einen Request für die Authentifizierung - Sendet User Infos als JSON und Access Tokes über http |
| 4 | Database | - Verbindet sich per Verbindungsstring mit der Anwendung - Tauscht über einen Connector SQL Queries mit der Anwendung aus |
| 5 | CarbonScore | - Stellt dem User eine Oberfläche zur Verfügung, welche über den Browser mit http angesprochen werden kann |
| 6 | API | - Erhält Anfragen als JSON über http - Sendet Antworten als JSON über http | 

 

**Erläuterung der externen fachlichen Schnittstellen**

| ID | Schnittstelle | Beschreibung |
|--------------|----------------|-------------------|
| 1 | CarbonInterface | - Der Schnittstelle müssen Details zur Aktivität zur Verfügung gestellt werden, die CO² abgeben - Verwendet die präziseste Methodik im Bereich zur Berechnung der geschätzten CO² Emission - Sendet eine Antwort, zur Verwendung im System |
| 2 | Auth0 | - Stellt eine Anmeldeverfahren/Authentifizierungsverfahren für das System zur Verfügung - Verwaltet die Userverbindung zur Anwendung und deren Access Tokens |
  

## Technischer Kontext


![technisches Kontextdiagramm](https://github.com/Major-Wudy/sqs-application/assets/47253607/2cee32e4-49d2-4d28-aaf9-be901545418a)

  

**Erläuterung der externen technischen Schnittstellen**

| ID | Schnittstelle | Beschreibung |
|--------------|----------------|-------------------|
| 1 | CarbonInterface | - Authorisierung über ein Bearer Token  - Input als JSON mit Content-Type application/json - Sendet JSON als Antwort |
| 2 | Auth0 | tdb |
  

**Mapping fachliche auf technische Schnittstellen**
| ID | Schnittstelle | Mapping |
|--------------|----------------|-------------------|-------------------|
| 1 | CarbonInterface | - Authentifizierung einer Anfrage über CarbonScore per Bearer Token - Stellt die Daten der CO²-Emissionsaktivität als JSON für die CarbonInterface API zur Verfügung - CarbonScore erhält von CarbonInterface eine JSON Antwort zur Weiterverarbeitung |
| 2 | Auth0 | - Anwender wird über die Authentifizierungsmethode per Socials für CarbonScore authentifiziert und erlangt Zugriff auf CarbonScore - Anwenderdaten für CarbonScore werden per Access Token als JSON angefordert. |

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
| Kontext | In welcher Programmiersprache soll die Anwendung entwickelt werden? Zur Auswahl stehen Java, .Net oder python |
| Entscheidung | tbd | 
| Status | proposed | 
| Konsequenzen | tbd |

# Qualitätsanforderungen

  

<div class="formalpara-title">

  

**Weiterführende Informationen**

  

</div>

  

Siehe [Qualitätsanforderungen](https://docs.arc42.org/section-10/) in

der online-Dokumentation (auf Englisch!).

  

## Qualitätsbaum

  

## Qualitätsszenarien

  

# Risiken und technische Schulden

  

# Glossar

  

| Begriff        | Definition        |

|----------------|-------------------|

| *\<Begriff-1>* | *\<Definition-1>* |

| *\<Begriff-2*  | *\<Definition-2>* |


