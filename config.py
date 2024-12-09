#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   @File Name:     config.py
   @Author:        izhar Nabi
   @Date:          20/10/2024
   @Description: configuration file
-------------------------------------------------
"""
from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())


# Source
SOURCES_LIST = ["Image", "Video", "Webcam"]


# DL model config
DETECTION_MODEL_DIR = ROOT / 'weights' / 'detection'
YOLOv9s = DETECTION_MODEL_DIR / "yolov9s_model.pt"
YOLOv10s = DETECTION_MODEL_DIR / "yolov10s_model.pt"
Detectron2 = DETECTION_MODEL_DIR / "Detectron2_model.pt"


DETECTION_MODEL_LIST = [
    "yolov9s_model.pt",
    "yolov10s_model.pt",
    "Detectron2_model.pt",
]
