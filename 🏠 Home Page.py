from pathlib import Path

import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_timeline import timeline

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Francisco Alonso"
PAGE_ICON = ":page_facing_up:"
NAME = "Francisco Alonso FernΓ‘ndez"
DESCRIPTION = """
Data Scientist. "You can have data without information, but you cannot have information without data".
"""
EMAIL = "falonsof96@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "π Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "π Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "π Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "π MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

st.sidebar.write("Hola")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" π Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("π«", EMAIL)

# --- TIMELINE ---
st.write('\n')
st.subheader("Timeline Overview")
with st.spinner(text="Building line"):
    with open('assets/timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- βοΈ 7 Years expereince extracting actionable insights from data
- βοΈ Strong hands on experience and knowledge in Python and Excel
- βοΈ Good understanding of statistical principles and their respective applications
- βοΈ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- π©βπ» Programming: Python (Scikit-learn, Pandas), SQL, VBA
- π Data Visulization: PowerBi, MS Excel, Plotly
- π Modeling: Logistic regression, linear regression, decition trees
- ποΈ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("π§", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- βΊ Used PowerBI and SQL to redeο¬ne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- βΊ Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- βΊ Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("π§", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- βΊ Built data models and maps to generate meaningful insights from customer data, boosting successful sales eο¬orts by 12%
- βΊ Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- βΊ Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write('\n')
st.write("π§", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- βΊ Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traο¬c
- βΊ Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- βΊ Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="es_ES" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="franciscoalonsofernandez" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/franciscoalonsofernandez?trk=profile-badge"></a></div>"""}

with st.sidebar:
    components.html(embed_component['linkedin'], height=310)