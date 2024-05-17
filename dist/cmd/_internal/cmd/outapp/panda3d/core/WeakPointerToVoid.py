# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PointerToVoid import PointerToVoid

class WeakPointerToVoid(PointerToVoid):
    """
    /**
     * This is the specialization of PointerToVoid for weak pointers.  It needs an
     * additional flag to indicate that the pointer has been deleted.
     */
    """
    def isValidPointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid_pointer(WeakPointerToVoid self)
        
        /**
         * Returns true if the pointer is not null and the object has not been
         * deleted.  See was_deleted() for caveats.
         */
        """
        pass

    def is_valid_pointer(self, WeakPointerToVoid_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid_pointer(WeakPointerToVoid self)
        
        /**
         * Returns true if the pointer is not null and the object has not been
         * deleted.  See was_deleted() for caveats.
         */
        """
        pass

    def wasDeleted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        was_deleted(WeakPointerToVoid self)
        
        /**
         * Returns true if the object we are pointing to has been deleted, false
         * otherwise.  If this returns true, it means that the pointer can not yet be
         * reused, but it does not guarantee that it can be safely accessed.  See the
         * lock() method for a safe way to access the underlying pointer.
         *
         * This will always return true for a null pointer, unlike is_valid_pointer().
         */
        """
        pass

    def was_deleted(self, WeakPointerToVoid_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        was_deleted(WeakPointerToVoid self)
        
        /**
         * Returns true if the object we are pointing to has been deleted, false
         * otherwise.  If this returns true, it means that the pointer can not yet be
         * reused, but it does not guarantee that it can be safely accessed.  See the
         * lock() method for a safe way to access the underlying pointer.
         *
         * This will always return true for a null pointer, unlike is_valid_pointer().
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
        '__doc__': '/**\n * This is the specialization of PointerToVoid for weak pointers.  It needs an\n * additional flag to indicate that the pointer has been deleted.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.WeakPointerToVoid' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE27B520>'
        'isValidPointer': None, # (!) real value is "<method 'isValidPointer' of 'panda3d.core.WeakPointerToVoid' objects>"
        'is_valid_pointer': None, # (!) real value is "<method 'is_valid_pointer' of 'panda3d.core.WeakPointerToVoid' objects>"
        'wasDeleted': None, # (!) real value is "<method 'wasDeleted' of 'panda3d.core.WeakPointerToVoid' objects>"
        'was_deleted': None, # (!) real value is "<method 'was_deleted' of 'panda3d.core.WeakPointerToVoid' objects>"
    }


