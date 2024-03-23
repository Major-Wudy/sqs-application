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

Die Anwendung ermöglicht es einem Anwender seinen Co²-Abdruck zu ermitteln, indem man auf sich zugeschnitten Co² austoßende Aktivitäten über die Anwendung anlegen kann. Diese eingegeben Daten werden einer API übergeben, welche die CO²-Emmissionen dieser Aktivität berechnet und zurück liefert. Die Anwendung dient als Management und Historie der eingetragenen Aktivitäten und zeigt in der Übersicht den aktuellen Carbon Score des Monats an basieren auf den eingegebenen Aktivitäten einer Person.

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
| Anwender | tdb  | Das System funktioniert, ist benutzerfreundlich und erfüllt die Erwartung, die der Anwender vom System hat |
| andere Entwickler/Maintainer | tdb | Das System ist wartbar, modizifierbar und lässt sich luaffähig aufsetzen |

  

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

![image](https://github.com/Major-Wudy/sqs-application/assets/47253607/39575ab4-e20c-4277-8b23-7fc9c3855d0f)

Liste von Kommunikationsbeziehungen und deren Schnittstellen:
| ID           | Nachbar        | Beschreibung |
|--------------|----------------|-------------------|
| 1 | User | Hier wird der Input für die Anwendung generiert. Benutzt die Schnittstellen CarbonInterface indirekt und die Schnittstelle Auth0 direkt zur Anmeldung am System. Greift direkt auf das System CarbonScore zu. |
| 2 | CarbonInterface | Ist eine API zur Berechnung der CO²-Emmissionen einer Aktivität. CarbonScore verwendet das CarbonInterface direkt und ist über einen API-Key angebunden. Kommunikation findet über das Internet per https statt. |
| 3 | Auth0 Interface | Ist eine API, welche die Userauthentifizierung übernimmt und nur über Auth0 authentifizierte User in die Anwendung lässt. CarbonScore verwenden Auth0 direkt als Authentifizierungsmöglichkeit. Kommunikation findet über das Internet per https statt. |
| 4 | Database | CarbonScore speichert die Daten der User in der Datenbank für persistente Datenhaltung. Kommunikation findet per Datenbanktreiber (ODBC) statt. |
| 5 | CarbonScore | Implementiert die Schnittstellen CarbonInterface zur Berechnung der CO²-Emmissionen einer Aktivität, Auth0 als Authentifizierungsmöglichkeit und eine Datenbank als persistenten Datenspeicher. Die Anwendung stellt dem User eine Benutzeroberfläche als Webanwendung zur Verfügung. Kommunikation findet über das Internet per http (localhost) / https (production) statt. |




## Fachlicher Kontext
Die 
  

**\<Diagramm und/oder Tabelle>**

  

**\<optional: Erläuterung der externen fachlichen Schnittstellen>**

  

## Technischer Kontext

  

**\<Diagramm oder Tabelle>**

  

**\<optional: Erläuterung der externen technischen Schnittstellen>**

  

**\<Mapping fachliche auf technische Schnittstellen>**

  

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


