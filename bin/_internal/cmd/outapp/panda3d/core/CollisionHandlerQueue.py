# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionHandler import CollisionHandler

class CollisionHandlerQueue(CollisionHandler):
    """
    /**
     * A special kind of CollisionHandler that does nothing except remember the
     * CollisionEntries detected the last pass.  This set of CollisionEntries may
     * then be queried by the calling function.  It's primarily useful when a
     * simple intersection test is being made, e.g.  for picking from the window.
     */
    """
    def clearEntries(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_entries(const CollisionHandlerQueue self)
        
        /**
         * Removes all the entries from the queue.
         */
        """
        pass

    def clear_entries(self, const_CollisionHandlerQueue_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_entries(const CollisionHandlerQueue self)
        
        /**
         * Removes all the entries from the queue.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getEntries(self, *args, **kwargs): # real signature unknown
        pass

    def getEntry(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_entry(CollisionHandlerQueue self, int n)
        
        /**
         * Returns the nth CollisionEntry detected last pass.
         */
        """
        pass

    def getNumEntries(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_entries(CollisionHandlerQueue self)
        
        /**
         * Returns the number of CollisionEntries detected last pass.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_entries(self, *args, **kwargs): # real signature unknown
        pass

    def get_entry(self, CollisionHandlerQueue_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_entry(CollisionHandlerQueue self, int n)
        
        /**
         * Returns the nth CollisionEntry detected last pass.
         */
        """
        pass

    def get_num_entries(self, CollisionHandlerQueue_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_entries(CollisionHandlerQueue self)
        
        /**
         * Returns the number of CollisionEntries detected last pass.
         */
        """
        pass

    def output(self, CollisionHandlerQueue_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(CollisionHandlerQueue self, ostream out)
        
        /**
         *
         */
        """
        pass

    def sortEntries(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sort_entries(const CollisionHandlerQueue self)
        
        /**
         * Sorts all the detected collisions front-to-back by
         * from_intersection_point() so that those intersection points closest to the
         * collider's origin (e.g., the center of the CollisionSphere, or the point_a
         * of a CollisionSegment) appear first.
         */
        """
        pass

    def sort_entries(self, const_CollisionHandlerQueue_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort_entries(const CollisionHandlerQueue self)
        
        /**
         * Sorts all the detected collisions front-to-back by
         * from_intersection_point() so that those intersection points closest to the
         * collider's origin (e.g., the center of the CollisionSphere, or the point_a
         * of a CollisionSegment) appear first.
         */
        """
        pass

    def write(self, CollisionHandlerQueue_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(CollisionHandlerQueue self, ostream out, int indent_level)
        
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

    def __reduce__(self, CollisionHandlerQueue_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(CollisionHandlerQueue self)
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CollisionHandlerQueue' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CollisionHandlerQueue' objects>"
        '__doc__': "/**\n * A special kind of CollisionHandler that does nothing except remember the\n * CollisionEntries detected the last pass.  This set of CollisionEntries may\n * then be queried by the calling function.  It's primarily useful when a\n * simple intersection test is being made, e.g.  for picking from the window.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionHandlerQueue' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CFC50>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.CollisionHandlerQueue' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.CollisionHandlerQueue' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'clearEntries': None, # (!) real value is "<method 'clearEntries' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'clear_entries': None, # (!) real value is "<method 'clear_entries' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'entries': None, # (!) real value is "<attribute 'entries' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CFC50>)>'
        'getEntries': None, # (!) real value is "<method 'getEntries' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'getEntry': None, # (!) real value is "<method 'getEntry' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'getNumEntries': None, # (!) real value is "<method 'getNumEntries' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CFC50>)>'
        'get_entries': None, # (!) real value is "<method 'get_entries' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'get_entry': None, # (!) real value is "<method 'get_entry' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'get_num_entries': None, # (!) real value is "<method 'get_num_entries' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'sortEntries': None, # (!) real value is "<method 'sortEntries' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'sort_entries': None, # (!) real value is "<method 'sort_entries' of 'panda3d.core.CollisionHandlerQueue' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.CollisionHandlerQueue' objects>"
    }


