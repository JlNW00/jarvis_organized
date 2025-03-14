# M.I.L.E.S GitHub Projects Research

## Overview
This document summarizes the research findings from two M.I.L.E.S GitHub projects that will serve as inspiration for our Jarvis AI assistant implementation.

## 1. small-cactus/M.I.L.E.S

### Project Description
A GPT-4-Turbo powered voice assistant that self-adapts its prompts and AI model. It can play Spotify songs, adjust system and Spotify volume, perform calculations, browse the web, search global weather, deliver date and time, and autonomously choose and retain long-term memories.

### Key Features
- **Wake Word Detection**: Uses openwakeword library trained on 50,000 samples
- **Voice Recognition**: Uses whisper for speech recognition
- **Text-to-Speech**: Powered by OpenAI's TTS technology for natural voice
- **Smart Home Integration**: Integration with Home Assistant
- **Spotify Integration**: Full control of Spotify with voice commands
- **Persistent Memory**: Ability to remember information for later retrieval
- **Calculator**: Built-in calculator with LaTeX formatting
- **Multi-tasking**: Can handle up to 3 tools or tasks simultaneously
- **Contextual Awareness**: Understands context about itself and the user
- **Internet Browsing**: Can search the internet for information
- **Image Recognition**: Can analyze and describe images in real-time

### Technical Implementation
- **Wake Word Detection**: openwakeword library
- **Speech Recognition**: whisper library
- **Voice Synthesis**: OpenAI's Text-to-Speech
- **API Integrations**: Weather API, Spotify API, Home Assistant
- **Memory Storage**: Local text file storage
- **UI**: Electron-based interface

### Planned Features
- **Annoyance Mode**: No wake word needed, always listening and transcribing to determine if speech is directed at the assistant
- **Plugin System**: Allows adding Python functions to the tool list

## 2. magneum/Miles-AI

### Project Description
A Python-based voice assistant with a more modular structure.

### Project Structure
- **app**: Application core
- **bin**: Binary files
- **components**: Modular components
- **database**: Database management
- **models**: AI models
- **public**: Public assets
- **router**: Routing logic
- **server**: Server components
- **temp**: Temporary files
- **views**: UI views

### Technical Implementation
- **Voice Synthesis**: pyttsx3 library
- **Voice Recognition**: PyAudio
- **UI**: Possibly web-based (JavaScript components)

### Dependencies
Key libraries used:
- beautifulsoup4
- colorama
- keras
- matplotlib
- nltk
- numpy
- openai
- opencv-python
- pandas
- pyttsx3
- PyAudio
- python-dotenv
- scikit-learn
- selenium
- sounddevice
- tensorflow

## Comparison and Insights

### Architectural Approaches
- **small-cactus/M.I.L.E.S**: More focused on AI integration with OpenAI's GPT models, with a desktop application approach
- **magneum/Miles-AI**: More modular structure with separate components, possibly with web interface capabilities

### Voice Processing
- Both use different approaches for speech recognition and synthesis
- small-cactus uses more advanced models (whisper, OpenAI TTS)
- magneum uses more traditional libraries (pyttsx3, PyAudio)

### Integration Capabilities
- Both support various integrations
- small-cactus has more documented integrations (Spotify, Home Assistant)

## Recommendations for Jarvis Implementation

1. **Modular Architecture**: Adopt the modular approach from magneum/Miles-AI for better maintainability
2. **Advanced Voice Processing**: Use the more advanced voice processing from small-cactus/M.I.L.E.S (whisper, OpenAI TTS)
3. **Wake Word System**: Implement the wake word system from small-cactus/M.I.L.E.S with potential for "annoyance mode"
4. **Memory System**: Implement persistent memory storage for remembering user information
5. **Integration Framework**: Create a flexible integration framework for adding new services
6. **UI Design**: Create a futuristic and skeuomorphic UI as specified in requirements
7. **Face Recognition**: Add face recognition capabilities using OpenCV
8. **Visitor Memory**: Implement database for storing visitor information
9. **Conversation Initiation**: Implement proactive greeting system for known and unknown visitors
