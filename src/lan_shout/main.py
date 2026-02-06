import sys
import argparse
import socket
from .listener import start_listening
from .sender import send_message, broadcast_message

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
    parser = argparse.ArgumentParser(description="LAN-Shout: CLI tool for instant messaging across a LAN")
    parser.add_argument("-l", "--listen", action="store_true", help="Start the listener to receive messages")
    parser.add_argument("target", nargs="?", help="IP address or first word of the message")
    parser.add_argument("message_parts", nargs="*", help="Remaining parts of the message")

    args = parser.parse_args()

    if args.listen:
        local_ip = get_local_ip()
        print(f"Starting LAN-Shout Listener on {local_ip}...")
        print(f"Your IP address is: {local_ip}")
        start_listening()
        return

    if args.target:
        # Check if first positional arg is an IP
        if is_valid_ip(args.target):
            if args.message_parts:
                ip = args.target
                message = " ".join(args.message_parts)
                send_message(ip, message)
            else:
                print("Error: Message required when specifying an IP.")
        else:
            # Not an IP, treat everything as a broadcast message
            message = args.target + " " + " ".join(args.message_parts) if args.message_parts else args.target
            broadcast_message(message.strip())
    else:
        parser.print_help()
        print("\nExamples:")
        print("  msg --listen             # Start listening")
        print("  msg 192.168.1.5 Hello    # Send to specific IP")
        print("  msg Hello everyone       # Broadcast to all")

if __name__ == "__main__":
    main()
