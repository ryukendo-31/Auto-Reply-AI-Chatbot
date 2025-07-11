import pyautogui
import pyperclip
import time
import openai
import os
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("API_KEY"))

def is_last_message_from(sender_name, chat_text):
    """Check if the last valid message is from the given sender."""
    lines = chat_text.strip().splitlines()
    for line in reversed(lines):
        match = re.match(r"\[.*?\]\s*(.*?):", line)
        if match:
            sender = match.group(1).strip().lower()
            return sender_name.lower() in sender
    return False

def extract_messages(chat_text):
    """Strip timestamps and sender names, return only the messages."""
    lines = chat_text.strip().splitlines()
    messages = []
    for line in lines:
        match = re.match(r"\[.*?\] .*?: (.*)", line)
        if match:
            messages.append(match.group(1))
    return "\n".join(messages)

# Let user open WhatsApp Web
print("You have 5 seconds to open WhatsApp Web...")
time.sleep(5)

# Click on browser/WhatsApp tab
pyautogui.click(1181, 1044)
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)

last_replied_text = ""

while True:
    # Drag to select chat
    pyautogui.moveTo(669, 195)
    pyautogui.mouseDown()
    pyautogui.moveTo(1863, 903, duration=1.0)
    pyautogui.mouseUp()
    time.sleep(0.5)

    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    chat_text = pyperclip.paste().strip()
    print(f"📋 Copied Message:\n{chat_text}\n")

    # Avoid duplicate reply or empty text
    if not chat_text or chat_text == last_replied_text:
        time.sleep(2)
        continue

    # Check sender
    if is_last_message_from("Colaba Hostel KJSCE", chat_text):
        last_replied_text = chat_text

        # Prepare GPT prompt
        cleaned_chat = extract_messages(chat_text)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Aaryan Sharma from India. You're funny, kind, and very sarcastic. "
                        "Talk like Chandler Bing from Friends. Based on the conversation history, reply like Aaryan."
                    )
                },
                {"role": "user", "content": cleaned_chat}
            ]
        )

        reply = response.choices[0].message.content.strip()
        pyperclip.copy(reply)
        print(f" Sending Reply:\n{reply}\n")

        # Click to type
        pyautogui.click(1216, 969)
        time.sleep(1)

        # Paste and send
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')

    time.sleep(3)
