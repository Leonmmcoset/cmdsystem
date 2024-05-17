# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CopyOnWriteObject import CopyOnWriteObject

class TransformBlendTable(CopyOnWriteObject):
    """
    /**
     * This structure collects together the different combinations of transforms
     * and blend amounts used by a GeomVertexData, to facilitate computing dynamic
     * vertices on the CPU at runtime.  Each vertex has a pointer to exactly one
     * of the entries in this table, and each entry defines a number of
     * transform/blend combinations.
     *
     * This structure is used for a GeomVertexData set up to compute its dynamic
     * vertices on the CPU.  See TransformTable for one set up to compute its
     * dynamic vertices on the graphics card.
     */
    """
    def addBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_blend(const TransformBlendTable self, const TransformBlend blend)
        
        /**
         * Adds a new blend to the table, and returns its index number.  If there is
         * already an identical blend in the table, simply returns that number
         * instead.
         */
        """
        pass

    def add_blend(self, const_TransformBlendTable_self, const_TransformBlend_blend): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_blend(const TransformBlendTable self, const TransformBlend blend)
        
        /**
         * Adds a new blend to the table, and returns its index number.  If there is
         * already an identical blend in the table, simply returns that number
         * instead.
         */
        """
        pass

    def assign(self, const_TransformBlendTable_self, const_TransformBlendTable_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TransformBlendTable self, const TransformBlendTable copy)
        """
        pass

    def getBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blend(TransformBlendTable self, int n)
        
        /**
         * Returns the nth blend in the table.
         */
        """
        pass

    def getBlends(self, *args, **kwargs): # real signature unknown
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMaxSimultaneousTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_simultaneous_transforms(TransformBlendTable self)
        
        /**
         * Returns the maximum number of unique VertexTransform objects that are
         * applied to any one vertex simultaneously.  This is the same limit reflected
         * by GraphicsStateGuardian::get_max_vertex_transforms().
         */
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(TransformBlendTable self, Thread current_thread)
        
        /**
         * Returns a counter which is guaranteed to increment at least when any
         * TransformBlends within the table have changed.
         */
        """
        pass

    def getNumBlends(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_blends(TransformBlendTable self)
        
        /**
         * Returns the total number of different blend combinations in the table.
         */
        """
        pass

    def getNumTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_transforms(TransformBlendTable self)
        
        /**
         * Returns the number of unique VertexTransform objects represented in the
         * table.  This will correspond to the size of the TransformTable object that
         * would represent the same table.  This is also the same limit reflected by
         * GraphicsStateGuardian::get_max_vertex_transform_indices().
         */
        """
        pass

    def getRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rows(TransformBlendTable self)
        
        /**
         * Returns the subset of rows (vertices) in the associated GeomVertexData that
         * this TransformBlendTable actually affects.
         */
        """
        pass

    def get_blend(self, TransformBlendTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blend(TransformBlendTable self, int n)
        
        /**
         * Returns the nth blend in the table.
         */
        """
        pass

    def get_blends(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_max_simultaneous_transforms(self, TransformBlendTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_simultaneous_transforms(TransformBlendTable self)
        
        /**
         * Returns the maximum number of unique VertexTransform objects that are
         * applied to any one vertex simultaneously.  This is the same limit reflected
         * by GraphicsStateGuardian::get_max_vertex_transforms().
         */
        """
        pass

    def get_modified(self, TransformBlendTable_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(TransformBlendTable self, Thread current_thread)
        
        /**
         * Returns a counter which is guaranteed to increment at least when any
         * TransformBlends within the table have changed.
         */
        """
        pass

    def get_num_blends(self, TransformBlendTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_blends(TransformBlendTable self)
        
        /**
         * Returns the total number of different blend combinations in the table.
         */
        """
        pass

    def get_num_transforms(self, TransformBlendTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_transforms(TransformBlendTable self)
        
        /**
         * Returns the number of unique VertexTransform objects represented in the
         * table.  This will correspond to the size of the TransformTable object that
         * would represent the same table.  This is also the same limit reflected by
         * GraphicsStateGuardian::get_max_vertex_transform_indices().
         */
        """
        pass

    def get_rows(self, TransformBlendTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rows(TransformBlendTable self)
        
        /**
         * Returns the subset of rows (vertices) in the associated GeomVertexData that
         * this TransformBlendTable actually affects.
         */
        """
        pass

    def modifyRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_rows(const TransformBlendTable self)
        
        /**
         * Returns a modifiable reference to the SparseArray that specifies the subset
         * of rows (vertices) in the associated GeomVertexData that this
         * TransformBlendTable actually affects.
         */
        """
        pass

    def modify_rows(self, const_TransformBlendTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_rows(const TransformBlendTable self)
        
        /**
         * Returns a modifiable reference to the SparseArray that specifies the subset
         * of rows (vertices) in the associated GeomVertexData that this
         * TransformBlendTable actually affects.
         */
        """
        pass

    def removeBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_blend(const TransformBlendTable self, int n)
        
        /**
         * Removes the blend at the nth position.
         */
        """
        pass

    def remove_blend(self, const_TransformBlendTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_blend(const TransformBlendTable self, int n)
        
        /**
         * Removes the blend at the nth position.
         */
        """
        pass

    def setBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blend(const TransformBlendTable self, int n, const TransformBlend blend)
        
        /**
         * Replaces the blend at the nth position with the indicated value.
         */
        """
        pass

    def setRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rows(const TransformBlendTable self, const SparseArray rows)
        
        /**
         * Specifies the subset of rows (vertices) in the associated GeomVertexData
         * that this TransformBlendTable actually affects.
         */
        """
        pass

    def set_blend(self, const_TransformBlendTable_self, int_n, const_TransformBlend_blend): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blend(const TransformBlendTable self, int n, const TransformBlend blend)
        
        /**
         * Replaces the blend at the nth position with the indicated value.
         */
        """
        pass

    def set_rows(self, const_TransformBlendTable_self, const_SparseArray_rows): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rows(const TransformBlendTable self, const SparseArray rows)
        
        /**
         * Specifies the subset of rows (vertices) in the associated GeomVertexData
         * that this TransformBlendTable actually affects.
         */
        """
        pass

    def write(self, TransformBlendTable_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TransformBlendTable self, ostream out, int indent_level)
        
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    blends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_simultaneous_transforms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_transforms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TransformBlendTable' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TransformBlendTable' objects>"
        '__doc__': '/**\n * This structure collects together the different combinations of transforms\n * and blend amounts used by a GeomVertexData, to facilitate computing dynamic\n * vertices on the CPU at runtime.  Each vertex has a pointer to exactly one\n * of the entries in this table, and each entry defines a number of\n * transform/blend combinations.\n *\n * This structure is used for a GeomVertexData set up to compute its dynamic\n * vertices on the CPU.  See TransformTable for one set up to compute its\n * dynamic vertices on the graphics card.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TransformBlendTable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FBE20>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TransformBlendTable' objects>"
        'addBlend': None, # (!) real value is "<method 'addBlend' of 'panda3d.core.TransformBlendTable' objects>"
        'add_blend': None, # (!) real value is "<method 'add_blend' of 'panda3d.core.TransformBlendTable' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TransformBlendTable' objects>"
        'blends': None, # (!) real value is "<attribute 'blends' of 'panda3d.core.TransformBlendTable' objects>"
        'getBlend': None, # (!) real value is "<method 'getBlend' of 'panda3d.core.TransformBlendTable' objects>"
        'getBlends': None, # (!) real value is "<method 'getBlends' of 'panda3d.core.TransformBlendTable' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FBE20>)>'
        'getMaxSimultaneousTransforms': None, # (!) real value is "<method 'getMaxSimultaneousTransforms' of 'panda3d.core.TransformBlendTable' objects>"
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.TransformBlendTable' objects>"
        'getNumBlends': None, # (!) real value is "<method 'getNumBlends' of 'panda3d.core.TransformBlendTable' objects>"
        'getNumTransforms': None, # (!) real value is "<method 'getNumTransforms' of 'panda3d.core.TransformBlendTable' objects>"
        'getRows': None, # (!) real value is "<method 'getRows' of 'panda3d.core.TransformBlendTable' objects>"
        'get_blend': None, # (!) real value is "<method 'get_blend' of 'panda3d.core.TransformBlendTable' objects>"
        'get_blends': None, # (!) real value is "<method 'get_blends' of 'panda3d.core.TransformBlendTable' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FBE20>)>'
        'get_max_simultaneous_transforms': None, # (!) real value is "<method 'get_max_simultaneous_transforms' of 'panda3d.core.TransformBlendTable' objects>"
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.TransformBlendTable' objects>"
        'get_num_blends': None, # (!) real value is "<method 'get_num_blends' of 'panda3d.core.TransformBlendTable' objects>"
        'get_num_transforms': None, # (!) real value is "<method 'get_num_transforms' of 'panda3d.core.TransformBlendTable' objects>"
        'get_rows': None, # (!) real value is "<method 'get_rows' of 'panda3d.core.TransformBlendTable' objects>"
        'max_simultaneous_transforms': None, # (!) real value is "<attribute 'max_simultaneous_transforms' of 'panda3d.core.TransformBlendTable' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.TransformBlendTable' objects>"
        'modifyRows': None, # (!) real value is "<method 'modifyRows' of 'panda3d.core.TransformBlendTable' objects>"
        'modify_rows': None, # (!) real value is "<method 'modify_rows' of 'panda3d.core.TransformBlendTable' objects>"
        'num_transforms': None, # (!) real value is "<attribute 'num_transforms' of 'panda3d.core.TransformBlendTable' objects>"
        'removeBlend': None, # (!) real value is "<method 'removeBlend' of 'panda3d.core.TransformBlendTable' objects>"
        'remove_blend': None, # (!) real value is "<method 'remove_blend' of 'panda3d.core.TransformBlendTable' objects>"
        'rows': None, # (!) real value is "<attribute 'rows' of 'panda3d.core.TransformBlendTable' objects>"
        'setBlend': None, # (!) real value is "<method 'setBlend' of 'panda3d.core.TransformBlendTable' objects>"
        'setRows': None, # (!) real value is "<method 'setRows' of 'panda3d.core.TransformBlendTable' objects>"
        'set_blend': None, # (!) real value is "<method 'set_blend' of 'panda3d.core.TransformBlendTable' objects>"
        'set_rows': None, # (!) real value is "<method 'set_rows' of 'panda3d.core.TransformBlendTable' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TransformBlendTable' objects>"
    }


