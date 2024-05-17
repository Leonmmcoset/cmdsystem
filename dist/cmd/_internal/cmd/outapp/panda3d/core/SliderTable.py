# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class SliderTable(TypedWritableReferenceCount):
    """
    /**
     * Stores the total set of VertexSliders that the vertices in a particular
     * GeomVertexData object might depend on.
     *
     * This is similar to a TransformTable, but it stores VertexSliders instead of
     * VertexTransforms, and it stores them by name instead of by index number.
     * Also, it is only used when animating vertices on the CPU, since GPU's don't
     * support morphs at this point in time.
     */
    """
    def addSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_slider(const SliderTable self, const VertexSlider slider, const SparseArray rows)
        
        /**
         * Adds a new slider to the table, and returns the index number of the new
         * slider.  Only valid for unregistered tables.
         */
        """
        pass

    def add_slider(self, const_SliderTable_self, const_VertexSlider_slider, const_SparseArray_rows): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_slider(const SliderTable self, const VertexSlider slider, const SparseArray rows)
        
        /**
         * Adds a new slider to the table, and returns the index number of the new
         * slider.  Only valid for unregistered tables.
         */
        """
        pass

    def assign(self, const_SliderTable_self, const_SliderTable_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const SliderTable self, const SliderTable copy)
        """
        pass

    def findSliders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_sliders(SliderTable self, const InternalName name)
        
        /**
         * Returns a list of slider indices that represent the list of sliders with
         * the indicated name, or an empty SparseArray if no slider in the table has
         * that name.
         */
        """
        pass

    def find_sliders(self, SliderTable_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_sliders(SliderTable self, const InternalName name)
        
        /**
         * Returns a list of slider indices that represent the list of sliders with
         * the indicated name, or an empty SparseArray if no slider in the table has
         * that name.
         */
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
        get_modified(SliderTable self, Thread current_thread)
        
        /**
         * Returns a sequence number that's guaranteed to change at least when any
         * VertexSliders in the table change.  (However, this is only true for a
         * registered table.  An unregistered table may or may not reflect an update
         * here when a VertexSlider changes.)
         */
        """
        pass

    def getNumSliders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_sliders(SliderTable self)
        
        /**
         * Returns the number of sliders in the table.
         */
        """
        pass

    def getSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slider(SliderTable self, int n)
        
        /**
         * Returns the nth slider in the table.
         */
        """
        pass

    def getSliderRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slider_rows(SliderTable self, int n)
        
        /**
         * Returns the set of rows (vertices) governed by the nth slider in the table.
         */
        """
        pass

    def getSliders(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_modified(self, SliderTable_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(SliderTable self, Thread current_thread)
        
        /**
         * Returns a sequence number that's guaranteed to change at least when any
         * VertexSliders in the table change.  (However, this is only true for a
         * registered table.  An unregistered table may or may not reflect an update
         * here when a VertexSlider changes.)
         */
        """
        pass

    def get_num_sliders(self, SliderTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_sliders(SliderTable self)
        
        /**
         * Returns the number of sliders in the table.
         */
        """
        pass

    def get_slider(self, SliderTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slider(SliderTable self, int n)
        
        /**
         * Returns the nth slider in the table.
         */
        """
        pass

    def get_sliders(self, *args, **kwargs): # real signature unknown
        pass

    def get_slider_rows(self, SliderTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slider_rows(SliderTable self, int n)
        
        /**
         * Returns the set of rows (vertices) governed by the nth slider in the table.
         */
        """
        pass

    def hasSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_slider(SliderTable self, const InternalName name)
        
        /**
         * Returns true if the table has at least one slider by the indicated name,
         * false otherwise.
         */
        """
        pass

    def has_slider(self, SliderTable_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_slider(SliderTable self, const InternalName name)
        
        /**
         * Returns true if the table has at least one slider by the indicated name,
         * false otherwise.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(SliderTable self)
        
        /**
         * Returns true if the table has no sliders, false if it has at least one.
         */
        """
        pass

    def isRegistered(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_registered(SliderTable self)
        
        /**
         * Returns true if this table has been registered.  Once it has been
         * registered, the set of sliders in a SliderTable may not be further
         * modified; but it must be registered before it can be assigned to a Geom.
         */
        """
        pass

    def is_empty(self, SliderTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(SliderTable self)
        
        /**
         * Returns true if the table has no sliders, false if it has at least one.
         */
        """
        pass

    def is_registered(self, SliderTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_registered(SliderTable self)
        
        /**
         * Returns true if this table has been registered.  Once it has been
         * registered, the set of sliders in a SliderTable may not be further
         * modified; but it must be registered before it can be assigned to a Geom.
         */
        """
        pass

    def registerTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_table(const SliderTable table)
        
        /**
         * Registers a SliderTable for use.  This is similar to
         * GeomVertexFormat::register_format().  Once registered, a SliderTable may no
         * longer be modified (although the individual VertexSlider objects may modify
         * their reported sliders).
         *
         * This must be called before a table may be used in a Geom.  After this call,
         * you should discard the original pointer you passed in (which may or may not
         * now be invalid) and let its reference count decrement normally; you should
         * use only the returned value from this point on.
         */
        """
        pass

    def register_table(self, const_SliderTable_table): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_table(const SliderTable table)
        
        /**
         * Registers a SliderTable for use.  This is similar to
         * GeomVertexFormat::register_format().  Once registered, a SliderTable may no
         * longer be modified (although the individual VertexSlider objects may modify
         * their reported sliders).
         *
         * This must be called before a table may be used in a Geom.  After this call,
         * you should discard the original pointer you passed in (which may or may not
         * now be invalid) and let its reference count decrement normally; you should
         * use only the returned value from this point on.
         */
        """
        pass

    def removeSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_slider(const SliderTable self, int n)
        
        /**
         * Removes the nth slider.  Only valid for unregistered tables.
         */
        """
        pass

    def remove_slider(self, const_SliderTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_slider(const SliderTable self, int n)
        
        /**
         * Removes the nth slider.  Only valid for unregistered tables.
         */
        """
        pass

    def setSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_slider(const SliderTable self, int n, const VertexSlider slider)
        
        /**
         * Replaces the nth slider.  Only valid for unregistered tables.
         */
        """
        pass

    def setSliderRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_slider_rows(const SliderTable self, int n, const SparseArray rows)
        
        /**
         * Replaces the rows affected by the nth slider.  Only valid for unregistered
         * tables.
         */
        """
        pass

    def set_slider(self, const_SliderTable_self, int_n, const_VertexSlider_slider): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_slider(const SliderTable self, int n, const VertexSlider slider)
        
        /**
         * Replaces the nth slider.  Only valid for unregistered tables.
         */
        """
        pass

    def set_slider_rows(self, const_SliderTable_self, int_n, const_SparseArray_rows): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_slider_rows(const SliderTable self, int n, const SparseArray rows)
        
        /**
         * Replaces the rows affected by the nth slider.  Only valid for unregistered
         * tables.
         */
        """
        pass

    def write(self, SliderTable_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(SliderTable self, ostream out)
        
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


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.SliderTable' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.SliderTable' objects>"
        '__doc__': "/**\n * Stores the total set of VertexSliders that the vertices in a particular\n * GeomVertexData object might depend on.\n *\n * This is similar to a TransformTable, but it stores VertexSliders instead of\n * VertexTransforms, and it stores them by name instead of by index number.\n * Also, it is only used when animating vertices on the CPU, since GPU's don't\n * support morphs at this point in time.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SliderTable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FC1C0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.SliderTable' objects>"
        'addSlider': None, # (!) real value is "<method 'addSlider' of 'panda3d.core.SliderTable' objects>"
        'add_slider': None, # (!) real value is "<method 'add_slider' of 'panda3d.core.SliderTable' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.SliderTable' objects>"
        'findSliders': None, # (!) real value is "<method 'findSliders' of 'panda3d.core.SliderTable' objects>"
        'find_sliders': None, # (!) real value is "<method 'find_sliders' of 'panda3d.core.SliderTable' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FC1C0>)>'
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.SliderTable' objects>"
        'getNumSliders': None, # (!) real value is "<method 'getNumSliders' of 'panda3d.core.SliderTable' objects>"
        'getSlider': None, # (!) real value is "<method 'getSlider' of 'panda3d.core.SliderTable' objects>"
        'getSliderRows': None, # (!) real value is "<method 'getSliderRows' of 'panda3d.core.SliderTable' objects>"
        'getSliders': None, # (!) real value is "<method 'getSliders' of 'panda3d.core.SliderTable' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FC1C0>)>'
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.SliderTable' objects>"
        'get_num_sliders': None, # (!) real value is "<method 'get_num_sliders' of 'panda3d.core.SliderTable' objects>"
        'get_slider': None, # (!) real value is "<method 'get_slider' of 'panda3d.core.SliderTable' objects>"
        'get_slider_rows': None, # (!) real value is "<method 'get_slider_rows' of 'panda3d.core.SliderTable' objects>"
        'get_sliders': None, # (!) real value is "<method 'get_sliders' of 'panda3d.core.SliderTable' objects>"
        'hasSlider': None, # (!) real value is "<method 'hasSlider' of 'panda3d.core.SliderTable' objects>"
        'has_slider': None, # (!) real value is "<method 'has_slider' of 'panda3d.core.SliderTable' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.SliderTable' objects>"
        'isRegistered': None, # (!) real value is "<method 'isRegistered' of 'panda3d.core.SliderTable' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.SliderTable' objects>"
        'is_registered': None, # (!) real value is "<method 'is_registered' of 'panda3d.core.SliderTable' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.SliderTable' objects>"
        'registerTable': None, # (!) real value is '<staticmethod(<built-in method registerTable of type object at 0x00007FFCFE2FC1C0>)>'
        'register_table': None, # (!) real value is '<staticmethod(<built-in method register_table of type object at 0x00007FFCFE2FC1C0>)>'
        'removeSlider': None, # (!) real value is "<method 'removeSlider' of 'panda3d.core.SliderTable' objects>"
        'remove_slider': None, # (!) real value is "<method 'remove_slider' of 'panda3d.core.SliderTable' objects>"
        'setSlider': None, # (!) real value is "<method 'setSlider' of 'panda3d.core.SliderTable' objects>"
        'setSliderRows': None, # (!) real value is "<method 'setSliderRows' of 'panda3d.core.SliderTable' objects>"
        'set_slider': None, # (!) real value is "<method 'set_slider' of 'panda3d.core.SliderTable' objects>"
        'set_slider_rows': None, # (!) real value is "<method 'set_slider_rows' of 'panda3d.core.SliderTable' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.SliderTable' objects>"
    }


