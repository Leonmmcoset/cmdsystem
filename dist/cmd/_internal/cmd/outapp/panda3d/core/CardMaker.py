# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Namable import Namable

class CardMaker(Namable):
    """
    /**
     * This class generates 2-d "cards", that is, rectangular polygons,
     * particularly useful for showing textures etc.  in the 2-d scene graph.
     */
    """
    def clearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_color(const CardMaker self)
        
        /**
         * Unsets the color of the card.
         */
        """
        pass

    def clearSourceGeometry(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_source_geometry(const CardMaker self)
        
        /**
         * Removes the node specified by an earlier call to set_source_geometry().
         */
        """
        pass

    def clear_color(self, const_CardMaker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_color(const CardMaker self)
        
        /**
         * Unsets the color of the card.
         */
        """
        pass

    def clear_source_geometry(self, const_CardMaker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_source_geometry(const CardMaker self)
        
        /**
         * Removes the node specified by an earlier call to set_source_geometry().
         */
        """
        pass

    def generate(self, const_CardMaker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate(const CardMaker self)
        
        /**
         * Generates a GeomNode that renders the specified geometry.
         */
        """
        pass

    def reset(self, const_CardMaker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const CardMaker self)
        
        /**
         * Resets all the parameters to their initial defaults.
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const CardMaker self, const LVecBase4f color)
        set_color(const CardMaker self, float r, float g, float b, float a)
        
        /**
         * Sets the color of the card.
         */
        
        /**
         * Sets the color of the card.
         */
        """
        pass

    def setFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame(const CardMaker self, const LVecBase4f frame)
        set_frame(const CardMaker self, const LPoint3f ll, const LPoint3f lr, const LPoint3f ur, const LPoint3f ul)
        set_frame(const CardMaker self, float left, float right, float bottom, float top)
        
        /**
         * Sets the size of the card.
         */
        
        /**
         * Sets the size of the card.
         */
        
        /**
         * Sets the size of the card.
         */
        """
        pass

    def setFrameFullscreenQuad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_fullscreen_quad(const CardMaker self)
        
        /**
         * Sets the card to (-1,1,-1,1), which is appropriate if you plan to parent it
         * to render2d and use it as a fullscreen quad.
         */
        """
        pass

    def setHas3dUvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_has_3d_uvs(const CardMaker self, bool flag)
        
        /**
         * Sets the flag indicating whether vertices will be generated with
         * 3-component UVW's (true) or 2-component UV's (the default, false).
         * Normally, this will be implicitly set by setting the uv_range.
         */
        """
        pass

    def setHasNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_has_normals(const CardMaker self, bool flag)
        
        /**
         * Sets the flag indicating whether vertices will be generated with normals or
         * not.  Normals are required if you intend to enable lighting on the card,
         * but are just wasted space and bandwidth otherwise, so there is a (slight)
         * optimization for disabling them.  If enabled, the normals will be generated
         * perpendicular to the card's face.
         */
        """
        pass

    def setHasUvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_has_uvs(const CardMaker self, bool flag)
        
        /**
         * Sets the flag indicating whether vertices will be generated with UV's or
         * not.
         */
        """
        pass

    def setSourceGeometry(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_source_geometry(const CardMaker self, PandaNode node, const LVecBase4f frame)
        
        /**
         * Sets a node that will be copied (and scaled and translated) to generate the
         * frame, instead of generating a new polygon.  The node may contain arbitrary
         * geometry that describes a flat polygon contained within the indicated left,
         * right, bottom, top frame.
         *
         * When generate() is called, the geometry in this node will be scaled and
         * translated appropriately to give it the size and aspect ratio specified by
         * set_frame().
         */
        """
        pass

    def setUvRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv_range(const CardMaker self, const Texture tex)
        set_uv_range(const CardMaker self, const LPoint2f ll, const LPoint2f ur)
        set_uv_range(const CardMaker self, const LVector4f x, const LVector4f y, const LVector4f z)
        set_uv_range(const CardMaker self, const LPoint3f ll, const LPoint3f lr, const LPoint3f ur, const LPoint3f ul)
        set_uv_range(const CardMaker self, const LPoint2f ll, const LPoint2f lr, const LPoint2f ur, const LPoint2f ul)
        
        /**
         * Sets the range of UV's that will be applied to the vertices.  If
         * set_has_uvs() is true (as it is by default), the vertices will be generated
         * with the indicated range of UV's, which will be useful if a texture is
         * applied.
         */
        
        /**
         * Sets the range of UV's that will be applied to the vertices.  If
         * set_has_uvs() is true (as it is by default), the vertices will be generated
         * with the indicated range of UV's, which will be useful if a texture is
         * applied.
         */
        
        /**
         * Sets the range of UV's that will be applied to the vertices.  If
         * set_has_uvs() is true (as it is by default), the vertices will be generated
         * with the indicated range of UV's, which will be useful if a texture is
         * applied.
         */
        
        /**
         * Sets the range of UV's that will be applied to the vertices.  If
         * set_has_uvs() is true (as it is by default), the vertices will be generated
         * with the indicated range of UV's, which will be useful if a texture is
         * applied.
         */
        
        /**
         * Sets the range of UV's that will be applied to the vertices appropriately
         * to show the non-pad region of the texture.
         */
        """
        pass

    def setUvRangeCube(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv_range_cube(const CardMaker self, int face)
        
        /**
         * Sets the range of UV's that will be applied to the vertices appropriately
         * for a cube-map face.
         */
        """
        pass

    def set_color(self, const_CardMaker_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const CardMaker self, const LVecBase4f color)
        set_color(const CardMaker self, float r, float g, float b, float a)
        
        /**
         * Sets the color of the card.
         */
        
        /**
         * Sets the color of the card.
         */
        """
        pass

    def set_frame(self, const_CardMaker_self, const_LVecBase4f_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame(const CardMaker self, const LVecBase4f frame)
        set_frame(const CardMaker self, const LPoint3f ll, const LPoint3f lr, const LPoint3f ur, const LPoint3f ul)
        set_frame(const CardMaker self, float left, float right, float bottom, float top)
        
        /**
         * Sets the size of the card.
         */
        
        /**
         * Sets the size of the card.
         */
        
        /**
         * Sets the size of the card.
         */
        """
        pass

    def set_frame_fullscreen_quad(self, const_CardMaker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_fullscreen_quad(const CardMaker self)
        
        /**
         * Sets the card to (-1,1,-1,1), which is appropriate if you plan to parent it
         * to render2d and use it as a fullscreen quad.
         */
        """
        pass

    def set_has_3d_uvs(self, const_CardMaker_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_has_3d_uvs(const CardMaker self, bool flag)
        
        /**
         * Sets the flag indicating whether vertices will be generated with
         * 3-component UVW's (true) or 2-component UV's (the default, false).
         * Normally, this will be implicitly set by setting the uv_range.
         */
        """
        pass

    def set_has_normals(self, const_CardMaker_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_has_normals(const CardMaker self, bool flag)
        
        /**
         * Sets the flag indicating whether vertices will be generated with normals or
         * not.  Normals are required if you intend to enable lighting on the card,
         * but are just wasted space and bandwidth otherwise, so there is a (slight)
         * optimization for disabling them.  If enabled, the normals will be generated
         * perpendicular to the card's face.
         */
        """
        pass

    def set_has_uvs(self, const_CardMaker_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_has_uvs(const CardMaker self, bool flag)
        
        /**
         * Sets the flag indicating whether vertices will be generated with UV's or
         * not.
         */
        """
        pass

    def set_source_geometry(self, const_CardMaker_self, PandaNode_node, const_LVecBase4f_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_source_geometry(const CardMaker self, PandaNode node, const LVecBase4f frame)
        
        /**
         * Sets a node that will be copied (and scaled and translated) to generate the
         * frame, instead of generating a new polygon.  The node may contain arbitrary
         * geometry that describes a flat polygon contained within the indicated left,
         * right, bottom, top frame.
         *
         * When generate() is called, the geometry in this node will be scaled and
         * translated appropriately to give it the size and aspect ratio specified by
         * set_frame().
         */
        """
        pass

    def set_uv_range(self, const_CardMaker_self, const_Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv_range(const CardMaker self, const Texture tex)
        set_uv_range(const CardMaker self, const LPoint2f ll, const LPoint2f ur)
        set_uv_range(const CardMaker self, const LVector4f x, const LVector4f y, const LVector4f z)
        set_uv_range(const CardMaker self, const LPoint3f ll, const LPoint3f lr, const LPoint3f ur, const LPoint3f ul)
        set_uv_range(const CardMaker self, const LPoint2f ll, const LPoint2f lr, const LPoint2f ur, const LPoint2f ul)
        
        /**
         * Sets the range of UV's that will be applied to the vertices.  If
         * set_has_uvs() is true (as it is by default), the vertices will be generated
         * with the indicated range of UV's, which will be useful if a texture is
         * applied.
         */
        
        /**
         * Sets the range of UV's that will be applied to the vertices.  If
         * set_has_uvs() is true (as it is by default), the vertices will be generated
         * with the indicated range of UV's, which will be useful if a texture is
         * applied.
         */
        
        /**
         * Sets the range of UV's that will be applied to the vertices.  If
         * set_has_uvs() is true (as it is by default), the vertices will be generated
         * with the indicated range of UV's, which will be useful if a texture is
         * applied.
         */
        
        /**
         * Sets the range of UV's that will be applied to the vertices.  If
         * set_has_uvs() is true (as it is by default), the vertices will be generated
         * with the indicated range of UV's, which will be useful if a texture is
         * applied.
         */
        
        /**
         * Sets the range of UV's that will be applied to the vertices appropriately
         * to show the non-pad region of the texture.
         */
        """
        pass

    def set_uv_range_cube(self, const_CardMaker_self, int_face): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv_range_cube(const CardMaker self, int face)
        
        /**
         * Sets the range of UV's that will be applied to the vertices appropriately
         * for a cube-map face.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CardMaker' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CardMaker' objects>"
        '__doc__': '/**\n * This class generates 2-d "cards", that is, rectangular polygons,\n * particularly useful for showing textures etc.  in the 2-d scene graph.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CardMaker' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BBFF0>'
        'clearColor': None, # (!) real value is "<method 'clearColor' of 'panda3d.core.CardMaker' objects>"
        'clearSourceGeometry': None, # (!) real value is "<method 'clearSourceGeometry' of 'panda3d.core.CardMaker' objects>"
        'clear_color': None, # (!) real value is "<method 'clear_color' of 'panda3d.core.CardMaker' objects>"
        'clear_source_geometry': None, # (!) real value is "<method 'clear_source_geometry' of 'panda3d.core.CardMaker' objects>"
        'generate': None, # (!) real value is "<method 'generate' of 'panda3d.core.CardMaker' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.CardMaker' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.core.CardMaker' objects>"
        'setFrame': None, # (!) real value is "<method 'setFrame' of 'panda3d.core.CardMaker' objects>"
        'setFrameFullscreenQuad': None, # (!) real value is "<method 'setFrameFullscreenQuad' of 'panda3d.core.CardMaker' objects>"
        'setHas3dUvs': None, # (!) real value is "<method 'setHas3dUvs' of 'panda3d.core.CardMaker' objects>"
        'setHasNormals': None, # (!) real value is "<method 'setHasNormals' of 'panda3d.core.CardMaker' objects>"
        'setHasUvs': None, # (!) real value is "<method 'setHasUvs' of 'panda3d.core.CardMaker' objects>"
        'setSourceGeometry': None, # (!) real value is "<method 'setSourceGeometry' of 'panda3d.core.CardMaker' objects>"
        'setUvRange': None, # (!) real value is "<method 'setUvRange' of 'panda3d.core.CardMaker' objects>"
        'setUvRangeCube': None, # (!) real value is "<method 'setUvRangeCube' of 'panda3d.core.CardMaker' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.core.CardMaker' objects>"
        'set_frame': None, # (!) real value is "<method 'set_frame' of 'panda3d.core.CardMaker' objects>"
        'set_frame_fullscreen_quad': None, # (!) real value is "<method 'set_frame_fullscreen_quad' of 'panda3d.core.CardMaker' objects>"
        'set_has_3d_uvs': None, # (!) real value is "<method 'set_has_3d_uvs' of 'panda3d.core.CardMaker' objects>"
        'set_has_normals': None, # (!) real value is "<method 'set_has_normals' of 'panda3d.core.CardMaker' objects>"
        'set_has_uvs': None, # (!) real value is "<method 'set_has_uvs' of 'panda3d.core.CardMaker' objects>"
        'set_source_geometry': None, # (!) real value is "<method 'set_source_geometry' of 'panda3d.core.CardMaker' objects>"
        'set_uv_range': None, # (!) real value is "<method 'set_uv_range' of 'panda3d.core.CardMaker' objects>"
        'set_uv_range_cube': None, # (!) real value is "<method 'set_uv_range_cube' of 'panda3d.core.CardMaker' objects>"
    }


