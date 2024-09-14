#This code belongs to BIBASH THAPA ( crNemo )
#It is a small model of text to speech robot

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.speak("Text to speech starting")
while True:
    speech=input("Enter the text you want to change (Press N for canceling): ")
    if speech=="N" or speech=="n":
        print("Robo is shutting off")
        speaker.speak(f"Robo is shutting off")
        break
    speaker.speak(f"{speech}")