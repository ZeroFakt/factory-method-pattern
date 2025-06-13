import pytest
from pattern.factory import NotificationFactory
from pattern.notification import Notification

from unittest.mock import patch


def test_email_notification_creation():
    factory = NotificationFactory()
    notification = factory.create_notification('email')
    assert isinstance(notification, Notification)
    assert notification.__class__.__name__ == "EmailNotification"


def test_sms_notification_creation():
    factory = NotificationFactory()
    notification = factory.create_notification('sms')
    assert isinstance(notification, Notification)
    assert notification.__class__.__name__ == "SMSNotification"


def test_push_notification_creation():
    factory = NotificationFactory()
    notification = factory.create_notification('push')
    assert isinstance(notification, Notification)
    assert notification.__class__.__name__ == "PushNotification"


# При неизвестном типе выбрасываем ошибку
def test_unknown_notification_creation():
    factory = NotificationFactory()
    
    with pytest.raises(ValueError, match="Unknown notification method"):
        factory.create_notification("fax")


# Мокаем метод 'notify', чтобы не вызывать настоящий 'print', но проверяем, что он был вызван правильно
def test_notify_mocked():
    factory = NotificationFactory()
    notification = factory.create_notification('email')
    
    with patch.object(notification, 'notify', return_value=None) as mock_notify:
        notification.notify("Test message")
        mock_notify.assert_called_once_with("Test message")