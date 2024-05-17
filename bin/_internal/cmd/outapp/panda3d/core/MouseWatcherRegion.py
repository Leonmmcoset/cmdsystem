# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

from .Namable import Namable

class MouseWatcherRegion(TypedWritableReferenceCount, Namable):
    """
    /**
     * This is the class that defines a rectangular region on the screen for the
     * MouseWatcher.
     */
    """
    def getActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active(MouseWatcherRegion self)
        
        /**
         * Returns whether the region is active or not.  See set_active().
         */
        """
        pass

    def getArea(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_area(MouseWatcherRegion self)
        
        /**
         * Returns the area of the rectangular region.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame(MouseWatcherRegion self)
        
        /**
         *
         */
        """
        pass

    def getKeyboard(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keyboard(MouseWatcherRegion self)
        
        /**
         * Returns whether the region is interested in global keyboard events; see
         * set_keyboard().
         */
        """
        pass

    def getSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sort(MouseWatcherRegion self)
        
        /**
         * Returns the current sorting order of this region.  See set_sort().
         */
        """
        pass

    def getSuppressFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_suppress_flags(MouseWatcherRegion self)
        
        /**
         * Returns the current suppress_flags.  See set_suppress_flags().
         */
        """
        pass

    def get_active(self, MouseWatcherRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active(MouseWatcherRegion self)
        
        /**
         * Returns whether the region is active or not.  See set_active().
         */
        """
        pass

    def get_area(self, MouseWatcherRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_area(MouseWatcherRegion self)
        
        /**
         * Returns the area of the rectangular region.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_frame(self, MouseWatcherRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame(MouseWatcherRegion self)
        
        /**
         *
         */
        """
        pass

    def get_keyboard(self, MouseWatcherRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keyboard(MouseWatcherRegion self)
        
        /**
         * Returns whether the region is interested in global keyboard events; see
         * set_keyboard().
         */
        """
        pass

    def get_sort(self, MouseWatcherRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sort(MouseWatcherRegion self)
        
        /**
         * Returns the current sorting order of this region.  See set_sort().
         */
        """
        pass

    def get_suppress_flags(self, MouseWatcherRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_suppress_flags(MouseWatcherRegion self)
        
        /**
         * Returns the current suppress_flags.  See set_suppress_flags().
         */
        """
        pass

    def output(self, MouseWatcherRegion_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(MouseWatcherRegion self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const MouseWatcherRegion self, bool active)
        
        /**
         * Sets whether the region is active or not.  If it is not active, the
         * MouseWatcher will never consider the mouse to be over the region.  The
         * region might still receive keypress events if its set_keyboard() flag is
         * true.
         */
        """
        pass

    def setFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame(const MouseWatcherRegion self, const LVecBase4f frame)
        set_frame(const MouseWatcherRegion self, float left, float right, float bottom, float top)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setKeyboard(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_keyboard(const MouseWatcherRegion self, bool keyboard)
        
        /**
         * Sets whether the region is interested in global keyboard events.  If this
         * is true, then any keyboard button events will be passed to press() and
         * release() regardless of the position of the mouse onscreen; otherwise,
         * these events will only be passed if the mouse is over the region.
         */
        """
        pass

    def setSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sort(const MouseWatcherRegion self, int sort)
        
        /**
         * Changes the sorting order of this particular region.  The sorting order is
         * used to resolve conflicts in the case of overlapping region; the region
         * with the highest sort value will be preferred, and between regions of the
         * same sort value, the smallest region will be preferred.  The default
         * sorting order, if none is explicitly specified, is 0.
         */
        """
        pass

    def setSuppressFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_suppress_flags(const MouseWatcherRegion self, int suppress_flags)
        
        /**
         * Sets which events are suppressed when the mouse is over the region.  This
         * is the union of zero or more various SF_* values.  Normally, this is 0,
         * indicating that no events are suppressed.
         *
         * If you set this to a non-zero value, for instance SF_mouse_position, then
         * the mouse position will not be sent along the data graph when the mouse is
         * over this particular region.
         */
        """
        pass

    def set_active(self, const_MouseWatcherRegion_self, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const MouseWatcherRegion self, bool active)
        
        /**
         * Sets whether the region is active or not.  If it is not active, the
         * MouseWatcher will never consider the mouse to be over the region.  The
         * region might still receive keypress events if its set_keyboard() flag is
         * true.
         */
        """
        pass

    def set_frame(self, const_MouseWatcherRegion_self, const_LVecBase4f_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame(const MouseWatcherRegion self, const LVecBase4f frame)
        set_frame(const MouseWatcherRegion self, float left, float right, float bottom, float top)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_keyboard(self, const_MouseWatcherRegion_self, bool_keyboard): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_keyboard(const MouseWatcherRegion self, bool keyboard)
        
        /**
         * Sets whether the region is interested in global keyboard events.  If this
         * is true, then any keyboard button events will be passed to press() and
         * release() regardless of the position of the mouse onscreen; otherwise,
         * these events will only be passed if the mouse is over the region.
         */
        """
        pass

    def set_sort(self, const_MouseWatcherRegion_self, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sort(const MouseWatcherRegion self, int sort)
        
        /**
         * Changes the sorting order of this particular region.  The sorting order is
         * used to resolve conflicts in the case of overlapping region; the region
         * with the highest sort value will be preferred, and between regions of the
         * same sort value, the smallest region will be preferred.  The default
         * sorting order, if none is explicitly specified, is 0.
         */
        """
        pass

    def set_suppress_flags(self, const_MouseWatcherRegion_self, int_suppress_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_suppress_flags(const MouseWatcherRegion self, int suppress_flags)
        
        /**
         * Sets which events are suppressed when the mouse is over the region.  This
         * is the union of zero or more various SF_* values.  Normally, this is 0,
         * indicating that no events are suppressed.
         *
         * If you set this to a non-zero value, for instance SF_mouse_position, then
         * the mouse position will not be sent along the data graph when the mouse is
         * over this particular region.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const MouseWatcherRegion self)
        
        upcast from MouseWatcherRegion to Namable
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const MouseWatcherRegion self)
        
        upcast from MouseWatcherRegion to TypedWritableReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_MouseWatcherRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const MouseWatcherRegion self)
        
        upcast from MouseWatcherRegion to Namable
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_MouseWatcherRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const MouseWatcherRegion self)
        
        upcast from MouseWatcherRegion to TypedWritableReferenceCount
        """
        pass

    def write(self, MouseWatcherRegion_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(MouseWatcherRegion self, ostream out, int indent_level)
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keyboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    suppress_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SFAnyButton': 3,
        'SFMouseButton': 1,
        'SFMousePosition': 4,
        'SFOtherButton': 2,
        'SF_any_button': 3,
        'SF_mouse_button': 1,
        'SF_mouse_position': 4,
        'SF_other_button': 2,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MouseWatcherRegion' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MouseWatcherRegion' objects>"
        '__doc__': '/**\n * This is the class that defines a rectangular region on the screen for the\n * MouseWatcher.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseWatcherRegion' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE366640>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.MouseWatcherRegion' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.MouseWatcherRegion' objects>"
        'active': None, # (!) real value is "<attribute 'active' of 'panda3d.core.MouseWatcherRegion' objects>"
        'area': None, # (!) real value is "<attribute 'area' of 'panda3d.core.MouseWatcherRegion' objects>"
        'frame': None, # (!) real value is "<attribute 'frame' of 'panda3d.core.MouseWatcherRegion' objects>"
        'getActive': None, # (!) real value is "<method 'getActive' of 'panda3d.core.MouseWatcherRegion' objects>"
        'getArea': None, # (!) real value is "<method 'getArea' of 'panda3d.core.MouseWatcherRegion' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE366640>)>'
        'getFrame': None, # (!) real value is "<method 'getFrame' of 'panda3d.core.MouseWatcherRegion' objects>"
        'getKeyboard': None, # (!) real value is "<method 'getKeyboard' of 'panda3d.core.MouseWatcherRegion' objects>"
        'getSort': None, # (!) real value is "<method 'getSort' of 'panda3d.core.MouseWatcherRegion' objects>"
        'getSuppressFlags': None, # (!) real value is "<method 'getSuppressFlags' of 'panda3d.core.MouseWatcherRegion' objects>"
        'get_active': None, # (!) real value is "<method 'get_active' of 'panda3d.core.MouseWatcherRegion' objects>"
        'get_area': None, # (!) real value is "<method 'get_area' of 'panda3d.core.MouseWatcherRegion' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE366640>)>'
        'get_frame': None, # (!) real value is "<method 'get_frame' of 'panda3d.core.MouseWatcherRegion' objects>"
        'get_keyboard': None, # (!) real value is "<method 'get_keyboard' of 'panda3d.core.MouseWatcherRegion' objects>"
        'get_sort': None, # (!) real value is "<method 'get_sort' of 'panda3d.core.MouseWatcherRegion' objects>"
        'get_suppress_flags': None, # (!) real value is "<method 'get_suppress_flags' of 'panda3d.core.MouseWatcherRegion' objects>"
        'keyboard': None, # (!) real value is "<attribute 'keyboard' of 'panda3d.core.MouseWatcherRegion' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.MouseWatcherRegion' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.MouseWatcherRegion' objects>"
        'setFrame': None, # (!) real value is "<method 'setFrame' of 'panda3d.core.MouseWatcherRegion' objects>"
        'setKeyboard': None, # (!) real value is "<method 'setKeyboard' of 'panda3d.core.MouseWatcherRegion' objects>"
        'setSort': None, # (!) real value is "<method 'setSort' of 'panda3d.core.MouseWatcherRegion' objects>"
        'setSuppressFlags': None, # (!) real value is "<method 'setSuppressFlags' of 'panda3d.core.MouseWatcherRegion' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.MouseWatcherRegion' objects>"
        'set_frame': None, # (!) real value is "<method 'set_frame' of 'panda3d.core.MouseWatcherRegion' objects>"
        'set_keyboard': None, # (!) real value is "<method 'set_keyboard' of 'panda3d.core.MouseWatcherRegion' objects>"
        'set_sort': None, # (!) real value is "<method 'set_sort' of 'panda3d.core.MouseWatcherRegion' objects>"
        'set_suppress_flags': None, # (!) real value is "<method 'set_suppress_flags' of 'panda3d.core.MouseWatcherRegion' objects>"
        'sort': None, # (!) real value is "<attribute 'sort' of 'panda3d.core.MouseWatcherRegion' objects>"
        'suppress_flags': None, # (!) real value is "<attribute 'suppress_flags' of 'panda3d.core.MouseWatcherRegion' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.MouseWatcherRegion' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.MouseWatcherRegion' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.MouseWatcherRegion' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.MouseWatcherRegion' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.MouseWatcherRegion' objects>"
    }
    SFAnyButton = 3
    SFMouseButton = 1
    SFMousePosition = 4
    SFOtherButton = 2
    SF_any_button = 3
    SF_mouse_button = 1
    SF_mouse_position = 4
    SF_other_button = 2


