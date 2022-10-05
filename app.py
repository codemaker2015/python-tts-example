import pyttsx3

engine = pyttsx3.init()
engine.say('This is a test phrase.')
engine.runAndWait()

voices = engine.getProperty('voices')
print(voices)

for voice in voices:
   engine.setProperty('voice', voice.id)
   print(voice.id)
   engine.say('This is a test phrase.')
engine.runAndWait()

rate = engine.getProperty('rate')
print(rate)


engine.setProperty('rate', 125)
engine.say('This is a test phrase.')
engine.runAndWait()


volume = engine.getProperty('volume')
print(volume)


engine.setProperty('volume', 0.5)
engine.say('This is a test phrase.')
engine.runAndWait()


engine.save_to_file('This is a test phrase.', 'test.mp3')
engine.runAndWait()

from pydub import AudioSegment
AudioSegment.from_file('test.mp3').export('test.mp3', format="mp3")

