import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import av
import time
import mediapipe as mp
import time
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import hand_tracking_module



st.title('Video capturing from OpenCV')

frame_ph = st.empty()
stop_stream_bottom = st.button('Stop')

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volume.GetMasterVolumeLevel()
min, max = volume.GetVolumeRange()[0], volume.GetVolumeRange()[1]
st.markdown(f"min max = {min}, {max}")
volume.SetMasterVolumeLevelScalar(0/100, None)

def video_frame_callback(frame: av.VideoFrame, volume = volume) -> av.VideoFrame:
    detector = hand_tracking_module.handDetector(min_tracking_confidence=.9)

    image = frame.to_ndarray(format="bgr24")
    img = detector.findHands(image)

    return av.VideoFrame.from_ndarray(img, format="bgr24")



webrtc_streamer(key="example"
                , rtc_configuration=
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
                },
media_stream_constraints={"video": True, "audio": False},
                video_frame_callback=video_frame_callback
                )

