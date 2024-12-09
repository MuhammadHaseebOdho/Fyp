

# Solar Panel Fault Detection System

## Overview
The **Solar Panel Fault Detection System** is an advanced solution designed to detect faulty solar panels using Deep Learning models integrated with a user-friendly Streamlit interface. It leverages models such as YOLOv9s, YOLOv10s, and Detectron2 to analyze images or videos of solar panels, identifying faulty and non-faulty panels in real-time.

---

## Features
- **Image and Video Analysis**: Detect faults in solar panels from uploaded images or video feeds.
- **Real-Time Detection**: Utilize webcam input for real-time monitoring.
- **Customizable Models**: Switch between different pre-trained models for detection.
- **Results Visualization**: Highlights detected faults on solar panels with bounding boxes and provides detailed detection statistics.

---

## Technologies Used
- **Frontend**: Streamlit for an interactive user interface.
- **Backend**: Python with integrated Deep Learning models.
- **Deep Learning Frameworks**: 
  - YOLOv9
  - YOLOv10
  - Detectron2
- **Computer Vision**: OpenCV for image processing and visualization.
- **Libraries**: 
  - `streamlit==1.22.0`
  - `ultralytics==8.0.98`
  - `opencv-python==4.7.0.72`
  - `Pillow==9.5.0`

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MuhammadHaseebOdho/Fyp.git
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Pre-trained Models**:
   Place the YOLOv9, YOLOv10, and Detectron2 models in the `weights/detection` directory. Update the paths in the `config.py` file if necessary.

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. Open the app in your browser using the provided URL after running `streamlit run`.
2. Use the sidebar to configure the detection:
   - Select the desired model (YOLOv9, YOLOv10, or Detectron2).
   - Choose the input source (Image, Video, or Webcam).
3. Upload an image or video file, or start the webcam for real-time analysis.
4. View the detection results with bounding boxes and counts of faulty and non-faulty panels.

---

## Directory Structure
```plaintext
solar-panel-fault-detection/
├── app.py              # Main application file
├── config.py           # Configuration settings for models and sources
├── utils.py            # Utility functions for detection and visualization
├── weights/            # Directory to store pre-trained models
│   └── detection/      # YOLO and Detectron2 models
├── requirements.txt    # Python dependencies
```

---

## Future Enhancements
- **Integration with IoT Devices**: Extend the system to capture data from solar panels in real-time.
- **Advanced Models**: Explore more robust models for improved accuracy.
- **Dashboard Analytics**: Incorporate a dashboard for detailed fault analysis and history tracking.

---


