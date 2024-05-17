# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ModelNode import ModelNode

class ModelRoot(ModelNode):
    """
    /**
     * A node of this type is created automatically at the root of each model file
     * that is loaded.  It may eventually contain some information about the
     * contents of the model; at the moment, it contains no special information,
     * but can be used as a flag to indicate the presence of a loaded model file.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullpath(ModelRoot self)
        
        /**
         * Returns the full pathname of the model represented by this node, as found
         * on disk.  This is mainly useful for reference purposes, but is also used to
         * index the ModelRoot into the ModelPool.
         */
        """
        pass

    def getModelRefCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_model_ref_count(ModelRoot self)
        
        /**
         * Returns the number of copies that exist of this particular ModelRoot node.
         * Each time ModelRoot::copy_subgraph() or make_copy() is called (or some
         * other copying mechanism, such as NodePath.copy_to(), is used), this count
         * will increment by one in all copies; when one of the copies is destructed,
         * this count will decrement.
         */
        """
        pass

    def getReference(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reference(ModelRoot self)
        
        /**
         * Returns the pointer that represents the object shared between all copies of
         * this ModelRoot.  Since there's not much associated with this object other
         * than a reference count, normally there's not much reason to get the pointer
         * (though it may be compared pointerwise with other ModelRoot objects).
         */
        """
        pass

    def getTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_timestamp(ModelRoot self)
        
        /**
         * Returns the timestamp of the file on disk that was read for this model, at
         * the time it was read, if it is known.  Returns 0 if the timestamp is not
         * known or could not be provided.  This can be used as a quick (but fallible)
         * check to verify whether the file might have changed since the model was
         * read.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_fullpath(self, ModelRoot_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullpath(ModelRoot self)
        
        /**
         * Returns the full pathname of the model represented by this node, as found
         * on disk.  This is mainly useful for reference purposes, but is also used to
         * index the ModelRoot into the ModelPool.
         */
        """
        pass

    def get_model_ref_count(self, ModelRoot_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_model_ref_count(ModelRoot self)
        
        /**
         * Returns the number of copies that exist of this particular ModelRoot node.
         * Each time ModelRoot::copy_subgraph() or make_copy() is called (or some
         * other copying mechanism, such as NodePath.copy_to(), is used), this count
         * will increment by one in all copies; when one of the copies is destructed,
         * this count will decrement.
         */
        """
        pass

    def get_reference(self, ModelRoot_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reference(ModelRoot self)
        
        /**
         * Returns the pointer that represents the object shared between all copies of
         * this ModelRoot.  Since there's not much associated with this object other
         * than a reference count, normally there's not much reason to get the pointer
         * (though it may be compared pointerwise with other ModelRoot objects).
         */
        """
        pass

    def get_timestamp(self, ModelRoot_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_timestamp(ModelRoot self)
        
        /**
         * Returns the timestamp of the file on disk that was read for this model, at
         * the time it was read, if it is known.  Returns 0 if the timestamp is not
         * known or could not be provided.  This can be used as a quick (but fallible)
         * check to verify whether the file might have changed since the model was
         * read.
         */
        """
        pass

    def setFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fullpath(const ModelRoot self, const Filename fullpath)
        
        /**
         * Sets the full pathname of the model represented by this node, as found on
         * disk.  This is mainly useful for reference purposes, but is also used to
         * index the ModelRoot into the ModelPool.
         *
         * This is normally set automatically when a model is loaded, and should not
         * be set directly by the user.  If you change this on a loaded model, then
         * ModelPool::release_model() may fail.
         */
        """
        pass

    def setReference(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_reference(const ModelRoot self, ModelReference ref)
        
        /**
         * Changes the pointer that represents the object shared between all copies of
         * this ModelRoot.  This will disassociate this ModelRoot from all of its
         * copies.  Normally, there's no reason to do this.
         */
        """
        pass

    def setTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_timestamp(const ModelRoot self, int timestamp)
        
        /**
         * Sets the timestamp of the file on disk that was read for this model.  This
         * is normally set automatically when a model is loaded, and should not be set
         * directly by the user.
         */
        """
        pass

    def set_fullpath(self, const_ModelRoot_self, const_Filename_fullpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fullpath(const ModelRoot self, const Filename fullpath)
        
        /**
         * Sets the full pathname of the model represented by this node, as found on
         * disk.  This is mainly useful for reference purposes, but is also used to
         * index the ModelRoot into the ModelPool.
         *
         * This is normally set automatically when a model is loaded, and should not
         * be set directly by the user.  If you change this on a loaded model, then
         * ModelPool::release_model() may fail.
         */
        """
        pass

    def set_reference(self, const_ModelRoot_self, ModelReference_ref): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_reference(const ModelRoot self, ModelReference ref)
        
        /**
         * Changes the pointer that represents the object shared between all copies of
         * this ModelRoot.  This will disassociate this ModelRoot from all of its
         * copies.  Normally, there's no reason to do this.
         */
        """
        pass

    def set_timestamp(self, const_ModelRoot_self, int_timestamp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_timestamp(const ModelRoot self, int timestamp)
        
        /**
         * Sets the timestamp of the file on disk that was read for this model.  This
         * is normally set automatically when a model is loaded, and should not be set
         * directly by the user.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    fullpath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model_ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'ModelReference': None, # (!) real value is "<class 'panda3d.core.ModelReference'>"
        '__doc__': '/**\n * A node of this type is created automatically at the root of each model file\n * that is loaded.  It may eventually contain some information about the\n * contents of the model; at the moment, it contains no special information,\n * but can be used as a flag to indicate the presence of a loaded model file.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ModelRoot' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE298FA0>'
        'fullpath': None, # (!) real value is "<attribute 'fullpath' of 'panda3d.core.ModelRoot' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE298FA0>)>'
        'getFullpath': None, # (!) real value is "<method 'getFullpath' of 'panda3d.core.ModelRoot' objects>"
        'getModelRefCount': None, # (!) real value is "<method 'getModelRefCount' of 'panda3d.core.ModelRoot' objects>"
        'getReference': None, # (!) real value is "<method 'getReference' of 'panda3d.core.ModelRoot' objects>"
        'getTimestamp': None, # (!) real value is "<method 'getTimestamp' of 'panda3d.core.ModelRoot' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE298FA0>)>'
        'get_fullpath': None, # (!) real value is "<method 'get_fullpath' of 'panda3d.core.ModelRoot' objects>"
        'get_model_ref_count': None, # (!) real value is "<method 'get_model_ref_count' of 'panda3d.core.ModelRoot' objects>"
        'get_reference': None, # (!) real value is "<method 'get_reference' of 'panda3d.core.ModelRoot' objects>"
        'get_timestamp': None, # (!) real value is "<method 'get_timestamp' of 'panda3d.core.ModelRoot' objects>"
        'model_ref_count': None, # (!) real value is "<attribute 'model_ref_count' of 'panda3d.core.ModelRoot' objects>"
        'reference': None, # (!) real value is "<attribute 'reference' of 'panda3d.core.ModelRoot' objects>"
        'setFullpath': None, # (!) real value is "<method 'setFullpath' of 'panda3d.core.ModelRoot' objects>"
        'setReference': None, # (!) real value is "<method 'setReference' of 'panda3d.core.ModelRoot' objects>"
        'setTimestamp': None, # (!) real value is "<method 'setTimestamp' of 'panda3d.core.ModelRoot' objects>"
        'set_fullpath': None, # (!) real value is "<method 'set_fullpath' of 'panda3d.core.ModelRoot' objects>"
        'set_reference': None, # (!) real value is "<method 'set_reference' of 'panda3d.core.ModelRoot' objects>"
        'set_timestamp': None, # (!) real value is "<method 'set_timestamp' of 'panda3d.core.ModelRoot' objects>"
        'timestamp': None, # (!) real value is "<attribute 'timestamp' of 'panda3d.core.ModelRoot' objects>"
    }
    ModelReference = None # (!) real value is "<class 'panda3d.core.ModelReference'>"


