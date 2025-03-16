# Use Case: UC 1.04 – Alarm bei Leistungsabweichung

## Ziel
Das System erkennt eine Abweichung von den erwarteten Leistungswerten und gibt automatisch eine Warnung aus.

## Akteure
- System (automatischer Sensor)
- Medizinisches Personal (Arzt, Labortechniker)

## Vorbedingungen
- Ein Leistungstest läuft.
- Sensoren erfassen kontinuierlich Leistungswerte (z. B. Herzfrequenz, Laktatwerte, Sauerstoffsättigung).

## Hauptablauf
1. Der Leistungstest beginnt, und die Sensoren erfassen regelmäßig die physiologischen Werte des Probanden.
2. Das System vergleicht die erfassten Werte mit den vordefinierten Grenzwerten.
3. Wenn eine Abweichung festgestellt wird, löst das System automatisch einen Alarm aus.
4. Der Alarm wird visuell (z. B. rotes Warnsymbol auf dem Bildschirm) und akustisch (Warnton) ausgegeben.
5. Das medizinische Personal wird benachrichtigt und kann eingreifen.
6. Falls notwendig, kann der Test abgebrochen oder eine Anpassung der Belastung vorgenommen werden.

## Alternative Abläufe
- **A1:** Falls der Wert nach kurzer Zeit wieder in den normalen Bereich fällt, wird der Alarm automatisch deaktiviert.
- **A2:** Falls der Wert weiter außerhalb des sicheren Bereichs bleibt, wird eine Eskalation eingeleitet (z. B. automatische Testunterbrechung).

## Fehlerfälle
- **F1:** Sensorfehler → Das System erkennt eine fehlerhafte Messung und fordert eine manuelle Überprüfung.
- **F2:** Alarm wurde fälschlicherweise ausgelöst → Das medizinische Personal kann eine manuelle Bewertung vornehmen und den Alarm zurücksetzen.

## Ergebnis
Das medizinische Personal wird frühzeitig über kritische Leistungsabweichungen informiert und kann angemessen reagieren.

## Notizen
Die Grenzwerte für die Abweichung sind anpassbar und können je nach Proband individuell eingestellt werden.
