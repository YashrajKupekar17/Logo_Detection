# Logo Detection

The Logo Detection project is a computer vision application that detects and tracks the presence of Pepsi and Coca-Cola logos in video streams. This project demonstrates the use of state-of-the-art object detection techniques, specifically the YOLOv8 model, to identify and localize the logos within the video frames.

## Features

•⁠  ⁠Detects Pepsi and Coca-Cola logos in video files
•⁠  ⁠Tracks the location, size, and distance from the center of the frame for each detected logo
•⁠  ⁠Generates an annotated video file with bounding boxes and metadata for the detected logos
•⁠  ⁠Saves the detection information (timestamps, sizes, and distances) in a JSON file

## Getting Started

### Prerequisites

•⁠  ⁠Python 3.9 or higher
•⁠  ⁠pip (Python package installer)
•⁠  ⁠Git (for cloning the repository)

### Installation

1.⁠ ⁠Clone the repository:
    ⁠ sh
    git clone https://github.com/your-username/logo-detection.git
     ⁠

2.⁠ ⁠Create a virtual environment:
    ⁠ sh
    cd logo-detection
    python -m venv env
     ⁠

3.⁠ ⁠Activate the virtual environment:

    On Windows:
    ⁠ sh
    env\Scripts\activate
     ⁠

    On macOS/Linux:
    ⁠ sh
    source env/bin/activate
     ⁠

4.⁠ ⁠Install the required dependencies:
    ⁠ sh
    pip install -r requirements.txt
     ⁠

5.⁠ ⁠Download the pre-trained model:
    - Visit the [Ultralytics YOLOv8 Releases page](https://github.com/ultralytics/yolov8/releases) and download the pre-trained model file (e.g., ⁠ yolov8n.pt ⁠).
    - Place the downloaded model file in the ⁠ models ⁠ directory within the project.

### Usage

1.⁠ ⁠Run the logo detection script:
    ⁠ sh
    python logo_detection.py
     ⁠

2.⁠ ⁠The script will prompt you to enter the following information:
    - Path to the trained model (e.g., 'models/yolov8n.pt')
    - Path to the video file (e.g., 'input_videos/video.mp4')
    - Directory to save the output files (e.g., 'output')
    - Path to save the detections JSON file (e.g., 'output/detections.json')

3.⁠ ⁠Explore the output:
    - The script will generate an annotated video file in the specified output directory.
    - The detections will be saved in a JSON file, also in the output directory.

## Approach

The development of this project followed an industry-driven approach, which is detailed in the ⁠ APPROACH.md ⁠ file. This document outlines the methodology, challenges, solutions, and potential advancements of the project.

## Contributing

We welcome contributions to the Logo Detection project! If you'd like to contribute, please follow these steps:

1.⁠ ⁠Fork the repository.
2.⁠ ⁠Create a new branch for your feature or bug fix.
3.⁠ ⁠Make your changes and ensure the code passes all tests.
4.⁠ ⁠Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

The Logo Detection project is built using the Ultralytics YOLOv8 library, which provides state-of-the-art object detection capabilities. The project also utilizes the OpenCV library for video processing and annotation.