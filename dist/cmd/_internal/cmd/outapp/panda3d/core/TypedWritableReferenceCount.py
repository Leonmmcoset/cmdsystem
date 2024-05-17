# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritable import TypedWritable

from .ReferenceCount import ReferenceCount

class TypedWritableReferenceCount(TypedWritable, ReferenceCount):
    """
    /**
     * A base class for things which need to inherit from both TypedWritable and
     * from ReferenceCount.  It's convenient to define this intermediate base
     * class instead of multiply inheriting from the two classes each time they
     * are needed, so that we can sensibly pass around pointers to things which
     * are both TypedWritables and ReferenceCounters.
     *
     * See also TypedObject for detailed instructions.
     */
    """
    def decodeFromBamStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        decode_from_bam_stream(bytes data, BamReader reader)
        
        /**
         * Reads the bytes created by a previous call to encode_to_bam_stream(), and
         * extracts and returns the single object on those bytes.  Returns NULL on
         * error.
         *
         * This method is intended to replace decode_raw_from_bam_stream() when you
         * know the stream in question returns an object of type
         * TypedWritableReferenceCount, allowing for easier reference count
         * management.  Note that the caller is still responsible for maintaining the
         * reference count on the return value.
         */
        """
        pass

    def decode_from_bam_stream(self, bytes_data, BamReader_reader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decode_from_bam_stream(bytes data, BamReader reader)
        
        /**
         * Reads the bytes created by a previous call to encode_to_bam_stream(), and
         * extracts and returns the single object on those bytes.  Returns NULL on
         * error.
         *
         * This method is intended to replace decode_raw_from_bam_stream() when you
         * know the stream in question returns an object of type
         * TypedWritableReferenceCount, allowing for easier reference count
         * management.  Note that the caller is still responsible for maintaining the
         * reference count on the return value.
         */
        """
        pass

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

    def upcastToReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ReferenceCount(const TypedWritableReferenceCount self)
        
        upcast from TypedWritableReferenceCount to ReferenceCount
        """
        pass

    def upcastToTypedWritable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritable(const TypedWritableReferenceCount self)
        
        upcast from TypedWritableReferenceCount to TypedWritable
        """
        pass

    def upcast_to_ReferenceCount(self, const_TypedWritableReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ReferenceCount(const TypedWritableReferenceCount self)
        
        upcast from TypedWritableReferenceCount to ReferenceCount
        """
        pass

    def upcast_to_TypedWritable(self, const_TypedWritableReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritable(const TypedWritableReferenceCount self)
        
        upcast from TypedWritableReferenceCount to TypedWritable
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
        '__doc__': "/**\n * A base class for things which need to inherit from both TypedWritable and\n * from ReferenceCount.  It's convenient to define this intermediate base\n * class instead of multiply inheriting from the two classes each time they\n * are needed, so that we can sensibly pass around pointers to things which\n * are both TypedWritables and ReferenceCounters.\n *\n * See also TypedObject for detailed instructions.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TypedWritableReferenceCount' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE36F700>'
        'decodeFromBamStream': None, # (!) real value is '<staticmethod(<built-in method decodeFromBamStream of type object at 0x00007FFCFE36F700>)>'
        'decode_from_bam_stream': None, # (!) real value is '<staticmethod(<built-in method decode_from_bam_stream of type object at 0x00007FFCFE36F700>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE36F700>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE36F700>)>'
        'upcastToReferenceCount': None, # (!) real value is "<method 'upcastToReferenceCount' of 'panda3d.core.TypedWritableReferenceCount' objects>"
        'upcastToTypedWritable': None, # (!) real value is "<method 'upcastToTypedWritable' of 'panda3d.core.TypedWritableReferenceCount' objects>"
        'upcast_to_ReferenceCount': None, # (!) real value is "<method 'upcast_to_ReferenceCount' of 'panda3d.core.TypedWritableReferenceCount' objects>"
        'upcast_to_TypedWritable': None, # (!) real value is "<method 'upcast_to_TypedWritable' of 'panda3d.core.TypedWritableReferenceCount' objects>"
    }


