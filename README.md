Project Description
This project demonstrates real-time face detection using OpenCV and interacts with a web browser based on whether a face is detected or not. The program continuously captures video from the webcam, detects faces using the Haar Cascade classifier, and opens a Google search page with specific text based on the detection result.

Features
Webcam Interaction: Utilizes the webcam to capture video frames for face detection.
Face Detection: Employs the Haar Cascade classifier to detect faces in the video stream.
Web Browser Interaction: Opens a Google search page with different text depending on whether a face is detected or not.
Real-Time Processing: Performs face detection and browser interaction in real-time with low latency.
Implementation Details
Library Usage: Utilizes the OpenCV library for video capture and face detection.
Haar Cascade Classifier: Loads the pre-trained Haar Cascade classifier for face detection.
Web Browser Interaction: Utilizes the webbrowser module to open Google search pages.
Infinite Loop: The program runs in an infinite loop to continuously capture video frames and perform face detection.
User Interaction: Pressing the 'q' key exits the program.
Usage
Execution: Run the script to start real-time face detection and web browser interaction.
Webcam Requirement: Ensure that a webcam is connected and accessible.
Key Press: Press the 'q' key to exit the program.
Dependencies
OpenCV (cv2)
webbrowser module
time module
