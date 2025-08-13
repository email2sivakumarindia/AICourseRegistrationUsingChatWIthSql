import streamlit as st

def load():
    st.title("Contact Our Team")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Office Information")
        st.write("""
        📍 123 Education Street, Tech City  
        📞 +1 (555) 123-4567  
        ✉️ contact@edutech.example  
        🕒 Mon-Fri: 9AM-5PM
        """)

        st.image("https://via.placeholder.com/400x300?text=Our+Campus", width=300)

    with col2:
        st.subheader("Send a Message")
        with st.form("contact_form"):
            st.text_input("Your Name")
            st.text_input("Your Email")
            st.selectbox("Subject", ["General Inquiry", "Technical Support", "Billing"])
            st.text_area("Message")
            if st.form_submit_button("Send Message"):
                st.success("Message sent! We'll respond within 24 hours.")


