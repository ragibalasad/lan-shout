from plyer import notification

def show_notification(sender_ip, message):
    """Shows a system notification when a message is received."""
    print(f"Triggering notification: [{sender_ip}] {message}")
    try:
        notification.notify(
            title=f"Message from {sender_ip}",
            message=message,
            app_name="LAN Msg Tool",
            timeout=10
        )
    except Exception as e:
        print(f"Notification error: {e}")
