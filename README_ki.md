# KI-App mit Streamlit – Dein Mini-Workshop

In diesem Mini-Workshop baust du Schritt für Schritt deine eigene kleine KI-Anwendung mit Streamlit. Du entscheidest selbst, was die KI für dich tun soll! Gehe die Aufgaben der Reihe nach durch und probiere alles direkt im Code aus.

---

### Einführung: Variablen in Python

Variablen sind wie kleine Boxen, in denen du Informationen speichern kannst. Du gibst ihnen einen Namen und kannst ihnen Werte zuweisen, zum Beispiel Zahlen oder Texte. Variablen helfen dir dabei, Daten im Programm zu merken und später wiederzuverwenden. Ohne Variablen könntest du keine Benutzereingaben speichern oder Berechnungen durchführen!

Beispiel:
```python
name = "Anna"
punkte = 5
```

## Aufgabe 1: Überlege dir eine KI-Anwendung

Überlege dir, welche Aufgabe die KI für dich erledigen soll.

- Beispiele: Lass dir Schulthemen erklären, Texte übersetzen oder aus Stichpunkten einen Text machen.
- Du kannst dir auch eine ganz eigene Anwendung ausdenken!

> **Tipp:** Schreibe deine Idee als Kommentar oben in die Datei `gpt_app.py`.

---

## Aufgabe 2: Passe den Titel deiner App an

Passe den Titel der App so an, dass er zu deiner Anwendung passt.

- Suche im Code die Zeile mit `st.title("Formulierungsmaschine")`.
- Ändere den Text in den Titel, der zu deiner Idee passt, zum Beispiel:
  ```python
  st.title("Dein eigener Vokabeltrainer")
  ```

> **Hinweis:** Der Titel erscheint oben in deiner Web-App.

---

## Aufgabe 3: Erkläre der KI ihre Aufgabe

Im sogenannten `system_prompt` kannst du der KI genau erklären, was sie für dich tun soll.

- Suche im Code die Zeile mit `system_prompt = ...`.
- Beschreibe, wie die KI antworten soll (z.B. einfach, für Grundschüler, als Liste, als Gedicht ...).
- Gib der KI eine Rolle und eine Aufgabe. Beispiele:
  ```python
  system_prompt = "Du bist Mathematiklehrer, erkläre für einen Grundschüler, wie Multiplikation funktioniert. Gib einen kurzen, motivierenden Erklärtext aus."
  ```

> **Tipp:** Je genauer du bist, desto besser wird die Antwort der KI.


