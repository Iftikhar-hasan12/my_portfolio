import streamlit as st
import pandas as pd
from PIL import Image
import os
import base64
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Page configuration
st.set_page_config(
    page_title="Iftikhar - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for clean professional design
st.markdown("""
<style>
    /* Remove top padding and margin */
    .stApp {
        margin-top: -10px;
    }
    
    /* Remove default Streamlit padding */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
    }
    
    /* Header styling */
    .header-container {
        text-align: center;
        padding: 1rem 0;
    }
    
    .profile-img {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 4px solid #2e86ab;
        margin: 0 auto;
        object-fit: cover;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .name-title {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 1rem 0 0.5rem 0;
        color: #2e86ab;
    }
    
    .subtitle {
        font-size: 1.3rem;
        color: #666;
        margin-bottom: 1rem;
    }
    
    .about-text {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        color: #333;
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 2rem auto;
        max-width: 800px;
        border-left: 4px solid #2e86ab;
    }
    
    .cards-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 3rem 0;
        padding: 0 1rem;
    }
    
    .card {
        background: white;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        border: 2px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        min-height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.15);
        border-color: #2e86ab;
    }
    
    .card-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #2e86ab;
        margin-bottom: 0.5rem;
    }
    
    .card-desc {
        color: #666;
        font-size: 0.9rem;
    }
    
    .content-section {
        background: white;
        border-radius: 10px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid #e0e0e0;
    }
    
    .section-title {
        color: #2e86ab;
        font-size: 2rem;
        margin-bottom: 1.5rem;
        text-align: center;
        border-bottom: 2px solid #2e86ab;
        padding-bottom: 0.5rem;
    }
    
    .back-button {
        background: #2e86ab;
        color: white;
        border: none;
        padding: 0.5rem 1.5rem;
        border-radius: 5px;
        cursor: pointer;
        margin-bottom: 1rem;
    }
    
    .contact-form {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
    }
    
    .captcha-box {
        background: #e9ecef;
        padding: 1rem;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
    }
    
    /* Welcome message styling */
    .welcome-message {
        text-align: center;
        color: #2e86ab;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 0.5rem 0;
        padding: 0.5rem;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Load profile picture
def load_profile_picture():
    try:
        possible_files = ['myPic.jpg', 'myPic.jpeg', 'myPic.png', 'profile.jpg', 'profile.png']
        for file in possible_files:
            if os.path.exists(file):
                return Image.open(file)
        return None
    except:
        return None

# Load CV file
def get_cv_download_link():
    try:
        cv_files = ['mycv.pdf', 'cv.pdf', 'resume.pdf', 'Iftikhar_CV.pdf']
        for file in cv_files:
            if os.path.exists(file):
                with open(file, "rb") as f:
                    data = f.read()
                b64 = base64.b64encode(data).decode()
                return f'data:application/pdf;base64,{b64}'
        return None
    except:
        return None

# Generate random math problem
def generate_math_problem():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2, num1 + num2

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'dashboard'

if 'math_problem' not in st.session_state:
    st.session_state.math_problem = generate_math_problem()

# Welcome message at the top
st.markdown('<div class="welcome-message">Welcome to My World of Innovation and Creativity</div>', unsafe_allow_html=True)

# Dashboard Page
def show_dashboard():
    # Header with profile picture
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        profile_img = load_profile_picture()
        if profile_img:
            st.image(profile_img, width=180, output_format="auto")
        else:
            st.markdown('<div style="width: 180px; height: 180px; border-radius: 50%; background: #f0f0f0; display: flex; align-items: center; justify-content: center; margin: 0 auto; border: 4px solid #2e86ab;">'
                       '<span style="color: #2e86ab; font-size: 2rem;">IA</span></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="name-title">Iftikhar Ahmed</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Machine Learning Engineer | Competitive Programmer</div>', unsafe_allow_html=True)
    
    # About section
    st.markdown('''
    <div class="about-text">
        <strong>About Myself</strong><br><br>
        A passionate Final year Computer Science and Engineering student at Green University of Bangladesh 
        with outstanding academic record (3.96/4.00 CGPA). Skilled in Machine Learning, Deep Learning, 
        and Competitive Programming. Created educational content, participated in Kaggle competitions, 
        and built real-world AI projects. Always eager to learn new technologies and solve challenging problems.
    </div>
    ''', unsafe_allow_html=True)
    
    # Cards Grid
    st.markdown('<div class="cards-container">', unsafe_allow_html=True)
    
    # First row of cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Education\n\nMy academic journey and achievements", use_container_width=True):
            st.session_state.current_page = 'education'
            st.rerun()
    
    with col2:
        if st.button("Projects\n\nFrom university to professional work", use_container_width=True):
            st.session_state.current_page = 'projects'
            st.rerun()
    
    with col3:
        if st.button("Current Work\n\nWhat I am working on now", use_container_width=True):
            st.session_state.current_page = 'current'
            st.rerun()
    
    # Second row of cards
    col4, col5, col6 = st.columns(3)
    
    with col4:
        if st.button("Achievements\n\nMy accomplishments and awards", use_container_width=True):
            st.session_state.current_page = 'achievements'
            st.rerun()
    
    with col5:
        if st.button("Skills & Tools\n\nTechnical expertise", use_container_width=True):
            st.session_state.current_page = 'skills'
            st.rerun()
    
    with col6:
        if st.button("Download CV\n\nGet my resume", use_container_width=True):
            st.session_state.current_page = 'cv'
            st.rerun()
    
    # Third row of cards
    col7, col8, col9 = st.columns(3)
    
    with col7:
        if st.button("Find Me\n\nMy social profiles", use_container_width=True):
            st.session_state.current_page = 'social'
            st.rerun()
    
    with col8:
        if st.button("My Playlist\n\nML tutorial series", use_container_width=True):
            st.session_state.current_page = 'playlist'
            st.rerun()
    
    with col9:
        if st.button("Say Hi\n\nSend me a message", use_container_width=True):
            st.session_state.current_page = 'contact'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Education Page
def show_education():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    if st.button("Back to Dashboard", type="primary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
    
    st.subheader("Green University of Bangladesh (GUB)")
    st.write("**BSc in Computer Science & Engineering**")
    st.write("**Duration:** 2022 - Present")
    st.write("**CGPA:** 3.96/4.00")
    st.write("**Current Status:** Final Year Student")
    
    st.markdown("---")
    
    st.subheader("Relevant Coursework")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        - C Programming Language
        - C++ Programming
        - Data Structures & Algorithms (C)
        - Object-Oriented Programming (Java)
        - Python Programming
        - Database Management Systems (SQL)
        """)
    
    with col2:
        st.write("""
        - Computer Networking Lab
        - Data Communication Lab
        - Advanced Mathematics
        - Machine Learning
        - Deep Learning
        - Natural Language Processing
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Projects Page
def show_projects():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    if st.button("Back to Dashboard", type="primary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    
    # Project 1
    st.subheader("SmartMach AI - Predictive Maintenance")
    st.write("""
    **Description:**  
    AI-powered predictive maintenance system that forecasts equipment failures 
    and optimizes maintenance schedules using machine learning algorithms.  

    **Technologies:** Python, Scikit-learn, Pandas, NumPy, Matplotlib  
    **Features:** Real-time monitoring, Failure prediction, Maintenance scheduling  
    **Status:** Completed
    """)

    st.markdown("---")

    # Project 2
    st.subheader("Medical Store Management System")
    st.write("""
    **Description:**  
    A Java-based Medical Store Management System built using Swing for GUI and MySQL for backend storage.  
    It supports an Admin interface with key features such as adding, updating, deleting, searching medicines, 
    selling medicines, checking sell history, and viewing the full medicine list — all integrated with a MySQL database.  
    The system dynamically retrieves and updates data via the database to ensure real-time accuracy.  

    **Technologies:** Java, Swing, MySQL, XAMPP  
    **Features:** Selling medicine history, Medicine quantity update, Store user information, etc.  
    **Status:** Completed
    """)

    st.markdown("---")

    # Project 3
    st.subheader("Library Management System")
    st.write("""
    **Description:**  
    A Java-based Library Management System built using Swing for GUI and MySQL for backend storage.  
    The system supports two interfaces: Admin and Student. Key features include issuing and returning books, 
    viewing book/member lists, managing members and books, viewing issue history, and more — 
    all integrated with a MySQL database to ensure real-time accuracy.  

    **Technologies:** Java, Swing, MySQL, XAMPP  
    **Features:** Book issue/return, Member management, Dynamic data update  
    **Status:** Completed
    """)

    st.markdown("---")

    # Project 4
    st.subheader("Multiple Game Project in Java")
    st.write("""
    **Description:**  
    A Java Swing-based multiplayer game application built using socket programming.  
    The project includes the following classic two-player games:  
    🪨✂️📄 Rock-Paper-Scissors  
    ❌⭕ Tic Tac Toe  
    🐍🎲 Snakes and Ladders  
    💬 Real-Time Chat between Players  

    All games support two-player mode over a network, allowing players to connect, chat, and compete in real time.  

    **Technologies:** Java, Swing, Socket Programming  
    **Features:** Socket-based two-player networking, Real-time chat, Game switching interface, Easy setup via NetBeans IDE  
    **Status:** Completed
    """)

    st.markdown("---")

    # Project 5
    st.subheader("Signal Simulator")
    st.write("""
    **Description:**  
    A Java Swing-based application that simulates digital signal encoding techniques 
    and visualizes their corresponding waveform transmission.  
    This project demonstrates how binary data is encoded using various encoding algorithms 
    and animated as square waveforms — making it easier to understand signal transmission in digital communication systems.  

    **Technologies:** Java, Swing  
    **Features:**  
    ✅ Text-to-Binary Conversion  
    ✅ Encoding Algorithms Implemented:  
    • NRZ-L (Non-Return to Zero-Level)  
    • NRZ-I (Non-Return to Zero-Inverted)  
    • Manchester Standard  
    • Manchester Differential  
    • Bit Stuffing  
    ✅ Waveform Visualization  
    ✅ Step-by-step Transmission Animation  
    ✅ User-Friendly GUI  

    **Status:** Completed
    """)

    st.markdown("---")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Current Activities Page
def show_current_work():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    if st.button("Back to Dashboard", type="primary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown('<div class="section-title">Current Work</div>', unsafe_allow_html=True)
    
    st.subheader("Currently Working On")
    
    st.write("""
    **Advanced Machine Learning Projects**
    - Exploring Deep Learning architectures
    - Working on NLP applications
    - Building end-to-end ML pipelines
    
  
    
    **Project Development**
    - Enhancing existing projects
    - Planning new AI-based applications
    - Collaborating on open-source projects
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Achievements Page
def show_achievements():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    if st.button("Back to Dashboard", type="primary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown('<div class="section-title">Achievements</div>', unsafe_allow_html=True)
    
    st.write("""
    **Academic Excellence**
    - Consistent CGPA of 3.97/4.00
    - Top performer in Computer Science department
    - Shortlisted in VisionX AI Project Showcasing Competition.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Skills Page
def show_skills():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    if st.button("Back to Dashboard", type="primary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown('<div class="section-title">Skills & Tools</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Programming Languages")
        st.write("""
        - C Language
        - C++
        - Python
        - Java
        - SQL
        - Shell Scripting
        """)
    
    with col2:
        st.subheader("Data Science & ML")
        st.write("""
        - Machine Learning
        - Deep Learning
        - Natural Language Processing
        - Pandas, NumPy
        - Scikit-learn
        - Matplotlib
        """)
    
    with col3:
        st.subheader("Tools & Technologies")
        st.write("""
        - Git & GitHub
        - Streamlit
        - Socket Programming
        - Competitive Programming
        - Data Structures
        - Algorithms
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# CV Download Page
def show_cv():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    if st.button("Back to Dashboard", type="primary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown('<div class="section-title">Download CV</div>', unsafe_allow_html=True)
    
    st.info("Click the button below to download my CV")
    
    cv_link = get_cv_download_link()
    if cv_link:
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <a href="{cv_link}" download="Iftikhar_CV.pdf" style="
                background: #2e86ab;
                color: white;
                padding: 0.8rem 1.5rem;
                border-radius: 5px;
                text-decoration: none;
                font-size: 1rem;
                display: inline-block;
                margin: 1rem 0;
            ">
                Download My CV
            </a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("CV file not found. Please make sure 'mycv.pdf' is in the same folder.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Social Profiles Page
def show_social():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    if st.button("Back to Dashboard", type="primary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown('<div class="section-title">Find Me Online</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Professional Profiles:**")
        st.write("- [LinkedIn](https://www.linkedin.com/in/iftikhar-hasan-30b4aa320/)")
        st.write("- [GitHub](https://github.com/Iftikhar-hasan12)")
        st.write("- [Kaggle](https://www.kaggle.com/iftikharhasan)")
        st.write("- [YouTube](https://www.youtube.com/@Iftikhar_Hasan)")
        st.write("- [Email](iftikharhasan04@gmail.com)")
    
    with col2:
        st.write("**Coding Platforms:**")
        st.write("- [Codeforces](https://codeforces.com/profile/Iftikhar12)")
        st.write("- [LeetCode](https://leetcode.com/u/Iftikhar_Hasan62/)")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Playlist Page
def show_playlist():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    if st.button("Back to Dashboard", type="primary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown('<div class="section-title">My ML Playlist</div>', unsafe_allow_html=True)
    
    st.write("""
    **Machine Learning Tutorial Series (33 Classes)**
    
    A comprehensive tutorial series covering machine learning from basics to intermediate level:
    
    **Topics Covered:**
    - Supervised Learning Algorithms
    - Unsupervised Learning Algorithms
    - Data Preprocessing and Cleaning
    - Model Evaluation Techniques
    - Real-world Project Implementations
    - Best Practices in ML
    
    **Highlights:**
    - 33 detailed classes
    - Practical implementations
    - Real-world examples
    - Code walkthroughs
    - Playlist :
    -[link](https://www.youtube.com/@Iftikhar_Hasan)
    
    This series has helped numerous students understand and apply machine learning concepts effectively.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Page
def show_contact():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    if st.button("Back to Dashboard", type="primary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown('<div class="section-title">Say Hi</div>', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        st.subheader("Send me a message")
        
        # User email
        user_email = st.text_input("Your Email", placeholder="Enter your email address")
        
        # Message
        message = st.text_area("Your Message", placeholder="Write your message here...", height=150)
        
        # CAPTCHA
        num1, num2, answer = st.session_state.math_problem
        st.markdown(f'<div class="captcha-box">Solve this: {num1} + {num2} = ?</div>', unsafe_allow_html=True)
        captcha_answer = st.text_input("Enter the answer", placeholder="Type the answer here")
        
        # Submit button
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            # Validate CAPTCHA
            if not captcha_answer:
                st.error("Please solve the math problem")
            elif not captcha_answer.isdigit() or int(captcha_answer) != answer:
                st.error("Incorrect answer. Please try again.")
                # Generate new math problem
                st.session_state.math_problem = generate_math_problem()
                st.rerun()
            elif not user_email or not message:
                st.error("Please fill in all fields")
            else:
                # Here you would typically integrate with an email service
                # For now, we'll just show a success message
                st.success("Thank you for your message! I'll get back to you soon.")
                
                # Generate new math problem for next time
                st.session_state.math_problem = generate_math_problem()
                
                # Clear form (optional)
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main App Router
def main():
    if st.session_state.current_page == 'dashboard':
        show_dashboard()
    elif st.session_state.current_page == 'education':
        show_education()
    elif st.session_state.current_page == 'projects':
        show_projects()
    elif st.session_state.current_page == 'current':
        show_current_work()
    elif st.session_state.current_page == 'achievements':
        show_achievements()
    elif st.session_state.current_page == 'skills':
        show_skills()
    elif st.session_state.current_page == 'cv':
        show_cv()
    elif st.session_state.current_page == 'social':
        show_social()
    elif st.session_state.current_page == 'playlist':
        show_playlist()
    elif st.session_state.current_page == 'contact':
        show_contact()

if __name__ == "__main__":

    main()




