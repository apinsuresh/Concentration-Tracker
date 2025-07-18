# 🧠 Concentration Tracker using MediaPipe and OpenCV

This project tracks a person's concentration in real-time using their webcam. It uses **MediaPipe FaceMesh** to detect facial landmarks, estimate eye positions, and determine if the user is focused or distracted. A live graph of the user's focus percentage is also shown using **Matplotlib**.

## 📸 Features

- Real-time webcam-based eye tracking
- Determines if the user is "Focused" or "Distracted"
- Displays live percentage graph of focus over time
- Uses OpenCV, MediaPipe, and Matplotlib
- ESC key to exit the application

## 🚀 How it works

- FaceMesh detects facial landmarks (iris and eyes)
- Eye direction is analyzed to infer focus
- If the user is looking roughly center, it's considered **focused**
- The focus percentage is tracked and plotted over time

## 🖥️ Screenshots<img width="1886" height="1000" alt="Screenshot 2025-07-18 124533" src="https://github.com/user-attachments/assets/f48cfa03-35e9-494a-a17c-9ddbd0c2b9bf" />
<img width="1888" height="1002" alt="Screenshot 2025-07-18 124853" src="https://github.com/user-attachments/assets/fd52e8e7-37d0-484f-91f8-64127294c4d6" />

