import streamlit as st
import coursespage

def load():

    st.header("AI Courses")

    st.markdown(
        """
            Unlock the Future with AI: Transform Your Career

            Artificial Intelligence is reshaping industries, creating unprecedented opportunities, and revolutionizing the way we work. 
            By learning AI today, you position yourself at the forefront of innovation, gaining skills that will be essential in the future job market.

            Why AI Matters for Your Career?

                ✅ High Demand: AI professionals are among the most sought-after, with competitive salaries.
                ✅ Future-Proof Skills: Automation and AI will dominate industries—stay ahead by mastering them.
                ✅ Versatility: AI applies to healthcare, finance, marketing, robotics, and more.
                ✅ Entrepreneurial Edge: Build AI-driven solutions and startups with cutting-edge knowledge.

            Start Your AI Journey Now

            Whether you're a student, professional, or entrepreneur, learning AI opens doors to lucrative careers, innovation, and global impact. 
            Explore courses, tutorials, and insights to future-proof your career with AI! 
        """
    )

    st.header("List of courses we offer")
    coursespage.load()






