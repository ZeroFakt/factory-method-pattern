from .notification import Notification, EmailNotification, SMSNotification, PushNotification

class NotificationFactory:
    def create_notification(self, method: str) -> Notification:
        if method == "email":
            return EmailNotification()
        elif method == "sms":
            return SMSNotification()
        elif method == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification method: {method}")