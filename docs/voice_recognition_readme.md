# Voice Recognition Module for Jarvis AI Assistant

This module handles the voice recognition capabilities of Jarvis, including wake word detection and speech-to-text conversion.

## Dependencies
- SpeechRecognition: For converting speech to text
- PyAudio: For audio input/output
- OpenWakeWord: For wake word detection
- Whisper: For advanced speech recognition

## Implementation Notes
- Wake word detection runs continuously in the background
- Speech recognition is activated after wake word detection
- Multiple language support is available
- Noise cancellation is implemented for better accuracy
