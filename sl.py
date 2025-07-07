# generator.py
import streamlit as st

st.title("🎨 Generátor cool pozdravov")

# --- NASTAVENIA V BOČNOM PANELI ---
st.sidebar.header("Tvoje nastavenia")

# 1. Vstup pre meno
meno = st.sidebar.text_input("Zadaj svoje meno", "Študent")

# 2. Výber smajlíka
emoji = st.sidebar.selectbox(
    "Vyber si emoji",
    ["", "👋", "🚀", "💻", "🎉", "🔥"]
)

# 3. Výber farby
farba = st.sidebar.color_picker("Vyber si farbu pre nadpis", "#FF5733")


# --- HLAVNÁ STRÁNKA S VÝSTUPOM ---
st.header("Tvoj pozdrav je hotový!")

# Použijeme markdown na zobrazenie farebného textu
# Je to trik, ako písať HTML priamo v Streamlite
st.markdown(
    f"<h2 style='color: {farba};'>Ahoj {meno}! {emoji}</h2>",
    unsafe_allow_html=True
)

st.write("Skús zmeniť nastavenia v bočnom paneli a uvidíš, čo sa stane!")

# Zobrazíme obrázok na základe výberu
if emoji == "🚀":
    st.image("https://static.streamlit.io/examples/owl.jpg", caption="Letíme ku hviezdam!")
elif emoji == "💻":
    st.image("https://static.streamlit.io/examples/cat.jpg", caption="Mačka programátorka.")