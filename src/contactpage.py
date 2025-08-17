import streamlit as st

def load():
    st.title("Contact Our Team")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Office Information")
        st.write("""
        📍 Heritagecounty, Sarjapur, Bangalore , India   \n
        📞 +91 6362620391 \n
        ✉️ email2sivkumarindia@gmail.com \n
        🕒 Mon-Fri: 9AM-5PM
        """)

        #st.image("https://via.placeholder.com/400x300?text=Our+Campus", width=300)

    with col2:
        st.subheader("Send a Message")
        with st.form("contact_form"):
            st.text_input("Your Name")
            st.text_input("Your Email")
            st.selectbox("Subject", ["Course Inquiry", "Technical Support", "Payment"])
            st.text_area("Message")
            if st.form_submit_button("Send Message"):
                st.success("Message sent! We'll respond within 24 hours. If not please contact us at email2sivakumarindia@gmail.com")


