from bus import EventBus
from events import EventA, EventB

def use_case_1(event_bus: EventBus):
    print("Running use case 1")

    # Notify other parts of the system about that important thing
    event_bus.publish(EventA(field_1="Hello", field_2=42))
    event_bus.publish(EventB(field_1="World", field_2=24, field_3=True))