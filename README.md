# QR Code App 📱

A lightweight, efficient Python application that generates custom QR codes directly in your terminal. This project uses the **Segno** library to produce high-quality, ISO-standard compliant QR codes and features a **FastAPI** backend that automatically prompts a download for the generated files when running locally.

---

## 🚀 Key Features
- **Dynamic Generation:** Accepts `GET` requests via FastAPI to generate QR codes from any provided string or URL.
- **Auto-Download:** Designed to automatically trigger a browser download for the QR code image when accessed.
- **High-Quality Output:** Powered by **Segno** for reliable and professional QR code signaling.
- **Automated Setup:** Includes a dedicated shell script to configure your environment instantly.

---

## 🛠️ Technical Stack
[cite_start]This project reflects my focus on automation and clean backend logic:
- [cite_start]**Primary Language:** Python 
- **Web Framework:** FastAPI
- **QR Library:** Segno
- [cite_start]**Scripting:** Bash (for automated installation) 
- [cite_start]**Skills Applied:** Problem Analysis, Object-Oriented Programming, and Build Scripting 

---

## ⚙️ Installation & Setup

To ensure all required libraries (Segno, FastAPI, and others) are correctly installed, use the provided installation script.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SciFan-San/qr-code-app.git](https://github.com/SciFan-San/qr-code-app.git)
   cd qr-code-app
   Run the installation script: This script automates the pip installation process for you.

Bash
chmod +x install.sh
./install.sh
🚀 How to Use
1. Launch the Application
Run the program using standard Python directly in your terminal:

Bash
python main.py

2. **Use the Interactive Documentation**
FastAPI provides a built-in UI that makes submitting GET requests significantly easier. Once the program is running:

Open your browser and go to: http://127.0.0.1:8000/docs or http://localhost:8000/docs

Click on the GET endpoint to expand it.

Select "Try it out".

Enter your desired URL or text in the data field and click Execute.

Optionally you cant enter WiFi information as a JSON in the following format:
WIFI:T:<EncryptionType>;S:<SSID>;P:<Password>;H:<Hidden>;

Examples of a WiFi JSON:
1. WPA2-protected network:
WIFI:T:WPA;S:HomeNetwork;P:SuperSecret123;;
2. Open network (no password):
WIFI:T:nopass;S:GuestNetwork;;
3. Hidden SSID:
WIFI:T:WPA;S:HiddenNetName;P:pass123;H:true;;

The browser will automatically prompt you to download the resulting QR code. The Qr will also have the exact some name as the input given.

## 🧠 Behind the Code
I built this just to practice real-world example of a useful tool. 

Automation: I implemented install.sh to demonstrate some of my proficiency in Build Scripting and Linux environments.

User-Friendliness: I chose FastAPI's /docs page, to make it easier for even non-technical users to easily interact with the API.

## 📫 Contact

Michael Johnston 

Email: mdjohnstonb4j@gmail.com 

GitHub: SciFan-San 

Education: Software Engineering (NQF6) at WeThinkCode_
