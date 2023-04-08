# Project Name to be Determined

def main():
    import os
    import openai
    from gtts import gTTS

    with open("ignore/key.txt") as f:
        key = f.readline()
        key = key.strip()

    openai.api_key = key

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    running = 1
    while running:
        message = input("You: ") # need to change input source... using this for testing

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

            os.system(f"afplay -v {volume} ignore/audio.mp3")
        else:
            running = 0

if __name__ == "__main__":
    main()
