from events import EventA, EventB

# Event handler can push information to websockets or just do any DECOUPLED processing.

def event_handler_a(event_a: EventA):
    print(f"Handling Event A: {event_a.field_1} {event_a.field_2}")


def event_handler_b(event_b: EventB):
    print(f"Handling Event B: {event_b.field_1} {event_b.field_2} {event_b.field_3}")
