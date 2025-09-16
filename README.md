# 🤖 Raja - Your Personal AI Voice Assistant

**Raja** is a Python-based AI virtual assistant that uses voice commands to perform various desktop and web-based tasks. It integrates with numerous Python libraries to provide functionalities like speech recognition, sending emails, weather forecasting, web browsing, fetching news, playing music, telling jokes, and much more.

---

## 🚀 Features

- 🔊 **Voice Interaction** (via `speech_recognition`, `pyttsx3`)
- 🌐 **Wikipedia Search**
- 📧 **Send Emails via Gmail**
- 🎵 **Play Music from Local Directory**
- 📸 **Take and Show Photos**
- 🔍 **Web Search (Google, YouTube, StackOverflow)**
- 📰 **Fetch Latest News (Times of India)**
- 🤓 **Answer Computational Questions (WolframAlpha)**
- 🕒 **Tell Time**
- 🌦️ **Weather Forecast (OpenWeatherMap API)**
- 😂 **Jokes (via `pyjokes`)**
- 📝 **Write and Read Notes**
- 🗑️ **Empty Recycle Bin**
- 🔒 **Lock, Shutdown, Hibernate, Restart System**
- 💬 **Twilio SMS Messaging**
- 📍 **Find Locations on Map**

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/raja-voice-assistant.git
   cd raja-voice-assistant
Create a virtual environment (optional but recommended)

'''bash
python -m venv venv
venv\Scripts\activate  # On Windows
Install the required dependencies

bash
Copy code
pip install -r requirements.txt
Edit your credentials

Open the Python script and replace placeholders like:

example@gmail.com

**Password**

APP_ID (WolframAlpha)

API_KEY (OpenWeatherMap)

ACCOUNT_SID, AUTH_TOKEN (Twilio)

Update music_dir to your songs folder

🧠 How It Works
Speech Recognition: Listens to your voice using speech_recognition and a microphone.

Text-to-Speech: Replies back using pyttsx3.

Conditional Logic: Parses keywords from your commands to determine the action.

Web Integration: Opens websites, searches Wikipedia, sends emails, and fetches weather/news.

System Control: Shuts down, hibernates, logs off, or locks your PC.

📁 File Structure
csharp
Copy code
├── ai.py                  # Main assistant script
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── new.txt                  # Notes file (created at runtime)
📌 Requirements
Ensure you have the following installed:

Python 3.x

Microphone & speaker (for voice input/output)

Internet connection (for online APIs)

Install the required Python modules:

bash
Copy code
pip install speechrecognition pyttsx3 wikipedia webbrowser opencv-python wolframalpha requests pyaudio pyjokes feedparser smtplib twilio beautifulsoup4 win32com pypiwin32 clint Pillow youtubesearchpython
🔒 Important Notes
Security: Do NOT hardcode sensitive information (passwords, API keys) in production. Use environment variables instead.

Twilio: You'll need a Twilio account and verified phone numbers to send messages.

Gmail Access: Enable “Less secure app access” or use App Passwords for Gmail SMTP.

🎯 Usage
Run the assistant:

bash
Copy code
python raja.py
Then, speak commands like:

“Search Python in Wikipedia”

“Play music”

“Send mail”

“What is the weather in London”

“Take a photo”

“Lock window”

“Tell me a joke”

📄 License
This project is open-source and available under the MIT License.

🙋‍♂️ Created by
Raja – Passionate about Python, AI, and automation.

"Raja 1.0 in your service!"
