#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   @File Name:     app.py
   @Author:        izhar Nabi
   @Date:          20/10/2024
   @Description:
-------------------------------------------------
"""
from pathlib import Path
from PIL import Image
import streamlit as st

import config
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

# setting page layout
st.set_page_config(
    page_title="Solar Panel Fault Detection System Interface",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
    )

# main page heading
st.title("Solar Panel Fault Detection System Interface")
from PIL import Image
import streamlit as st

import base64

# Function to encode image to Base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# # Path to your local image file
# background_image_path = "E:\Practice_Project\Emergency_Call_Classification\FYP_Final_Project\YOLOv8-streamlit-app\pexels-nc-farm-bureau-mark-15751130.jpg"  # Replace with the path to your image

# # Get Base64 string of the image
# base64_image = get_base64_of_bin_file(background_image_path)

# # Embed CSS to set the background image
# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url("data:{background_image_path};base64,{base64_image}");
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Load an image
# image = Image.open("YOLOv8-streamlit-app\pexels-kelly-1179532-4320449.jpg")

# # Resize the image
# resized_image = image.resize((1200, 400))  # Specify your desired width and height

# # Display the resized image in Streamlit
# st.image(resized_image, caption="Solar Panels")

# sidebar
st.sidebar.header("DL Model Config")

# model options
task_type = st.sidebar.selectbox(
    "Select Task",
    ["Detection"]
)

model_type = None
if task_type == "Detection":
    model_type = st.sidebar.selectbox(
        "Select Model",
        config.DETECTION_MODEL_LIST
    )
else:
    st.error("Currently only 'Detection' function is implemented")

# confidence = float(st.sidebar.slider(
#     "Select Model Confidence", 30, 100, 50)) / 100

model_path = ""
if model_type:
    model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))
else:
    st.error("Please Select Model in Sidebar")

# load pretrained DL model
try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"Unable to load model. Please check the specified path: {model_path}")

# image/video options
st.sidebar.header("Image/Video Config")
source_selectbox = st.sidebar.selectbox(
    "Select Source",
    config.SOURCES_LIST
)

source_img = None
if source_selectbox == config.SOURCES_LIST[0]: # Image
    infer_uploaded_image(model) #confidence
elif source_selectbox == config.SOURCES_LIST[1]: # Video
    infer_uploaded_video(model) #confidence
elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
    infer_uploaded_webcam(model) #confidence
else:
    st.error("Currently only 'Image' and 'Video' source are implemented")