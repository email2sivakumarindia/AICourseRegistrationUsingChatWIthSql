import streamlit as st
from langchain_community.utilities import SQLDatabase
from streamlit.components.v1 import html
import homepage
import contactpage
import aiassistant
import coursespage

# Top page
def header():
    st.set_page_config(page_title="AI Courses", page_icon=":speech_balloon:")
    st.title("Welcome to AI Courses - Your guide to future AI World")
    #st.image("/Users/apple/Desktop/AIKickstarterCourseAI/Images/Topheader.webp", use_container_width=True)
    url = "https://media.geeksforgeeks.org/wp-content/uploads/20240628162127/Best-courses-for-artificial-intelligence.webp"
    st.image(url, use_container_width=True)

#Footer for all pages
def footer():
    st.markdown("---")
    st.markdown("© 2025 AICourses Ltd | [Privacy Policy]() | [Terms of Service]()")

# Page content functions
def home():
  homepage.load()

def registration(aiassistant: aiassistant.AIAssistant):
    aiassistant.start_ai_registration_assistant()
    # ... (rest of registration content)

def courses():
    #st.header("Here I am loading all the course pages")
    coursespage.load()

def contact():
    st.title("Contact Us")
    contactpage.load()
    # ... (rest of contact page content)

def load(aiassistant: aiassistant.AIAssistant,db: SQLDatabase):
    # Load pages here
    header()

    # Define pages with icons
    PAGES = {
        "Home": "home",
        "Courses": "courses",
        "Registration": "registration",
        "Contact": "contact"
    }

    # Initialize session state for active page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "home"

    # Sidebar navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="margin: 0;"></h2>
            <p style="margin: 0;"></p>
        </div>
        """, unsafe_allow_html=True)

        # Create navigation buttons
        for page_name, page_id in PAGES.items():
            if st.button(page_name, key=f"nav_{page_id}"):
                st.session_state.current_page = page_id

        # Add some space and footer
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        st.markdown("""
        <div style="color: #aaa; font-size: 0.8rem; text-align: center; margin-top: auto;">
            
        </div>
        """, unsafe_allow_html=True)

    # JavaScript to handle active state
    html(f"""
    <script>
    // Function to highlight active button
    function setActiveButton() {{
        const buttons = parent.document.querySelectorAll('.stButton button');
        buttons.forEach(button => {{
            if(button.textContent.trim() === "{list(PAGES.keys())[list(PAGES.values()).index(st.session_state.current_page)]}") {{
                button.classList.add('active');
            }} else {{
                button.classList.remove('active');
            }}
        }});
    }}

    // Run on page load
    setActiveButton();

    // Set up mutation observer to handle Streamlit's dynamic updates
    const observer = new MutationObserver(setActiveButton);
    observer.observe(parent.document.querySelector('[data-testid="stSidebar"]'), {{
        childList: true,
        subtree: true
    }});
    </script>
    """)

    # Page routing
    if st.session_state.current_page == "home":
        home()
    elif st.session_state.current_page == "courses":
        courses()
    elif st.session_state.current_page == "registration":
        registration(aiassistant)
    elif st.session_state.current_page == "contact":
        contact()

    #footer()