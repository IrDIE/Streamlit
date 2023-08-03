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
                , rtc_configuration=
                {
                    "iceServers": [
                        {
                            "urls": "stun:stun.relay.metered.ca:80",
                        },
                        {
                            "urls": "turn:a.relay.metered.ca:80",
                            "username": "0e053deab7300457f9ecbb03",
                            "credential": "QlkpT5au/NwMGyNj",
                        },
                        {
                            "urls": "turn:a.relay.metered.ca:80?transport=tcp",
                            "username": "0e053deab7300457f9ecbb03",
                            "credential": "QlkpT5au/NwMGyNj",
                        },
                        {
                            "urls": "turn:a.relay.metered.ca:443",
                            "username": "0e053deab7300457f9ecbb03",
                            "credential": "QlkpT5au/NwMGyNj",
                        },
                        {
                            "urls": "turn:a.relay.metered.ca:443?transport=tcp",
                            "username": "0e053deab7300457f9ecbb03",
                            "credential": "QlkpT5au/NwMGyNj",
                        },
                    ],
                }
                )



###########
# RTCConfiguration(
# {"iceServers":[{"urls": ["stun:eu-turn6.xirsys.com"]},
# {"username": user,
# "credential": cred,
# "urls": ["turn:eu-turn6.xirsys.com:80?transport=udp",
# "turn:eu-turn6.xirsys.com:3478?transport=udp",
# "turn:eu-turn6.xirsys.com:80?transport=tcp",
# "turn:eu-turn6.xirsys.com:3478?transport=tcp",
# "turns:eu-turn6.xirsys.com:443?transport=tcp",
# "turns:eu-turn6.xirsys.com:5349?transport=tcp"]}]}
# )