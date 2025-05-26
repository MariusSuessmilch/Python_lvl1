# Tutorial: Python Funktionen - Notenschnitt berechnen
# ====================================================

"""
🎯 WARUM BRAUCHEN WIR FUNKTIONEN?

Stell dir vor, du musst immer wieder den Notenschnitt berechnen:
- Für deine Klausuren in Mathe
- Für deine Tests in Deutsch  
- Für die Noten deiner Freunde
- Für verschiedene Fächer

Würdest du jedes Mal den gleichen Code neu schreiben? 
Das wäre mühsam und fehleranfällig!

Funktionen lösen dieses Problem: 
✅ Einmal schreiben, überall verwenden
✅ Code wird übersichtlicher
✅ Weniger Fehler
✅ Einfacher zu ändern

Denkst du, dass schon mal jemand eine Funktion geschrieben hat, 
die den Durchschnitt berechnet? Bestimmt! 
Aber lernen wir, wie wir unsere eigenen Funktionen erstellen.
"""

# ====================================================
# 📚 SCHRITT 1: DAS PROBLEM OHNE FUNKTIONEN
# ====================================================

print("=== Notenschnitt OHNE Funktionen ===")
print()

# Notenschnitt für Mathe berechnen
mathe_noten = [2, 1, 3, 2, 1]
summe_mathe = 0
for note in mathe_noten:
    summe_mathe += note
schnitt_mathe = summe_mathe / len(mathe_noten)
print(f"Mathe-Notenschnitt: {schnitt_mathe:.2f}")

# Notenschnitt für Deutsch berechnen (GLEICHER CODE!)
deutsch_noten = [1, 2, 2, 1, 3]
summe_deutsch = 0
for note in deutsch_noten:
    summe_deutsch += note
schnitt_deutsch = summe_deutsch / len(deutsch_noten)
print(f"Deutsch-Notenschnitt: {schnitt_deutsch:.2f}")

print()
print("😩 Das war viel zu viel gleicher Code!")
print("💡 Lass uns eine Funktion schreiben!")
print()

# ====================================================
# 🚀 SCHRITT 2: UNSERE ERSTE FUNKTION
# ====================================================

def notenschnitt_berechnen(noten_liste):
    """
    Berechnet den Durchschnitt einer Liste von Noten.
    
    Parameter:
    noten_liste (list): Eine Liste mit Noten (z.B. [1, 2, 3])
    
    Rückgabe:
    float: Der Notenschnitt
    """
    # Alle Noten zusammenzählen
    summe = 0
    for note in noten_liste:
        summe += note
    
    # Durchschnitt berechnen
    schnitt = summe / len(noten_liste)
    return schnitt

# ====================================================
# ✨ SCHRITT 3: FUNKTION VERWENDEN
# ====================================================

print("=== Notenschnitt MIT Funktionen ===")
print()

# Jetzt können wir unsere Funktion überall nutzen!
mathe_noten = [2, 1, 3, 2, 1]
deutsch_noten = [1, 2, 2, 1, 3]
englisch_noten = [2, 2, 1, 3, 2]

# Viel sauberer und kürzer!
print(f"Mathe-Notenschnitt: {notenschnitt_berechnen(mathe_noten):.2f}")
print(f"Deutsch-Notenschnitt: {notenschnitt_berechnen(deutsch_noten):.2f}")
print(f"Englisch-Notenschnitt: {notenschnitt_berechnen(englisch_noten):.2f}")

print()

# ====================================================
# 🎉 SCHRITT 4: ERWEITERTE FUNKTION
# ====================================================

def notenschnitt_mit_info(noten_liste, fach_name):
    """
    Berechnet Notenschnitt und gibt schöne Ausgabe zurück.
    
    Parameter:
    noten_liste (list): Liste mit Noten
    fach_name (str): Name des Fachs
    
    Rückgabe:
    str: Formatierte Ausgabe mit allen Infos
    """
    if len(noten_liste) == 0:
        return f"{fach_name}: Keine Noten vorhanden!"
    
    schnitt = notenschnitt_berechnen(noten_liste)  # Unsere andere Funktion nutzen!
    anzahl = len(noten_liste)
    beste_note = min(noten_liste)  # In Deutschland: 1 ist die beste Note
    schlechteste_note = max(noten_liste)
    
    return f"{fach_name}: {schnitt:.2f} (aus {anzahl} Noten, beste: {beste_note}, schlechteste: {schlechteste_note})"

print("=== Erweiterte Funktion ===")
print(notenschnitt_mit_info([1, 2, 1, 3, 2], "Biologie"))
print(notenschnitt_mit_info([2, 2, 1, 1, 3], "Geschichte"))
print(notenschnitt_mit_info([], "Sport"))  # Test mit leerer Liste

print()

# ====================================================
# 📝 AUFGABEN FÜR DICH
# ====================================================

print("=== DEINE AUFGABEN ===")
print()

print("🎯 AUFGABE 1 (mit Hilfe):")
print("Schreibe eine Funktion 'ist_bestanden', die prüft ob der Notenschnitt besser als 4.0 ist")
print()

def ist_bestanden(noten_liste):
    """
    Prüft ob der Notenschnitt zum Bestehen reicht (besser als 4.0).
    
    TIPP: Verwende die Funktion notenschnitt_berechnen() von oben!
    TIPP: In Deutschland bedeutet Note 4 = ausreichend, alles darüber ist durchgefallen
    
    Parameter:
    noten_liste (list): Liste mit Noten
    
    Rückgabe:
    bool: True wenn bestanden, False wenn nicht bestanden
    """
    # TODO: Schreibe hier deinen Code
    # schnitt = notenschnitt_berechnen(noten_liste)
    # return schnitt <= 4.0
    pass

# Test deine Funktion:
# print(f"Bestanden? {ist_bestanden([3, 4, 2, 3])}")  # Sollte True sein
# print(f"Bestanden? {ist_bestanden([5, 6, 4, 5])}")  # Sollte False sein

print()
print("🎯 AUFGABE 2 (ohne Hilfe):")
print("Schreibe eine Funktion 'note_zu_text', die eine Zahl in einen Text umwandelt:")
print("1 = 'sehr gut', 2 = 'gut', 3 = 'befriedigend', 4 = 'ausreichend', 5 = 'mangelhaft', 6 = 'ungenügend'")
print()

def note_zu_text(note):
    """
    Wandelt eine Notenzahl in einen Beschreibungstext um.
    
    Parameter:
    note (int): Note als Zahl (1-6)
    
    Rückgabe:
    str: Beschreibung der Note als Text
    """
    # TODO: Schreibe hier deinen Code komplett selbst!
    # TIPP: Verwende if/elif/else
    pass

# Test deine Funktion:
# print(f"Note 1 ist: {note_zu_text(1)}")
# print(f"Note 3 ist: {note_zu_text(3)}")
# print(f"Note 6 ist: {note_zu_text(6)}")

print()
print("🎯 BONUS-AUFGABE:")
print("Erstelle eine Funktion, die alle Noten einer Liste in Texte umwandelt.")

def noten_liste_zu_text(noten_liste):
    """
    Wandelt eine Liste von Noten in eine Liste von Texten um.
    
    Parameter:
    noten_liste (list): Liste mit Noten als Zahlen
    
    Rückgabe:
    list: Liste mit Noten als Texte
    """
    # TODO: Bonus-Aufgabe für die Schnellen!
    # TIPP: Verwende deine note_zu_text() Funktion!
    # TIPP: Gehe durch die Liste mit einer for-Schleife
    pass

# Test:
# test_noten = [1, 3, 2, 4, 2]
# print(f"Noten als Zahlen: {test_noten}")
# print(f"Noten als Text: {noten_liste_zu_text(test_noten)}")

print("💫 Viel Erfolg beim Programmieren!")
print("💡 Nutze den Cascade Chat, wenn du Hilfe brauchst!")