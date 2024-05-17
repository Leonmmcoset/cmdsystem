# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

class TypedWritable(TypedObject):
    """
    /**
     * Base class for objects that can be written to and read from Bam files.
     *
     * See also TypedObject for detailed instructions.
     */
    """
    def encodeToBamStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        encode_to_bam_stream(TypedWritable self)
        
        /**
         * Converts the TypedWritable object into a single stream of data using a
         * BamWriter, and returns that data as a bytes object.  Returns an empty bytes
         * object on failure.
         *
         * This is a convenience method particularly useful for cases when you are
         * only serializing a single object.  If you have many objects to process, it
         * is more efficient to use the same BamWriter to serialize all of them
         * together.
         */
        
        /**
         * Converts the TypedWritable object into a single stream of data using a
         * BamWriter, and stores that data in the indicated string.  Returns true on
         * success, false on failure.
         *
         * This is a convenience method particularly useful for cases when you are
         * only serializing a single object.  If you have many objects to process, it
         * is more efficient to use the same BamWriter to serialize all of them
         * together.
         */
        """
        pass

    def encode_to_bam_stream(self, TypedWritable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        encode_to_bam_stream(TypedWritable self)
        
        /**
         * Converts the TypedWritable object into a single stream of data using a
         * BamWriter, and returns that data as a bytes object.  Returns an empty bytes
         * object on failure.
         *
         * This is a convenience method particularly useful for cases when you are
         * only serializing a single object.  If you have many objects to process, it
         * is more efficient to use the same BamWriter to serialize all of them
         * together.
         */
        
        /**
         * Converts the TypedWritable object into a single stream of data using a
         * BamWriter, and stores that data in the indicated string.  Returns true on
         * success, false on failure.
         *
         * This is a convenience method particularly useful for cases when you are
         * only serializing a single object.  If you have many objects to process, it
         * is more efficient to use the same BamWriter to serialize all of them
         * together.
         */
        """
        pass

    def fillin(self, const_TypedWritable_self, DatagramIterator_scan, BamReader_manager): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fillin(const TypedWritable self, DatagramIterator scan, BamReader manager)
        
        /**
         * This internal function is intended to be called by each class's
         * make_from_bam() method to read in all of the relevant data from the BamFile
         * for the new object.  It is also called directly by the BamReader to re-read
         * the data for an object that has been placed on the stream for an update.
         */
        """
        pass

    def getBamModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bam_modified(TypedWritable self)
        
        /**
         * Returns the current bam_modified counter.  This counter is normally
         * incremented automatically whenever the object is modified.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_bam_modified(self, TypedWritable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bam_modified(TypedWritable self)
        
        /**
         * Returns the current bam_modified counter.  This counter is normally
         * incremented automatically whenever the object is modified.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def markBamModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mark_bam_modified(const TypedWritable self)
        
        /**
         * Increments the bam_modified counter, so that this object will be
         * invalidated and retransmitted on any open bam streams.  This should
         * normally not need to be called by user code; it should be called internally
         * when the object has been changed in a way that legitimately requires its
         * retransmission to any connected clients.
         */
        """
        pass

    def mark_bam_modified(self, const_TypedWritable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mark_bam_modified(const TypedWritable self)
        
        /**
         * Increments the bam_modified counter, so that this object will be
         * invalidated and retransmitted on any open bam streams.  This should
         * normally not need to be called by user code; it should be called internally
         * when the object has been changed in a way that legitimately requires its
         * retransmission to any connected clients.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_persist__(self, TypedWritable_self, object_pickler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce_persist__(TypedWritable self, object pickler)
        """
        pass

    def __reduce__(self, TypedWritable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(TypedWritable self)
        """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Base class for objects that can be written to and read from Bam files.\n *\n * See also TypedObject for detailed instructions.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TypedWritable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE36F530>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.TypedWritable' objects>"
        '__reduce_persist__': None, # (!) real value is "<method '__reduce_persist__' of 'panda3d.core.TypedWritable' objects>"
        'encodeToBamStream': None, # (!) real value is "<method 'encodeToBamStream' of 'panda3d.core.TypedWritable' objects>"
        'encode_to_bam_stream': None, # (!) real value is "<method 'encode_to_bam_stream' of 'panda3d.core.TypedWritable' objects>"
        'fillin': None, # (!) real value is "<method 'fillin' of 'panda3d.core.TypedWritable' objects>"
        'getBamModified': None, # (!) real value is "<method 'getBamModified' of 'panda3d.core.TypedWritable' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE36F530>)>'
        'get_bam_modified': None, # (!) real value is "<method 'get_bam_modified' of 'panda3d.core.TypedWritable' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE36F530>)>'
        'markBamModified': None, # (!) real value is "<method 'markBamModified' of 'panda3d.core.TypedWritable' objects>"
        'mark_bam_modified': None, # (!) real value is "<method 'mark_bam_modified' of 'panda3d.core.TypedWritable' objects>"
    }


