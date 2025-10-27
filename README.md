<h1 align="center">🤖 Mega Project 1 - JARVIS (Your Personal AI Voice Assistant)</h1>

<p align="center">
  <img src="https://github.com/prashantpkg777-blip.png" width="100" style="border-radius:50%">
</p>

<p align="center">
  <b>Built with ❤️ in Python by <a href="https://github.com/prashantpkg777-blip">Prashant Kumar</a></b><br>
  <i>“Your Voice. Your Assistant. Your Jarvis.”</i>
</p>

---

## 🌟 Overview

**Jarvis** is a Python-based voice assistant that listens to your commands, replies intelligently, and performs real-time actions — like opening Google, fetching live news, or launching apps — just by your voice.

This project demonstrates **speech recognition**, **text-to-speech**, and **API integration** in Python — all without using any AI API keys.

---

## 🚀 Features

- 🎙️ **Voice Recognition** — Understands what you say  
- 🗣️ **Text-to-Speech** — Speaks responses in real-time  
- 🌐 **Smart Web Commands** — Opens Google or any website  
- 📰 **Live News** — Fetches top headlines using News API  
- 💻 **App Launcher** — Opens local apps like Notepad, Chrome, VS Code, etc.  
- 🕓 **Time & Date** — Tells you the current time and date  
- 🧠 **Wake Word System** — Responds only when you say “Jarvis”  
- 🧍‍♂️ **Friendly Personality** — Replies casually like a real assistant  

---

## 🧩 Tech Stack

| Library | Use |
|----------|-----|
| `speech_recognition` | Convert voice to text |
| `pyttsx3` | Convert text to speech |
| `requests` | Fetch news headlines |
| `webbrowser` | Open websites |
| `os` | Launch apps |
| `time` | Delay control |

---

## ⚙️ Setup & Installation

### Step 1️⃣ – Clone the Repo
```bash
git clone https://github.com/prashantpkg777-blip/Mega-Project-1---Jarvis.git
cd Mega-Project-1---Jarvis

Step 2️⃣ – Create Virtual Environment
python -m venv jarvis-env

Step 3️⃣ – Activate Environment

For PowerShell (Windows):

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\jarvis-env\Scripts\activate


For macOS/Linux:

source jarvis-env/bin/activate

Step 4️⃣ – Install Required Libraries
pip install speechrecognition pyttsx3 requests pyaudio

Step 5️⃣ – Run the Project
python main.py

🗣️ Example Voice Commands
Command	Action
“Jarvis”	Wakes up the assistant
“Open Google”	Opens Google in browser
“Tell me the news”	Reads top headlines
“Open Notepad”	Opens Notepad
“Exit”	Closes the program
📰 News Setup (Optional)

If you want to fetch live headlines:

Get a free API key from https://newsapi.org

Replace it inside your main.py:

url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY"


Run again and say — “Jarvis, tell me the latest news.”

📂 Project Structure
Mega-Project-1---Jarvis/
│
├── main.py
├── README.md
└── jarvis-env/ (virtual environment)

🧠 Future Enhancements

🤖 ChatGPT integration for smarter replies

📨 Send emails or WhatsApp messages

🎵 Play songs and YouTube control

📅 Add reminders & alarms

💡 Smart home controls

💬 Output Example
Listening for wake word...
You: Jarvis
Jarvis: Yes bro
You: Open Google
Jarvis: Opening Google

✨ Author

👨‍💻 Prashant Kumar
B.Tech CSE | Aspiring Cyber Security Engineer 🔐
Proud Desi Boy 🇮🇳 | Loves building cool tech projects

🌐 GitHub

💼 LinkedIn

💖 Support

If you like this project, please ⭐ star the repo and share it with your developer friends!
Every star motivates me to build even better projects! 🌟
