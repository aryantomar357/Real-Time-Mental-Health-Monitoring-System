import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont
import threading
from PIL import Image, ImageTk
from emotion_detector import start_emotion_detection, stop_emotion_detection
from mental_health_analyzer import run_mental_health_analysis

# ---------------- Global Theme Variables ---------------- #
theme = {
    "dark": {
        "bg": "#1c1f2e",
        "fg": "#ffffff",
        "btn": {
            "start": "#32CD32",
            "stop": "#FF4C4C",
            "analyze": "#00bcd4",
            "custom": "#ba68c8",
        }
    },
    "light": {
        "bg": "#f8f9fa",
        "fg": "#212529",
        "btn": {
            "start": "#28a745",
            "stop": "#dc3545",
            "analyze": "#007bff",
            "custom": "#6f42c1",
        }
    }
}
current_theme = "dark"

# ---------------- Main Window ---------------- #
root = tk.Tk()
root.title("Real-Time Mental Health Monitoring System")
root.geometry("1200x700")
root.minsize(1000, 600)

# ---------------- Sidebar Frame ---------------- #
sidebar = tk.Frame(root, width=250)
sidebar.pack(side="left", fill="y")

# ---------------- Content Frame ---------------- #
content = tk.Frame(root)
content.pack(side="right", expand=True, fill="both")

# ---------------- Fonts ---------------- #
title_font = tkfont.Font(family="Helvetica", size=22, weight="bold")
button_font = tkfont.Font(family="Helvetica", size=11)

# ---------------- Video Feed ---------------- #
video_frame = tk.Label(content, bd=3, relief="groove")
video_frame.pack(padx=30, pady=20, expand=True, fill="both")

# ---------------- Status Indicator ---------------- #
status_label = tk.Label(sidebar, text="Status: Idle", font=("Helvetica", 10, "bold"))
status_label.pack(pady=(15, 5))

# ---------------- Action Functions ---------------- #
def update_status(text):
    status_label.config(text=f"Status: {text}")

def start_detection_thread():
    update_status("Detecting...")
    threading.Thread(target=start_emotion_detection, args=(video_frame,), daemon=True).start()

def stop_detection():
    stop_emotion_detection()
    update_status("Stopped")

def analyze_latest_csv_thread():
    update_status("Analyzing CSV...")
    threading.Thread(target=run_mental_health_analysis, daemon=True).start()

def analyze_custom_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        update_status("Analyzing Custom CSV...")
        threading.Thread(target=run_mental_health_analysis, args=(file_path,), daemon=True).start()

def toggle_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    apply_theme()

def apply_theme():
    t = theme[current_theme]
    root.config(bg=t["bg"])
    sidebar.config(bg=t["bg"])
    content.config(bg=t["bg"])
    video_frame.config(bg=t["bg"])
    status_label.config(bg=t["bg"], fg=t["fg"])
    title_label.config(bg=t["bg"], fg=t["fg"])
    start_btn.config(bg=t["btn"]["start"], fg=t["fg"])
    stop_btn.config(bg=t["btn"]["stop"], fg=t["fg"])
    analyze_btn.config(bg=t["btn"]["analyze"], fg=t["fg"])
    custom_btn.config(bg=t["btn"]["custom"], fg=t["fg"])
    toggle_btn.config(bg="#444" if current_theme == "dark" else "#ddd")

# ---------------- Title ---------------- #
title_label = tk.Label(sidebar, text="🧠 Mental Tracker", font=title_font)
title_label.pack(pady=20)

# ---------------- Buttons ---------------- #
start_btn = tk.Button(sidebar, text="🎥 Start Detection", font=button_font, command=start_detection_thread, padx=20, pady=10, relief="raised")
start_btn.pack(pady=10, fill="x", padx=20)

stop_btn = tk.Button(sidebar, text="⏹ STOP", font=button_font, command=stop_detection, padx=20, pady=10, relief="raised")
stop_btn.pack(pady=10, fill="x", padx=20)

analyze_btn = tk.Button(sidebar, text="📊 Analyze Latest CSV", font=button_font, command=analyze_latest_csv_thread, padx=20, pady=10, relief="raised")
analyze_btn.pack(pady=10, fill="x", padx=20)

custom_btn = tk.Button(sidebar, text="📁 Analyze Custom CSV", font=button_font, command=analyze_custom_csv, padx=20, pady=10, relief="raised")
custom_btn.pack(pady=10, fill="x", padx=20)

# ---------------- Toggle Theme ---------------- #
toggle_btn = tk.Button(sidebar, text="🌙/☀️", font=button_font, command=toggle_theme)
toggle_btn.pack(pady=(40, 10), side="bottom")

# ---------------- Initial Theme ---------------- #
apply_theme()

# ---------------- Start App ---------------- #
root.mainloop()