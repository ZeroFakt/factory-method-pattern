from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

class EmailNotification(Notification):
    def notify(self, message: str):
        print(f"Email: {message}")

class SMSNotification(Notification):
    def notify(self, message: str):
        print(f"SMS: {message}")

class PushNotification(Notification):
    def notify(self, message: str):
        print(f"Push: {message}")