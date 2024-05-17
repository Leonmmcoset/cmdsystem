# encoding: utf-8
# module pygame.event
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\event.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module for interacting with events and queues """
# no imports

# functions

def clear(eventtype=None): # real signature unknown; restored from __doc__
    """
    clear(eventtype=None) -> None
    clear(eventtype=None, pump=True) -> None
    remove all events from the queue
    """
    pass

def custom_type(): # real signature unknown; restored from __doc__
    """
    custom_type() -> int
    make custom user event type
    """
    return 0

def event_name(type): # real signature unknown; restored from __doc__
    """
    event_name(type) -> string
    get the string name from an event id
    """
    return ""

def get(eventtype=None): # real signature unknown; restored from __doc__
    """
    get(eventtype=None) -> Eventlist
    get(eventtype=None, pump=True) -> Eventlist
    get(eventtype=None, pump=True, exclude=None) -> Eventlist
    get events from the queue
    """
    pass

def get_blocked(type): # real signature unknown; restored from __doc__
    """
    get_blocked(type) -> bool
    get_blocked(typelist) -> bool
    test if a type of event is blocked from the queue
    """
    return False

def get_grab(): # real signature unknown; restored from __doc__
    """
    get_grab() -> bool
    test if the program is sharing input devices
    """
    return False

def get_keyboard_grab(): # real signature unknown; restored from __doc__
    """
    get_keyboard_grab() -> bool
    get the current keyboard grab state
    """
    return False

def peek(eventtype=None): # real signature unknown; restored from __doc__
    """
    peek(eventtype=None) -> bool
    peek(eventtype=None, pump=True) -> bool
    test if event types are waiting on the queue
    """
    return False

def poll(): # real signature unknown; restored from __doc__
    """
    poll() -> Event instance
    get a single event from the queue
    """
    return Event

def post(Event): # real signature unknown; restored from __doc__
    """
    post(Event) -> bool
    place a new event on the queue
    """
    return False

def pump(): # real signature unknown; restored from __doc__
    """
    pump() -> None
    internally process pygame event handlers
    """
    pass

def set_allowed(type): # real signature unknown; restored from __doc__
    """
    set_allowed(type) -> None
    set_allowed(typelist) -> None
    set_allowed(None) -> None
    control which events are allowed on the queue
    """
    pass

def set_blocked(type): # real signature unknown; restored from __doc__
    """
    set_blocked(type) -> None
    set_blocked(typelist) -> None
    set_blocked(None) -> None
    control which events are allowed on the queue
    """
    pass

def set_grab(bool): # real signature unknown; restored from __doc__
    """
    set_grab(bool) -> None
    control the sharing of input devices with other applications
    """
    pass

def set_keyboard_grab(bool): # real signature unknown; restored from __doc__
    """
    set_keyboard_grab(bool) -> None
    grab enables capture of system keyboard shortcuts like Alt+Tab or the Meta/Super key.
    """
    pass

def wait(): # real signature unknown; restored from __doc__
    """
    wait() -> Event instance
    wait(timeout) -> Event instance
    wait for a single event from the queue
    """
    return Event

def _internal_mod_init(*args, **kwargs): # real signature unknown
    """ auto initialize for event module """
    pass

def _internal_mod_quit(*args, **kwargs): # real signature unknown
    """ auto quit for event module """
    pass

# classes

class EventType(object):
    """
    Event(type, dict) -> Event
    Event(type, **attributes) -> Event
    pygame object for representing events
    """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    dict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FFFCCE2B550>, '__repr__': <slot wrapper '__repr__' of 'pygame.event.Event' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'pygame.event.Event' objects>, '__setattr__': <slot wrapper '__setattr__' of 'pygame.event.Event' objects>, '__delattr__': <slot wrapper '__delattr__' of 'pygame.event.Event' objects>, '__lt__': <slot wrapper '__lt__' of 'pygame.event.Event' objects>, '__le__': <slot wrapper '__le__' of 'pygame.event.Event' objects>, '__eq__': <slot wrapper '__eq__' of 'pygame.event.Event' objects>, '__ne__': <slot wrapper '__ne__' of 'pygame.event.Event' objects>, '__gt__': <slot wrapper '__gt__' of 'pygame.event.Event' objects>, '__ge__': <slot wrapper '__ge__' of 'pygame.event.Event' objects>, '__init__': <slot wrapper '__init__' of 'pygame.event.Event' objects>, '__bool__': <slot wrapper '__bool__' of 'pygame.event.Event' objects>, '__dict__': <member '__dict__' of 'pygame.event.Event' objects>, 'type': <member 'type' of 'pygame.event.Event' objects>, 'dict': <member 'dict' of 'pygame.event.Event' objects>, '__doc__': 'Event(type, dict) -> Event\\nEvent(type, **attributes) -> Event\\npygame object for representing events', '__hash__': None})"
    __hash__ = None


Event = EventType


# variables with complex values

_joy_instance_map = {}

_PYGAME_C_API = None # (!) real value is '<capsule object "pygame.event._PYGAME_C_API" at 0x000001DD25B11DA0>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DD25B1B390>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.event', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DD25B1B390>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\event.cp311-win_amd64.pyd')"

