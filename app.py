import streamlit as st
import pandas as pd

st.set_page_config(page_title="DJEFF ALUMINIUM", layout="wide")

st.title("🏠 DJEFF ALUMINIUM")
st.subheader("Version 2 - Gestion multi-articles")

# ---------------------------
# Tarifs
# ---------------------------

with st.sidebar:

    st.header("Tarifs")

    prix_alu = st.number_input(
        "Aluminium (DA/ML)",
        value=8500.0
    )

    prix_pvc = st.number_input(
        "PVC (DA/ML)",
        value=6500.0
    )

    prix_double = st.number_input(
        "Double vitrage",
        value=4000.0
    )

    prix_oscillo = st.number_input(
        "Oscillo-battant",
        value=5000.0
    )

    prix_volet_manuel = st.number_input(
        "Volet manuel",
        value=12000.0
    )

    prix_volet_motorise = st.number_input(
        "Volet motorisé",
        value=25000.0
    )

# ---------------------------
# Client
# ---------------------------

client = st.text_input("Nom du client")

# ---------------------------
# Stockage Session
# ---------------------------

if "devis" not in st.session_state:
    st.session_state.devis = []

# ---------------------------
# Nouvel Article
# ---------------------------

st.header("Ajouter un article")

col1, col2, col3 = st.columns(3)

with col1:
    produit = st.selectbox(
        "Produit",
        [
            "Fenêtre",
            "Porte",
            "Baie vitrée",
            "Porte placard"
        ]
    )

    materiau = st.selectbox(
        "Matériau",
        [
            "Aluminium",
            "PVC"
        ]
    )

with col2:

    ouverture = st.selectbox(
        "Ouverture",
        [
            "Simple",
            "Oscillo-Battant"
        ]
    )

    vitrage = st.selectbox(
        "Vitrage",
        [
            "Simple",
            "Double"
        ]
    )

with col3:

    rideau = st.selectbox(
        "Rideau",
        [
            "Aucun",
            "Manuel",
            "Motorisé"
        ]
    )

    quantite = st.number_input(
        "Quantité",
        min_value=1,
        value=1
    )

largeur = st.number_input(
    "Largeur (m)",
    min_value=0.10,
    value=1.20
)

hauteur = st.number_input(
    "Hauteur (m)",
    min_value=0.10,
    value=1.40
)

# ---------------------------
# Ajouter article
# ---------------------------

if st.button("Ajouter au devis"):

    ml = (largeur + hauteur) * 2

    prix_ml = prix_alu if materiau == "Aluminium" else prix_pvc

    prix = ml * prix_ml * quantite

    if vitrage == "Double":
        prix += prix_double * quantite

    if ouverture == "Oscillo-Battant":
        prix += prix_oscillo * quantite

    if rideau == "Manuel":
        prix += prix_volet_manuel * quantite

    elif rideau == "Motorisé":
        prix += prix_volet_motorise * quantite

    st.session_state.devis.append({
        "Produit": produit,
        "Matériau": materiau,
        "Ouverture": ouverture,
        "Vitrage": vitrage,
        "Rideau": rideau,
        "Qté": quantite,
        "ML": round(ml, 2),
        "Total DA": round(prix, 2)
    })

# ---------------------------
# Tableau devis
# ---------------------------

st.header("Devis")

if len(st.session_state.devis) > 0:

    df = pd.DataFrame(
        st.session_state.devis
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    total_general = df["Total DA"].sum()

    st.success(
        f"TOTAL GENERAL : {total_general:,.0f} DA"
    )

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Télécharger CSV",
        csv,
        file_name="devis_djeff.csv",
        mime="text/csv"
    )

    if st.button("Effacer devis"):
        st.session_state.devis = []
        st.rerun()

else:

    st.info(
        "Aucun article ajouté"
    )
