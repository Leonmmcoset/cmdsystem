# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class MultitexReducer(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This object presents an interface for generating new texture images that
     * represent the combined images from one or more individual textures,
     * reproducing certain kinds of multitexture effects without depending on
     * multitexture support in the hardware.
     *
     * This also flattens out texture matrices and removes extra texture
     * coordinates from the Geoms.  It is thus not a complete substitute for true
     * multitexturing, because it does not lend itself well to dynamic animation
     * of the textures once they have been flattened.  It is, however, useful for
     * "baking in" a particular multitexture effect.
     */
    """
    def clear(self, const_MultitexReducer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const MultitexReducer self)
        """
        pass

    def flatten(self, const_MultitexReducer_self, GraphicsOutput_window): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flatten(const MultitexReducer self, GraphicsOutput window)
        """
        pass

    def scan(self, const_MultitexReducer_self, const_NodePath_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scan(const MultitexReducer self, const NodePath node)
        scan(const MultitexReducer self, const NodePath node, const NodePath state_from)
        scan(const MultitexReducer self, PandaNode node, const RenderState state, const TransformState transform)
        
        /**
         * Starts scanning the hierarchy beginning at the indicated node.  Any
         * GeomNodes discovered in the hierarchy with multitexture will be added to
         * internal structures in the MultitexReducer so that a future call to
         * flatten() will operate on all of these at once.
         *
         * This version of this method does not accumulate state from the parents of
         * the indicated node; thus, only multitexture effects that have been applied
         * at node and below will be considered.
         */
        
        /**
         * Starts scanning the hierarchy beginning at the indicated node.  Any
         * GeomNodes discovered in the hierarchy with multitexture will be added to
         * internal structures in the MultitexReducer so that a future call to
         * flatten() will operate on all of these at once.
         *
         * The second parameter represents the NodePath from which to accumulate the
         * state that is considered for the multitexture.  Pass an empty NodePath to
         * accumulate all the state from the root of the graph, or you may specify
         * some other node here in order to not consider nodes above that as
         * contributing to the state to be flattened.  This is particularly useful if
         * you have some texture stage which is applied globally to a scene (for
         * instance, a caustics effect), which you don't want to be considered for
         * flattening by the MultitexReducer.
         */
        """
        pass

    def setAllowTexMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_allow_tex_mat(const MultitexReducer self, bool allow_tex_mat)
        """
        pass

    def setTarget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_target(const MultitexReducer self, TextureStage stage)
        """
        pass

    def setUseGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_use_geom(const MultitexReducer self, bool use_geom)
        """
        pass

    def set_allow_tex_mat(self, const_MultitexReducer_self, bool_allow_tex_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_allow_tex_mat(const MultitexReducer self, bool allow_tex_mat)
        """
        pass

    def set_target(self, const_MultitexReducer_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_target(const MultitexReducer self, TextureStage stage)
        """
        pass

    def set_use_geom(self, const_MultitexReducer_self, bool_use_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_use_geom(const MultitexReducer self, bool use_geom)
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MultitexReducer' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MultitexReducer' objects>"
        '__doc__': '/**\n * This object presents an interface for generating new texture images that\n * represent the combined images from one or more individual textures,\n * reproducing certain kinds of multitexture effects without depending on\n * multitexture support in the hardware.\n *\n * This also flattens out texture matrices and removes extra texture\n * coordinates from the Geoms.  It is thus not a complete substitute for true\n * multitexturing, because it does not lend itself well to dynamic animation\n * of the textures once they have been flattened.  It is, however, useful for\n * "baking in" a particular multitexture effect.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MultitexReducer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BD040>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.MultitexReducer' objects>"
        'flatten': None, # (!) real value is "<method 'flatten' of 'panda3d.core.MultitexReducer' objects>"
        'scan': None, # (!) real value is "<method 'scan' of 'panda3d.core.MultitexReducer' objects>"
        'setAllowTexMat': None, # (!) real value is "<method 'setAllowTexMat' of 'panda3d.core.MultitexReducer' objects>"
        'setTarget': None, # (!) real value is "<method 'setTarget' of 'panda3d.core.MultitexReducer' objects>"
        'setUseGeom': None, # (!) real value is "<method 'setUseGeom' of 'panda3d.core.MultitexReducer' objects>"
        'set_allow_tex_mat': None, # (!) real value is "<method 'set_allow_tex_mat' of 'panda3d.core.MultitexReducer' objects>"
        'set_target': None, # (!) real value is "<method 'set_target' of 'panda3d.core.MultitexReducer' objects>"
        'set_use_geom': None, # (!) real value is "<method 'set_use_geom' of 'panda3d.core.MultitexReducer' objects>"
    }


