# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class LensNode(PandaNode):
    """
    /**
     * A node that contains a Lens.  The most important example of this kind of
     * node is a Camera, but other kinds of nodes also contain a lens (for
     * instance, a Spotlight).
     */
    """
    def activateLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        activate_lens(const LensNode self, int index)
        
        /**
         * An alternate way to call set_lens_active(index, true).
         */
        """
        pass

    def activate_lens(self, const_LensNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        activate_lens(const LensNode self, int index)
        
        /**
         * An alternate way to call set_lens_active(index, true).
         */
        """
        pass

    def copyLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_lens(const LensNode self, const Lens lens)
        copy_lens(const LensNode self, int index, const Lens lens)
        
        /**
         * Sets up the LensNode using a copy of the indicated Lens.  If the original
         * Lens is changed or destroyed, this LensNode is not affected.
         */
        
        /**
         * Copies the indicated lens into the specified slot.
         */
        """
        pass

    def copy_lens(self, const_LensNode_self, const_Lens_lens): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_lens(const LensNode self, const Lens lens)
        copy_lens(const LensNode self, int index, const Lens lens)
        
        /**
         * Sets up the LensNode using a copy of the indicated Lens.  If the original
         * Lens is changed or destroyed, this LensNode is not affected.
         */
        
        /**
         * Copies the indicated lens into the specified slot.
         */
        """
        pass

    def deactivateLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        deactivate_lens(const LensNode self, int index)
        
        /**
         * An alternate way to call set_lens_active(index, false).
         */
        """
        pass

    def deactivate_lens(self, const_LensNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        deactivate_lens(const LensNode self, int index)
        
        /**
         * An alternate way to call set_lens_active(index, false).
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lens(LensNode self, int index)
        
        /**
         * Returns a pointer to the particular Lens associated with this LensNode, or
         * NULL if there is not yet a Lens associated.  If an index number is
         * specified, returns the nth lens.
         */
        """
        pass

    def getLensActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lens_active(LensNode self, int index)
        
        /**
         * Returns the active flag for the nth lens.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_lens(self, LensNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lens(LensNode self, int index)
        
        /**
         * Returns a pointer to the particular Lens associated with this LensNode, or
         * NULL if there is not yet a Lens associated.  If an index number is
         * specified, returns the nth lens.
         */
        """
        pass

    def get_lens_active(self, LensNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lens_active(LensNode self, int index)
        
        /**
         * Returns the active flag for the nth lens.
         */
        """
        pass

    def hideFrustum(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hide_frustum(const LensNode self)
        
        /**
         * Disables the drawing of the lens's frustum to aid in visualization.
         */
        """
        pass

    def hide_frustum(self, const_LensNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hide_frustum(const LensNode self)
        
        /**
         * Disables the drawing of the lens's frustum to aid in visualization.
         */
        """
        pass

    def isInView(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_in_view(const LensNode self, const LPoint3f pos)
        is_in_view(const LensNode self, int index, const LPoint3f pos)
        
        /**
         * Returns true if the given point is within the bounds of the lens of the
         * LensNode (i.e.  if the camera can see the point).
         */
        
        /**
         * Returns true if the given point is within the bounds of the lens of the
         * LensNode (i.e.  if the camera can see the point).  The point is assumed to
         * be relative to the LensNode itself.
         */
        """
        pass

    def is_in_view(self, const_LensNode_self, const_LPoint3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_in_view(const LensNode self, const LPoint3f pos)
        is_in_view(const LensNode self, int index, const LPoint3f pos)
        
        /**
         * Returns true if the given point is within the bounds of the lens of the
         * LensNode (i.e.  if the camera can see the point).
         */
        
        /**
         * Returns true if the given point is within the bounds of the lens of the
         * LensNode (i.e.  if the camera can see the point).  The point is assumed to
         * be relative to the LensNode itself.
         */
        """
        pass

    def setLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lens(const LensNode self, Lens lens)
        set_lens(const LensNode self, int index, Lens lens)
        
        /**
         * Sets up the LensNode using this particular Lens pointer.  If the lens is
         * subsequently modified, the LensNode properties immediately reflect the
         * change.
         */
        
        /**
         * Sets the indicated lens.  Although a LensNode normally holds only one lens,
         * it may optionally include multiple lenses, each with a different index
         * number.  The different lenses may be referenced by index number on the
         * DisplayRegion.  Adding a new lens automatically makes it active.
         */
        """
        pass

    def setLensActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lens_active(const LensNode self, int index, bool active)
        
        /**
         * Sets the active flag for the nth lens.  When a lens is inactive, it is not
         * used for rendering, and any DisplayRegions associated with it are
         * implicitly inactive as well.  Returns true if the flag is changed, false if
         * it already had this value.
         */
        """
        pass

    def set_lens(self, const_LensNode_self, Lens_lens): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lens(const LensNode self, Lens lens)
        set_lens(const LensNode self, int index, Lens lens)
        
        /**
         * Sets up the LensNode using this particular Lens pointer.  If the lens is
         * subsequently modified, the LensNode properties immediately reflect the
         * change.
         */
        
        /**
         * Sets the indicated lens.  Although a LensNode normally holds only one lens,
         * it may optionally include multiple lenses, each with a different index
         * number.  The different lenses may be referenced by index number on the
         * DisplayRegion.  Adding a new lens automatically makes it active.
         */
        """
        pass

    def set_lens_active(self, const_LensNode_self, int_index, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lens_active(const LensNode self, int index, bool active)
        
        /**
         * Sets the active flag for the nth lens.  When a lens is inactive, it is not
         * used for rendering, and any DisplayRegions associated with it are
         * implicitly inactive as well.  Returns true if the flag is changed, false if
         * it already had this value.
         */
        """
        pass

    def showFrustum(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_frustum(const LensNode self)
        
        /**
         * Enables the drawing of the lens's frustum to aid in visualization.  This
         * actually creates a GeomNode which is parented to the LensNode.
         */
        """
        pass

    def show_frustum(self, const_LensNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_frustum(const LensNode self)
        
        /**
         * Enables the drawing of the lens's frustum to aid in visualization.  This
         * actually creates a GeomNode which is parented to the LensNode.
         */
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
        '__doc__': '/**\n * A node that contains a Lens.  The most important example of this kind of\n * node is a Camera, but other kinds of nodes also contain a lens (for\n * instance, a Spotlight).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LensNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2948F0>'
        'activateLens': None, # (!) real value is "<method 'activateLens' of 'panda3d.core.LensNode' objects>"
        'activate_lens': None, # (!) real value is "<method 'activate_lens' of 'panda3d.core.LensNode' objects>"
        'copyLens': None, # (!) real value is "<method 'copyLens' of 'panda3d.core.LensNode' objects>"
        'copy_lens': None, # (!) real value is "<method 'copy_lens' of 'panda3d.core.LensNode' objects>"
        'deactivateLens': None, # (!) real value is "<method 'deactivateLens' of 'panda3d.core.LensNode' objects>"
        'deactivate_lens': None, # (!) real value is "<method 'deactivate_lens' of 'panda3d.core.LensNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2948F0>)>'
        'getLens': None, # (!) real value is "<method 'getLens' of 'panda3d.core.LensNode' objects>"
        'getLensActive': None, # (!) real value is "<method 'getLensActive' of 'panda3d.core.LensNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2948F0>)>'
        'get_lens': None, # (!) real value is "<method 'get_lens' of 'panda3d.core.LensNode' objects>"
        'get_lens_active': None, # (!) real value is "<method 'get_lens_active' of 'panda3d.core.LensNode' objects>"
        'hideFrustum': None, # (!) real value is "<method 'hideFrustum' of 'panda3d.core.LensNode' objects>"
        'hide_frustum': None, # (!) real value is "<method 'hide_frustum' of 'panda3d.core.LensNode' objects>"
        'isInView': None, # (!) real value is "<method 'isInView' of 'panda3d.core.LensNode' objects>"
        'is_in_view': None, # (!) real value is "<method 'is_in_view' of 'panda3d.core.LensNode' objects>"
        'setLens': None, # (!) real value is "<method 'setLens' of 'panda3d.core.LensNode' objects>"
        'setLensActive': None, # (!) real value is "<method 'setLensActive' of 'panda3d.core.LensNode' objects>"
        'set_lens': None, # (!) real value is "<method 'set_lens' of 'panda3d.core.LensNode' objects>"
        'set_lens_active': None, # (!) real value is "<method 'set_lens_active' of 'panda3d.core.LensNode' objects>"
        'showFrustum': None, # (!) real value is "<method 'showFrustum' of 'panda3d.core.LensNode' objects>"
        'show_frustum': None, # (!) real value is "<method 'show_frustum' of 'panda3d.core.LensNode' objects>"
    }


