# 🤖 Auto-Reply AI Chatbot

This is a Python-based AI-powered auto-reply chatbot that integrates with applications (like messaging apps or browser windows) using GUI automation and responds intelligently to messages using OpenAI's GPT API.

---

## 🔧 Features

- 📋 Copies the latest chat messages from screen
- 🧠 Uses GPT-3.5 (or GPT-4) to generate intelligent and sarcastic replies (Chandler-style)
- ✍️ Pastes and sends the reply automatically
- 🔁 Runs continuously to simulate real-time interaction
- 🔒 Keeps your API key secure using `.env`

---

## 🚀 Setup

### Clone the repository

```bash
git clone https://github.com/ryukendo-31/Auto-Reply-AI-Chatbot.git
cd Auto-Reply-AI-Chatbot
pip install -r requirements.txt
pip install pyautogui pyperclip python-dotenv openai
python main.py
```

Auto-Reply-AI-Chatbot/
├── main.py              # Main script to run the bot
├── client.py            # OpenAI API wrapper logic (optional)
├── position.py          # Helper for determining screen positions
├── .env.example         # Template for your OpenAI API key
├── .gitignore           # Ignores .env and other secrets
---

This project uses GUI automation (via pyautogui) and may control your mouse/keyboard. Run responsibly.


✨ Contribute
Feel free to fork and create pull requests if you'd like to enhance this project!

🧑‍💻 Author
Aaryan Sharma
Made with ❤️ for automation and AI fun



