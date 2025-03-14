# Jarvis AI Assistant

A sophisticated AI assistant with voice recognition, task automation, information retrieval, and visitor memory capabilities.

## Directory Structure

```
jarvis/
├── core/               # Core AI functionality
│   ├── voice_recognition.py    # Voice recognition module
│   ├── information_retrieval.py # Information retrieval module
│   ├── memory_system.py        # Memory and visitor tracking system
│   ├── task_automation.py      # Task automation module
│   └── integration.py          # Main integration module
│
├── gui/                # GUI components
│   ├── App.js                  # Main application component
│   ├── ConversationPanel.js    # Conversation display component
│   ├── Dashboard.js            # Main dashboard component
│   ├── GlobalStyles.js         # Global styling
│   ├── StatusBar.js            # Status bar component
│   ├── Theme.js                # Theme configuration
│   └── TitleBar.js             # Title bar component
│
├── utils/              # Utility scripts
│   ├── index.js                # Main entry point for the application
│   ├── main.js                 # Main process script
│   └── preload.js              # Preload script for Electron
│
├── docs/               # Documentation
│   ├── architecture.md         # System architecture documentation
│   ├── gui_design.md           # GUI design documentation
│   ├── installation_guide.md   # Installation instructions
│   ├── miles_research.md       # Research on M.I.L.E.S
│   ├── requirements.md         # System requirements
│   ├── technical_documentation.md # Technical documentation
│   ├── user_guide.md           # User guide
│   └── voice_recognition_readme.md # Voice recognition documentation
│
├── tests/              # Test scripts
│   ├── test_jarvis.py          # Test suite for Jarvis
│   └── run_tests.sh            # Script to run tests
│
└── package.json        # Project configuration
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   npm install
   ```
3. Follow the detailed instructions in `docs/installation_guide.md`

## Features

- **Voice Recognition**: Wake word detection and speech-to-text conversion
- **Task Automation**: Execute predefined tasks and routines
- **Information Retrieval**: Search for information from various sources
- **Memory System**: Remember user preferences, conversations, and visitors
- **GUI Interface**: Dark-themed interface with purple accents

## Usage

Start the Jarvis AI Assistant:

```
npm start
```

For detailed usage instructions, refer to `docs/user_guide.md`.

## Development

To run tests:

```
./tests/run_tests.sh
```

For development guidelines, refer to `docs/technical_documentation.md`.
