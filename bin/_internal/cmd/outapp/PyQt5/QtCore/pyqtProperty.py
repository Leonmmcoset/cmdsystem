# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .object import object

class pyqtProperty(object):
    """
    pyqtProperty(type, fget=None, fset=None, freset=None, fdel=None, doc=None,
            designable=True, scriptable=True, stored=True, user=False,
            constant=False, final=False, notify=None,
            revision=0) -> property attribute
    
    type is the type of the property.  It is either a type object or a string
    that is the name of a C++ type.
    freset is a function for resetting an attribute to its default value.
    designable sets the DESIGNABLE flag (the default is True for writable
    properties and False otherwise).
    scriptable sets the SCRIPTABLE flag.
    stored sets the STORED flag.
    user sets the USER flag.
    constant sets the CONSTANT flag.
    final sets the FINAL flag.
    notify is the NOTIFY signal.
    revision is the REVISION.
    The other parameters are the same as those required by the standard Python
    property type.  Properties defined using pyqtProperty behave as both Python
    and Qt properties.
    Decorators can be used to define new properties or to modify existing ones.
    """
    def deleter(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the deleter on a property. """
        pass

    def getter(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the getter on a property. """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the getter on a property. """
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the reset on a property. """
        pass

    def setter(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the setter on a property. """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """ Descriptor to change the setter on a property. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __delete__(self, *args, **kwargs): # real signature unknown
        """ Delete an attribute of instance. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, type, fget=None, fset=None, freset=None, fdel=None, doc=None, designable=True, scriptable=True, stored=True, user=False, constant=False, final=False, notify=None, revision=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        """ Set an attribute of instance to value. """
        pass

    fdel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



