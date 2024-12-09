import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np

# Replace with your model loading code
def load_model():
    # Load your trained YOLO model here
    # For example: model = YOLOv9.load("path_to_your_trained_model")
    model = YOLO("Counting_classes\yolov9s_model.pt")  # Placeholder
    return model

# Replace with your model prediction code
def predict(image, model):
    """
    Perform prediction using the YOLO model.
    This function should return a list of detections in the format:
    [x_center, y_center, width, height, confidence, class_id]
    """
    # Placeholder for actual prediction
    # Replace this with your model's inference code
    detections = model.predict(image)
    # detections = [
    #     [223.1802, 134.9060, 27.0698, 45.4013, 0.9, 1],  # Example faulty panel
    #     [432.7804, 140.4587, 26.7912, 45.0982, 0.8, 0],  # Example non-faulty panel
    #     # Add more dummy detections as needed for testing
    # ]
    return detections

def count_panels_with_class(detections, class_names):
    """
    Counts the number of faulty and non-faulty solar panels based on YOLO detections.
    """
    panel_counts = {'faulty': 0, 'non_faulty': 0}

    for detection in detections:
        class_id = int(detection[-1])
        class_name = class_names[class_id]

        if class_name == 'faulty':
            panel_counts['faulty'] += 1
        elif class_name == 'non_faulty':
            panel_counts['non_faulty'] += 1

    return panel_counts

def draw_detections(image, detections, class_names):
    """
    Draw bounding boxes around detected panels on the image.
    """
    for detection in detections:
        x_center, y_center, width, height, confidence, class_id = detection
        class_name = class_names[class_id]

        # Convert to top-left corner format
        x_min = int(x_center - width / 2)
        y_min = int(y_center - height / 2)
        x_max = int(x_center + width / 2)
        y_max = int(y_center + height / 2)

        # Draw bounding box
        color = (0, 255, 0) if class_name == 'non_faulty' else (0, 0, 255)
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 2)
        cv2.putText(image, f"{class_name} ({confidence:.2f})", (x_min, y_min - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return image

# Streamlit app
def main():
    st.title("Solar Panel Fault Detection")
    st.write("Upload an image to detect faulty and non-faulty solar panels.")

    # Load your model (placeholder)
    model = load_model()

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Read the image file
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Display the original image
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Perform detection
        detections = predict(image, model)

        # Count panels
        class_names = ['non_faulty', 'faulty']
        panel_counts = count_panels_with_class(detections, class_names)

        # Draw detections on the image
        image_with_boxes = draw_detections(image.copy(), detections, class_names)

        # Display results
        st.image(image_with_boxes, caption='Detection Results', use_column_width=True)
        st.write(f"Number of faulty panels: {panel_counts['faulty']}")
        st.write(f"Number of non-faulty panels: {panel_counts['non_faulty']}")

if __name__ == "__main__":
    main()
