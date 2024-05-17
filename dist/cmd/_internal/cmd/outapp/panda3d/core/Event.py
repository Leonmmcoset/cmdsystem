# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class Event(TypedReferenceCount):
    """
    /**
     * A named event, possibly with parameters.  Anyone in any thread may throw an
     * event at any time; there will be one process responsible for reading and
     * dispacting on the events (but not necessarily immediately).
     *
     * This function use to inherit from Namable, but that makes it too expensive
     * to get its name the Python code.  Now it just copies the Namable interface
     * in.
     */
    """
    def addParameter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_parameter(const Event self, const EventParameter obj)
        
        /**
         *
         */
        """
        pass

    def add_parameter(self, const_Event_self, const_EventParameter_obj): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_parameter(const Event self, const EventParameter obj)
        
        /**
         *
         */
        """
        pass

    def assign(self, const_Event_self, const_Event_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const Event self, const Event copy)
        """
        pass

    def clearName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_name(const Event self)
        
        /**
         * Resets the Event's name to empty.
         */
        """
        pass

    def clearReceiver(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_receiver(const Event self)
        
        /**
         *
         */
        """
        pass

    def clear_name(self, const_Event_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_name(const Event self)
        
        /**
         * Resets the Event's name to empty.
         */
        """
        pass

    def clear_receiver(self, const_Event_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_receiver(const Event self)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(Event self)
        
        /**
         *
         */
        """
        pass

    def getNumParameters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_parameters(Event self)
        
        /**
         *
         */
        """
        pass

    def getParameter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parameter(Event self, int n)
        
        /**
         *
         */
        """
        pass

    def getParameters(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_name(self, Event_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(Event self)
        
        /**
         *
         */
        """
        pass

    def get_num_parameters(self, Event_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_parameters(Event self)
        
        /**
         *
         */
        """
        pass

    def get_parameter(self, Event_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parameter(Event self, int n)
        
        /**
         *
         */
        """
        pass

    def get_parameters(self, *args, **kwargs): # real signature unknown
        pass

    def hasName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_name(Event self)
        
        /**
         * Returns true if the Event has a nonempty name set, false if the name is
         * empty.
         */
        """
        pass

    def hasReceiver(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_receiver(Event self)
        
        /**
         *
         */
        """
        pass

    def has_name(self, Event_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_name(Event self)
        
        /**
         * Returns true if the Event has a nonempty name set, false if the name is
         * empty.
         */
        """
        pass

    def has_receiver(self, Event_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_receiver(Event self)
        
        /**
         *
         */
        """
        pass

    def output(self, Event_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Event self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const Event self, str name)
        
        /**
         *
         */
        """
        pass

    def set_name(self, const_Event_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const Event self, str name)
        
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

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Event' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Event' objects>"
        '__doc__': '/**\n * A named event, possibly with parameters.  Anyone in any thread may throw an\n * event at any time; there will be one process responsible for reading and\n * dispacting on the events (but not necessarily immediately).\n *\n * This function use to inherit from Namable, but that makes it too expensive\n * to get its name the Python code.  Now it just copies the Namable interface\n * in.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Event' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F0700>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Event' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Event' objects>"
        'addParameter': None, # (!) real value is "<method 'addParameter' of 'panda3d.core.Event' objects>"
        'add_parameter': None, # (!) real value is "<method 'add_parameter' of 'panda3d.core.Event' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.Event' objects>"
        'clearName': None, # (!) real value is "<method 'clearName' of 'panda3d.core.Event' objects>"
        'clearReceiver': None, # (!) real value is "<method 'clearReceiver' of 'panda3d.core.Event' objects>"
        'clear_name': None, # (!) real value is "<method 'clear_name' of 'panda3d.core.Event' objects>"
        'clear_receiver': None, # (!) real value is "<method 'clear_receiver' of 'panda3d.core.Event' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2F0700>)>'
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.Event' objects>"
        'getNumParameters': None, # (!) real value is "<method 'getNumParameters' of 'panda3d.core.Event' objects>"
        'getParameter': None, # (!) real value is "<method 'getParameter' of 'panda3d.core.Event' objects>"
        'getParameters': None, # (!) real value is "<method 'getParameters' of 'panda3d.core.Event' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2F0700>)>'
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.Event' objects>"
        'get_num_parameters': None, # (!) real value is "<method 'get_num_parameters' of 'panda3d.core.Event' objects>"
        'get_parameter': None, # (!) real value is "<method 'get_parameter' of 'panda3d.core.Event' objects>"
        'get_parameters': None, # (!) real value is "<method 'get_parameters' of 'panda3d.core.Event' objects>"
        'hasName': None, # (!) real value is "<method 'hasName' of 'panda3d.core.Event' objects>"
        'hasReceiver': None, # (!) real value is "<method 'hasReceiver' of 'panda3d.core.Event' objects>"
        'has_name': None, # (!) real value is "<method 'has_name' of 'panda3d.core.Event' objects>"
        'has_receiver': None, # (!) real value is "<method 'has_receiver' of 'panda3d.core.Event' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.Event' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Event' objects>"
        'parameters': None, # (!) real value is "<attribute 'parameters' of 'panda3d.core.Event' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.Event' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.Event' objects>"
    }


