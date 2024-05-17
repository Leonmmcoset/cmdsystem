# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PartBundleNode import PartBundleNode

class Character(PartBundleNode):
    """
    /**
     * An animated character, with skeleton-morph animation and either soft-
     * skinned or hard-skinned vertices.
     */
    """
    def clearLodAnimation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_lod_animation(const Character self)
        
        /**
         * Undoes the effect of a recent call to set_lod_animation().  Henceforth, the
         * character will animate every frame, regardless of its distance from the
         * camera.
         */
        """
        pass

    def clear_lod_animation(self, const_Character_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_lod_animation(const Character self)
        
        /**
         * Undoes the effect of a recent call to set_lod_animation().  Henceforth, the
         * character will animate every frame, regardless of its distance from the
         * camera.
         */
        """
        pass

    def findJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_joint(Character self, str name)
        
        /**
         * Returns a pointer to the joint with the given name, if there is such a
         * joint, or NULL if there is no such joint.  This will not return a pointer
         * to a slider.
         */
        """
        pass

    def findSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_slider(Character self, str name)
        
        /**
         * Returns a pointer to the slider with the given name, if there is such a
         * slider, or NULL if there is no such slider.  This will not return a pointer
         * to a joint.
         */
        """
        pass

    def find_joint(self, Character_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_joint(Character self, str name)
        
        /**
         * Returns a pointer to the joint with the given name, if there is such a
         * joint, or NULL if there is no such joint.  This will not return a pointer
         * to a slider.
         */
        """
        pass

    def find_slider(self, Character_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_slider(Character self, str name)
        
        /**
         * Returns a pointer to the slider with the given name, if there is such a
         * slider, or NULL if there is no such slider.  This will not return a pointer
         * to a joint.
         */
        """
        pass

    def forceUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        force_update(const Character self)
        
        /**
         * Recalculates the character even if we think it doesn't need it.
         */
        """
        pass

    def force_update(self, const_Character_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        force_update(const Character self)
        
        /**
         * Recalculates the character even if we think it doesn't need it.
         */
        """
        pass

    def getBundle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bundle(Character self, int i)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_bundle(self, Character_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bundle(Character self, int i)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def mergeBundles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        merge_bundles(const Character self, PartBundle old_bundle, PartBundle other_bundle)
        
        /**
         * Merges old_bundle with new_bundle.  old_bundle must be one of the
         * PartBundles within this node.  At the end of this call, the old_bundle
         * pointer within this node will be replaced with the new_bundle pointer, and
         * all geometry within this node will be updated to reference new_bundle.
         *
         * @deprecated Use the newer version of this method, below.
         */
        
        /**
         * Merges old_bundle_handle->get_bundle() with new_bundle.  old_bundle_handle
         * must be one of the PartBundleHandle within this node.  At the end of this
         * call, the bundle pointer within the old_bundle_handle will be replaced with
         * that within the new_bundle_handle pointer, and all geometry within this
         * node will be updated to reference new_bundle.
         *
         * Normally, this is called when the two bundles have the same, or nearly the
         * same, hierarchies.  In this case, new_bundle will simply be assigned over
         * the old_bundle position.  However, if any joints are present in one bundle
         * or the other, new_bundle will be modified to contain the union of all
         * joints.
         *
         * The geometry below this node is also updated to reference new_bundle,
         * instead of the original old_bundle.
         *
         * This method is intended to unify two different models that share a common
         * skeleton, for instance, different LOD's of the same model.
         */
        """
        pass

    def merge_bundles(self, const_Character_self, PartBundle_old_bundle, PartBundle_other_bundle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        merge_bundles(const Character self, PartBundle old_bundle, PartBundle other_bundle)
        
        /**
         * Merges old_bundle with new_bundle.  old_bundle must be one of the
         * PartBundles within this node.  At the end of this call, the old_bundle
         * pointer within this node will be replaced with the new_bundle pointer, and
         * all geometry within this node will be updated to reference new_bundle.
         *
         * @deprecated Use the newer version of this method, below.
         */
        
        /**
         * Merges old_bundle_handle->get_bundle() with new_bundle.  old_bundle_handle
         * must be one of the PartBundleHandle within this node.  At the end of this
         * call, the bundle pointer within the old_bundle_handle will be replaced with
         * that within the new_bundle_handle pointer, and all geometry within this
         * node will be updated to reference new_bundle.
         *
         * Normally, this is called when the two bundles have the same, or nearly the
         * same, hierarchies.  In this case, new_bundle will simply be assigned over
         * the old_bundle position.  However, if any joints are present in one bundle
         * or the other, new_bundle will be modified to contain the union of all
         * joints.
         *
         * The geometry below this node is also updated to reference new_bundle,
         * instead of the original old_bundle.
         *
         * This method is intended to unify two different models that share a common
         * skeleton, for instance, different LOD's of the same model.
         */
        """
        pass

    def setLodAnimation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lod_animation(const Character self, const LPoint3f center, float far_distance, float near_distance, float delay_factor)
        
        /**
         * Activates a special mode in which the character animates less frequently as
         * it gets further from the camera.  This is intended as a simple optimization
         * to minimize the effort of computing animation for lots of characters that
         * may not necessarily be very important to animate every frame.
         *
         * If the character is closer to the camera than near_distance, then it is
         * animated its normal rate, every frame.  If the character is exactly
         * far_distance away, it is animated only every delay_factor seconds (which
         * should be a number greater than 0).  If the character is between
         * near_distance and far_distance, its animation rate is linearly interpolated
         * according to its distance between the two.  The interpolation function
         * continues beyond far_distance, so that the character is animated
         * increasingly less frequently as it gets farther away.
         *
         * The distance calculations are made from center, which is a fixed point
         * relative to the character node, to the camera's lod center or cull center
         * node (or to the camera node itself).
         *
         * If multiple cameras are viewing the character in any given frame, the
         * closest one counts.
         */
        """
        pass

    def set_lod_animation(self, const_Character_self, const_LPoint3f_center, float_far_distance, float_near_distance, float_delay_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lod_animation(const Character self, const LPoint3f center, float far_distance, float near_distance, float delay_factor)
        
        /**
         * Activates a special mode in which the character animates less frequently as
         * it gets further from the camera.  This is intended as a simple optimization
         * to minimize the effort of computing animation for lots of characters that
         * may not necessarily be very important to animate every frame.
         *
         * If the character is closer to the camera than near_distance, then it is
         * animated its normal rate, every frame.  If the character is exactly
         * far_distance away, it is animated only every delay_factor seconds (which
         * should be a number greater than 0).  If the character is between
         * near_distance and far_distance, its animation rate is linearly interpolated
         * according to its distance between the two.  The interpolation function
         * continues beyond far_distance, so that the character is animated
         * increasingly less frequently as it gets farther away.
         *
         * The distance calculations are made from center, which is a fixed point
         * relative to the character node, to the camera's lod center or cull center
         * node (or to the camera node itself).
         *
         * If multiple cameras are viewing the character in any given frame, the
         * closest one counts.
         */
        """
        pass

    def update(self, const_Character_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const Character self)
        
        /**
         * Recalculates the Character's joints and vertices for the current frame.
         * Normally this is performed automatically during the render and need not be
         * called explicitly.
         */
        """
        pass

    def updateToNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_to_now(const Character self)
        
        /**
         * Advances the character's frame to the current time, and then calls
         * update().  This can be used by show code to force an update of the
         * character's position to the current frame, regardless of whether the
         * character is currently onscreen and animating.
         *
         * @deprecated Call update() instead.
         */
        """
        pass

    def update_to_now(self, const_Character_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_to_now(const Character self)
        
        /**
         * Advances the character's frame to the current time, and then calls
         * update().  This can be used by show code to force an update of the
         * character's position to the current frame, regardless of whether the
         * character is currently onscreen and animating.
         *
         * @deprecated Call update() instead.
         */
        """
        pass

    def writeParts(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_parts(Character self, ostream out)
        
        /**
         * Writes a list of the Character's joints and sliders, in their hierchical
         * structure, to the indicated output stream.
         */
        """
        pass

    def writePartValues(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_part_values(Character self, ostream out)
        
        /**
         * Writes a list of the Character's joints and sliders, along with each
         * current position, in their hierchical structure, to the indicated output
         * stream.
         */
        """
        pass

    def write_parts(self, Character_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_parts(Character self, ostream out)
        
        /**
         * Writes a list of the Character's joints and sliders, in their hierchical
         * structure, to the indicated output stream.
         */
        """
        pass

    def write_part_values(self, Character_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_part_values(Character self, ostream out)
        
        /**
         * Writes a list of the Character's joints and sliders, along with each
         * current position, in their hierchical structure, to the indicated output
         * stream.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Character' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Character' objects>"
        '__doc__': '/**\n * An animated character, with skeleton-morph animation and either soft-\n * skinned or hard-skinned vertices.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Character' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CB430>'
        'clearLodAnimation': None, # (!) real value is "<method 'clearLodAnimation' of 'panda3d.core.Character' objects>"
        'clear_lod_animation': None, # (!) real value is "<method 'clear_lod_animation' of 'panda3d.core.Character' objects>"
        'findJoint': None, # (!) real value is "<method 'findJoint' of 'panda3d.core.Character' objects>"
        'findSlider': None, # (!) real value is "<method 'findSlider' of 'panda3d.core.Character' objects>"
        'find_joint': None, # (!) real value is "<method 'find_joint' of 'panda3d.core.Character' objects>"
        'find_slider': None, # (!) real value is "<method 'find_slider' of 'panda3d.core.Character' objects>"
        'forceUpdate': None, # (!) real value is "<method 'forceUpdate' of 'panda3d.core.Character' objects>"
        'force_update': None, # (!) real value is "<method 'force_update' of 'panda3d.core.Character' objects>"
        'getBundle': None, # (!) real value is "<method 'getBundle' of 'panda3d.core.Character' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CB430>)>'
        'get_bundle': None, # (!) real value is "<method 'get_bundle' of 'panda3d.core.Character' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CB430>)>'
        'mergeBundles': None, # (!) real value is "<method 'mergeBundles' of 'panda3d.core.Character' objects>"
        'merge_bundles': None, # (!) real value is "<method 'merge_bundles' of 'panda3d.core.Character' objects>"
        'setLodAnimation': None, # (!) real value is "<method 'setLodAnimation' of 'panda3d.core.Character' objects>"
        'set_lod_animation': None, # (!) real value is "<method 'set_lod_animation' of 'panda3d.core.Character' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.core.Character' objects>"
        'updateToNow': None, # (!) real value is "<method 'updateToNow' of 'panda3d.core.Character' objects>"
        'update_to_now': None, # (!) real value is "<method 'update_to_now' of 'panda3d.core.Character' objects>"
        'writePartValues': None, # (!) real value is "<method 'writePartValues' of 'panda3d.core.Character' objects>"
        'writeParts': None, # (!) real value is "<method 'writeParts' of 'panda3d.core.Character' objects>"
        'write_part_values': None, # (!) real value is "<method 'write_part_values' of 'panda3d.core.Character' objects>"
        'write_parts': None, # (!) real value is "<method 'write_parts' of 'panda3d.core.Character' objects>"
    }


