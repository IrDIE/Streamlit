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
                , rtc_configuration=  # stun.l.google.com:19305
                {
                    "iceServers": [
                        {
                            "urls": ["stun:fr-turn2.xirsys.com"]
                        }, {
                            "username": "PhUZzBq2wugeeSwzRxiwKCluHmp2OrZVfKvSWUMKVKJNK8B08EiCqVacNkLcfxkvAAAAAGTMeP1JcmluYQ==",
                            "credential": "1f5dbe1c-327c-11ee-a998-0242ac120004",
                            "urls": [
                                "turn:fr-turn2.xirsys.com:80?transport=udp",
                                "turn:fr-turn2.xirsys.com:3478?transport=udp",
                                "turn:fr-turn2.xirsys.com:80?transport=tcp",
                                "turn:fr-turn2.xirsys.com:3478?transport=tcp",
                                "turns:fr-turn2.xirsys.com:443?transport=tcp",
                                "turns:fr-turn2.xirsys.com:5349?transport=tcp"
                            ]}

                    ]
                }
                )

