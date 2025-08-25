# **spidroid**

AI-powered crop health monitoring system combining an autonomous quadruped robot, a Flutter mobile app, and a Next.js backend integrated with Firebase.

---

## **Spidroid Bot**

Autonomous quadruped robot built on **Arduino Nano**, powered via **DC-DC buck converters**, and programmed using **Inverse Kinematics** for precise locomotion. Controlled via Bluetooth and constructed with 3D-printed parts.

### **Hardware Overview**

* 12 SG90 servo motors (3 per leg)
* Arduino Nano with expansion shield
* HC-06 Bluetooth module
* OLED display for visual feedback
* DC-DC Buck Converters:

  * LM2596 → 7V for Arduino
  * XL4015 → 5V for servos
* Dual 18650 Li-ion batteries
* 3D-printed modular frame

### **Power & Control Flow**

```
[ 18650 Batteries ] → [ Buck Converters ]
    ├── 7V → Arduino Nano
    └── 5V → Servo Motors
[ Arduino Nano ] → PWM to 12 servos
Bluetooth input → Motion control
Inverse Kinematics → Leg movement
```

### **Progress**

[View build progress on Google Drive](https://drive.google.com/drive/folders/1AXG8rX9oEhByYURuzwPRJS5ren4q2I4T?usp=sharing)

Some progress images: 

<img width="507" height="503" src="https://github.com/user-attachments/assets/88ea1bda-be8d-489c-be29-d65982c8820a" /> <img width="811" height="708" src="https://github.com/user-attachments/assets/0b280840-181f-46e8-9387-9425b4350a62" />

---

## **Next.js Backend**

Backend service for handling plant health data, integrated with Firebase for storage and retrieval.

### **Features**

* REST API to receive data from Spidroid bot
* Uploads images to Firebase Storage
* Stores metadata in Firestore
* Serves data to Flutter app for farmer access

### **Data Flow**

```
Spidroid Bot → Next.js API → Firebase (Firestore + Storage)
                                  ↓
                        Flutter App (UI)
```

### **Tech Stack**

* **Framework:** Next.js
* **Database & Storage:** Firebase Firestore + Storage
* **Security:** API key-based authentication
* **Deployment:** Firebase Hosting

---

## **Project Structure**

```
spidroid/
├── mobile_app/                # Flutter app (in progress)
│   └── lib/
│       └── homescreen.dart
├── nextjsBackend/             # Next.js backend
│   ├── app/
│   ├── lib/
│   └── ...
├── plant_disease_detection-main/  # AI Model (TensorFlow)
│   └── trained_dataset/
└── spidroid_ardrino/          # Arduino code for Spidroid bot
```

---

## **Progress Checklist**

* [x] **Spidroid Bot** – Hardware assembled & tested
* [x] **Next.js Backend** – API endpoints functional
* [x] **AI Model** – Trained for Healthy, Powdery Mildew, Rust detection
* [ ] **Raspberry Pi Integration** – To run TensorFlow Lite model on edge
* [ ] **Flutter App** – UI & data visualization in progress
* [ ] **Full System Integration** – Bot → Backend → App pipeline

---

### **Quick Start**

```sh
git clone https://github.com/JacobMaximus/spidroid
cd nextjsBackend
npm install
npm run dev
```      
