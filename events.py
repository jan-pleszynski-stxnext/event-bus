from bus import EventTypes, BaseEvent


class EventA(BaseEvent):
    type: EventTypes = EventTypes.EVENT_A
    field_1: str
    field_2: int


class EventB(BaseEvent):
    type: EventTypes = EventTypes.EVENT_B
    field_1: str
    field_2: int
    field_3: bool
