# automation-podcast generator
This project converts text material (books or articles) into an appealing podcast script and generates audio using text-to-speech APIs.

## Requirements
1. Python 3.8+
2. `ffmpeg` installed and added to PATH
3. Internet connection for API calls

## Setup Instructions

1. Clone the Repository
git clone <repository_url>
cd <repository_name>

2. Create and Activate Virtual Environment
python -m venv env
source env/Scripts/activate  # For Git Bash or Linux
env\Scripts\activate.bat     # For Windows CMD

4. Install Dependencies
pip install -r requirements.txt

6. Install ffmpeg
Download ffmpeg from ffmpeg.org.
Extract and add the bin folder to the system PATH.
Verify installation:
ffmpeg -version

8. Set API Key
Replace YOUR_API_KEY in podcast_generator.py with a valid API key from ElevenLabs or another TTS service.

10. Run the Script
python podcast_generator.py

Output
The script generates:
Individual speaker audio files (e.g., speaker_a.mp3, speaker_b.mp3).
Combined podcast file (podcast.mp3).

Notes
Ensure punkt_tab is downloaded for NLTK:
import nltk
nltk.download('punkt_tab')
