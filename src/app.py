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

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
  #db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
  password = "Welcome@1"  # Example password with special characters
  encoded_password = quote_plus(password)  # Encodes '@' -> '%40', '!' -> '%21'

  db_uri = f"mysql+mysqlconnector://root:{encoded_password}@localhost:3306/testsqlai"
  #db_uri = "mysql+mysqlconnector://root:Welcome@123@localhost:3306/mydatabase"
  return SQLDatabase.from_uri(db_uri)

def get_sql_chain(db):
  template = """
    You are a course registration assistant in a company. You are interacting with a user who is asking you questions about the course and registration details.
    Based on the table schema below, write a SQL query that would answer the user's question also assist registration process. Take the conversation history into account.
    
    <SCHEMA>{schema}</SCHEMA>
    
    Conversation History: {chat_history}
    
    Write only the SQL query and nothing else. Also check for all mandatory field value entered by user.Do not wrap the SQL query in any other text, not even backticks.
    
    For example:
    Question: which 3 artists have the most tracks?
    SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
    Question: Name 10 artists
    SQL Query: SELECT Name FROM Artist LIMIT 10;
    
    Your turn:
    
    Question: {question}
    SQL Query:
    """
    
  prompt = ChatPromptTemplate.from_template(template)
  
  # llm = ChatOpenAI(model="gpt-4-0125-preview")
  llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
  
  def get_schema(_):
    return db.get_table_info()
  
  return (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | llm
    | StrOutputParser()
  )
    
def get_response(user_query: str, db: SQLDatabase, chat_history: list):
  sql_chain = get_sql_chain(db)
  
  template = """
    You are a course registration assistant at a company. You are interacting with a user who is asking you questions about the list of courses available and to register for the course.
    First all available courses from courses table if currently running with details.
    Based on the table schema below, question, sql query, and sql response, write a natural language response. Use indian rupees and timezone .
    Assist user to register into the course by getting all mandatory fields one after another from the registration table one by one. Also validate course currently running.
    <SCHEMA>{schema}</SCHEMA>

    Conversation History: {chat_history}
    SQL Query: <SQL>{query}</SQL>
    User question: {question}
    SQL Response: {response}"""

  prompt = ChatPromptTemplate.from_template(template)
  
  #llm = ChatOpenAI(model="gpt-4-0125-preview")
  llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
  
  chain = (
    RunnablePassthrough.assign(query=sql_chain).assign(
      schema=lambda _: db.get_table_info(),
      response=lambda vars: db.run(vars["query"]),
    )
    | prompt
    | llm
    | StrOutputParser()
  )
  
  return chain.invoke({
    "question": user_query,
    "chat_history": chat_history,
  })


# Main flow starts here

load_dotenv()

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
#st.image("path/to/your/image.jpg")
# Add more Streamlit elements here

with tab3:
    st.header("AI Course Professional")
#st.dataframe({"Column A": [1, 2, 3], "Column B": ["X", "Y", "Z"]})
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

# AI Course Assitant Starts From Here

st.title("Chat with our AI Assistant to Register ")

db = init_database('root','Welcome@1','localhost','3306','courses')

st.session_state.db = db

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
      AIMessage(content="Hello! I'm a AI Course Registration Assistant. Do you want to any help to know about courses or registration?"),
    ]

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

user_query = st.chat_input("Type a message...")

if user_query is not None and user_query.strip() != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = get_response(user_query, st.session_state.db, st.session_state.chat_history)
        st.markdown(response)
        st.session_state.chat_history.append(AIMessage(content=response))
