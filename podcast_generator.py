from elevenlabs import ElevenLabs
from nltk.tokenize import sent_tokenize

# Initialize ElevenLabs client
client = ElevenLabs(
    api_key="sk_11985ec4758a076c65f86aefa5abde49d85027cca7cbd4eb"
)

# voice IDs for two speakers
voice_1_id = "21m00Tcm4TlvDq8ikWAM"  
voice_2_id = "pqHfZKP75CvOlQylNhV4"  

# conversational tone logic
def generate_conversation(script):
    sentences = sent_tokenize(script)
    speaker_1_lines = sentences[::2]  # Odd sentences for Speaker 1
    speaker_2_lines = sentences[1::2]  # Even sentences for Speaker 2

    conversation = []
    for speaker_1, speaker_2 in zip(speaker_1_lines, speaker_2_lines):
        conversation.append((voice_1_id, speaker_1))  # Speaker 1's line
        conversation.append((voice_2_id, speaker_2))  # Speaker 2's line

    if len(speaker_1_lines) > len(speaker_2_lines):
        conversation.append((voice_1_id, speaker_1_lines[-1])) 

    return conversation

# Convert script to audio using ElevenLabs API
def convert_script_to_audio(script, output_file="podcast.mp3"):
    conversation = generate_conversation(script)

    
    with open(output_file, "wb") as f:
        for voice_id, text in conversation:
            audio = client.text_to_speech.convert(
                voice_id=voice_id,
                output_format="mp3_44100_128",
                text=text,
                model_id="eleven_multilingual_v2"
            )
            for chunk in audio:  
                f.write(chunk)
    print(f"Podcast saved as {output_file}")


def main():
    # Example material
    material = """
    Welcome to our podcast! Today, we’re exploring the fascinating world of artificial intelligence.
    Speaker 1: AI has been transforming industries worldwide.
    Speaker 2: Absolutely, and it’s not just limited to tech; even healthcare and education are benefiting.
    """
    convert_script_to_audio(material)

if __name__ == "__main__":
    main()

