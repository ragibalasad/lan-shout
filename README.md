# 📣 LAN-Shout

A powerful, lightweight Python tool to send and receive messages across your Local Area Network (LAN). It supports direct messaging via TCP and network-wide broadcasting via UDP, with instant desktop notifications.

---

## 🚀 Installation & Setup

Follow these steps to get the `msg` command working on your machine.

### 1. Download the Project
Clone this repository or download the source code to your machine:
```bash
git clone <your-repo-url>
cd msg-lan-tool
```

### 2. Make the `msg` Command Available System-wide
To use the tool by simply typing `msg` from any terminal directory, you need to install it using `pip`. 

**Option A: Standard Installation (Best for users)**
```bash
pip install .
```

**Option B: Editable Installation (Best for developers)**
*Changes you make to the code will take effect immediately.*
```bash
pip install -e .
```

> **Note:** Depending on your system, you might need to use `pip3` or ensure your Python scripts folder is in your system's PATH.

---

## 🛠️ Usage Guide

The tool operates in two modes: **Listening** (to receive) and **Sending** (to talk).

### 1. Start Listening (Must be running to receive messages)
Run this command to start the background server. It will listen for both direct and broadcast messages.
```bash
msg listen
```
*   It will display your **Local IP Address**. Share this with others so they can message you directly.
*   Keep this terminal window open.

### 2. Sending a Direct Message
To send a private message to a specific device on your network:
```bash
msg <ip-address> <your message>
```
**Example:**
```bash
msg 192.168.1.15 "Hey, are we still meeting at 5?"
```

### 3. Broadcasting to Everyone
To send a message to **every single device** on the LAN that is running the listener:
```bash
msg <your message>
```
*(If the first word isn't a valid IP address, the tool automatically switches to broadcast mode.)*

**Example:**
```bash
msg "Pizza is here in the breakroom!"
```
*Note: You will also receive a notification for your own broadcast messages.*

---

## 🛡️ Important: Firewall & Connection
For the tool to work across different machines:
1.  **Same Network**: Both devices must be connected to the same Wi-Fi or local network.
2.  **Firewall**: Your OS firewall must allow incoming connections on **Port 9999** (TCP and UDP).
    *   On Linux (ufw): `sudo ufw allow 9999`
    *   On Windows: Add an inbound rule for Port 9999 in Windows Defender Firewall.

---

## 📦 Requirements
- Python 3.x
- `plyer` (automatically installed via `pip install .`)
