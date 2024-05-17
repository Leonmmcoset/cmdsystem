# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

class MeshDrawer2D(TypedObject):
    """
    /**
     * This class allows the drawing of 2D objects - mainly based on quads and
     * rectangles.  It allows clipping and several high level UI theme functions.
     */
    """
    def begin(self, const_MeshDrawer2D_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin(const MeshDrawer2D self)
        
        /**
         * Opens up the geom for drawing, don't forget to call MeshDrawer2D::end()
         */
        """
        pass

    def end(self, const_MeshDrawer2D_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        end(const MeshDrawer2D self)
        
        /**
         * Finish the drawing and clearing off the remaining vertexes.
         */
        """
        pass

    def getBudget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_budget(const MeshDrawer2D self)
        
        /**
         * Gets the total triangle budget of the drawer.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_root(const MeshDrawer2D self)
        
        /**
         * Returns the root NodePath.
         */
        """
        pass

    def get_budget(self, const_MeshDrawer2D_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_budget(const MeshDrawer2D self)
        
        /**
         * Gets the total triangle budget of the drawer.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_root(self, const_MeshDrawer2D_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_root(const MeshDrawer2D self)
        
        /**
         * Returns the root NodePath.
         */
        """
        pass

    def quadRaw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        quad_raw(const MeshDrawer2D self, const LVector3f v1, const LVector4f c1, const LVector2f uv1, const LVector3f v2, const LVector4f c2, const LVector2f uv2, const LVector3f v3, const LVector4f c3, const LVector2f uv3, const LVector3f v4, const LVector4f c4, const LVector2f uv4)
        
        /**
         * Draws a 2D rectangle.  Ignores the clipping rectangle.
         */
        """
        pass

    def quad_raw(self, const_MeshDrawer2D_self, const_LVector3f_v1, const_LVector4f_c1, const_LVector2f_uv1, const_LVector3f_v2, const_LVector4f_c2, const_LVector2f_uv2, const_LVector3f_v3, const_LVector4f_c3, const_LVector2f_uv3, const_LVector3f_v4, const_LVector4f_c4, const_LVector2f_uv4): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        quad_raw(const MeshDrawer2D self, const LVector3f v1, const LVector4f c1, const LVector2f uv1, const LVector3f v2, const LVector4f c2, const LVector2f uv2, const LVector3f v3, const LVector4f c3, const LVector2f uv3, const LVector3f v4, const LVector4f c4, const LVector2f uv4)
        
        /**
         * Draws a 2D rectangle.  Ignores the clipping rectangle.
         */
        """
        pass

    def rectangle(self, const_MeshDrawer2D_self, float_x, float_y, float_w, float_h, float_u, float_v, float_us, float_vs, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rectangle(const MeshDrawer2D self, float x, float y, float w, float h, float u, float v, float us, float vs, const LVector4f color)
        
        /**
         * Draws a 2D rectangle which can be clipped.
         */
        """
        pass

    def rectangleBorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rectangle_border(const MeshDrawer2D self, float x, float y, float w, float h, float r, float t, float l, float b, float tr, float tt, float tl, float tb, float u, float v, float us, float vs, const LVector4f color)
        
        /**
         * Draws a 2d rectangle, with borders and corders, taken from the surrounding
         * texture
         */
        """
        pass

    def rectangleBorderTiled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rectangle_border_tiled(const MeshDrawer2D self, float x, float y, float w, float h, float r, float t, float l, float b, float tr, float tt, float tl, float tb, float u, float v, float us, float vs, const LVector4f color)
        
        /**
         * Draws a 2d rectangle, with borders and corders, taken from the surrounding
         * texture
         */
        """
        pass

    def rectangleRaw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rectangle_raw(const MeshDrawer2D self, float x, float y, float w, float h, float u, float v, float us, float vs, const LVector4f color)
        """
        pass

    def rectangleTiled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rectangle_tiled(const MeshDrawer2D self, float x, float y, float w, float h, float u, float v, float us, float vs, const LVector4f color)
        
        /**
         * Draws a tiled rectangle, size of tiles is in us and vs
         */
        """
        pass

    def rectangle_border(self, const_MeshDrawer2D_self, float_x, float_y, float_w, float_h, float_r, float_t, float_l, float_b, float_tr, float_tt, float_tl, float_tb, float_u, float_v, float_us, float_vs, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rectangle_border(const MeshDrawer2D self, float x, float y, float w, float h, float r, float t, float l, float b, float tr, float tt, float tl, float tb, float u, float v, float us, float vs, const LVector4f color)
        
        /**
         * Draws a 2d rectangle, with borders and corders, taken from the surrounding
         * texture
         */
        """
        pass

    def rectangle_border_tiled(self, const_MeshDrawer2D_self, float_x, float_y, float_w, float_h, float_r, float_t, float_l, float_b, float_tr, float_tt, float_tl, float_tb, float_u, float_v, float_us, float_vs, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rectangle_border_tiled(const MeshDrawer2D self, float x, float y, float w, float h, float r, float t, float l, float b, float tr, float tt, float tl, float tb, float u, float v, float us, float vs, const LVector4f color)
        
        /**
         * Draws a 2d rectangle, with borders and corders, taken from the surrounding
         * texture
         */
        """
        pass

    def rectangle_raw(self, const_MeshDrawer2D_self, float_x, float_y, float_w, float_h, float_u, float_v, float_us, float_vs, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rectangle_raw(const MeshDrawer2D self, float x, float y, float w, float h, float u, float v, float us, float vs, const LVector4f color)
        """
        pass

    def rectangle_tiled(self, const_MeshDrawer2D_self, float_x, float_y, float_w, float_h, float_u, float_v, float_us, float_vs, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rectangle_tiled(const MeshDrawer2D self, float x, float y, float w, float h, float u, float v, float us, float vs, const LVector4f color)
        
        /**
         * Draws a tiled rectangle, size of tiles is in us and vs
         */
        """
        pass

    def setBudget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_budget(const MeshDrawer2D self, int budget)
        
        /**
         * Sets the total triangle budget of the drawer.
         */
        """
        pass

    def setClip(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clip(const MeshDrawer2D self, float x, float y, float w, float h)
        
        /**
         * Sets the clipping rectangle.
         */
        """
        pass

    def set_budget(self, const_MeshDrawer2D_self, int_budget): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_budget(const MeshDrawer2D self, int budget)
        
        /**
         * Sets the total triangle budget of the drawer.
         */
        """
        pass

    def set_clip(self, const_MeshDrawer2D_self, float_x, float_y, float_w, float_h): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clip(const MeshDrawer2D self, float x, float y, float w, float h)
        
        /**
         * Sets the clipping rectangle.
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
        '__doc__': '/**\n * This class allows the drawing of 2D objects - mainly based on quads and\n * rectangles.  It allows clipping and several high level UI theme functions.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MeshDrawer2D' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BCCA0>'
        'begin': None, # (!) real value is "<method 'begin' of 'panda3d.core.MeshDrawer2D' objects>"
        'end': None, # (!) real value is "<method 'end' of 'panda3d.core.MeshDrawer2D' objects>"
        'getBudget': None, # (!) real value is "<method 'getBudget' of 'panda3d.core.MeshDrawer2D' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BCCA0>)>'
        'getRoot': None, # (!) real value is "<method 'getRoot' of 'panda3d.core.MeshDrawer2D' objects>"
        'get_budget': None, # (!) real value is "<method 'get_budget' of 'panda3d.core.MeshDrawer2D' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BCCA0>)>'
        'get_root': None, # (!) real value is "<method 'get_root' of 'panda3d.core.MeshDrawer2D' objects>"
        'quadRaw': None, # (!) real value is "<method 'quadRaw' of 'panda3d.core.MeshDrawer2D' objects>"
        'quad_raw': None, # (!) real value is "<method 'quad_raw' of 'panda3d.core.MeshDrawer2D' objects>"
        'rectangle': None, # (!) real value is "<method 'rectangle' of 'panda3d.core.MeshDrawer2D' objects>"
        'rectangleBorder': None, # (!) real value is "<method 'rectangleBorder' of 'panda3d.core.MeshDrawer2D' objects>"
        'rectangleBorderTiled': None, # (!) real value is "<method 'rectangleBorderTiled' of 'panda3d.core.MeshDrawer2D' objects>"
        'rectangleRaw': None, # (!) real value is "<method 'rectangleRaw' of 'panda3d.core.MeshDrawer2D' objects>"
        'rectangleTiled': None, # (!) real value is "<method 'rectangleTiled' of 'panda3d.core.MeshDrawer2D' objects>"
        'rectangle_border': None, # (!) real value is "<method 'rectangle_border' of 'panda3d.core.MeshDrawer2D' objects>"
        'rectangle_border_tiled': None, # (!) real value is "<method 'rectangle_border_tiled' of 'panda3d.core.MeshDrawer2D' objects>"
        'rectangle_raw': None, # (!) real value is "<method 'rectangle_raw' of 'panda3d.core.MeshDrawer2D' objects>"
        'rectangle_tiled': None, # (!) real value is "<method 'rectangle_tiled' of 'panda3d.core.MeshDrawer2D' objects>"
        'setBudget': None, # (!) real value is "<method 'setBudget' of 'panda3d.core.MeshDrawer2D' objects>"
        'setClip': None, # (!) real value is "<method 'setClip' of 'panda3d.core.MeshDrawer2D' objects>"
        'set_budget': None, # (!) real value is "<method 'set_budget' of 'panda3d.core.MeshDrawer2D' objects>"
        'set_clip': None, # (!) real value is "<method 'set_clip' of 'panda3d.core.MeshDrawer2D' objects>"
    }


