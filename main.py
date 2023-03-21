import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Set the speed and volume of the voice
engine.setProperty('rate', 250)  # 150 words per minute
engine.setProperty('volume', 1)  # 80% volume
engine.setProperty('voice', 'ru')  # Russian voice

for voice in voices:
    if voice.name == 'Anna':
        engine.setProperty('voice', voice.id)

# Get the text to voice from the user
text = input("Enter the text to voice: ")

# Convert the text to speech
engine.say(text)
engine.runAndWait()
