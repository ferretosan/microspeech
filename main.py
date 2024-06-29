import speech

while True:
    text = input("What do you want your micro:bit to say? ")
    speech.pronounce(speech.translate(text))