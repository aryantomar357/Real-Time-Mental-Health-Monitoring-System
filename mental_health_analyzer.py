import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pyttsx3
import threading
import random
import pygame

# Function to get the most recent CSV file
def get_latest_csv(directory):
    files = [f for f in os.listdir(directory) if f.endswith(".csv")]
    if not files:
        raise FileNotFoundError("No CSV files found in directory.")
    latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(directory, f)))
    return os.path.join(directory, latest_file)

# Function to play relaxing music
def play_relaxing_music(avg_stress, avg_depression):
    script_dir = os.path.dirname(os.path.abspath(__file__))  
    music_files = [
        os.path.join(script_dir, "relaxing_music1.mp3"),
        os.path.join(script_dir, "relaxing_music2.mp3"),
        os.path.join(script_dir, "relaxing_music3.mp3")
    ]
    music_files = [m for m in music_files if os.path.exists(m)]
    if not music_files:
        print("🚨 No music files found! Please add .mp3 files.")
        return
    if avg_stress > 0.2 or avg_depression > 0.3:
        music = random.choice(music_files)
        print(f"🎵 Playing: {music}")
        pygame.mixer.init()
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

# Voice-powered Chatbot
def mental_health_chatbot(avg_stress, avg_depression, avg_anxiety, avg_happiness):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    print("\n--- AI Mental Health Chatbot ---")
    messages = []

    if avg_stress > 0.2:
        msg = "You seem stressed. Try taking deep breaths or listening to calming music."
        print("💡", msg)
        messages.append(msg)
    
    if avg_depression > 0.3 and avg_happiness < 0.5:
        msg = "It's okay to feel low sometimes. Talk to a loved one or engage in activities you enjoy."
        print("💙", msg)
        messages.append(msg)

    if avg_anxiety > 0.15:
        msg = "Anxiety detected. Consider mindfulness exercises or short walks outside."
        print("🌿", msg)
        messages.append(msg)

    if avg_happiness > 0.5:
        msg = "You're doing great! Keep up the positive vibes."
        print("😊", msg)
        messages.append(msg)

    if not messages:
        msg = "Your emotional health looks balanced. Keep maintaining a healthy lifestyle!"
        print(msg)
        messages.append(msg)

    print("\nNeed more help? Talking to someone might help. Stay strong! 💪")

    for message in messages:
        engine.say(message)
    engine.runAndWait()

# MAIN FUNCTION for GUI usage
def run_mental_health_analysis(csv_path=None):
    try:
        data_file = csv_path if csv_path else get_latest_csv(".")

        if os.stat(data_file).st_size == 0:
            print(f"❌ Error: '{data_file}' is empty.")
            return

        df = pd.read_csv(data_file, parse_dates=["Timestamp"])
        if df.empty:
            print("❌ CSV loaded but contains no data.")
            return

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    if "Emotion" not in df.columns:
        print("❌ 'Emotion' column not found in CSV.")
        return

    df["TimeDelta"] = df["Timestamp"].diff()

    # Thresholds
    stress_threshold = 0.2
    depression_threshold = 0.3
    anxiety_threshold = 0.15
    happiness_threshold = 0.5

    df["Stress"] = (df["Emotion"] == "fear") | (df["Emotion"] == "angry")
    df["Depression"] = df["Emotion"] == "sad"
    df["Anxiety"] = df["Emotion"] == "surprise"
    df["Happiness"] = df["Emotion"] == "happy"

    avg_stress = df["Stress"].mean()
    avg_depression = df["Depression"].mean()
    avg_anxiety = df["Anxiety"].mean()
    avg_happiness = df["Happiness"].mean()

    if avg_happiness > happiness_threshold:
        avg_depression = 0

    # Start relaxing music
    music_thread = threading.Thread(target=play_relaxing_music, args=(avg_stress, avg_depression), daemon=True)
    music_thread.start()

    # Radar chart
    categories = ["Stress", "Depression", "Anxiety", "Happiness"]
    values = [avg_stress, avg_depression, avg_anxiety, avg_happiness]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    plt.figure(figsize=(8, 8))
    plt.polar(angles, values, marker="o")
    plt.fill(angles, values, alpha=0.25)
    plt.xticks(angles[:-1], categories)
    plt.title("Emotional Health Indicators")
    plt.show()

    # Chatbot
    mental_health_chatbot(avg_stress, avg_depression, avg_anxiety, avg_happiness)
