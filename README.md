# 🦈 WhiteShark

**WhiteShark** is a simple OSINT-style command line tool designed to scan text files and identify **email addresses** and **phone numbers** using pattern matching.  
It is built for **educational purposes, cybersecurity learning, and security auditing**.

Created by **Ankon Polley**

---

## ⚡ Features

- 📧 Extract email addresses from text files
- 📱 Extract phone numbers from text files
- 🎨 Colorful terminal banner
- 🖥 Simple bash launcher script
- 🐍 Python-based modular structure

---

## 📂 Project Structure

```
WhiteShark/
│
├── whiteshark.py
├── whiteshark.sh
├── target.txt
│
└── modules/
    ├── __init__.py
    ├── email_scan.py
    └── phone_scan.py
```

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/anknpolley123/WhiteShark.git
```

# Go into the directory:

```bash
cd WhiteShark
```

# Make the script executable:

```bash
chmod +x whiteshark.sh

---

## ▶ Usage

Prepare a text file containing sample data.

# Example 
nano target.txt

# Enter Victim's details

User list for testing


Name: Ankon Polley 
Email: ankonpolley@proton.me
Phone: XXXXXXXXXX

Support contact: support@example.com
Emergency phone: +1 2XXXXXXXXX


## Run the tool:

./whiteshark.sh -f target.txt


Output example:

```
Emails Found:
rahul@gmail.com
support@example.com

Phone Numbers Found:
+919876543210
+12025550191
```

---

## 📚 Requirements

- Python 3.x
- Linux / macOS / Kali Linux
- Bash

---

## ⚠ Legal Disclaimer

This tool is created for **educational purposes, cybersecurity research, and authorized security testing only**.

The developer **Ankon Polley** is not responsible for any misuse of this software.  
Users must ensure they have **proper authorization and permission** before scanning, analyzing, or collecting information from any system, dataset, or individual.

Any misuse of this tool for **illegal activities, privacy violations, harassment, or unauthorized data collection** is strictly prohibited.

By using this software, you agree that you are **solely responsible for your actions** and compliance with all applicable laws and regulations.

---

## 👨‍💻 Author

**Ankon Polley**

GitHub:  
https://github.com/anknpolley123

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
