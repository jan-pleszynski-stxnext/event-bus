from bus import EventBus, EventTypes
from event_handlers import event_handler_a, event_handler_b
from use_cases import use_case_1


def main():
    event_bus = EventBus()
    event_bus.subscribe(EventTypes.EVENT_A, event_handler_a)
    event_bus.subscribe(EventTypes.EVENT_B, event_handler_b)

    # This will be normally invoked from the api
    use_case_1(event_bus)


if __name__ == "__main__":
    main()