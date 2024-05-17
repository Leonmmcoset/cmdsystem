# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TransformBlend(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This defines a single entry in a TransformBlendTable.  It represents a
     * unique combination of VertexTransform pointers and blend amounts.
     */
    """
    def addTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_transform(const TransformBlend self, const VertexTransform transform, float weight)
        
        /**
         * Adds a new transform to the blend.  If the transform already existed,
         * increases its weight factor.
         */
        """
        pass

    def add_transform(self, const_TransformBlend_self, const_VertexTransform_transform, float_weight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_transform(const TransformBlend self, const VertexTransform transform, float weight)
        
        /**
         * Adds a new transform to the blend.  If the transform already existed,
         * increases its weight factor.
         */
        """
        pass

    def assign(self, const_TransformBlend_self, const_TransformBlend_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TransformBlend self, const TransformBlend copy)
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(TransformBlend self, const TransformBlend other)
        
        /**
         * Defines an arbitrary ordering for TransformBlend objects.
         */
        """
        pass

    def compare_to(self, TransformBlend_self, const_TransformBlend_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(TransformBlend self, const TransformBlend other)
        
        /**
         * Defines an arbitrary ordering for TransformBlend objects.
         */
        """
        pass

    def getBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blend(TransformBlend self, LMatrix4f result, Thread current_thread)
        
        /**
         * Returns the current value of the blend, based on the current value of all
         * of the nested transform objects and their associated weights.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
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
        get_modified(TransformBlend self, Thread current_thread)
        
        /**
         * Returns a counter which is guaranteed to increment at least as often as the
         * result of get_blend() changes.
         */
        """
        pass

    def getNumTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_transforms(TransformBlend self)
        
        /**
         * Returns the number of transforms stored in the blend object.
         */
        """
        pass

    def getTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform(TransformBlend self, int n)
        
        /**
         * Returns the nth transform stored in the blend object.
         */
        """
        pass

    def getTransforms(self, *args, **kwargs): # real signature unknown
        pass

    def getWeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_weight(TransformBlend self, const VertexTransform transform)
        get_weight(TransformBlend self, int n)
        
        /**
         * Returns the weight associated with the nth transform stored in the blend
         * object.
         */
        
        /**
         * Returns the weight associated with the indicated transform, or 0 if there
         * is no entry for the transform.
         */
        """
        pass

    def get_blend(self, TransformBlend_self, LMatrix4f_result, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blend(TransformBlend self, LMatrix4f result, Thread current_thread)
        
        /**
         * Returns the current value of the blend, based on the current value of all
         * of the nested transform objects and their associated weights.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_modified(self, TransformBlend_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(TransformBlend self, Thread current_thread)
        
        /**
         * Returns a counter which is guaranteed to increment at least as often as the
         * result of get_blend() changes.
         */
        """
        pass

    def get_num_transforms(self, TransformBlend_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_transforms(TransformBlend self)
        
        /**
         * Returns the number of transforms stored in the blend object.
         */
        """
        pass

    def get_transform(self, TransformBlend_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform(TransformBlend self, int n)
        
        /**
         * Returns the nth transform stored in the blend object.
         */
        """
        pass

    def get_transforms(self, *args, **kwargs): # real signature unknown
        pass

    def get_weight(self, TransformBlend_self, const_VertexTransform_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_weight(TransformBlend self, const VertexTransform transform)
        get_weight(TransformBlend self, int n)
        
        /**
         * Returns the weight associated with the nth transform stored in the blend
         * object.
         */
        
        /**
         * Returns the weight associated with the indicated transform, or 0 if there
         * is no entry for the transform.
         */
        """
        pass

    def hasTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_transform(TransformBlend self, const VertexTransform transform)
        
        /**
         * Returns true if the blend has the indicated transform, false otherwise.
         */
        """
        pass

    def has_transform(self, TransformBlend_self, const_VertexTransform_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_transform(TransformBlend self, const VertexTransform transform)
        
        /**
         * Returns true if the blend has the indicated transform, false otherwise.
         */
        """
        pass

    def limitTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        limit_transforms(const TransformBlend self, int max_transforms)
        
        /**
         * If the total number of transforms in the blend exceeds max_transforms,
         * removes the n least-important transforms as needed to reduce the number of
         * transforms to max_transforms.
         */
        """
        pass

    def limit_transforms(self, const_TransformBlend_self, int_max_transforms): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        limit_transforms(const TransformBlend self, int max_transforms)
        
        /**
         * If the total number of transforms in the blend exceeds max_transforms,
         * removes the n least-important transforms as needed to reduce the number of
         * transforms to max_transforms.
         */
        """
        pass

    def normalizeWeights(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        normalize_weights(const TransformBlend self)
        
        /**
         * Rescales all of the weights on the various transforms so that they sum to
         * 1.0.  It is generally a good idea to call this after adding or removing
         * transforms from the blend.
         */
        """
        pass

    def normalize_weights(self, const_TransformBlend_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalize_weights(const TransformBlend self)
        
        /**
         * Rescales all of the weights on the various transforms so that they sum to
         * 1.0.  It is generally a good idea to call this after adding or removing
         * transforms from the blend.
         */
        """
        pass

    def output(self, TransformBlend_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(TransformBlend self, ostream out)
        
        /**
         *
         */
        """
        pass

    def removeTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_transform(const TransformBlend self, const VertexTransform transform)
        remove_transform(const TransformBlend self, int n)
        
        /**
         * Removes the nth transform stored in the blend object.
         */
        
        /**
         * Removes the indicated transform from the blend.
         */
        """
        pass

    def remove_transform(self, const_TransformBlend_self, const_VertexTransform_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_transform(const TransformBlend self, const VertexTransform transform)
        remove_transform(const TransformBlend self, int n)
        
        /**
         * Removes the nth transform stored in the blend object.
         */
        
        /**
         * Removes the indicated transform from the blend.
         */
        """
        pass

    def setTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform(const TransformBlend self, int n, const VertexTransform transform)
        
        /**
         * Replaces the nth transform stored in the blend object.
         */
        """
        pass

    def setWeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_weight(const TransformBlend self, int n, float weight)
        
        /**
         * Replaces the weight associated with the nth transform stored in the blend
         * object.
         */
        """
        pass

    def set_transform(self, const_TransformBlend_self, int_n, const_VertexTransform_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform(const TransformBlend self, int n, const VertexTransform transform)
        
        /**
         * Replaces the nth transform stored in the blend object.
         */
        """
        pass

    def set_weight(self, const_TransformBlend_self, int_n, float_weight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_weight(const TransformBlend self, int n, float weight)
        
        /**
         * Replaces the weight associated with the nth transform stored in the blend
         * object.
         */
        """
        pass

    def transformPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        transform_point(TransformBlend self, LPoint3d point, Thread current_thread)
        transform_point(TransformBlend self, LPoint3f point, Thread current_thread)
        transform_point(TransformBlend self, LPoint4f point, Thread current_thread)
        transform_point(TransformBlend self, LPoint4d point, Thread current_thread)
        
        /**
         * Transforms the indicated point by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        
        /**
         * Transforms the indicated point by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        
        /**
         * Transforms the indicated point by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        
        /**
         * Transforms the indicated point by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        """
        pass

    def transformVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        transform_vector(TransformBlend self, LVector3f point, Thread current_thread)
        transform_vector(TransformBlend self, LVector3d point, Thread current_thread)
        
        /**
         * Transforms the indicated vector by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        
        /**
         * Transforms the indicated vector by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        """
        pass

    def transform_point(self, TransformBlend_self, LPoint3d_point, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform_point(TransformBlend self, LPoint3d point, Thread current_thread)
        transform_point(TransformBlend self, LPoint3f point, Thread current_thread)
        transform_point(TransformBlend self, LPoint4f point, Thread current_thread)
        transform_point(TransformBlend self, LPoint4d point, Thread current_thread)
        
        /**
         * Transforms the indicated point by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        
        /**
         * Transforms the indicated point by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        
        /**
         * Transforms the indicated point by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        
        /**
         * Transforms the indicated point by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        """
        pass

    def transform_vector(self, TransformBlend_self, LVector3f_point, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform_vector(TransformBlend self, LVector3f point, Thread current_thread)
        transform_vector(TransformBlend self, LVector3d point, Thread current_thread)
        
        /**
         * Transforms the indicated vector by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        
        /**
         * Transforms the indicated vector by the blend matrix.
         *
         * You should call update_blend() to ensure that the cache is up-to-date
         * before calling this.
         */
        """
        pass

    def updateBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_blend(TransformBlend self, Thread current_thread)
        
        /**
         * Recomputes the internal representation of the blend value, if necessary.
         * You should call this before calling get_blend() or transform_point().
         */
        """
        pass

    def update_blend(self, TransformBlend_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_blend(TransformBlend self, Thread current_thread)
        
        /**
         * Recomputes the internal representation of the blend value, if necessary.
         * You should call this before calling get_blend() or transform_point().
         */
        """
        pass

    def write(self, TransformBlend_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TransformBlend self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transforms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TransformBlend' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TransformBlend' objects>"
        '__doc__': '/**\n * This defines a single entry in a TransformBlendTable.  It represents a\n * unique combination of VertexTransform pointers and blend amounts.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.TransformBlend' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.TransformBlend' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.TransformBlend' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.TransformBlend' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TransformBlend' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.TransformBlend' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.TransformBlend' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.TransformBlend' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FBC50>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.TransformBlend' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TransformBlend' objects>"
        'addTransform': None, # (!) real value is "<method 'addTransform' of 'panda3d.core.TransformBlend' objects>"
        'add_transform': None, # (!) real value is "<method 'add_transform' of 'panda3d.core.TransformBlend' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TransformBlend' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.TransformBlend' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.TransformBlend' objects>"
        'getBlend': None, # (!) real value is "<method 'getBlend' of 'panda3d.core.TransformBlend' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FBC50>)>'
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.TransformBlend' objects>"
        'getNumTransforms': None, # (!) real value is "<method 'getNumTransforms' of 'panda3d.core.TransformBlend' objects>"
        'getTransform': None, # (!) real value is "<method 'getTransform' of 'panda3d.core.TransformBlend' objects>"
        'getTransforms': None, # (!) real value is "<method 'getTransforms' of 'panda3d.core.TransformBlend' objects>"
        'getWeight': None, # (!) real value is "<method 'getWeight' of 'panda3d.core.TransformBlend' objects>"
        'get_blend': None, # (!) real value is "<method 'get_blend' of 'panda3d.core.TransformBlend' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FBC50>)>'
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.TransformBlend' objects>"
        'get_num_transforms': None, # (!) real value is "<method 'get_num_transforms' of 'panda3d.core.TransformBlend' objects>"
        'get_transform': None, # (!) real value is "<method 'get_transform' of 'panda3d.core.TransformBlend' objects>"
        'get_transforms': None, # (!) real value is "<method 'get_transforms' of 'panda3d.core.TransformBlend' objects>"
        'get_weight': None, # (!) real value is "<method 'get_weight' of 'panda3d.core.TransformBlend' objects>"
        'hasTransform': None, # (!) real value is "<method 'hasTransform' of 'panda3d.core.TransformBlend' objects>"
        'has_transform': None, # (!) real value is "<method 'has_transform' of 'panda3d.core.TransformBlend' objects>"
        'limitTransforms': None, # (!) real value is "<method 'limitTransforms' of 'panda3d.core.TransformBlend' objects>"
        'limit_transforms': None, # (!) real value is "<method 'limit_transforms' of 'panda3d.core.TransformBlend' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.TransformBlend' objects>"
        'normalizeWeights': None, # (!) real value is "<method 'normalizeWeights' of 'panda3d.core.TransformBlend' objects>"
        'normalize_weights': None, # (!) real value is "<method 'normalize_weights' of 'panda3d.core.TransformBlend' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.TransformBlend' objects>"
        'removeTransform': None, # (!) real value is "<method 'removeTransform' of 'panda3d.core.TransformBlend' objects>"
        'remove_transform': None, # (!) real value is "<method 'remove_transform' of 'panda3d.core.TransformBlend' objects>"
        'setTransform': None, # (!) real value is "<method 'setTransform' of 'panda3d.core.TransformBlend' objects>"
        'setWeight': None, # (!) real value is "<method 'setWeight' of 'panda3d.core.TransformBlend' objects>"
        'set_transform': None, # (!) real value is "<method 'set_transform' of 'panda3d.core.TransformBlend' objects>"
        'set_weight': None, # (!) real value is "<method 'set_weight' of 'panda3d.core.TransformBlend' objects>"
        'transformPoint': None, # (!) real value is "<method 'transformPoint' of 'panda3d.core.TransformBlend' objects>"
        'transformVector': None, # (!) real value is "<method 'transformVector' of 'panda3d.core.TransformBlend' objects>"
        'transform_point': None, # (!) real value is "<method 'transform_point' of 'panda3d.core.TransformBlend' objects>"
        'transform_vector': None, # (!) real value is "<method 'transform_vector' of 'panda3d.core.TransformBlend' objects>"
        'transforms': None, # (!) real value is "<attribute 'transforms' of 'panda3d.core.TransformBlend' objects>"
        'updateBlend': None, # (!) real value is "<method 'updateBlend' of 'panda3d.core.TransformBlend' objects>"
        'update_blend': None, # (!) real value is "<method 'update_blend' of 'panda3d.core.TransformBlend' objects>"
        'weights': None, # (!) real value is "<attribute 'weights' of 'panda3d.core.TransformBlend' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TransformBlend' objects>"
    }


