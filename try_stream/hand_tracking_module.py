import cv2
import time
import mediapipe as mp
import streamlit as st

import math
from streamlit_webrtc import webrtc_streamer

class handDetector():
    def __init__(self, mode : bool = False, max_num_hands : int  = 1, min_detection_confidence = 0.5, min_tracking_confidence = 0.5):

        self.static_image_mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode = self.static_image_mode, max_num_hands = self.max_num_hands)
        self.mp_display = mp.solutions.drawing_utils



    def findHands(self, img ):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        self.res = self.hands.process(img_rgb)
        if self.res.multi_hand_landmarks is not None:
            for hand_lm in self.res.multi_hand_landmarks:
                for id, landMark in enumerate(hand_lm.landmark):
                    h, w, c = img.shape
                    cx, cy = int(landMark.x * w), int(landMark.y * h)

                self.mp_display.draw_landmarks(img, hand_lm, self.mpHands.HAND_CONNECTIONS)

        return img

    def find_positions(self, img, handN = 0, draw = True):
        bbox = []
        self.lm_list = []

        if self.res.multi_hand_landmarks is not None:
            hand =  self.res.multi_hand_landmarks[handN]
            for id, landMark in enumerate(hand.landmark):
                h, w, c = img.shape
                cx, cy = int(landMark.x * w), int(landMark.y * h)
                self.lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (44, 252, 3), cv2.FILLED)  # green

            x_max , y_max = max([self.lm_list[i][1] for i in range(len(self.lm_list))]), max([self.lm_list[i][2] for i in range(len(self.lm_list)) ])
            x_min, y_min = min([self.lm_list[i][1] for i in range(len(self.lm_list)) ]), min([self.lm_list[i][2] for i in range(len(self.lm_list))])

            bbox = x_min, y_min, x_max, y_max
            if draw:
                cv2.rectangle(img, (bbox[0]-15, bbox[1]-15), (bbox[2]+15, bbox[3]+15), (0,255,0), 1)

        return self.lm_list, bbox

    def find_distance(self, finger1_id, finger2_id, img, draw = True):
        x2, y2 = self.lm_list[finger1_id][1], self.lm_list[finger1_id][2]
        x1, y1 = self.lm_list[finger2_id][1], self.lm_list[finger2_id][2]

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.circle(img, (x2, y2), 7, (3, 186, 252), cv2.FILLED)
            cv2.circle(img, (x1, y1), 7, (3, 186, 252), cv2.FILLED)
            cv2.circle(img, (cx, cy), 9, (245, 135, 66), 2)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        lenght_line = math.hypot(x2 - x1, y2 - y1)
        return lenght_line, img, [[x1, y1],[x2, y2], [cx, cy] ]

    def check_if_fingers_up(self):
        if self.lm_list[14][2] > self.lm_list[16][2]:
            return True
        else:
            return False


def main():
    cap = cv2.VideoCapture(0)
    prev_time = 0
    curr_time = 0
    detector = handDetector()

    while True:
        success, img = cap.read()
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        img = detector.findHands(img)
        positions_list = detector.find_positions(img, draw = True)


        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 225), 1)

        cv2.imshow("hi there", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break




def main():
    st.title("Live AI Squat Counter")
    webrtc_streamer(key="example2"
                    , rtc_configuration=
                    {
                        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
                        #     [
                        #     {
                        #         "urls": ["stun:fr-turn2.xirsys.com"]
                        #     }, {
                        #         "username": "PhUZzBq2wugeeSwzRxiwKCluHmp2OrZVfKvSWUMKVKJNK8B08EiCqVacNkLcfxkvAAAAAGTMeP1JcmluYQ==",
                        #         "credential": "1f5dbe1c-327c-11ee-a998-0242ac120004",
                        #         "urls": [
                        #             "turn:fr-turn2.xirsys.com:80?transport=udp",
                        #             "turn:fr-turn2.xirsys.com:3478?transport=udp",
                        #             "turn:fr-turn2.xirsys.com:80?transport=tcp",
                        #             "turn:fr-turn2.xirsys.com:3478?transport=tcp",
                        #             "turns:fr-turn2.xirsys.com:443?transport=tcp",
                        #             "turns:fr-turn2.xirsys.com:5349?transport=tcp"
                        #         ]}
                        #
                        # ]
                    },
                    media_stream_constraints={"video": True, "audio": False},

                    )


if __name__ == "__main__":
    main()