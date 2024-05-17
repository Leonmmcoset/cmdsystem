# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ReferenceCount(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A base class for all things that want to be reference-counted.
     * ReferenceCount works in conjunction with PointerTo to automatically delete
     * objects when the last pointer to them goes away.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getRefCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ref_count(ReferenceCount self)
        
        /**
         * Returns the current reference count.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_ref_count(self, ReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ref_count(ReferenceCount self)
        
        /**
         * Returns the current reference count.
         */
        """
        pass

    def ref(self, ReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ref(ReferenceCount self)
        
        /**
         * Explicitly increments the reference count.  User code should avoid using
         * ref() and unref() directly, which can result in missed reference counts.
         * Instead, let a PointerTo object manage the reference counting
         * automatically.
         *
         * This function is const, even though it changes the object, because
         * generally fiddling with an object's reference count isn't considered part
         * of fiddling with the object.  An object might be const in other ways, but
         * we still need to accurately count the number of references to it.
         */
        """
        pass

    def testRefCountIntegrity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_ref_count_integrity(ReferenceCount self)
        
        /**
         * Does some easy checks to make sure that the reference count isn't
         * completely bogus.  Returns true if ok, false otherwise.
         */
        """
        pass

    def testRefCountNonzero(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_ref_count_nonzero(ReferenceCount self)
        
        /**
         * Does some easy checks to make sure that the reference count isn't zero, or
         * completely bogus.  Returns true if ok, false otherwise.
         */
        """
        pass

    def test_ref_count_integrity(self, ReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_ref_count_integrity(ReferenceCount self)
        
        /**
         * Does some easy checks to make sure that the reference count isn't
         * completely bogus.  Returns true if ok, false otherwise.
         */
        """
        pass

    def test_ref_count_nonzero(self, ReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_ref_count_nonzero(ReferenceCount self)
        
        /**
         * Does some easy checks to make sure that the reference count isn't zero, or
         * completely bogus.  Returns true if ok, false otherwise.
         */
        """
        pass

    def unref(self, ReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unref(ReferenceCount self)
        
        /**
         * Explicitly decrements the reference count.  Note that the object will not
         * be implicitly deleted by unref() simply because the reference count drops
         * to zero.  (Having a member function delete itself is problematic.) However,
         * see the helper function unref_delete().
         *
         * User code should avoid using ref() and unref() directly, which can result
         * in missed reference counts.  Instead, let a PointerTo object manage the
         * reference counting automatically.
         *
         * This function is const, even though it changes the object, because
         * generally fiddling with an object's reference count isn't considered part
         * of fiddling with the object.  An object might be const in other ways, but
         * we still need to accurately count the number of references to it.
         *
         * The return value is true if the new reference count is nonzero, false if it
         * is zero.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// The current reference count."""


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A base class for all things that want to be reference-counted.\n * ReferenceCount works in conjunction with PointerTo to automatically delete\n * objects when the last pointer to them goes away.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ReferenceCount' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE277210>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE277210>)>'
        'getRefCount': None, # (!) real value is "<method 'getRefCount' of 'panda3d.core.ReferenceCount' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE277210>)>'
        'get_ref_count': None, # (!) real value is "<method 'get_ref_count' of 'panda3d.core.ReferenceCount' objects>"
        'ref': None, # (!) real value is "<method 'ref' of 'panda3d.core.ReferenceCount' objects>"
        'ref_count': None, # (!) real value is "<attribute 'ref_count' of 'panda3d.core.ReferenceCount' objects>"
        'testRefCountIntegrity': None, # (!) real value is "<method 'testRefCountIntegrity' of 'panda3d.core.ReferenceCount' objects>"
        'testRefCountNonzero': None, # (!) real value is "<method 'testRefCountNonzero' of 'panda3d.core.ReferenceCount' objects>"
        'test_ref_count_integrity': None, # (!) real value is "<method 'test_ref_count_integrity' of 'panda3d.core.ReferenceCount' objects>"
        'test_ref_count_nonzero': None, # (!) real value is "<method 'test_ref_count_nonzero' of 'panda3d.core.ReferenceCount' objects>"
        'unref': None, # (!) real value is "<method 'unref' of 'panda3d.core.ReferenceCount' objects>"
    }


