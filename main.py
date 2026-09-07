import speech_recognition as sr
import pyttsx3

from config import (
    ASSISTANT_NAME,
    USER_NAME,
    VOICE_RATE,
    VOICE_VOLUME,
    LISTEN_TIMEOUT,
    PHRASE_TIME_LIMIT,
    WAKE_WORD_REQUIRED,
    AI_API_KEY,
    AI_MODEL,
    SYSTEM_PROMPT,
)

from actions import handle_basic_command


# ==========================================
# SPEAK
# ==========================================

def jarvis_speak(text):

    text = str(text)

    print(f"JARVIS: {text}")

    try:

        engine = pyttsx3.init()

        engine.setProperty(
            "rate",
            VOICE_RATE
        )

        engine.setProperty(
            "volume",
            VOICE_VOLUME
        )

        voices = engine.getProperty("voices")

        if voices:

            engine.setProperty(
                "voice",
                voices[0].id
            )

        engine.say(text)

        engine.runAndWait()

        engine.stop()

    except Exception as error:

        print(f"VOICE ERROR: {error}")


# ==========================================
# LISTEN
# ==========================================

def listen(recognizer, microphone):

    try:

        print("\nListening...")

        with microphone as source:

            audio = recognizer.listen(
                source,
                timeout=LISTEN_TIMEOUT,
                phrase_time_limit=PHRASE_TIME_LIMIT
            )

        print("Processing...")

        command = recognizer.recognize_google(audio)

        print(f"You: {command}")

        return command.lower().strip()

    except sr.WaitTimeoutError:

        return ""

    except sr.UnknownValueError:

        print("I couldn't understand that.")

        return ""

    except sr.RequestError:

        print("Speech recognition service unavailable.")

        return ""

    except Exception as error:

        print(f"Microphone error: {error}")

        return ""


# ==========================================
# AI
# ==========================================

def ask_ai(message):

    try:

        from openai import OpenAI

        client = OpenAI(
            api_key=AI_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

        response = client.chat.completions.create(

            model=AI_MODEL,

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as error:

        print(f"AI ERROR: {error}")

        return (
            "I couldn't connect to my AI brain, Sir."
        )


# ==========================================
# MAIN
# ==========================================

def main():

    print("=" * 60)

    print("                 J.A.R.V.I.S.")

    print(
        "       JUST A RATHER VERY INTELLIGENT SYSTEM"
    )

    print("=" * 60)

    print()

    # ======================================
    # VOICE TEST
    # ======================================

    print("TESTING JARVIS VOICE...")

    jarvis_speak(
        "Hello Sir. JARVIS voice is working."
    )

    print("VOICE TEST COMPLETE")

    print()

    # ======================================
    # MICROPHONE
    # ======================================

    recognizer = sr.Recognizer()

    recognizer.dynamic_energy_threshold = True

    try:

        microphone = sr.Microphone()

    except Exception as error:

        print(f"MICROPHONE ERROR: {error}")

        return

    # ======================================
    # CALIBRATION
    # ======================================

    print("Calibrating microphone...")

    with microphone as source:

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

    print("Microphone ready.")

    print()

    # ======================================
    # STARTUP
    # ======================================

    jarvis_speak(
        "JARVIS online. All systems are ready, Sir."
    )

    print()

    print("JARVIS IS READY")

    print()

    # ======================================
    # LOOP
    # ======================================

    while True:

        command = listen(
            recognizer,
            microphone
        )

        if not command:

            continue

        # ----------------------------------
        # WAKE WORD
        # ----------------------------------

        if WAKE_WORD_REQUIRED:

            wake_word = ASSISTANT_NAME.lower()

            if wake_word not in command:

                print(
                    "Wake word not detected."
                )

                continue

            command = command.replace(
                wake_word,
                "",
                1
            ).strip()

        # ----------------------------------
        # BASIC COMMANDS
        # ----------------------------------

        running, answer = handle_basic_command(
            command
        )

        if running and answer:

            jarvis_speak(answer)

            if command in [
                "exit",
                "quit",
                "goodbye",
                "go offline",
                "shutdown jarvis"
            ]:

                break

            continue

        # ----------------------------------
        # AI
        # ----------------------------------

        print("JARVIS is thinking...")

        answer = ask_ai(command)

        print()

        print("AI ANSWER:")

        print(answer)

        print()

        jarvis_speak(answer)


# ==========================================
# START
# ==========================================

if __name__ == "__main__":

    main()