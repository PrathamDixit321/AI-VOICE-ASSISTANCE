# AI-VOICE-ASSISTANCE

This project showcases a real-time AI voice assistant built with Python, leveraging the ElevenLabs Conversational AI API. It demonstrates how to create a conversational agent that listens, processes user speech, and responds in real-time. What once required a complex pipeline of multiple libraries can now be accomplished with a single powerful API.

Key Features
Real-time Interaction: The assistant listens to the user and responds instantly.

Minimalistic Code: Achieves voice-based conversational AI with a single API, simplifying the development process.

Customizable: Easily configure the assistant's personality and first message through Python code.

Integrated Pipeline: The ElevenLabs API handles all the heavy lifting, including voice recording, transcription, LLM processing, speech synthesis, and audio playback.

Technologies Used
Python: The core programming language for the project.

ElevenLabs API: Provides the all-in-one conversational AI functionality.

python-dotenv: Securely loads environment variables from a .env file.

elevenlabs: The official Python library to interact with the ElevenLabs API.

Project Structure
The project consists of a single Python script that handles all the logic:

voice_assistant.py:

Loads credentials from the .env file.

Configures the ElevenLabs conversation with a custom prompt and first message.

Implements callback functions to print the agent's and user's responses.

Starts the real-time conversation session.

ElevenLabs Setup
Sign up for ElevenLabs and go to the Conversational AI section.

Create a new Agent from blank.

Go to the Security tab of your agent and enable "First message" and "System prompt" overrides. Save your changes.

Navigate to API keys from your profile and copy your API key.

Prerequisites
Make sure you have Python installed on your system.

Bash

python --version
Then, install the required Python packages.

Bash

pip install elevenlabs elevenlabs[pyaudio] python-dotenv
If you are on Linux or macOS, you may need to install an additional dependency for PyAudio:

For Linux: sudo apt install portaudio19

For macOS: brew install portaudio
