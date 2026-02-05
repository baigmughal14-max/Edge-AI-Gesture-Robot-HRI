import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def fingers_up(hand):
    tips = [8, 12, 16, 20]     # index, middle, ring, pinky
    bases = [6, 10, 14, 18]

    fingers = []
    for tip, base in zip(tips, bases):
        fingers.append(hand.landmark[tip].y < hand.landmark[base].y)

    return fingers  # [index, middle, ring, pinky]

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)
    gesture = "NONE"

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            fingers = fingers_up(hand)
            wrist_x = hand.landmark[0].x
            index_x = hand.landmark[8].x

            if fingers == [False, False, False, False]:
                gesture = "FORWARD"

            elif fingers == [True, True, True, True]:
                gesture = "STOP"

            elif fingers == [True, False, False, False]:
                if index_x > wrist_x:
                    gesture = "RIGHT"
                else:
                    gesture = "LEFT"

    # ✅ ✅ ✅ ADD THIS EXACTLY HERE ✅ ✅ ✅
    with open("/tmp/gesture.txt", "w") as f:
        f.write(gesture)

    cv2.putText(frame, f"Gesture: {gesture}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Gesture Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

