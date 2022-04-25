import speech_recognition as sr
from gtts import gTTS
import os

voice = ""
print("Pls w8 a few seconds and then say something........")
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text == "stop":
                break
            text = r.recognize_google(audio)
            voice = voice + str(text)
        except:
            print("Say something please........")
hr = gTTS(text=voice, lang='en', slow=False)
hr.save("1.wav")





# import speech_recognition as sr
# import pyttsx3
#
# # Initialize the recognizer
# r = sr.Recognizer()
#
#
# # Function to convert text to
# # speech
# def SpeakText(command):
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()
#
#
# # Loop infinitely for user to
# # speak
#
# while (1):
#
#     # Exception handling to handle
#     # exceptions at the runtime
#     try:
#
#         # use the microphone as source for input.
#         with sr.Microphone() as source2:
#             print('Please say something......')
#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             r.adjust_for_ambient_noise(source2, duration=0.2)
#
#             # listens for the user's input
#             audio2 = r.listen(source2)
#
#             # Using ggogle to recognize audio
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()
#
#             print(MyText)
#             SpeakText(MyText)
#
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#
#     except sr.UnknownValueError:
#         print("unknown error occured")
