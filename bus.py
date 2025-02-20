from abc import ABC
from collections import defaultdict
from enum import StrEnum, auto
from typing import Callable

from pydantic import BaseModel


class EventTypes(StrEnum):
    EVENT_A = auto()
    EVENT_B = auto()

class BaseEvent(BaseModel, ABC):
    type: EventTypes


class EventBus:
    def __init__(self):
        self.subscribers: dict[EventTypes, list[Callable[[BaseEvent], None]]] = defaultdict(list)

    def subscribe(self, event_type: EventTypes, subscriber: Callable[[BaseEvent], None]) -> None:
        self.subscribers[event_type].append(subscriber)

    def publish(self, event: BaseEvent) -> None:
        for subscriber in self.subscribers[event.type]:
            subscriber(event)
