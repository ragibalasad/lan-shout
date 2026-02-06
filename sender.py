import socket

DEFAULT_PORT = 9999

def send_message(ip, message):
    """Sends a message to the specified IP address (TCP)."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((ip, DEFAULT_PORT))
            s.sendall(message.encode('utf-8'))
            print(f"Message sent to {ip}")
    except Exception as e:
        print(f"Error sending message to {ip}: {e}")

def broadcast_message(message):
    """Broadcasts a message to everyone on the LAN (UDP)."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            # Send to global broadcast
            s.sendto(message.encode('utf-8'), ('255.255.255.255', DEFAULT_PORT))
            # Also send to localhost to ensure the local listener picks it up
            s.sendto(message.encode('utf-8'), ('127.0.0.1', DEFAULT_PORT))
            print("Broadcast message sent to everyone (including you).")
    except Exception as e:
        print(f"Error broadcasting message: {e}")
