import os
import pyaudio
from google.cloud import speech_v1 as speech

# Set the environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'red-road-430907-n7-25e5a173b18e.json'

speech_client = speech.SpeechClient()

# Audio recording parameters
RATE = 16000
CHUNK = 1024

# Initialize PyAudio
audio_interface = pyaudio.PyAudio()

def listen_print_loop(responses):
    """Iterates through server responses and prints them."""
    for response in responses:
        if not response.results:
            continue

        result = response.results[0]
        if not result.alternatives:
            continue

        transcript = result.alternatives[0].transcript
        print("Transcript: {}".format(transcript))

def record_and_transcribe():
    # Create a streaming recognition configuration
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code="en-US"
    )
    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True
    )

    # Open audio stream
    audio_stream = audio_interface.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    print("Listening...")

    audio_generator = (audio_stream.read(CHUNK) for _ in range(int(RATE / CHUNK * 60)))  # Adjust the range for longer recording
    requests = (speech.StreamingRecognizeRequest(audio_content=content) for content in audio_generator)
    
    responses = speech_client.streaming_recognize(streaming_config, requests)
    listen_print_loop(responses)

    # Close the audio stream
    audio_stream.stop_stream()
    audio_stream.close()

if __name__ == '__main__':
    record_and_transcribe()
# import os
# import pyaudio
# from google.cloud import speech_v1 as speech

# CREDENTIALS_PATH = 'client_secret_303100921412-s9il8etjmsfdokq6klmb511drifr2kob.apps.googleusercontent.com.json'
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'red-road-430907-n7-25e5a173b18e.json'
# speech_client = speech.SpeechClient()

# # Audio recording parameters
# RATE = 16000
# CHUNK = 1024

# # Initialize PyAudio
# audio_interface = pyaudio.PyAudio()

# def listen_print_loop(responses):
#     """Iterates through server responses and prints them."""
#     for response in responses:
#         if not response.results:
#             continue

#         result = response.results[0]
#         if not result.alternatives:
#             continue

#         transcript = result.alternatives[0].transcript
#         print("Transcript: {}".format(transcript))

# def record_and_transcribe():
#     # Create a streaming recognition configuration
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=RATE,
#         language_code="en-US"
#     )
#     streaming_config = speech.StreamingRecognitionConfig(
#         config=config,
#         interim_results=True
#     )

#     # Open audio stream
#     audio_stream = audio_interface.open(
#         format=pyaudio.paInt16,
#         channels=1,
#         rate=RATE,
#         input=True,
#         frames_per_buffer=CHUNK
#     )

#     print("Listening...")

#     audio_generator = (audio_stream.read(CHUNK) for _ in range(int(RATE / CHUNK * 60)))  # Adjust the range for longer recording
#     requests = (speech.StreamingRecognizeRequest(audio_content=content) for content in audio_generator)
    
#     responses = speech_client.streaming_recognize(streaming_config, requests)
#     listen_print_loop(responses)

#     # Close the audio stream
#     audio_stream.stop_stream()
#     audio_stream.close()

# if __name__ == '__main__':
#     record_and_transcribe()