import socket
import speech_recognition as sr

def start_server(host, port): 

    # Create a socket object and bind to the host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind((host, port)) 

    # Start listening for connections
    server_socket.listen(5) 
    
    print("Server listening....")

    while True: 
        # Establish a connection with the client
        print('Waiting for a connection')
        client_socket, addr = server_socket.accept() 
        print('Connected to:', addr)

        # Receive the data in small chunks
        data = b""
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            data += chunk
        
        # Save the received audio data as a new file
        with open("received.wav", "wb") as audio_file:
            audio_file.write(data)
        
        print("Audio file saved.")
        r = sr.Recognizer()
        with sr.AudioFile("F://voice_client//received.wav") as source:
            audio_text = r.listen(source)

    # Convert speech audio to text
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print("Text: " + text)
        except:
            print('Sorry.. run again...')
        
        # Close the connection with the client
        client_socket.close()


# Define server and port here
host = socket.gethostname()
port = 12345
start_server(host, port)
