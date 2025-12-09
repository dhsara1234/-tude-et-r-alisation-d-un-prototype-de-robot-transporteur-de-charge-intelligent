# AI-Based Autonomous Load Transport Robot – Final Year Project

## 📌 Project Overview
This project involves the design and development of an **autonomous load-carrying robot** using **artificial intelligence** for navigation and obstacle detection. The robot is capable of following predefined paths, detecting stations, avoiding obstacles in real time, and transporting loads up to **15 kg** in an industrial environment.

---

## 🏗️ Features
- **Autonomous Navigation**: Follows a predefined route using visual cues.
- **Obstacle Detection**: Uses a **USB camera** and **SSD MobileNet V2** model for real-time object detection.
- **Remote Control**: Desktop application (built with **Qt**) for remote command and monitoring via Wi-Fi (TCP/IP).
- **Mechanical Design**: Custom chassis, motor mounts, and wheel assemblies designed in **SolidWorks**.
- **Power Management**: Powered by **Li-ion batteries** with a runtime of 2 hours.

---

## 🔧 Hardware Components
| Component | Specification |
|-----------|---------------|
| **Microcontroller** | Raspberry Pi 3 Model B |
| **Motors** | 2x DC motors (JGB37-520, 12V, 0.29 N.m) |
| **Motor Driver** | L298N Dual H-Bridge |
| **Battery** | BOSH Li-ion 18V, 5.0 Ah |
| **Camera** | Hikvision DS-U18 (USB, 4K) |
| **Wheels** | Rubber-tired drive wheels + 360° swivel caster |

---

## 🧠 AI & Software Stack
| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **TensorFlow/Keras** | Deep learning model for object detection |
| **OpenCV** | Real-time image processing |
| **SSD MobileNet V2** | Pre-trained model for object detection |
| **Qt** | Desktop application for remote control |
| **Socket Programming** | Wi-Fi communication between PC and robot |
| **SolidWorks** | 3D mechanical design |

---

## 📁 Repository Structure
```
├── /mechanical_designs/   # SolidWorks files (chassis, mounts, etc.)
├── /src/
│   ├── navigation/        # Path planning and route training
│   ├── object_detection/  # SSD MobileNet V2 implementation
│   ├── station_detection/ # Color-based station detection (Mask R-CNN)
│   ├── control/           # Motor control and remote commands
│   └── desktop_app/       # Qt-based remote control interface
├── /docs/                 # Project report and documentation
├── /datasets/             # Training images and labeled data
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/autonomous-load-robot.git
cd autonomous-load-robot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Robot Control
```bash
python src/control/main.py
```

### 4. Launch the Desktop App
```bash
python src/desktop_app/robot_controller.py
```

---

## 📸 Demo & Results
- The robot successfully detects obstacles and stations using the camera:
- ![Screenshot_9-12-2025_12266_](https://github.com/user-attachments/assets/215a80de-ce07-4dea-a996-ab6964910b5c)
- Remote control via the Qt desktop app over Wi-Fi:
- ![Screenshot_9-12-2025_122722_](https://github.com/user-attachments/assets/b724ae59-6623-4965-a7e4-988f5368a6d9)

- Modular mechanical design allows for easy assembly and modification:
- ![Screenshot_9-12-2025_12281_](https://github.com/user-attachments/assets/fed21dce-6e3b-4d3d-9284-d21c7aea72dd)


---

## 📄 Report & Documentation
The full project report (in French) is available in the `/docs/` folder. It includes:
- Detailed hardware selection and sizing
- AI methodology and model training
- Mechanical design and assembly steps
- Test results and future improvements

---

## 👥 Team
- **Dhahri Sarra**  
- **Troudi Dalel**  

Supervised by:
- Dr. Albouchi Adnen (University Supervisor)
- Mr. Zied Oueslati (Industrial Supervisor)

---

## 🏫 Institution
- **University of Monastir, Faculty of Sciences Monastir**
- **LEONI Wiring Systems Tunisia (LTN3)**
- Academic Year: 2021/2022

---

## 📜 License
This project is developed for academic purposes. All rights reserved by the authors and the supervising institution.

---
