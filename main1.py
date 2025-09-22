import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig 
import uuid

user_id = str(uuid.uuid4())

# Load environment variables from a .env file
load_dotenv()

# Retrieve API Key and Agent ID from environment variables
# Note: It's crucial that these names match the ones in your .env file
API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
AGENT_ID = os.getenv("ELEVEN_LABS_AGENT_ID")

# --- Error Handling ---
# This check ensures the environment variables were loaded successfully.
# If they are not found, the script will raise an error.
if not API_KEY:
    raise ValueError("ELEVEN_LABS_API_KEY environment variable not found. Please check your .env file.")
if not AGENT_ID:
    raise ValueError("ELEVEN_LABS_AGENT_ID environment variable not found. Please check your .env file.")

# --- Conversation Setup ---


user_name = "Pratham"
schedule = "College from 9:00 to 5:00; Meet friends at 6:00; DO work till 8:00; Dinner at 8:30; Self Learning at 9:00; Self Project making at last till 12:00; Sleep at 12:00"
preferences = "Likes Indian food; Enjoys playing chess; Prefers morning workouts"
reminders = "Call mom at 7:00 PM; Submit assignment by 11:59 PM"
location = "Currently in Delhi"
goals = "Finish reading a book; Practice coding for 1 hour"

prompt = (
    f"You are a helpful assistant. "
    f"Your interlocutor has the following schedule: {schedule}. "
    f"Preferences: {preferences}. "
    f"Reminders: {reminders}. "
    f"Location: {location}. "
    f"Today's goals: {goals}."
)
first_message = f"Hello {user_name}, how can I help you today?"



conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
    user_id=user_id  # Add this line
)

# --- ElevenLabs Client Initialization ---
client = ElevenLabs(api_key=API_KEY)

# --- Define Callback Functions ---
# These functions handle how the conversation's events are displayed.
def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

# --- Conversation Instance Creation ---
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

# --- Start the Conversation Session ---
print("Starting conversation. Press 'q' and Enter to quit.")
try:
    conversation.start_session()
except Exception as e:
    print(f"An error occurred: {e}")