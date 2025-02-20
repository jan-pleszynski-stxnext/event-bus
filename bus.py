from collections import defaultdict
from enum import StrEnum, auto


class EventTypes(StrEnum):
    EVENT_A = auto()
    EVENT_B = auto()



class EventBus:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, event_type: EventTypes, subscriber):
        self.subscribers[event_type].append(subscriber)

    def publish(self, event):
        for subscriber in self.subscribers[event.type]:
            subscriber(event)
