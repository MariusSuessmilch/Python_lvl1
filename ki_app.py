import streamlit as st
from gpt_helper import chat_gpt

# Aufgabe 1
# TODO Welche Aufgabe soll die KI für dich erledigen? Lege einen passenden Titel für deine App fest.
st.title("Meine App")

# Hier kann der Benutzer seine Frage an die KI eingeben. Diese Zeile kannst du so stehen lassen.
user_prompt = st.text_input("Deine Anfrage an die KI")

# Aufgabe 2
# system_prompt legt fest, wie das KI-Modell auf Anfragen reagiert. 
# TODO formuliere den Systemprompt und ersetze den bisherigen prompt dadurch.
system_prompt = "Du bist ein KI Assistent, der hilfreich und motivierend ist."

if user_prompt: 
    response = st.write_stream(chat_gpt(user_prompt, system_prompt))
