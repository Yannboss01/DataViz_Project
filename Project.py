import streamlit as st
from PIL import Image


st.title("Project Presentation")


st.markdown("## **Analyse sur les jeux en ligne de 2010 à 2023**")
st.write("""
 Ce projet réalise l'analyse du marché des jeux en ligne de l'année 2010 à 2023 et leur évolution au fil du temps. Eprouvant de l'intérêt dans le domaine des jeux en ligne j'ai choisi 
de réaliser cette analyse afin de regarder les différences au fil des années et la construction de leur business.
""")


st.markdown("### *Grâce à quels outils les opérateurs de jeux en ligne ont réussi à attirer de plus en plus de joueurs pour augmenter leurs gains ?*")


st.write("## *Quelques chiffres essentiels*")


col1, col2 = st.columns(2)

with col1:
    st.image("Corrélations_nombre_de_comptes.png", use_column_width=True)
    st.image("nbr_CJA_ps.png", use_column_width=True)

with col2:
    st.image("evol_mises_nbre_joueur.png", use_column_width=True)
    st.image("Ratio_Gain_Mise.png", use_column_width=True)

st.write("## *Une explication de l'augmentation du nombre de joueurs avec une solution d'amélioration*")

st.image("evol_budg_nbre_joueur.png", use_column_width=True)
st.image("part_femmes.png", use_column_width=True)


st.markdown("""
### **Conclusion**
Les jeux en ligne ont connu une croissance significative grâce aux stratégies mises en place par les opérateurs pour attirer de nouveaux joueurs et optimiser leurs gains.
""")


