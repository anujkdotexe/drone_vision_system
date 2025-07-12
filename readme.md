
# 🚁 Drone Vision System

A modular real-time object detection system using YOLOv8, built for drones or high-speed cameras — with MongoDB logging and telemetry support.

## 🎯 Features

- 📷 Real-time object detection via YOLOv8
- 🧠 Detection confidence + bounding box area %
- ⏱ Object visibility duration tracking
- 🗺 Mock GPS + battery telemetry logging
- ☁️ MongoDB database integration
- 🧱 Modular structure (camera / model / logger / config)

## 🛠 Project Structure

```

drone\_vision\_system/
├── camera/              # Webcam / high-speed camera streaming
├── ml\_model/            # YOLO inference, model, tracker
├── logger/              # MongoDB logger
├── utils/               # Helper tools, telemetry
├── config/              # Configs (camera ID, model, Mongo URI)
├── data/                # Raw and processed image/video frames
├── main.py              # Starts the full pipeline
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md

````

## 🚀 Run the System

```bash
# Install dependencies
pip install -r requirements.txt

# Run the main detection system
python main.py
````

> Press `q` to exit the live feed.

---

## ⚙️ Config

Edit `config/settings.yaml`:

```yaml
camera_id: 0
model_path: yolov8n.pt
mongo_uri: mongodb://localhost:27017
```

---

## 📌 Roadmap

* [x] YOLOv8 webcam detection
* [x] MongoDB logging
* [x] Mock drone GPS/battery
* [x] Modular file structure
* [ ] Real drone telemetry
* [ ] Confidence threshold filtering
* [ ] Training pipeline for custom dataset
* [ ] Web dashboard to review logs

---

## 👨‍💻 Made by [Anuj Kondawar](https://github.com/anujkdotexe)