
import streamlit as st
import pandas as pd
import info



st.image(info.border, width = 1500)

# About me

def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write("---")
about_me_section()

st.image(info.border, width = 1500)

import random

st.header("Generate A Fun Fact About Me!")

if 'fun_fact' not in st.session_state:
    st.session_state.fun_fact = ""

if st.button("Give me a fun fact!"):
    st.session_state.fun_fact = random.choice(info.fun_facts)

st.write(st.session_state.fun_fact)


# Side Bar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn!")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Follow me on Instagram!")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Instagram" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)


links_section()

#Education
def education_section(education_data,course_data):
    st.header("Education")
    st.subheader(f'**{education_data["Institution"]}**')
    st. write(f"**Degree:** {education_data['Degree']}")
    st. write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write(f"**Education In Progress:** {education_data['Current']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "names": "Course Names",
        "year_taken": "Year Taken",
        "skills" : "What I Learned"},
        hide_index=True,)
        
st.image(info.border, width = 1500)
education_section(info.education_data,info.course_data)
        
#Professional Experience
def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title,(job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width = 250)
        for bullet in job_description:
            expander.write(bullet)
st.image(info.border, width = 1500)
experience_section(info.experience_data)

#skills

def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,'')}") #doesnt match
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken,'')}:{proficiency}")#doesnt match
skills_section(info.programming_data, info.spoken_data)

st.image(info.border, width = 1500)


# Activities

def activities_section(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, (details, image) in activity_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)

activities_section(info.leadership_data, info.activity_data)
























    
    
