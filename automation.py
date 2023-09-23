import cv2
import time
import webbrowser

# Load the cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start an infinite loop
while True:
    # Start the webcam
    cap = cv2.VideoCapture(0)

    # Initialize the face detected flag
    face_detected = False

    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Check if a face is detected
    if len(faces) > 0:
        # Open a Google search with a specific text if a face is detected
        webbrowser.open("https://www.google.com/search?q=face+detected")
        face_detected = True

    # Check if no face is detected
    if len(faces) == 0:
        # Open a Google search with a different text if no face is detected
        webbrowser.open("https://www.google.com/search?q=face+not+detected")
        face_detected = False
        break

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the output
    cv2.imshow("Live Face Detection", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Release the webcam
    cap.release()
    
    # Sleep for 10 seconds before checking again
    time.sleep(10)

# Destroy all windows
cv2.destroyAllWindows()


