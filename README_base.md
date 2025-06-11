# Eis-Bewertungs-App – Dein Mini-Workshop

In diesem Mini-Workshop baust du eine eigene kleine App, mit der du verschiedene Eissorten bewerten kannst. Gehe die Aufgaben Schritt für Schritt durch und probiere alles direkt im Code aus!

---

### Einführung: Variablen in Python

Variablen sind wie kleine Boxen, in denen du Informationen speichern kannst. Du gibst ihnen einen Namen und kannst ihnen Werte zuweisen, zum Beispiel Zahlen oder Texte. Variablen helfen dir dabei, Daten im Programm zu merken und später wiederzuverwenden. Ohne Variablen könntest du keine Benutzereingaben speichern oder Berechnungen durchführen!

Beispiel:
```python
name = "Anna"
punkte = 5
```

## Aufgabe 1: Titel und Beschreibung

Gib deiner App einen passenden Titel und eine kurze Beschreibung.

- Suche im Code die Zeile mit `st.title()` und trage dort einen Titel ein, zum Beispiel:
  ```python
  st.title("Eis-Bewertungs-App")
  ```
- Schreibe darunter eine kurze Beschreibung mit `st.write()`, zum Beispiel:
  ```python
  st.write("Trage deine Lieblings-Eissorte ein und bewerte sie auf einer Skala von 1 bis 10!")
  ```

---

## Aufgabe 2: Eissorte & Bewertung

Baue die Eingabeelemente für die Bewertung ein:

- Erstelle ein Textfeld, in das du eine Eissorte eintragen kannst:
  ```python
  eissorte = st.text_input("Welche Eissorte möchtest du bewerten?")
  ```
- Füge einen Slider hinzu, mit dem du eine Bewertung von 1 bis 10 auswählen kannst:
  ```python
  bewertung = st.slider("Wie lecker findest du diese Sorte?", min_value=1, max_value=10, value=5)
  ```

---

## Aufgabe 3: Bewertung anzeigen

### Einführung: f-strings in Python

Mit sogenannten f-strings kannst du Variablen ganz einfach in Texte einbauen. Das macht Ausgaben übersichtlicher und deinen Code einfacher zu lesen. Du schreibst einfach ein `f` vor die Anführungszeichen und setzt Variablennamen in geschweifte Klammern:

```python
name = "Anna"
punkte = 5
print(f"{name} hat {punkte} Punkte!")
```

Das Ergebnis ist: `Anna hat 5 Punkte!`


Füge einen Button hinzu. Wenn du darauf klickst, soll die Bewertung für die eingegebene Eissorte angezeigt werden.

- Beispiel:
  ```python
  if st.button("Bewertung abgeben"):
      st.success(f"Du hast '{eissorte}' mit {bewertung}/10 Punkten bewertet!")
  ```

---

> **Tipp:** Nutze die Beispiele aus der Hilfsapp unter "2. Eingabe-Elemente". Probiere verschiedene Eissorten und Bewertungen aus!
