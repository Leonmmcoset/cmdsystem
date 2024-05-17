# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class VertexTransform(TypedWritableReferenceCount):
    """
    /**
     * This is an abstract base class that holds a pointer to some transform,
     * computed in some arbitrary way, that is to be applied to vertices during
     * rendering.  This is used to implement soft-skinned and animated vertices.
     * Derived classes will define how the transform is actually computed.
     */
    """
    def accumulateMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        accumulate_matrix(VertexTransform self, LMatrix4f accum, float weight)
        
        /**
         * Adds the value of this transform's matrix, modified by the indicated
         * weight, into the indicated accumulation matrix.  This is used to compute
         * the result of several blended transforms.
         */
        """
        pass

    def accumulate_matrix(self, VertexTransform_self, LMatrix4f_accum, float_weight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        accumulate_matrix(VertexTransform self, LMatrix4f accum, float weight)
        
        /**
         * Adds the value of this transform's matrix, modified by the indicated
         * weight, into the indicated accumulation matrix.  This is used to compute
         * the result of several blended transforms.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGlobalModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_modified(Thread current_thread)
        
        /**
         * Returns the currently highest VertexTransform::get_modified() value in the
         * world.  This can be used as a quick way to determine if any
         * VertexTransforms have changed value recently.
         */
        """
        pass

    def getMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_matrix(VertexTransform self, LMatrix4f matrix)
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(VertexTransform self, Thread current_thread)
        
        /**
         * Returns a sequence number that's guaranteed to change at least every time
         * the value reported by get_matrix() changes.
         */
        """
        pass

    def getNextModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_modified(Thread current_thread)
        
        /**
         * Returns a monotonically increasing sequence.  Each time this is called, a
         * new sequence number is returned, higher than the previous value.
         *
         * This is used to ensure that all VertexTransform::get_modified() calls
         * return an increasing number in the same space, so that
         * TransformBlend::get_modified() is easy to determine.  It is similar to
         * Geom::get_modified(), but it is in a different space.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_global_modified(self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_modified(Thread current_thread)
        
        /**
         * Returns the currently highest VertexTransform::get_modified() value in the
         * world.  This can be used as a quick way to determine if any
         * VertexTransforms have changed value recently.
         */
        """
        pass

    def get_matrix(self, VertexTransform_self, LMatrix4f_matrix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_matrix(VertexTransform self, LMatrix4f matrix)
        """
        pass

    def get_modified(self, VertexTransform_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(VertexTransform self, Thread current_thread)
        
        /**
         * Returns a sequence number that's guaranteed to change at least every time
         * the value reported by get_matrix() changes.
         */
        """
        pass

    def get_next_modified(self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_modified(Thread current_thread)
        
        /**
         * Returns a monotonically increasing sequence.  Each time this is called, a
         * new sequence number is returned, higher than the previous value.
         *
         * This is used to ensure that all VertexTransform::get_modified() calls
         * return an increasing number in the same space, so that
         * TransformBlend::get_modified() is easy to determine.  It is similar to
         * Geom::get_modified(), but it is in a different space.
         */
        """
        pass

    def multMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mult_matrix(VertexTransform self, LMatrix4f result, const LMatrix4f previous)
        
        /**
         * Premultiplies this transform's matrix with the indicated previous matrix,
         * so that the result is the net composition of the given transform with this
         * transform.  The result is stored in the parameter "result", which should
         * not be the same matrix as previous.
         */
        """
        pass

    def mult_matrix(self, VertexTransform_self, LMatrix4f_result, const_LMatrix4f_previous): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mult_matrix(VertexTransform self, LMatrix4f result, const LMatrix4f previous)
        
        /**
         * Premultiplies this transform's matrix with the indicated previous matrix,
         * so that the result is the net composition of the given transform with this
         * transform.  The result is stored in the parameter "result", which should
         * not be the same matrix as previous.
         */
        """
        pass

    def output(self, VertexTransform_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(VertexTransform self, ostream out)
        
        /**
         *
         */
        """
        pass

    def write(self, VertexTransform_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(VertexTransform self, ostream out, int indent_level)
        
        /**
         *
         */
        """
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

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is an abstract base class that holds a pointer to some transform,\n * computed in some arbitrary way, that is to be applied to vertices during\n * rendering.  This is used to implement soft-skinned and animated vertices.\n * Derived classes will define how the transform is actually computed.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VertexTransform' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FB8B0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.VertexTransform' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.VertexTransform' objects>"
        'accumulateMatrix': None, # (!) real value is "<method 'accumulateMatrix' of 'panda3d.core.VertexTransform' objects>"
        'accumulate_matrix': None, # (!) real value is "<method 'accumulate_matrix' of 'panda3d.core.VertexTransform' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FB8B0>)>'
        'getGlobalModified': None, # (!) real value is '<staticmethod(<built-in method getGlobalModified of type object at 0x00007FFCFE2FB8B0>)>'
        'getMatrix': None, # (!) real value is "<method 'getMatrix' of 'panda3d.core.VertexTransform' objects>"
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.VertexTransform' objects>"
        'getNextModified': None, # (!) real value is '<staticmethod(<built-in method getNextModified of type object at 0x00007FFCFE2FB8B0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FB8B0>)>'
        'get_global_modified': None, # (!) real value is '<staticmethod(<built-in method get_global_modified of type object at 0x00007FFCFE2FB8B0>)>'
        'get_matrix': None, # (!) real value is "<method 'get_matrix' of 'panda3d.core.VertexTransform' objects>"
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.VertexTransform' objects>"
        'get_next_modified': None, # (!) real value is '<staticmethod(<built-in method get_next_modified of type object at 0x00007FFCFE2FB8B0>)>'
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.VertexTransform' objects>"
        'multMatrix': None, # (!) real value is "<method 'multMatrix' of 'panda3d.core.VertexTransform' objects>"
        'mult_matrix': None, # (!) real value is "<method 'mult_matrix' of 'panda3d.core.VertexTransform' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.VertexTransform' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.VertexTransform' objects>"
    }


