# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TextNode import TextNode

class FrameRateMeter(TextNode):
    """
    /**
     * This is a special TextNode that automatically updates itself with the
     * current frame rate.  It can be placed anywhere in the world where you'd
     * like to see the frame rate.
     *
     * It also has a special mode in which it may be attached directly to a
     * channel or window.  If this is done, it creates a DisplayRegion for itself
     * and renders itself in the upper-right-hand corner.
     */
    """
    def clearWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_window(const FrameRateMeter self)
        
        /**
         * Undoes the effect of a previous call to setup_window().
         */
        """
        pass

    def clear_window(self, const_FrameRateMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_window(const FrameRateMeter self)
        
        /**
         * Undoes the effect of a previous call to setup_window().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClockObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clock_object(FrameRateMeter self)
        
        /**
         * Returns the clock that is used to determine the frame rate.
         */
        """
        pass

    def getDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_region(FrameRateMeter self)
        
        /**
         * Returns the DisplayRegion that the meter has created to render itself into
         * the window to setup_window(), or NULL if setup_window() has not been
         * called.
         */
        """
        pass

    def getTextPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_text_pattern(FrameRateMeter self)
        
        /**
         * Returns the sprintf() pattern that is used to format the text.
         */
        """
        pass

    def getUpdateInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_update_interval(FrameRateMeter self)
        
        /**
         * Returns the number of seconds that will elapse between updates to the frame
         * rate indication.
         */
        """
        pass

    def getWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_window(FrameRateMeter self)
        
        /**
         * Returns the GraphicsOutput that was passed to setup_window(), or NULL if
         * setup_window() has not been called.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_clock_object(self, FrameRateMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clock_object(FrameRateMeter self)
        
        /**
         * Returns the clock that is used to determine the frame rate.
         */
        """
        pass

    def get_display_region(self, FrameRateMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_region(FrameRateMeter self)
        
        /**
         * Returns the DisplayRegion that the meter has created to render itself into
         * the window to setup_window(), or NULL if setup_window() has not been
         * called.
         */
        """
        pass

    def get_text_pattern(self, FrameRateMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_text_pattern(FrameRateMeter self)
        
        /**
         * Returns the sprintf() pattern that is used to format the text.
         */
        """
        pass

    def get_update_interval(self, FrameRateMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_update_interval(FrameRateMeter self)
        
        /**
         * Returns the number of seconds that will elapse between updates to the frame
         * rate indication.
         */
        """
        pass

    def get_window(self, FrameRateMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_window(FrameRateMeter self)
        
        /**
         * Returns the GraphicsOutput that was passed to setup_window(), or NULL if
         * setup_window() has not been called.
         */
        """
        pass

    def setClockObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clock_object(const FrameRateMeter self, ClockObject clock_object)
        
        /**
         * Sets the clock that is used to determine the frame rate.  The default is
         * the application's global clock (ClockObject::get_global_clock()).
         */
        """
        pass

    def setTextPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_text_pattern(const FrameRateMeter self, str text_pattern)
        
        /**
         * Sets the sprintf() pattern that is used to format the text.  The string
         * "%f" or some variant will be replaced with the current frame rate in frames
         * per second.
         */
        """
        pass

    def setUpdateInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_update_interval(const FrameRateMeter self, double update_interval)
        
        /**
         * Specifies the number of seconds that should elapse between updates to the
         * frame rate indication.  This should be reasonably slow (e.g.  0.2 to 1.0)
         * so that the calculation of the frame rate text does not itself dominate the
         * frame rate.
         */
        """
        pass

    def setupWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_window(const FrameRateMeter self, GraphicsOutput window)
        
        /**
         * Sets up the frame rate meter to create a DisplayRegion to render itself
         * into the indicated window.
         */
        """
        pass

    def setup_window(self, const_FrameRateMeter_self, GraphicsOutput_window): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_window(const FrameRateMeter self, GraphicsOutput window)
        
        /**
         * Sets up the frame rate meter to create a DisplayRegion to render itself
         * into the indicated window.
         */
        """
        pass

    def set_clock_object(self, const_FrameRateMeter_self, ClockObject_clock_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clock_object(const FrameRateMeter self, ClockObject clock_object)
        
        /**
         * Sets the clock that is used to determine the frame rate.  The default is
         * the application's global clock (ClockObject::get_global_clock()).
         */
        """
        pass

    def set_text_pattern(self, const_FrameRateMeter_self, str_text_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_text_pattern(const FrameRateMeter self, str text_pattern)
        
        /**
         * Sets the sprintf() pattern that is used to format the text.  The string
         * "%f" or some variant will be replaced with the current frame rate in frames
         * per second.
         */
        """
        pass

    def set_update_interval(self, const_FrameRateMeter_self, double_update_interval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_update_interval(const FrameRateMeter self, double update_interval)
        
        /**
         * Specifies the number of seconds that should elapse between updates to the
         * frame rate indication.  This should be reasonably slow (e.g.  0.2 to 1.0)
         * so that the calculation of the frame rate text does not itself dominate the
         * frame rate.
         */
        """
        pass

    def update(self, const_FrameRateMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const FrameRateMeter self)
        
        /**
         * You can call this to explicitly force the FrameRateMeter to update itself
         * with the latest frame rate information.  Normally, it is not necessary to
         * call this explicitly.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.FrameRateMeter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.FrameRateMeter' objects>"
        '__doc__': "/**\n * This is a special TextNode that automatically updates itself with the\n * current frame rate.  It can be placed anywhere in the world where you'd\n * like to see the frame rate.\n *\n * It also has a special mode in which it may be attached directly to a\n * channel or window.  If this is done, it creates a DisplayRegion for itself\n * and renders itself in the upper-right-hand corner.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FrameRateMeter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BC390>'
        'clearWindow': None, # (!) real value is "<method 'clearWindow' of 'panda3d.core.FrameRateMeter' objects>"
        'clear_window': None, # (!) real value is "<method 'clear_window' of 'panda3d.core.FrameRateMeter' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BC390>)>'
        'getClockObject': None, # (!) real value is "<method 'getClockObject' of 'panda3d.core.FrameRateMeter' objects>"
        'getDisplayRegion': None, # (!) real value is "<method 'getDisplayRegion' of 'panda3d.core.FrameRateMeter' objects>"
        'getTextPattern': None, # (!) real value is "<method 'getTextPattern' of 'panda3d.core.FrameRateMeter' objects>"
        'getUpdateInterval': None, # (!) real value is "<method 'getUpdateInterval' of 'panda3d.core.FrameRateMeter' objects>"
        'getWindow': None, # (!) real value is "<method 'getWindow' of 'panda3d.core.FrameRateMeter' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BC390>)>'
        'get_clock_object': None, # (!) real value is "<method 'get_clock_object' of 'panda3d.core.FrameRateMeter' objects>"
        'get_display_region': None, # (!) real value is "<method 'get_display_region' of 'panda3d.core.FrameRateMeter' objects>"
        'get_text_pattern': None, # (!) real value is "<method 'get_text_pattern' of 'panda3d.core.FrameRateMeter' objects>"
        'get_update_interval': None, # (!) real value is "<method 'get_update_interval' of 'panda3d.core.FrameRateMeter' objects>"
        'get_window': None, # (!) real value is "<method 'get_window' of 'panda3d.core.FrameRateMeter' objects>"
        'setClockObject': None, # (!) real value is "<method 'setClockObject' of 'panda3d.core.FrameRateMeter' objects>"
        'setTextPattern': None, # (!) real value is "<method 'setTextPattern' of 'panda3d.core.FrameRateMeter' objects>"
        'setUpdateInterval': None, # (!) real value is "<method 'setUpdateInterval' of 'panda3d.core.FrameRateMeter' objects>"
        'set_clock_object': None, # (!) real value is "<method 'set_clock_object' of 'panda3d.core.FrameRateMeter' objects>"
        'set_text_pattern': None, # (!) real value is "<method 'set_text_pattern' of 'panda3d.core.FrameRateMeter' objects>"
        'set_update_interval': None, # (!) real value is "<method 'set_update_interval' of 'panda3d.core.FrameRateMeter' objects>"
        'setupWindow': None, # (!) real value is "<method 'setupWindow' of 'panda3d.core.FrameRateMeter' objects>"
        'setup_window': None, # (!) real value is "<method 'setup_window' of 'panda3d.core.FrameRateMeter' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.core.FrameRateMeter' objects>"
    }


