# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class TransformTable(TypedWritableReferenceCount):
    """
    /**
     * Stores the total set of VertexTransforms that the vertices in a particular
     * GeomVertexData object might depend on.
     *
     * This structure is used for a GeomVertexData set up to compute its dynamic
     * vertices on the graphics card.  See TransformBlendTable for one set up to
     * compute its dynamic vertices on the CPU.
     */
    """
    def addTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_transform(const TransformTable self, const VertexTransform transform)
        
        /**
         * Adds a new transform to the table and returns the index number of the new
         * transform.  Only valid for unregistered tables.
         *
         * This does not automatically uniquify the pointer; if the transform is
         * already present in the table, it will be added twice.
         */
        """
        pass

    def add_transform(self, const_TransformTable_self, const_VertexTransform_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_transform(const TransformTable self, const VertexTransform transform)
        
        /**
         * Adds a new transform to the table and returns the index number of the new
         * transform.  Only valid for unregistered tables.
         *
         * This does not automatically uniquify the pointer; if the transform is
         * already present in the table, it will be added twice.
         */
        """
        pass

    def assign(self, const_TransformTable_self, const_TransformTable_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TransformTable self, const TransformTable copy)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(TransformTable self, Thread current_thread)
        
        /**
         * Returns a sequence number that's guaranteed to change at least when any
         * VertexTransforms in the table change.  (However, this is only true for a
         * registered table.  An unregistered table may or may not reflect an update
         * here when a VertexTransform changes.)
         */
        """
        pass

    def getNumTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_transforms(TransformTable self)
        
        /**
         * Returns the number of transforms in the table.
         */
        """
        pass

    def getTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform(TransformTable self, int n)
        
        /**
         * Returns the nth transform in the table.
         */
        """
        pass

    def getTransforms(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_modified(self, TransformTable_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(TransformTable self, Thread current_thread)
        
        /**
         * Returns a sequence number that's guaranteed to change at least when any
         * VertexTransforms in the table change.  (However, this is only true for a
         * registered table.  An unregistered table may or may not reflect an update
         * here when a VertexTransform changes.)
         */
        """
        pass

    def get_num_transforms(self, TransformTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_transforms(TransformTable self)
        
        /**
         * Returns the number of transforms in the table.
         */
        """
        pass

    def get_transform(self, TransformTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform(TransformTable self, int n)
        
        /**
         * Returns the nth transform in the table.
         */
        """
        pass

    def get_transforms(self, *args, **kwargs): # real signature unknown
        pass

    def insertTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_transform(const TransformTable self, int n, const VertexTransform transform)
        
        /**
         * Inserts a new transform to the table at the given index position.  If the
         * index is beyond the end of the table, appends it to the end.  Only valid
         * for unregistered tables.
         *
         * This does not automatically uniquify the pointer; if the transform is
         * already present in the table, it will be added twice.
         */
        """
        pass

    def insert_transform(self, const_TransformTable_self, int_n, const_VertexTransform_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_transform(const TransformTable self, int n, const VertexTransform transform)
        
        /**
         * Inserts a new transform to the table at the given index position.  If the
         * index is beyond the end of the table, appends it to the end.  Only valid
         * for unregistered tables.
         *
         * This does not automatically uniquify the pointer; if the transform is
         * already present in the table, it will be added twice.
         */
        """
        pass

    def isRegistered(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_registered(TransformTable self)
        
        /**
         * Returns true if this table has been registered.  Once it has been
         * registered, the set of transforms in a TransformTable may not be further
         * modified; but it must be registered before it can be assigned to a Geom.
         */
        """
        pass

    def is_registered(self, TransformTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_registered(TransformTable self)
        
        /**
         * Returns true if this table has been registered.  Once it has been
         * registered, the set of transforms in a TransformTable may not be further
         * modified; but it must be registered before it can be assigned to a Geom.
         */
        """
        pass

    def registerTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_table(const TransformTable table)
        
        /**
         * Registers a TransformTable for use.  This is similar to
         * GeomVertexFormat::register_format().  Once registered, a TransformTable may
         * no longer be modified (although the individual VertexTransform objects may
         * modify their reported transforms).
         *
         * This must be called before a table may be used in a Geom.  After this call,
         * you should discard the original pointer you passed in (which may or may not
         * now be invalid) and let its reference count decrement normally; you should
         * use only the returned value from this point on.
         */
        """
        pass

    def register_table(self, const_TransformTable_table): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_table(const TransformTable table)
        
        /**
         * Registers a TransformTable for use.  This is similar to
         * GeomVertexFormat::register_format().  Once registered, a TransformTable may
         * no longer be modified (although the individual VertexTransform objects may
         * modify their reported transforms).
         *
         * This must be called before a table may be used in a Geom.  After this call,
         * you should discard the original pointer you passed in (which may or may not
         * now be invalid) and let its reference count decrement normally; you should
         * use only the returned value from this point on.
         */
        """
        pass

    def removeTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_transform(const TransformTable self, int n)
        
        /**
         * Removes the nth transform.  Only valid for unregistered tables.
         */
        """
        pass

    def remove_transform(self, const_TransformTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_transform(const TransformTable self, int n)
        
        /**
         * Removes the nth transform.  Only valid for unregistered tables.
         */
        """
        pass

    def setTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform(const TransformTable self, int n, const VertexTransform transform)
        
        /**
         * Replaces the nth transform.  Only valid for unregistered tables.
         */
        """
        pass

    def set_transform(self, const_TransformTable_self, int_n, const_VertexTransform_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform(const TransformTable self, int n, const VertexTransform transform)
        
        /**
         * Replaces the nth transform.  Only valid for unregistered tables.
         */
        """
        pass

    def write(self, TransformTable_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TransformTable self, ostream out)
        
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

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    registered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transforms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TransformTable' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TransformTable' objects>"
        '__doc__': '/**\n * Stores the total set of VertexTransforms that the vertices in a particular\n * GeomVertexData object might depend on.\n *\n * This structure is used for a GeomVertexData set up to compute its dynamic\n * vertices on the graphics card.  See TransformBlendTable for one set up to\n * compute its dynamic vertices on the CPU.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TransformTable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FBA80>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TransformTable' objects>"
        'addTransform': None, # (!) real value is "<method 'addTransform' of 'panda3d.core.TransformTable' objects>"
        'add_transform': None, # (!) real value is "<method 'add_transform' of 'panda3d.core.TransformTable' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TransformTable' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FBA80>)>'
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.TransformTable' objects>"
        'getNumTransforms': None, # (!) real value is "<method 'getNumTransforms' of 'panda3d.core.TransformTable' objects>"
        'getTransform': None, # (!) real value is "<method 'getTransform' of 'panda3d.core.TransformTable' objects>"
        'getTransforms': None, # (!) real value is "<method 'getTransforms' of 'panda3d.core.TransformTable' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FBA80>)>'
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.TransformTable' objects>"
        'get_num_transforms': None, # (!) real value is "<method 'get_num_transforms' of 'panda3d.core.TransformTable' objects>"
        'get_transform': None, # (!) real value is "<method 'get_transform' of 'panda3d.core.TransformTable' objects>"
        'get_transforms': None, # (!) real value is "<method 'get_transforms' of 'panda3d.core.TransformTable' objects>"
        'insertTransform': None, # (!) real value is "<method 'insertTransform' of 'panda3d.core.TransformTable' objects>"
        'insert_transform': None, # (!) real value is "<method 'insert_transform' of 'panda3d.core.TransformTable' objects>"
        'isRegistered': None, # (!) real value is "<method 'isRegistered' of 'panda3d.core.TransformTable' objects>"
        'is_registered': None, # (!) real value is "<method 'is_registered' of 'panda3d.core.TransformTable' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.TransformTable' objects>"
        'registerTable': None, # (!) real value is '<staticmethod(<built-in method registerTable of type object at 0x00007FFCFE2FBA80>)>'
        'register_table': None, # (!) real value is '<staticmethod(<built-in method register_table of type object at 0x00007FFCFE2FBA80>)>'
        'registered': None, # (!) real value is "<attribute 'registered' of 'panda3d.core.TransformTable' objects>"
        'removeTransform': None, # (!) real value is "<method 'removeTransform' of 'panda3d.core.TransformTable' objects>"
        'remove_transform': None, # (!) real value is "<method 'remove_transform' of 'panda3d.core.TransformTable' objects>"
        'setTransform': None, # (!) real value is "<method 'setTransform' of 'panda3d.core.TransformTable' objects>"
        'set_transform': None, # (!) real value is "<method 'set_transform' of 'panda3d.core.TransformTable' objects>"
        'transforms': None, # (!) real value is "<attribute 'transforms' of 'panda3d.core.TransformTable' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TransformTable' objects>"
    }


