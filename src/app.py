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
    You are a course registration assistant in a conmpany. You are interacting with a user who is asking you questions about the course and registration details.
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
    Based on the table schema below, question, sql query, and sql response, write a natural language response. Use indian rupees and timezone . Also do not show any computer or sql error , instead show I am not able to understand please clarify
    Show initially all courses available to the user from courses table. Also assist user to register into the course by getting all mandatory fields from the registration table one by one. Also validate course currently running. Do not show any sql error.
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
    
  
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
      AIMessage(content="Hello! I'm a AI Course Registration Assistatnt. Ask me anything about the course."),
    ]

load_dotenv()

st.set_page_config(page_title="AI Course Registration Assistant", page_icon=":speech_balloon:")

st.title("AI Course Registration Assistant")

db = init_database('root','Welcome@1','localhost','3306','courses')

st.session_state.db = db

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