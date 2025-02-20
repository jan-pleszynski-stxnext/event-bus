from pydantic import BaseModel

from bus import EventTypes


class EventA(BaseModel):
    type: EventTypes = EventTypes.EVENT_A
    field_1: str
    field_2: int


class EventB(BaseModel):
    type: EventTypes = EventTypes.EVENT_B
    field_1: str
    field_2: int
    field_3: bool
