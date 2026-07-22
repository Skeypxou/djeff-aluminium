import streamlit as st

st.set_page_config(page_title="DJEFF ALUMINIUM")

st.title("🏠 DJEFF ALUMINIUM")

client = st.text_input("Nom du client")

materiau = st.selectbox(
    "Matériau",
    ["Aluminium", "PVC"]
)

largeur = st.number_input("Largeur (m)", value=1.20)
hauteur = st.number_input("Hauteur (m)", value=1.40)

prix_ml = st.number_input(
    "Prix du profilé (DA/ML)",
    value=8500.0
)

if st.button("Calculer"):

    ml = (largeur + hauteur) * 2

    total = ml * prix_ml

    st.success("Devis calculé")

    st.write(f"Mètre linéaire : {ml:.2f} ML")
    st.write(f"Total : {total:,.0f} DA")
