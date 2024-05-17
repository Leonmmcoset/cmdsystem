# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CallbackData import CallbackData

class GeomDrawCallbackData(CallbackData):
    """
    /**
     * This specialization on CallbackData is passed when the callback is
     * initiated from deep within the draw traversal, for a particular Geom.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_force(GeomDrawCallbackData self)
        
        /**
         * Returns true if any required data should be forced into memory if necessary
         * to render the object, or false if the object should be omitted if some of
         * the data is not available (at least until the data becomes available
         * later).
         */
        """
        pass

    def getGsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gsg(GeomDrawCallbackData self)
        
        /**
         * Returns a pointer to the current GSG.
         */
        """
        pass

    def getLostState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lost_state(GeomDrawCallbackData self)
        
        /**
         * Returns the lost_state flag.  See set_lost_state().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_force(self, GeomDrawCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_force(GeomDrawCallbackData self)
        
        /**
         * Returns true if any required data should be forced into memory if necessary
         * to render the object, or false if the object should be omitted if some of
         * the data is not available (at least until the data becomes available
         * later).
         */
        """
        pass

    def get_gsg(self, GeomDrawCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gsg(GeomDrawCallbackData self)
        
        /**
         * Returns a pointer to the current GSG.
         */
        """
        pass

    def get_lost_state(self, GeomDrawCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lost_state(GeomDrawCallbackData self)
        
        /**
         * Returns the lost_state flag.  See set_lost_state().
         */
        """
        pass

    def setLostState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lost_state(const GeomDrawCallbackData self, bool lost_state)
        
        /**
         * Sets the lost_state flag.  If this is true, the callback does not have to
         * be quite so careful to clean up after itself; Panda will assume that the
         * graphics state is in an unknown state after the callback has finished, and
         * will issue all the necessary calls to restore it.  If this is false, Panda
         * will assume the callback will leave the graphics state exactly as it came
         * in, and won't bother to try to restore it.  The default is true.
         */
        """
        pass

    def set_lost_state(self, const_GeomDrawCallbackData_self, bool_lost_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lost_state(const GeomDrawCallbackData self, bool lost_state)
        
        /**
         * Sets the lost_state flag.  If this is true, the callback does not have to
         * be quite so careful to clean up after itself; Panda will assume that the
         * graphics state is in an unknown state after the callback has finished, and
         * will issue all the necessary calls to restore it.  If this is false, Panda
         * will assume the callback will leave the graphics state exactly as it came
         * in, and won't bother to try to restore it.  The default is true.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This specialization on CallbackData is passed when the callback is\n * initiated from deep within the draw traversal, for a particular Geom.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomDrawCallbackData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE296F00>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE296F00>)>'
        'getForce': None, # (!) real value is "<method 'getForce' of 'panda3d.core.GeomDrawCallbackData' objects>"
        'getGsg': None, # (!) real value is "<method 'getGsg' of 'panda3d.core.GeomDrawCallbackData' objects>"
        'getLostState': None, # (!) real value is "<method 'getLostState' of 'panda3d.core.GeomDrawCallbackData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE296F00>)>'
        'get_force': None, # (!) real value is "<method 'get_force' of 'panda3d.core.GeomDrawCallbackData' objects>"
        'get_gsg': None, # (!) real value is "<method 'get_gsg' of 'panda3d.core.GeomDrawCallbackData' objects>"
        'get_lost_state': None, # (!) real value is "<method 'get_lost_state' of 'panda3d.core.GeomDrawCallbackData' objects>"
        'setLostState': None, # (!) real value is "<method 'setLostState' of 'panda3d.core.GeomDrawCallbackData' objects>"
        'set_lost_state': None, # (!) real value is "<method 'set_lost_state' of 'panda3d.core.GeomDrawCallbackData' objects>"
    }


