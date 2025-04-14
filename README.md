# 🧠 Real-Time Mental Health Monitoring System

An AI-based application designed to monitor real-time emotional states using webcam input, analyze mental health indicators (stress, anxiety, depression, and happiness), and provide personalized support through music and a voice-based chatbot.

---

## 📌 Project Overview

This project offers an innovative solution for monitoring mental well-being using Artificial Intelligence. It captures emotional expressions via webcam, performs real-time analysis, and provides coping strategies with music and chatbot assistance — all integrated within an intuitive GUI.

### 🔍 Key Features
- 🎥 Real-time **Emotion Detection** using webcam and deep learning.
- 📊 **Mental Health Analysis** covering stress, depression, anxiety, and happiness.
- 🎶 **Relaxing Music Suggestions** tailored to emotional state.
- 💬 AI-powered **Voice Chatbot** offering coping strategies and mental health support.
- 💻 **Modern GUI** built with Tkinter, supporting Light/Dark mode.
- 📁 CSV-based emotion logging and graphical insights.

---

## ⚙️ Installation & Setup

### ✅ Prerequisites 
- Python 3.6+
- A functioning webcam
- `pip` for Python package management

### 🔧 Steps to Set Up

1. **Clone the Repository**
   ```bash
   git clone https://github.com/aryantomar357/Real-Time-Mental-Health-Monitoring-System.git
2. **Navigate to the Project Directory**
   ```bash
   cd Real-Time-Mental-Health-Monitoring-System
4. **Create a Virtual Environment**
   ```bash
   python -m venv venv
6. **Activate the Virtual Environment**
   
   **On Windows:**
   
   ```
   
   .\venv\Scripts\activate
   ```
   
   **On Mac/Linux:**
   ```
   
   source venv/bin/activate
   ```
   
8. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
10. **Run the Application**
    ```bash
    python gui_main.py

### 🧠 System Architecture
```

+-----------------+     +----------------+     +--------------------+
|   Webcam Input  | --> |  Emotion Model | --> |  Emotion Prediction |
+-----------------+     +----------------+     +--------------------+
                                                        |
                                                        v
                                          +----------------------------+
                                          |  Mental Health Analyzer    |
                                          | (Stress, Anxiety, etc.)    |
                                          +----------------------------+
                                                        |
                       +-------------------------+------+----------------------+
                       |                         |                             |
                       v                         v                             v
          +-------------------+     +------------------------+     +----------------------+
          | Music Recommendation |  | Voice Chatbot Support |     | Graphical Feedback   |
          +-------------------+     +------------------------+     +----------------------+

```

### 🧰 Technologies Used
| Purpose            | Technology                    |
|--------------------|-------------------------------|
| GUI                | Tkinter                       |
| Emotion Detection  | OpenCV, Keras, TensorFlow     |
| Voice Engine       | pyttsx3                       |
| Music Playback     | pygame                        |
| Data Analysis      | pandas                        |
| Graphical Analysis | matplotlib                    |
| File Handling      | CSV                           |

### 📊 Output & Visualization
- 📈 Real-time radar chart showing emotion-based mental health metrics.
- 🗂️ Logs stored in CSV for future analysis.
- 🌗 Theme toggler for switching between light/dark modes.
- 💡 Interactive chatbot with emotion-sensitive responses.

### 🤝 Contributing
We welcome contributions to enhance this project!

**How to Contribute:**

- Fork the repository
- Create a new branch (git checkout -b feature-name)
- Make your changes and commit (git commit -m 'Add feature')
- Push to your branch (git push origin feature-name)
- Open a Pull Request

Please ensure all changes are well-documented and tested.

### 🙌 Acknowledgments
- Inspired by the need to promote emotional well-being through technology.
- Powered by open-source tools and research in AI and mental health.

### 🌐 Connect
**GitHub Repo: @aryantomar357**
