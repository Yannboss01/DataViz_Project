import streamlit as st


page = st.sidebar.selectbox("Select a page", ["Profile", "Project Presentation"])

if page == "Profile":
    import Profile
elif page == "Project Presentation":
    import Project