# ==========================================
# JARVIS CONFIGURATION
# ==========================================

# Assistant name
ASSISTANT_NAME = "jarvis"

# Your name
USER_NAME = "Sir"


# ==========================================
# VOICE SETTINGS
# ==========================================

VOICE_RATE = 170

VOICE_VOLUME = 1.0


# ==========================================
# SPEECH RECOGNITION
# ==========================================

LISTEN_TIMEOUT = 5

PHRASE_TIME_LIMIT = 10

# False = you don't need to say "Jarvis"
# True  = you must say "Jarvis"
WAKE_WORD_REQUIRED = False


# ==========================================
# AI SETTINGS
# ==========================================

# Put your OpenRouter API key between the quotes
AI_API_KEY = "YOUR_API_KEY_HERE"

# Example model
AI_MODEL = "openai/gpt-4o-mini"


# ==========================================
# JARVIS PERSONALITY
# ==========================================

SYSTEM_PROMPT = """
You are JARVIS, a helpful personal AI assistant.

Address the user as Sir.

Be intelligent, concise, polite, and helpful.

When answering simple questions, give a clear and direct answer.
"""