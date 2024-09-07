import streamlit as st

# Page configuration
st.set_page_config(page_title="Peeratat Untichai", page_icon="😎")

# Title
st.title(" Whoami")

# Introduction
st.subheader("I'm Peeratat Untichai (Namkhang)")
st.write("""
- Present 🧑 Student in Debsirin school
- 2024 MUIC Open day 2024
- 2024 KMITL K-engineering World Tour and Workshop 2024
""")

# Current Activities
st.subheader("🧑‍💻 What I'm Doing Now")
st.write("""
- 📖 studying Sci-Math
- 💻 start learning computer and coding
- 👨‍💻 For fun [Leet Code](https://tryhackme.com/)
""")

# Tech Stack & Skills
st.subheader("📚 Tech Stack & Skills")

# Programming Languages
with st.expander("👨‍💻 Programming Languages"):
    st.image("https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54", use_column_width=True)
    st.image("https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E", use_column_width=True)

# Frontend Development
with st.expander("🪟 Frontend Development"):
    st.image("https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white", use_column_width=True)

# My Skills
st.subheader("🐥 My Skills")
st.image("https://skillicons.dev/icons?i=python,java", use_column_width=True)

# Future Plans
st.subheader("🌟 What in Future")
st.write("""
- [ ] Study Computer Engineering
- [ ] Working in ~~software development~~ 
""")

# Contact Information
st.subheader("📩 Connect with Me")
st.write("""
- 📩 jeerasakananta@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/jeerasak-ananta-a1b4231a2/)
- 📖 [Medium](https://medium.com/@jeerasakananta_1762/about)
""")

# Footer
st.write("Thank for reading :) 😼")
