import streamlit as st
from datetime import datetime
import os

# Function to validate input
def validate_answer(answer):
    try:
        value = float(answer)
        return 0 <= value <= 10
    except ValueError:
        return False

# Define the folder where you want to save the files
SAVE_DIR = "Answers"
os.makedirs(SAVE_DIR, exist_ok=True)

# Title
st.title("Encuesta")

# Instructions
st.markdown("Por favor responde las siguientes preguntas:")

# Questions
questions = [
    "¿Qué tan cansado/a (cansancio general) te sientes ahora del 0 al 10 (0 = nada cansado/a, 10 = muy cansado/a)?",
    "¿Qué tan cansado/a mentalmente te sientes ahora del 0 al 10 (0 = nada cansado/a, 10 = muy cansado/a)?",
    "¿Qué tan cansado/a físicamente te sientes ahora del 0 al 10 (0 = nada cansado/a, 10 = muy cansado/a)?",
    "¿Qué tan cansado/a emocionalmente te sientes ahora del 0 al 10 (0 = nada cansado/a, 10 = muy cansado/a)?",
    "¿Qué tan pesada sientes la cabeza ahora del 0 al 10 (0 = nada de pesadez, 10 = muy pesada)?",
    "¿Qué tanto dolor de cabeza sientes ahora del 0 al 10 (0 = nada de dolor, 10 = mucho dolor)?",
    "¿Cómo está tu estado de ánimo ahora del 0 al 10 (0 = muy triste o desanimado, 10 = muy feliz o animado)?",
    "¿Qué tan estresado/a te sientes ahora del 0 al 10 (0 = nada estresado/a, 10 = muy estresado/a)?",
    "¿Qué tanto dolor muscular/corporal sientes ahora del 0 al 10 (0 = nada de dolor, 10 = mucho dolor)?",
    "¿Qué tanto dolor en el pecho o síntomas de gripe tienes ahora (0 = nada de dolor o síntomas, 10 = mucho dolor o síntomas)?",
    "¿Qué nivel de problemas digestivos sientes ahora (0 = nada de problemas digestivos, 10 = muchos problemas digestivos)?",
    "¿Cuánto consumo de alcohol tuviste ayer del 0 al 10 (0 = nada de consumo de alcohol, 10 = mucho consumo de alcohol)?",
    "¿Cuánto consumo de azúcar has tenido hoy del 0 al 10 (0 = nada de consumo de azúcar, 10 = mucho consumo de azúcar)?",
    "¿Qué tan nutritivo fue tu desayuno hoy del 0 al 10 (0 = nada nutritivo, 10 = muy nutritivo)?",
    "¿Qué tan nutritivo fue tu almuerzo hoy del 0 al 10 (0 = nada nutritivo, 10 = muy nutritivo)?",
    "¿Qué tan nutritivo fue tu cena hoy del 0 al 10 (0 = nada nutritivo, 10 = muy nutritivo)?",
    "¿Qué tan bien dormiste ayer del 0 al 10 (0 = muy mal, 10 = muy bien)?",
    "¿Qué tanto ejercicio físico has realizado hasta ahora del 0 al 10 (0 = nada de ejercicio, 10 = mucho ejercicio)?",
]

# Create sliders for each question
answers = {}
for i, question in enumerate(questions, 1):
    answers[f"q{i}"] = st.slider(question, min_value=0, max_value=10, step=1)

# Submit button
if st.button("Enviar respuesta"):
    # Validate all answers
    if all(validate_answer(value) for value in answers.values()):
        # Get the current date
        current_date = datetime.now().strftime("%Y%m%d_%H")
        filename = os.path.join(SAVE_DIR, f"answers_{current_date}.txt")

        # Save answers to a file
        with open(filename, "w") as file:
            for i, question in enumerate(questions, 1):
                file.write(f"{question}: {answers[f'q{i}']}\n")

        # Confirmation message
        st.success("Tus respuestas han sido guardadas!")
    else:
        st.error("Por favor ingresa un valor válido (0 a 10) para todas las preguntas.")
