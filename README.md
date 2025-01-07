# Automation Podcast Solution

This project provides an automation solution that transforms written material into an engaging podcast-style audio format. The solution uses the ElevenLabs API for text-to-speech conversion and emulates a conversational tone by generating audio for two distinct speakers.

# Features

- **Text-to-Speech Conversion**: Converts written scripts into realistic, human-like speech.
- **Dual-Speaker Emulation**: Simulates a natural conversation between two speakers with distinct voices.
- **Customizable Output**: Saves the output as an MP3 file for easy playback.
- **Multi-Language Support**: Uses ElevenLabs' multilingual capabilities to generate audio in different languages (default: English).

## Technologies Used

- [**ElevenLabs API**](https://elevenlabs.io): For realistic text-to-speech conversion.
- **Python**: Core programming language for script generation and audio synthesis.
- **nltk (Natural Language Toolkit)**: For sentence tokenization to split the script into conversational dialogue.

## Prerequisites

1. Python 3.7 or later installed on your system.
2. An API key from [ElevenLabs](https://elevenlabs.io) (sign up and generate an API key).
3. Install the required Python libraries:
   pip install elevenlabs nltk
