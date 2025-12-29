from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        return f"Sending email: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"Sending SMS: {message}"

class PushNotification(Notification):
    def send(self, message):
        return f"Sending push notification: {message}"

class SlackNotification(Notification):
    def send(self, message):
        return f"Sending Slack message: {message}"

class NotificationFactory:
    _notifications = {
            'email': EmailNotification,
            'sms': SMSNotification,
            'push': PushNotification,
            'slack': SlackNotification
    }

    @classmethod
    def create_notification(cls, notification_type):
        notification_class = cls._notifications.get(notification_type.lower())
        if notification_class:
            return notification_class()
        raise ValueError(f"Unknown notification type: {notification_type}")

    @classmethod
    def register_notification(cls, name, notification_class):
        cls._notifications[name.lower()] = notification_class

# Usage
notifier = NotificationFactory.create_notification('email')
print(notifier.send("Hello, World!"))

notifier = NotificationFactory.create_notification('sms')
print(notifier.send("Hello, World!"))
