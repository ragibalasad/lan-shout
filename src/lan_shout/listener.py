import socket
import threading
from .notifier import show_notification

DEFAULT_PORT = 9999

def start_udp_listener():
    """Starts a UDP listener to receive broadcast messages."""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        udp_socket.bind(('', DEFAULT_PORT))
        print(f"UDP Listener started on port {DEFAULT_PORT}...")
        while True:
            data, addr = udp_socket.recvfrom(1024)
            if data:
                message = data.decode('utf-8')
                sender_ip = addr[0]
                print(f"Received BROADCAST from {sender_ip}: {message}")
                show_notification(f"{sender_ip} (Broadcast)", message)
    except Exception as e:
        print(f"Error in UDP listener: {e}")
    finally:
        udp_socket.close()

def start_listening():
    """Starts the listener server (TCP and UDP) to receive messages."""
    # Start UDP listener in background
    udp_thread = threading.Thread(target=start_udp_listener, daemon=True)
    udp_thread.start()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server_socket.bind(('0.0.0.0', DEFAULT_PORT))
        server_socket.listen(5)
        print(f"TCP Listener started on port {DEFAULT_PORT}...")
        
        while True:
            conn, addr = server_socket.accept()
            with conn:
                data = conn.recv(1024)
                if data:
                    message = data.decode('utf-8')
                    sender_ip = addr[0]
                    print(f"Received message from {sender_ip}: {message}")
                    show_notification(sender_ip, message)
    except Exception as e:
        print(f"Error in TCP listener: {e}")
    finally:
        server_socket.close()

def run_listener_background():
    """Runs the listener in a background thread."""
    thread = threading.Thread(target=start_listening, daemon=True)
    thread.start()
    return thread
