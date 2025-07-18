import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
from collections import deque
import numpy as np
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

LEFT_EYE = 33
RIGHT_EYE = 362

focus_history = deque(maxlen=300)
focus_percentages = []
timestamps = []

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], 'g-')
ax.set_ylim(0, 100)
ax.set_xlim(0, 60)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Focus %')
ax.set_title('Live Focus Percentage
             
cap = cv2.VideoCapture(0)
start_time = time.time()
last_update_time = time.time()

def get_eye_center(landmarks, eye_idx, img_w, img_h):
    x = int(landmarks[eye_idx].x * img_w)
    y = int(landmarks[eye_idx].y * img_h)
    return (x, y)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_h, img_w = frame.shape[:2]
    results = face_mesh.process(rgb)

    status = "No Face Detected"
    color = (255, 255, 255)
    is_focused = 0

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            left_eye = get_eye_center(face_landmarks.landmark, LEFT_EYE, img_w, img_h)
            right_eye = get_eye_center(face_landmarks.landmark, RIGHT_EYE, img_w, img_h)

            cv2.circle(frame, left_eye, 3, (0, 255, 0), -1)
            cv2.circle(frame, right_eye, 3, (0, 255, 0), -1)

            center_x = (left_eye[0] + right_eye[0]) / 2
            if img_w * 0.35 < center_x < img_w * 0.65:
                status = "✅ Focused"
                color = (0, 255, 0)
                is_focused = 1
            else:
                status = "❌ Distracted"
                color = (0, 0, 255)

    focus_history.append(is_focused)

    # Update graph every 1 second
    current_time = time.time()
    if current_time - last_update_time >= 1:
        if len(focus_history) > 0:
            percent = sum(focus_history) / len(focus_history) * 100
            elapsed = current_time - start_time
            focus_percentages.append(percent)
            timestamps.append(elapsed)

            # Keep only last 60s
            if len(timestamps) > 60:
                focus_percentages.pop(0)
                timestamps.pop(0)

            line.set_xdata(timestamps)
            line.set_ydata(focus_percentages)
            ax.set_xlim(max(0, elapsed - 60), elapsed + 1)
            fig.canvas.draw()
            fig.canvas.flush_events()

        last_update_time = current_time

    # Show video
    cv2.putText(frame, status, (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
    cv2.imshow("Focus Tracker", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()    
    
