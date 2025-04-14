import csv
import cv2
import numpy as np
from datetime import datetime
from tensorflow.keras.models import load_model
from PIL import Image, ImageTk

# Load trained emotion detection model
model = load_model('model/emotion_detection_model.h5')

# Emotion labels
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Load the face cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

running = False  # Global flag to control detection loop

def start_emotion_detection(video_label=None):
    global running
    running = True
    cap = cv2.VideoCapture(0)

    # Open CSV file for writing
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"emotions_{timestamp}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Emotion"])

        while running:
            ret, frame = cap.read()
            if not ret:
                break

            # Detect faces in the frame
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                face_roi = gray_frame[y:y + h, x:x + w]
                face_roi = cv2.resize(face_roi, (64, 64))
                face_roi = face_roi.astype('float32') / 255.0
                face_roi = np.expand_dims(face_roi, axis=-1)
                face_roi = np.expand_dims(face_roi, axis=0)

                predictions = model.predict(face_roi)
                max_index = np.argmax(predictions[0])
                emotion = emotion_labels[max_index]

                current_timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                writer.writerow([current_timestamp, emotion])

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            if video_label:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(rgb_frame)
                imgtk = ImageTk.PhotoImage(image=img)
                video_label.imgtk = imgtk
                video_label.config(image=imgtk)

    cap.release()

def stop_emotion_detection():
    global running
    running = False