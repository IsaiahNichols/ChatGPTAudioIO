# Project Name to be Determined

'''
TODO:
- add audio input on bound button press
- print user and chat audio input and output in the form of
You: [input]
Chat: [Response]

In order to use:
- install dependancies: pip install openai, gTTs, and ...
- Change directory to same as main.py file.
- Create directory \"ignore\" and paste API key in a text file named \"key.txt\" within that file.
'''

def main():
    import os
    import openai
    import speech_recognition as sr
    from gtts import gTTS

    recog = sr.Recognizer()

    with open("ignore/key.txt") as f:
        key = f.readline()
        key = key.strip()

    openai.api_key = key

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    input_choices = ["text", "voice"]
    input_type = input(f"Input source {input_choices}? ")
    while not (input_type in input_choices):
        input_type = input()
    
    running = 1
    while running:
        if input_type == "text":
            message = input("You: ")
        elif input_type == "voice":
            with sr.Microphone() as mic:
                recog.adjust_for_ambient_noise(mic, duration=0.5)
                message = recog.listen(mic)
                message = recog.recognize_google(message)
                message = message.lower()

        if message:
            # Interacting with API
            messages.append({"role": "user", "content": message})

            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            response_text = response.choices[0].message.content
            
            # Terminal output
            print(f"Chat: {response_text}")

            # Audio output
            lang = "en"
            volume = 0.05
            audio = gTTS(response_text, lang=lang, slow=False)
            audio.save("ignore/audio.mp3")

            os.system(f"afplay -v {volume} ignore/audio.mp3") # this uses the mac terminal command to play audio and needs to be changed to be used on other OSs
        else:
            running = 0

if __name__ == "__main__":
    main()
