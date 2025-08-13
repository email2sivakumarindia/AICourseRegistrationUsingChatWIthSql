from dotenv import load_dotenv
import database
import aiassistant
import layout


# Main flow starts here

load_dotenv()

# Initiate DB
db = database.init_database('root', 'Welcome@1', 'localhost', '3306', 'courses')

# Construct AI Course Assitant
aiassistant = aiassistant.AIAssistant("Chat with our AI Assistant to Register ", db)

#aiassistant.start_ai_registration_assistant()
# aiassistant.start_popover()
# aiassistant.start_model()
# aiassistant.start_dialog()
# aiassistant.start_sidebar()

# load layout
layout.load(aiassistant)



