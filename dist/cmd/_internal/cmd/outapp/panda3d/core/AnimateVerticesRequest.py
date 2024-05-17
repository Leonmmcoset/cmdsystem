# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AsyncTask import AsyncTask

class AnimateVerticesRequest(AsyncTask):
    """
    /**
     * This class object manages a single asynchronous request to animate vertices
     * on a GeomVertexData object.  animate_vertices will be called with
     * force=true (i.e.  blocking) in a sub-thread (if threading is available).
     * No result is stored or returned from this object.  It is expected that the
     * result will be cached and available for immediate use later during
     * rendering.  Thus it is important that the main thread block while these
     * requests are being run (presumably on multiple CPUs/cores), to ensure that
     * the data has been computed by the time it's needed.
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

    def isReady(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ready(AnimateVerticesRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
         */
        """
        pass

    def is_ready(self, AnimateVerticesRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ready(AnimateVerticesRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AnimateVerticesRequest' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AnimateVerticesRequest' objects>"
        '__doc__': "/**\n * This class object manages a single asynchronous request to animate vertices\n * on a GeomVertexData object.  animate_vertices will be called with\n * force=true (i.e.  blocking) in a sub-thread (if threading is available).\n * No result is stored or returned from this object.  It is expected that the\n * result will be cached and available for immediate use later during\n * rendering.  Thus it is important that the main thread block while these\n * requests are being run (presumably on multiple CPUs/cores), to ensure that\n * the data has been computed by the time it's needed.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimateVerticesRequest' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FC560>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FC560>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FC560>)>'
        'isReady': None, # (!) real value is "<method 'isReady' of 'panda3d.core.AnimateVerticesRequest' objects>"
        'is_ready': None, # (!) real value is "<method 'is_ready' of 'panda3d.core.AnimateVerticesRequest' objects>"
    }


