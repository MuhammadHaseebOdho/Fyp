#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   @File Name:     utils.py
   @Author:        Izhar Nabi
   @Date:          20/10/2024
   @Description:
-------------------------------------------------
"""
from ultralytics import YOLO
import streamlit as st
import cv2
from PIL import Image
import tempfile


def _display_detected_frames(model, st_frame, image):
    """
    Display the detected objects on a video frame using the YOLOv8 model.
    :param conf (float): Confidence threshold for object detection.
    :param model (YOLOv8): An instance of the `YOLOv8` class containing the YOLOv8 model.
    :param st_frame (Streamlit object): A Streamlit object to display the detected video.
    :param image (numpy array): A numpy array representing the video frame.
    :return: None
    """
    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720 * (9 / 16))))

    # Predict the objects in the image using YOLO models
    res = model.predict(image) #conf=conf)

    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )


@st.cache_resource
def load_model(model_path):
    """
    Loads a YOLO object detection model from the specified model_path.

    Parameters:
        model_path (str): The path to the YOLO model file.

    Returns:
        A YOLO object detection model.
    """
    model = YOLO(model_path)
    return model


def infer_uploaded_image(model): #conf
    """
    Execute inference for uploaded image
    :param conf: Confidence of YOLOvX model
    :param model: An instance of the `YOLOvX` class containing the YOLOvX model.
    :return: None
    """
    source_img = st.sidebar.file_uploader(
        label="Choose an image...",
        type=("jpg", "jpeg", "png", 'bmp', 'webp')
    )

    col1, col2 = st.columns(2)

    with col1:
        if source_img:
            uploaded_image = Image.open(source_img)
            # adding the uploaded image to the page with caption
            st.image(
                image=source_img,
                caption="Uploaded Image",
                use_column_width=True
            )

    if source_img:
        if st.button("Detect"):
            with st.spinner("Running..."):
                res = model.predict(uploaded_image,) #conf
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]

                # with col2:
                #     st.image(res_plotted,
                #              caption="Detected Image",
                #              use_column_width=True)
                #     try:
                #         with st.expander("Detection Results"):
                #             for box in boxes:
                #                 st.write(box.xywh)
                #     except Exception as ex:
                #         st.write("No image is uploaded yet!")
                #         st.write(ex)
                # Counters for faulty and non-faulty panels
                faulty_count = 0
                non_faulty_count = 0
                normal = 0
                # Get the class IDs for "faulty" and "non_faulty" panels
                FAULTY_CLASS_ID = None
                NON_FAULTY_CLASS_ID = None
                NORMAL = None

                # Loop through the model's class names to find the corresponding class IDs
                for class_id, class_name in model.names.items():
                    if class_name.lower() == "faulty":
                        FAULTY_CLASS_ID = class_id
                    elif class_name.lower() == "not_faulty":
                        NON_FAULTY_CLASS_ID = class_id
                    elif class_name.lower() == "normal":
                        NORMAL = class_id


                # # Define class IDs for faulty and non-faulty (adjust according to your model's classes)
                # FAULTY_CLASS_ID = "Not_faulty" # Example class ID for faulty panel
                # NON_FAULTY_CLASS_ID = "Faulty" # Example class ID for non-faulty panel

                # Count panels based on detected class IDs
                for box in boxes:
                    class_id = int(box.cls)
                    if class_id == FAULTY_CLASS_ID:
                        faulty_count += 1
                    elif class_id == NON_FAULTY_CLASS_ID:
                        non_faulty_count += 1
                    elif class_id == NORMAL:
                        normal += 1

                with col2:
                    st.image(res_plotted,
                             caption="Detected Image",
                             use_column_width=True)
                    try:
                        with st.expander("Detection Results"):
                            st.write(f"Total Number of panels are : {faulty_count+non_faulty_count+normal}")
                            st.write(f"Faulty Panels Detected: {faulty_count}")
                            st.write(f"Non-Faulty Panels Detected: {non_faulty_count}")
                            st.write(f"Normal panels Detected : {normal}")
                            for box in boxes:
                                st.write(box.xywh)
                    except Exception as ex:
                        st.write("No image is uploaded yet!")
                        st.write(ex)


def infer_uploaded_video(model): #conf
    """
    Execute inference for uploaded video
    :param conf: Confidence of YOLOvX model
    :param model: An instance of the `YOLOvX` class containing the YOLOvX model.
    :return: None
    """
    source_video = st.sidebar.file_uploader(
        label="Choose a video..."
    )

    if source_video:
        st.video(source_video)

    if source_video:
        if st.button("Detect"):
            with st.spinner("Running..."):
                try:
                    tfile = tempfile.NamedTemporaryFile()
                    tfile.write(source_video.read())
                    vid_cap = cv2.VideoCapture(
                        tfile.name)
                    st_frame = st.empty()
                    while (vid_cap.isOpened()):
                        success, image = vid_cap.read()
                        if success:
                            _display_detected_frames(
                                                     model,
                                                     st_frame,
                                                     image
                                                     ) #conf
                        else:
                            vid_cap.release()
                            break
                except Exception as e:
                    st.error(f"Error loading video: {e}")


def infer_uploaded_webcam(model): #conf
    """
    Execute inference for webcam.
    :param conf: Confidence of YOLOvX model
    :param model: An instance of the `YOLOvX` class containing the YOLOvX model.
    :return: None
    """
    try:
        flag = st.button(
            label="Stop running"
        )
        vid_cap = cv2.VideoCapture(0)  # local camera
        st_frame = st.empty()
        while not flag:
            success, image = vid_cap.read()
            if success:
                _display_detected_frames(
                    model,
                    st_frame,
                    image
                ) #conf
            else:
                vid_cap.release()
                break
    except Exception as e:
        st.error(f"Error loading video: {str(e)}")
