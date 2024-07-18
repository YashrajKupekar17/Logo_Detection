# from ultralytics import YOLO

# model = YOLO('models/best-9.pt')   

# result = model.predict('/Users/yashrajkupekar/code/Machine Learning/project/input_video/Y2meta.app-Make Amazing Cups Using Soda Cans and earn money-(720p) (online-video-cutter.com).mp4',save=True)
# print(result[0])
# print("=====================================")
# for box in result[0].boxes:
#     print(box)
import os
import json
import cv2
from ultralytics import YOLO
from datetime import datetime
from collections import defaultdict

class LogoDetector:
    def __init__(self, model_path, video_path, output_dir, output_json_path):
        self.model = YOLO(model_path)
        self.video_capture = cv2.VideoCapture(video_path)
        self.output_dir = output_dir
        self.output_json_path = output_json_path

        self.frame_rate = self.video_capture.get(cv2.CAP_PROP_FPS)
        self.frame_width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.center_x = self.frame_width // 2
        self.center_y = self.frame_height // 2

        self.logo_detections = defaultdict(list)

    def detect_logos(self):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_video_path = os.path.join(self.output_dir, f"output_video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4")
        video_writer = cv2.VideoWriter(output_video_path, fourcc, self.frame_rate, (self.frame_width, self.frame_height))

        current_frame_number = 0
        while self.video_capture.isOpened():
            ret, frame = self.video_capture.read()
            if not ret:
                break

            results = self.model.predict(frame, imgsz=640)

            for result in results:
                if hasattr(result, 'boxes') and result.boxes is not None:
                    for box in result.boxes:
                        class_label = result.names[int(box.cls[0])]
                        confidence_score = box.conf[0]
                        bounding_box = box.xyxy[0].cpu().numpy()

                        box_width = bounding_box[2] - bounding_box[0]
                        box_height = bounding_box[3] - bounding_box[1]
                        box_size = int(box_width * box_height)
                        box_center_x = (bounding_box[0] + bounding_box[2]) // 2
                        box_center_y = (bounding_box[1] + bounding_box[3]) // 2
                        distance_from_center = int(((box_center_x - self.center_x) ** 2 + (box_center_y - self.center_y) ** 2) ** 0.5)

                        timestamp = current_frame_number / self.frame_rate

                        self.logo_detections[class_label].append({
                            "timestamp": timestamp,
                            "size": box_size,
                            "distance_from_center": distance_from_center,
                            "confidence_score": confidence_score
                        })

                        self.annotate_frame(frame, class_label, bounding_box, box_size, distance_from_center)

            video_writer.write(frame)
            current_frame_number += 1

        self.video_capture.release()
        video_writer.release()

    def annotate_frame(self, frame, class_label, bounding_box, box_size, distance_from_center):
        if class_label == "Pepsi-Logo":
            color = (255, 0, 0)
        elif class_label == "CocoCola-Logo":
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)

        cv2.rectangle(frame, (int(bounding_box[0]), int(bounding_box[1])), (int(bounding_box[2]), int(bounding_box[3])), color, 2)
        cv2.putText(frame, f"{class_label}", (int(bounding_box[0]), int(bounding_box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        cv2.putText(frame, f"Size: {box_size}", (int(bounding_box[0]), int(bounding_box[3]) + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        cv2.putText(frame, f"Dist: {distance_from_center:.2f}", (int(bounding_box[0]), int(bounding_box[3]) + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    def save_output(self):
        output_data = {}
        for class_label, detections in self.logo_detections.items():
            output_data[class_label] = []
            for detection in detections:
                output_data[class_label].append({
                    "timestamp": detection["timestamp"],
                    "size": int(detection["size"]),
                    "distance_from_center": int(detection["distance_from_center"]),
                    "confidence_score": float(detection["confidence_score"])
                })

        os.makedirs(os.path.dirname(self.output_json_path), exist_ok=True)
        with open(self.output_json_path, "w") as json_file:
            json.dump(output_data, json_file, indent=4)

        print(f"Detections have been saved to {self.output_json_path}")
        print(f"Annotated video has been saved to {os.path.join(self.output_dir, os.path.basename(self.output_json_path.replace('.json', '.mp4')))}")
if __name__ == "__main__":
    model_path = input("Enter the path to the trained model (e.g., 'path/to/your/model.pt'): ")
    video_path = input("Enter the path to the video file (e.g., 'path/to/your/video.mp4'): ")
    output_dir = input("Enter the directory to save the output files (e.g., 'path/to/your/directory'): ")
    output_json_path = input("Enter the path to save the detections JSON file (e.g., 'path/to/your/output.json'): ")

    logo_detector = LogoDetector(model_path, video_path, output_dir, output_json_path)
    logo_detector.detect_logos()
    logo_detector.save_output()
    