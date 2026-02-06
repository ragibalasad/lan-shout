import sys
import argparse
import socket
from listener import start_listening
from sender import send_message, broadcast_message

def is_valid_ip(ip):
    """Simple check for valid IPv4 address."""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def get_local_ip():
# ... (omitted for brevity in replacement chunk but I'll keep it)
    """Returns the local IP address of the machine."""
    try:
        # Create a dummy socket to find the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def main():
    parser = argparse.ArgumentParser(description="LAN Message Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Listen command
    listen_parser = subparsers.add_parser("listen", help="Start the listener to receive messages")

    # Send command logic (default if not 'listen')
    # If the user just runs `msg <ip> <msg>`, we handle it.
    
    if len(sys.argv) > 1 and sys.argv[1] == "listen":
        local_ip = get_local_ip()
        print(f"Starting LAN Message Listener on {local_ip}...")
        print(f"Your IP address is: {local_ip}")
        start_listening()
    elif len(sys.argv) >= 2:
        # Check if sys.argv[1] is an IP
        if is_valid_ip(sys.argv[1]):
            if len(sys.argv) >= 3:
                ip = sys.argv[1]
                message = " ".join(sys.argv[2:])
                send_message(ip, message)
            else:
                print("Error: Message required when specifying an IP.")
        else:
            # Not an IP, treat everything as a broadcast message
            message = " ".join(sys.argv[1:])
            broadcast_message(message)
    else:
        print("Usage:")
        print("  To listen:        msg listen")
        print("  Send to IP:       msg <ip> <message>")
        print("  Broadcast all:    msg <message>")

if __name__ == "__main__":
    main()
