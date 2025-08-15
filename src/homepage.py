import streamlit as st
import coursespage

def load():

    st.header("AI Courses")

    st.markdown(
        """ 
        The future of AI is transformative, driving advancements in automation, healthcare, finance, and beyond, with innovations like AGI (Artificial General Intelligence), AI-powered robotics, and real-time decision-making systems reshaping industries. 
        These courses—AI Beginner, AI Advanced, and AI Professional—are designed to equip learners with the necessary skills to thrive in this evolving landscape. 
        Starting with foundational concepts, progressing to deep learning and NLP, and culminating in advanced AI research and deployment, this structured pathway ensures mastery of cutting-edge tools and ethical considerations.
        By combining theory with hands-on projects, learners will be prepared to contribute to AI-driven solutions, adapt to emerging trends, and lead in the next wave of technological innovation.
        """
    )

    st.header("List of courses we offer")
    coursespage.load()






