from langchain_community.llms.modal import Modal
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import streamlit as st
from streamlit_modal import Modal

import database

class AIAssistant:
    __title__ = "AIAssistant"
    __db__ = None

    def __init__(self, title:str,db:SQLDatabase):
        self.title = str
        self.db = db

    def get_sql_chain(self,db):
        template = """
        You are a course registration assistant in a company. 
        You are interacting with a user who is asking you questions about the courses and registration details.
        Based on the table schema below, write a SQL query that would answer the user's question also assist registration process. 
        Take the conversation history into account.
    
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


    def get_response(self,user_query: str, db: SQLDatabase, chat_history: list):
        sql_chain = self.get_sql_chain(db)

        template = """
        You are a course registration assistant at a company. You are interacting with a user who is asking you questions about the list of courses available and to register for the course.
        Based on the table schema below, question, sql query, and sql response, write a natural language response. 
        First list only all available courses from courses table if currently running with details.
        Also validate course currently running.
        Use indian rupees and timezone .
        Assist user to register into the course by getting all mandatory fields one by one from the registration table. 
        Just say payment link will be send to your email and your phone number , Upon payment you will be enrolled. 
        <SCHEMA>{schema}</SCHEMA>
    
        Conversation History: {chat_history}
        SQL Query: <SQL>{query}</SQL>
        User question: {question}
        SQL Response: {response}"""

        prompt = ChatPromptTemplate.from_template(template)

        # llm = ChatOpenAI(model="gpt-4-0125-preview")
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


    def start_ai_registration_assistant(self):

        st.title = self.title
        st.session_state.db =  self.db
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
                response = self.get_response(user_query, st.session_state.db, st.session_state.chat_history)
                st.markdown(response)
                st.session_state.chat_history.append(AIMessage(content=response))



    def start_popover(self):
        with st.popover("Click to Register!"):
           self.start_ai_registration_assistant()

    def start_model(self):
        modal = Modal(key="course-registration-modal", title="AI Course Registration Assistant")

        if st.button("Click to Register!"):
            modal.open()

        if modal.is_open():
            with modal.container():
                self.start_ai_registration_assistant()


    def start_dialog(self):
        # Initialize session state
        if 'show_ai_dialog' not in st.session_state:
            st.session_state.show_ai_dialog = False

        # Toggle dialog button
        if st.button("AI Course Registration Assistant"):
            st.session_state.show_ai_dialog = not st.session_state.show_ai_dialog

        # Dialog content
        if st.session_state.show_ai_dialog:
            with st.container(border=True):

                self.start_ai_registration_assitant()
                if st.button("Close"):
                    st.session_state.show_ai_dialog = False
                    st.rerun()

    def start_sidebar(self):
        with st.sidebar:
            self.start_ai_registration_assistant()
