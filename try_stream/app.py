import streamlit as st
#from streamlit_webrtc import webrtc_streamer
import cv2
import mediapipe as mp
import os
import av
import time
import math

#import hand_tracking_module



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

                )

