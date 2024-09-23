import os
from pydub import AudioSegment
import whisper

"""
 Use which ffmpeg at terminal to discovery where the tool is installed
 """
AudioSegment.converter = "/opt/homebrew/bin/ffmpeg"
AudioSegment.ffprobe = "/opt/homebrew/bin/ffprobe"

def ogg_to_mp3(directory):
    """
    Converts all ogg files in the specified directory to mp3 and saves them with the same name.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".ogg"):
            ogg_file = os.path.join(directory, filename)
            mp3_file = os.path.join(directory, filename.replace('.ogg', '.mp3'))

            # Load the ogg file and export it as mp3
            audio = AudioSegment.from_file(ogg_file)
            audio.export(mp3_file, format="mp3")
            print(f"Converted {filename} to mp3")

def transcribe_audio(directory):
    """
    Transcribes all mp3 files in the specified directory and writes the transcript to a text file.
    """
    # Load the Whisper model (you can choose between 'tiny', 'base', 'small', 'medium', 'large')
    model = whisper.load_model("base")

    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            mp3_file = os.path.join(directory, filename)
            txt_file = os.path.join(directory, filename.replace('.mp3', '.txt'))

            # Transcribe the mp3 file
            print(f"Transcribing {filename}...")
            result = model.transcribe(mp3_file)

            # Save the transcription to a text file
            with open(txt_file, 'w') as f:
                f.write(result['text'])
            print(f"Transcription saved to {txt_file}")

def process_ogg_files(directory):
    """
    Process ogg files in a directory by converting them to mp3 and transcribing them.
    """
    ogg_to_mp3(directory)
    transcribe_audio(directory)

# Example usage:
directory_path = "/Users/mariaclaraseixascheffel/PycharmProjects/crm/audios"
process_ogg_files(directory_path)