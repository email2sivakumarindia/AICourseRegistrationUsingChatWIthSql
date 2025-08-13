from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import streamlit as st
import homepage
import database
import aiassistant


# Main flow starts here

load_dotenv()

# Load static home page
homepage.load_static_homepage()



# Initiate DB
db = database.init_database('root','Welcome@1','localhost','3306','courses')

# AI Course Assistant Starts From Here
aiassistant = aiassistant.AIAssistant("Chat with our AI Assistant to Register ", db)
aiassistant.start_ai_registration_assistant()
#aiassistant.start_popover()
#aiassistant.start_model()
#aiassistant.start_dialog()
#aiassistant.start_sidebar()
