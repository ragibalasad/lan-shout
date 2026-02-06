# LAN Message Tool

A simple tool to send and receive messages across a Local Area Network (LAN).

## Installation

1.  Clone this repository.
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Install the tool globally (optional but recommended for the `msg` command):
    ```bash
    pip install -e .
    ```

## Usage

### 1. Start the Listener
The listener must be running to receive messages. It will show a desktop notification for every incoming message.

```bash
msg listen
```

### 2. Send a Message
To send a message to another device on the same network that is running the listener:

```bash
msg <ip-address> <your message here>
```

Example:
```bash
msg 192.168.1.5 Hello there!
```

## Requirements
- Python 3.x
- `plyer` library for notifications.
- Both devices must be on the same LAN and have the listener running.
- Firewall should allow incoming connections on port 9999.
