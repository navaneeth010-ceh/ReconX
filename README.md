# 🔎 ReconX – Automated Web Recon Tool

ReconX is a Python-based automated reconnaissance tool designed to map a target's attack surface by performing subdomain enumeration, live host detection, and port scanning.

---

## ⚡ Features

* 🌐 Passive Subdomain Enumeration (API-based)
* 🔍 Active Subdomain Bruteforce (wordlist-based)
* 🟢 Live Host Detection (HTTP/HTTPS probing)
* 🚪 Multi-threaded Port Scanning
* 📊 Progress Tracking (custom progress bar)
* 📄 Structured JSON Output

---

## 🧠 Workflow

```
Target Domain
      ↓
Subdomain Enumeration (Passive + Active)
      ↓
Live Host Detection
      ↓
Port Scanning
      ↓
JSON Report
```

---

## 🛠️ Tech Stack

* Python 3
* requests
* dnspython
* socket
* concurrent.futures

---

## 📦 Installation

```bash
git clone https://github.com/navaneeth010-ceh/ReconX.git
cd reconx
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py example.com
```

---

## 📄 Output Example

```json
[
  {
    "domain": "api.example.com",
    "status": 200,
    "server": "nginx",
    "ports": [80, 443]
  }
]
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.

Do NOT use this tool on systems you do not own or have explicit permission to test.

---

## 🚀 Future Improvements

* 🔍 Technology Fingerprinting
* 📸 Screenshot Capture (Web UI)
* 🧠 Vulnerability Hint Engine
* ⚡ Async Scanning Engine
* 📊 Web Dashboard

---

## 👨‍💻 Author

Navaneeth Krishna

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
