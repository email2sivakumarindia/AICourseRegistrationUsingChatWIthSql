from dotenv import load_dotenv
import database
from aiassistant import AIAssistant
import layout

def main():

    # Main flow starts here

    load_dotenv()

    # Initiate DB
    db = database.init_database('root', 'Welcome@1', 'localhost', '8080', 'courses')

    # Construct AI Course Assistant
    aiassistant = AIAssistant("Chat with our AI Assistant to Register ", db)

    #aiassistant.start_ai_registration_assistant()
    # aiassistant.start_popover()
    # aiassistant.start_model()
    # aiassistant.start_dialog()
    # aiassistant.start_sidebar()

    # load layout
    layout.load(aiassistant,db)

if __name__ == "__main__":
    main()



