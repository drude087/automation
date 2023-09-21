# automation
Purpose:

The script uses a pre-trained Haar Cascade classifier to detect faces in real-time from your computer's webcam feed.
Depending on whether a face is detected or not, it opens a Google search with specific queries.
Workflow:

The script starts the webcam and continuously captures video frames.
It converts each frame to grayscale and uses the Haar Cascade classifier to detect faces.
If a face is detected, it opens a Google search for "face detected."
If no face is detected, it opens a Google search for "face not detected."
It draws green rectangles around detected faces in the video frame.
The loop can be exited by pressing the 'q' key.
After each iteration, it releases the webcam for 10 seconds before checking again.
All windows are closed when the script ends.
