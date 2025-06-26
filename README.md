# 🛡🔐 ExamGuardian: Cloud-Based Monitoring & Reporting Tool

**ExamGuardian** is a cloud-integrated monitoring tool built in Python to support remote exam invigilation and desktop activity tracking. It captures **keystrokes**, **screenshots**, **audio**, and **system/network details**, and sends reports via email using **Mailtrap SMTP (Cloud)**.

---

## 🚀 Features

- ⌨️ Records Keystrokes
- 📸 Captures Screenshots
- 🎤 Records Surrounding Audio
- 💻 Collects System & Network Info
- 🔐 Fetches Wi-Fi Passwords & Installed Programs
- ☁️ Sends Encrypted Reports with Attachments via **Mailtrap Cloud SMTP**
- 📅 Monitors every 60 seconds automatically

---

## 💻 Tech Stack

| Component        | Tech Used                            |
|------------------|--------------------------------------|
| Language         | Python 3                             |
| Screenshot       | `pyautogui`                          |
| Audio Recording  | `sounddevice`, `scipy`               |
| Keylogger        | `pynput`                             |
| System Info      | `platform`, `psutil`, `socket`       |
| Email Alerts     | **Mailtrap SMTP (Cloud)**            |

---

## ☁️ Cloud Integration

This project uses **Mailtrap Cloud SMTP** to securely send reports and files (audio, screenshot, keystroke logs) as email attachments. No data is stored locally or exposed in the running terminal (VS Code), ensuring privacy and security.

---

## 📦 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/GodiSaiSantoshReddy/Exam-Guardian-cloud-monitoring
   cd Exam-Guardian-cloud-monitoring
