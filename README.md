### SS-2425 SWE

# Use Case: UC 1.04 – Alarm bei Leistungsabweichung

## Ziel
Das System erkennt eine Abweichung von den erwarteten Leistungswerten und gibt automatisch eine Warnung aus.

## Akteure
- System (automatischer Sensor)
- Medizinisches Personal (Arzt, Labortechniker)

## Vorbedingungen
- Ein Leistungstest läuft.
- Sensoren erfassen kontinuierlich Leistungswerte (z. B. Herzfrequenz, Sauerstoffsättigung).

## Hauptablauf
1. Der Leistungstest beginnt, und die Sensoren erfassen regelmäßig die Vitalwerte des Probanden.
2. Das System vergleicht die erfassten Werte mit den definierten Grenzwerten.
3. Wenn eine Abweichung festgestellt wird, löst das System automatisch einen Alarm aus.
4. Der Alarm wird visuell und akustisch ausgegeben.
5. Dadurch wird das medizinische Personal benachrichtigt und kann eingreifen.
6. Falls notwendig, kann der Test abgebrochen oder eine Anpassung der Belastung vorgenommen werden.

## Alternative Abläufe
- **A1:** Falls die Werte nach kurzer Zeit wieder in den normalen Bereich fallen, wird der Alarm automatisch deaktiviert.
- **A2:** Falls die Werte weiter außerhalb des sicheren Bereichs bleiben, kommt es zu einem Not-Halt.

## Fehlerfälle
- **F1:** Sensorfehler: Das System erkennt eine fehlerhafte Messung und fordert eine manuelle Überprüfung.
- **F2:** Alarm wurde fälschlicherweise ausgelöst:  Das medizinische Personal kann eine manuelle Bewertung vornehmen und den Alarm zurücksetzen.

## Ergebnis
Das medizinische Personal wird frühzeitig über kritische Leistungsabweichungen informiert und kann angemessen reagieren.

## Notizen
Die Grenzwerte für die Abweichung sind anpassbar und können je nach Proband individuell eingestellt werden.
