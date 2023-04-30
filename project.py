import speech_recognition as sr
import pywhatkit

# Set up speech recognition
r = sr.Recognizer()

# Define function to listen for speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Define function to search for music
def search_music(query):
    pywhatkit.playonyt(query)

# Define function to recommend music
def recommend_music():
    url = "https://youtu.be/c6-gUhb7hxQ"  # Change to your recommended video URL
    pywhatkit.playonyt(url)

# Define main function
def main():
    while True:
        # Listen for wake word "Hey My"
        text = listen()
        if "hey my" in text.lower():
            print("Listening for command...")
            # Listen for command
            text = listen()
            if "play" in text.lower():
                query = text.replace("play", "").strip()
                search_music(query)
            elif "recommend" in text.lower():
                recommend_music()
            elif "stop" in text.lower():
                break
            else:
                print("Sorry, I did not understand that command.")

if __name__ == '__main__':
    main()