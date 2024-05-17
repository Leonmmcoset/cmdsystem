# encoding: utf-8
# module pygame.time
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\time.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module for monitoring time """
# no imports

# functions

def delay(milliseconds): # real signature unknown; restored from __doc__
    """
    delay(milliseconds) -> time
    pause the program for an amount of time
    """
    pass

def get_ticks(): # real signature unknown; restored from __doc__
    """
    get_ticks() -> milliseconds
    get the time in milliseconds
    """
    pass

def set_timer(event, millis): # real signature unknown; restored from __doc__
    """
    set_timer(event, millis) -> None
    set_timer(event, millis, loops=0) -> None
    repeatedly create an event on the event queue
    """
    pass

def wait(milliseconds): # real signature unknown; restored from __doc__
    """
    wait(milliseconds) -> time
    pause the program for an amount of time
    """
    pass

def _internal_mod_init(*args, **kwargs): # real signature unknown
    """ auto initialize function for time """
    pass

def _internal_mod_quit(*args, **kwargs): # real signature unknown
    """ auto quit function for time """
    pass

# classes

class Clock(object):
    """
    Clock() -> Clock
    create an object to help track time
    """
    def get_fps(self): # real signature unknown; restored from __doc__
        """
        get_fps() -> float
        compute the clock framerate
        """
        return 0.0

    def get_rawtime(self): # real signature unknown; restored from __doc__
        """
        get_rawtime() -> milliseconds
        actual time used in the previous tick
        """
        pass

    def get_time(self): # real signature unknown; restored from __doc__
        """
        get_time() -> milliseconds
        time used in the previous tick
        """
        pass

    def tick(self, framerate=0): # real signature unknown; restored from __doc__
        """
        tick(framerate=0) -> milliseconds
        update the clock
        """
        pass

    def tick_busy_loop(self, framerate=0): # real signature unknown; restored from __doc__
        """
        tick_busy_loop(framerate=0) -> milliseconds
        update the clock
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000206FB793D10>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.time', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000206FB793D10>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\time.cp311-win_amd64.pyd')"

