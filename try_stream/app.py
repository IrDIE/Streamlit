import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2




st.title('Video capturing from OpenCV')

frame_ph = st.empty()
stop_stream_bottom = st.button('Stop')
# cap = cv2.VideoCapture(0)
# while cap.isOpened() and not stop_stream_bottom:
#     success, img = cap.read()
#
#     frame_ph.image(img, channels="BGR")
#     cv2.imshow("Show from client webcam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q') or stop_stream_bottom:
#         break
# cap.release()
# cv2.destroyAllWindows()

webrtc_streamer(key="example"
                , rtc_configuration={     "iceServers": [{"urls": ["stun:stun.relay.metered.ca:80"]}]    }
                )