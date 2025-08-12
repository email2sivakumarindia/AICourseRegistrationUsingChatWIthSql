from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import streamlit as st
from urllib.parse import quote_plus  # Correct import statement
import requests

def load_static_homepage():

    st.set_page_config(page_title="AI Courses", page_icon=":speech_balloon:")

    st.title("Welcome to AI Courses - Your guide to future AI World")

    st.markdown(
        """ 
        The future of AI is transformative, driving advancements in automation, healthcare, finance, and beyond, with innovations like AGI (Artificial General Intelligence), AI-powered robotics, and real-time decision-making systems reshaping industries. 
        These courses—AI Beginner, AI Advanced, and AI Professional—are designed to equip learners with the necessary skills to thrive in this evolving landscape. 
        Starting with foundational concepts, progressing to deep learning and NLP, and culminating in advanced AI research and deployment, this structured pathway ensures mastery of cutting-edge tools and ethical considerations.
        By combining theory with hands-on projects, learners will be prepared to contribute to AI-driven solutions, adapt to emerging trends, and lead in the next wave of technological innovation.
        """
    )

    st.title("List of courses we offer")

    tab1, tab2, tab3 = st.tabs(["AI Course Beginner", "AI Course Advanced", "AI Course Professional"])

    with tab1:
        st.header("AI Course Beginner")
        st.markdown(
            """
            Target Audience:
    
            Individuals with little to no prior knowledge of AI.
            Students, professionals, or enthusiasts looking to understand AI fundamentals.
            Course Duration: 6-8 Weeks 
    
            Key Topics Covered:
    
            ✅ Introduction to Artificial Intelligence
    
            What is AI? History & Evolution
            Types of AI (Narrow AI, General AI, Super AI)
            Real-world AI applications
            ✅ Machine Learning Basics
    
            Supervised vs. Unsupervised Learning
            Regression & Classification
            Introduction to Neural Networks
            ✅ Python for AI
    
            Basics of Python programming
            Libraries: NumPy, Pandas, Matplotlib
            Simple AI projects (e.g., chatbot, image recognition)
            ✅ Ethics & Future of AI
    
            Bias in AI, Privacy Concerns
            AI in society & job market impact
            Learning Outcomes:
            ✔ Understand AI concepts & terminology.
            ✔ Write basic Python code for AI tasks.
            ✔ Build simple ML models using scikit-learn.
            ✔ Recognize AI applications in daily life.")
            """
        )
    # Add more Streamlit elements here

    with tab2:
        st.header("AI Course Advanced")
        st.markdown(
            """
            Target Audience:
    
            Those with basic AI/ML knowledge (e.g., completed Beginner Course).
            Programmers, data analysts, engineers looking to deepen AI expertise.
            Course Duration: 10-12 Weeks
    
            Key Topics Covered:
    
            ✅ Deep Learning Fundamentals
    
            Neural Networks (CNNs, RNNs, Transformers)
            TensorFlow & PyTorch frameworks
            Hyperparameter Tuning
            ✅ Natural Language Processing (NLP)
    
            Text Preprocessing, Word Embeddings (Word2Vec, BERT)
            Sentiment Analysis, Text Generation
            ✅ Computer Vision
    
            Image Classification, Object Detection (YOLO, Faster R-CNN)
            GANs (Generative Adversarial Networks)
            ✅ Reinforcement Learning
    
            Q-Learning, Deep Q Networks (DQN)
            Applications in Robotics & Gaming
            ✅ Model Deployment
    
            Flask/Django for AI APIs
            Cloud AI (AWS SageMaker, Google AI)
            Learning Outcomes:
            ✔ Build and train deep learning models.
            ✔ Work with NLP & Computer Vision datasets.
            ✔ Deploy AI models in real-world applications.
            ✔ Understand cutting-edge AI research trends.
        """
        )
    # st.image("path/to/your/image.jpg")
    # Add more Streamlit elements here

    with tab3:
        st.header("AI Course Professional")
        # st.dataframe({"Column A": [1, 2, 3], "Column B": ["X", "Y", "Z"]})
        # Add more Streamlit elements here
        st.markdown(
            """
            Target Audience:
    
            Experienced AI practitioners, researchers, or engineers.
            Those aiming for AI leadership roles or advanced research.
            Course Duration: 16-20 Weeks
    
            Key Topics Covered:
    
            ✅ Advanced Deep Learning
    
            Attention Mechanisms (Transformers, GPT, BERT)
            Self-Supervised Learning
            Explainable AI (XAI)
            ✅ AI Research & Development
    
            Reading & Implementing AI Papers
            Optimizing Large-Scale AI Models
            ✅ AI in Industry
    
            MLOps (MLflow, Kubeflow)
            AI for Healthcare, Finance, Autonomous Vehicles
            ✅ AI Ethics & Governance
    
            AI Policy, Fairness, Accountability
            AI Safety & Alignment
            ✅ Capstone Project
    
            End-to-end AI solution (e.g., AI-driven recommendation system, autonomous agent)
            Learning Outcomes:
            ✔ Master state-of-the-art AI models (e.g., GPT, Diffusion Models).
            ✔ Lead AI projects from research to deployment.
            ✔ Publish AI research or contribute to open-source AI.
            ✔ Solve complex industry problems with AI.
            """
        )

    st.markdown(
        """
        Certification & Career Pathways
    
        Beginner: AI Fundamentals Certification
        Advanced: Deep Learning & NLP Specialist
        Professional: AI Research Scientist / AI Engineer
        """
    )
