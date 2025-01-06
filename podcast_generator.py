import nltk
from nltk.tokenize import sent_tokenize
import requests
from pydub import AudioSegment

# Step 2: Generate Script from Material
nltk.download('punkt')

def generate_script(material):
    sentences = sent_tokenize(material)
    script = []
    speakers = ["Speaker A", "Speaker B"]
    for i, sentence in enumerate(sentences):
        script.append(f"{speakers[i % 2]}: {sentence}")
    return "\n".join(script)

# Step 3: Convert Script to Audio (Using ElevenLabs API)
def synthesize_voice(text, voice_id="default", api_key="YOUR_API_KEY"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {"text": text, "model_id": "eleven_monolingual_v1"}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        audio_file = f"{voice_id}.mp3"
        with open(audio_file, "wb") as file:
            file.write(response.content)
        return audio_file
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Combine Generated Audio Files
def create_podcast(audio_files, output_file="podcast.mp3"):
    podcast = AudioSegment.empty()
    for audio_file in audio_files:
        segment = AudioSegment.from_file(audio_file)
        podcast += segment + AudioSegment.silent(duration=500)
    podcast.export(output_file, format="mp3")
    print(f"Podcast saved at {output_file}")

# Main Function to Integrate Steps
def main():
    # Input Material
    material = """Artificial intelligence is revolutionizing industries. It helps automate tasks, improve efficiency, and create innovative solutions."""
    
    # Generate Script
    script = generate_script(material)
    print("Generated Script:\n", script)
    
    # Divide script by speakers
    speaker_a_text = " ".join([line.split(": ")[1] for line in script.split("\n") if line.startswith("Speaker A")])
    speaker_b_text = " ".join([line.split(": ")[1] for line in script.split("\n") if line.startswith("Speaker B")])

    # Generate audio files
    speaker_a_audio = synthesize_voice(speaker_a_text, voice_id="speaker_a", api_key="YOUR_API_KEY")
    speaker_b_audio = synthesize_voice(speaker_b_text, voice_id="speaker_b", api_key="YOUR_API_KEY")

    # Create podcast
    if speaker_a_audio and speaker_b_audio:
        create_podcast([speaker_a_audio, speaker_b_audio])

if __name__ == "__main__":
    main()
