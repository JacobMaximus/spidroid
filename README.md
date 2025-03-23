# spidroid

# Next.js Backend for Spider-Bot Crop Disease Detection

## 🚀 Project Overview
This is a **Next.js backend** for an **AI-powered spider-bot** that detects crop diseases. The backend integrates **Firebase** for data storage and serves data to a **Flutter mobile app** used by farmers.

---
## 📂 Project Structure
```
├── app/
│   └── api/
│       ├── upload-data/
│       │   └── route.ts         # Handles image & data upload
│       └── diseased-plants/
│           ├── route.ts         # Lists all plants
│           └── [id]/
│               └── route.ts     # Single plant details
├── lib/
│   ├── firebase-admin.ts       # Admin SDK setup
│   ├── firebase.ts             # Client SDK setup
│   └── middleware.ts           # API authentication
└── .env.example                # Environment configuration
```

---
## ⚡ Key Features
### **1️⃣ API Endpoints**
- `POST /api/upload-data` → **Receives plant data from the spider-bot**
  - Uploads images to **Firebase Storage**
  - Stores metadata in **Firestore**
- `GET /api/diseased-plants` → **Retrieves all plant records**
- `GET /api/diseased-plants/:id` → **Fetches details of a specific plant**

### **2️⃣ Data Flow**
```
Spider-Bot → API Endpoints → Firebase Storage (images)
                         ↘ Firestore (metadata)
                                ↓
Flutter App ← API Endpoints ← Firestore/Storage
```
### **3️⃣ Firebase Integration**
#### **Firestore Schema:**
```ts
interface Plant {
  id: string;
  imageUrl: string;
  disease: string;
  latitude: number;
  longitude: number;
  timestamp: string;
}
```
#### **Storage Structure:**
- Images stored in: `plants/{timestamp}_{filename}`
- Public URLs generated for **Flutter app access**

---
## 🔒 Security Implementation
### **API Authentication:**
- Custom middleware checks for `x-api-key` in headers
- API key validation through environment variables
- **All routes are protected by default**

### **Firebase Security:**
- **Admin SDK** for backend operations
- Separate **client SDK** configuration
- Sensitive credentials stored in **environment variables**




---
## 📌 Getting Started
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/JacobMaximus/spidroid
cd spider-bot-backend
```
### **2️⃣ Install Dependencies**
```sh
npm install
```
### **3️⃣ Set Up Firebase**
- Create a **Firebase project**
- Enable **Firestore** & **Storage**
- Copy `.env.example` to `.env` and fill in Firebase credentials

### **4️⃣ Run the Development Server**
```sh
npm run dev
```


