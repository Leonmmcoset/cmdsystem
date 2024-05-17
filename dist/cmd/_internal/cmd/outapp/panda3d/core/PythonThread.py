# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Thread import Thread

class PythonThread(Thread):
    """
    /**
     * This class is exposed to Python to allow creation of a Panda thread from
     * the Python level.  It will spawn a thread that executes an arbitrary Python
     * functor.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def join(self, const_PythonThread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        join(const PythonThread self)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class is exposed to Python to allow creation of a Panda thread from\n * the Python level.  It will spawn a thread that executes an arbitrary Python\n * functor.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PythonThread' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2ECE60>'
        'args': None, # (!) real value is "<attribute 'args' of 'panda3d.core.PythonThread' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2ECE60>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2ECE60>)>'
        'join': None, # (!) real value is "<method 'join' of 'panda3d.core.PythonThread' objects>"
    }


