import streamlit as st
import info

text = "Welcome to My Web App!"
st.markdown(
    f"""
    <h1 style='text-align: center; color: #f48c94;'>
        {text}
    </h1>
    """,
    unsafe_allow_html=True
)

st.image(info.border, width = 1500)
st.subheader("Samantha Norris — CS 1301")

st.write("This is my multi-page Streamlit app for the Web Development Lab01 assignment!")

st.markdown("""
### Pages in this App:
1. **Portfolio**: My personal portfolio showcasing my background, skills, and goals. You can also find out some fun facts about me here!
2. **Data Exploration**: An interactive data visualization page where you can explore data related to my study habits!
""")

st.write("Feel free to explore the pages using the navigation sidebar!")

st.image(info.border, width = 1500)

text = '"Believe in yourself and you’re halfway there.” — Theodore Roosevelt'
st.markdown(
    f"""
    <div style='text-align: center; color: #f48c94;'>
        {text}
    </div>
    """,
    unsafe_allow_html=True
)
st.image(info.border, width = 1500)
