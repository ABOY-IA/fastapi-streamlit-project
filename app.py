import streamlit as st
import requests

st.title("Générateur de citations inspirantes")

API_URL = "http://localhost:8000/"

def get_citation():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["citation"]
    return "Impossible de récupérer une citation."

if "citation" not in st.session_state:
    st.session_state.citation = get_citation()

st.write(st.session_state.citation)

if st.button("Nouvelle citation"):
    st.session_state.citation = get_citation()
    st.rerun()

new_citation = st.text_input("Ajouter une citation :")
if st.button("Ajouter"):
    response = requests.post(f"{API_URL}/add_citation", json={"new_citation": new_citation})
    if response.status_code == 200:
        st.success("Citation ajoutée avec succès!")
    else:
        st.error("Erreur lors de l'ajout de la citation.")




