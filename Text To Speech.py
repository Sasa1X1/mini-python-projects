from gtts import gTTS
import os

def save_text_to_speech(text, language, filename):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the speech to a file
    tts.save(filename)

def main():
    # Ask the user for input text
    text = input("Enter the text to convert to speech: ")

    # Ask the user to choose the language
    print("Select language for text-to-speech conversion:")
    print("1. English")
    print("2. French")
    print("3. German")
    print("4. Spanish")
    print("5. Arabic")
    choice = int(input("Enter your choice (1/2/3/4/5): "))

    languages = {
        1: 'en',
        2: 'fr',
        3: 'de',
        4: 'es',
        5: 'ar'
    }

    if choice in languages:
        language = languages[choice]
    else:
        print("Invalid choice. Using English as default.")
        language = 'en'

    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Ask the user for the filename
    filename = input("Enter the filename (without extension): ")
    full_path = os.path.join(script_dir, f"{filename}.mp3")

    # Convert text to speech and save to file
    save_text_to_speech(text, language, full_path)
    print(f"Text-to-speech file saved at {full_path}")

if __name__ == "__main__":
    main()
