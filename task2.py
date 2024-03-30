# Variant 1: Print the coordinates of the marker in the upper left corner

import cv2


def find_marker(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    marker = max(contours, key=cv2.contourArea) if contours else None
    return marker


def get_marker_position(marker):
    if marker is not None:
        x, y, w, h = cv2.boundingRect(marker)
        return x, y
    return None


video_path = 'blackbox.mp4'
cap = cv2.VideoCapture(video_path)
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Frame', 360, 640)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    marker = find_marker(frame)
    position = get_marker_position(marker)

    if position:
        print(f"Marker position: {position}")
        x, y, w, h = cv2.boundingRect(marker)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"X: {position[0]}, Y: {position[1]}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                    2)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
