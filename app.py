import streamlit as st
from ml_model import classify_sequence, predict_mutations
import matplotlib.pyplot as plt

# --- Título ---
st.title("🔬 DNA / RNA Analyzer — Regalo para aprender 💖")

st.markdown(
    "<p style='font-size:14px; color:gray; opacity:0.7;'>"
    "Se que no es mucho pero te servirá un poco para que vayas practicando mi amor, espero te sirva ❤️🥰."
    "</p>",
    unsafe_allow_html=True
)

# --- Input ---
st.subheader("1️⃣ Ingresa tu secuencia de ADN / ARN")
seq_input = st.text_area("Pega aquí la secuencia (A, T, C, G, U):", height=150)

# --- Clasificación ---
if st.button("🔎 Clasificar organismo"):
    if seq_input.strip() == "":
        st.warning("Por favor ingresa una secuencia.")
    else:
        result = classify_sequence(seq_input)
        st.success(f"✅ Clasificación: {result}")

# --- Predicción de mutaciones ---
if st.button("🧬 Predecir mutaciones probables"):
    if seq_input.strip() == "":
        st.warning("Por favor ingresa una secuencia.")
    else:
        muts = predict_mutations(seq_input)
        st.info("🔄 Mutaciones sugeridas:")

        for m in muts:
            st.write(f"- {m}")

        # Ejemplo gráfico (conteo de mutaciones)
        fig, ax = plt.subplots()
        ax.bar(range(len(muts)), [1]*len(muts))
        ax.set_xticks(range(len(muts)))
        ax.set_xticklabels(muts, rotation=45)
        ax.set_title("Mutaciones sugeridas")
        st.pyplot(fig)
