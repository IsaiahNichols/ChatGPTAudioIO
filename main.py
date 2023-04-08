# Project Name to be Determined
import os
import openai
from gtts import gTTS

def main():
    text = ""
    volume = 0.05

    while text != "stop":
        lang = "en"
        text = input("Enter Words to be Spoken: ")

        audio = gTTS(text, lang=lang, slow=False)
        audio.save("audio.mp3")

        os.system(f"afplay -v {volume} assets/audio.mp3")

if __name__ == "__main__":
    main()
