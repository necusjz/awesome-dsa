from abc import ABC, abstractmethod


class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.send_notification(event, self.name)


class YoutubeSubscriber(ABC):
    @abstractmethod
    def send_notification(self, event):
        pass


class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def send_notification(self, event, channel=None):
        return f"User {self.name} received notification from {channel}: {event}"
