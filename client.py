import socket
import speech_recognition as sr

# This is client code
def send_audio_data(host, port, audio_file_path):
    # Create a socket object and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send audio data
    with open(audio_file_path, 'rb') as audio_file:
        while True:
            data = audio_file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    print("Data sent successfully.")
    
    # Close the client socket
    client_socket.close()


# Define server and port here
host = socket.gethostname()
port = 12345
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
audio_file_path = 'F://voice_client//microphone-results.wav'
send_audio_data(host, port, audio_file_path)