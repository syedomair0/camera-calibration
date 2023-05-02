import cv2
import numpy as np

cap = cv2.VideoCapture('labeled/0.hevc')
_, prev_frame = cap.read()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Define the parameters for optical flow
lk_params = dict(winSize=(15, 15),
                 maxLevel=4,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

while True:
    _, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate optical flow
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Compute the magnitude and angle of the flow vectors
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    # Compute the average direction of motion
    avg_angle = np.mean(angle)

    # Convert the angle to degrees
    avg_angle_degrees = avg_angle * 180 / np.pi

    # Draw the optical flow vectors
    for y in range(0, gray.shape[0], 10):
        for x in range(0, gray.shape[1], 10):
            x2 = int(x + flow[y, x, 0])
            y2 = int(y + flow[y, x, 1])
            cv2.arrowedLine(frame, (x, y), (x2, y2), (0, 255, 0), 1)

    # Show the frame and the direction of motion
    cv2.imshow("Frame", frame)
    print("Direction of motion: %.2f degrees" % avg_angle_degrees)

    # Update the previous frame and the previous grayscale image
    prev_frame = frame.copy()
    prev_gray = gray.copy()

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
