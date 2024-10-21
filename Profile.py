import streamlit as st


col1, col2 = st.columns([3, 1])  

with col1:
    st.title("Yann Scardigli")

with col2:
    st.image("profile.jpg", width=200)


st.header("About me")
st.write("""
I'm specialized in Data science, more precisely in Business inteligence analytics. I'm studying at Efrei Paris for my Fourth year in BIA.
I'm passionate about Data visualization and data analytics. You will find my project on the next page
""")



st.header("Contact")
st.write("**Email**: yann.scardigli@efrei.net")
st.write("**Localisation**: Chatou, France")
st.write("**Numéro de téléphone**: +33 6 87 22 39 63")
st.write("[**LinkedIn**](https://www.linkedin.com/in/yann-scardigli-5969571b8/)")



st.header("Formation")
st.write("""
**Efrei Paris - Master M1**  
DATA Major : Business Artificial Intelligence  
2020 - 2026
""")



st.header("Projects")
st.write("### Project Factory Efrei 2023 - Project Manager")
st.write("**Solution** for analyzing product reviews using web scraping to improve the product.")
st.write("""
**Compétences**: Python, UML diagram, SQL, machine learning's algorithms
**Outils and Frameworks**: Git, Flask
""")




col1, col2 = st.columns(2)

with col1:
    st.subheader("Soft Skills")
    st.write("""
    - Competitive
    - Sense of organization
    - Team spirit
    - Autonomous
    """)

with col2:
    st.subheader("Hard Skills")
    st.write("""
    - SQL/NoSql
    - Python/Machine Learning
    - Data Vizualisation
    - Power BI
    """)
