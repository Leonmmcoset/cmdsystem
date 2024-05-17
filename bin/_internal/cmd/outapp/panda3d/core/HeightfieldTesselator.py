# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Namable import Namable

class HeightfieldTesselator(Namable):
    # no doc
    def generate(self, const_HeightfieldTesselator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate(const HeightfieldTesselator self)
        
        /**
         * Generates a tree of nodes that represents the heightfield.  This can be
         * reparented into the scene.
         */
        """
        pass

    def getElevation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_elevation(const HeightfieldTesselator self, double x, double y)
        
        /**
         * Fetches the elevation at (x,y), where the input coordinate is specified in
         * pixels.  This ignores the current tesselation level and instead provides an
         * accurate number.  Linear blending is used for non-integral coordinates.
         */
        """
        pass

    def get_elevation(self, const_HeightfieldTesselator_self, double_x, double_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_elevation(const HeightfieldTesselator self, double x, double y)
        
        /**
         * Fetches the elevation at (x,y), where the input coordinate is specified in
         * pixels.  This ignores the current tesselation level and instead provides an
         * accurate number.  Linear blending is used for non-integral coordinates.
         */
        """
        pass

    def heightfield(self, const_HeightfieldTesselator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        heightfield(const HeightfieldTesselator self)
        
        /**
         * Returns a reference to the heightfield (a PNMImage) contained inside the
         * HeightfieldTesselator.  You can use the reference to alter the heightfield.
         */
        """
        pass

    def setFocalPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_focal_point(const HeightfieldTesselator self, int x, int y)
        
        /**
         * Sets the focal point.  The tesselator generates high-resolution terrain
         * around the focal point, and progressively lower and lower resolution
         * terrain as you get farther away.  The units are in pixels.
         */
        """
        pass

    def setHeightfield(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_heightfield(const HeightfieldTesselator self, const Filename filename)
        
        /**
         * Loads the specified greyscale image file into the heightfield.
         */
        """
        pass

    def setHorizontalScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_horizontal_scale(const HeightfieldTesselator self, double h)
        
        /**
         * Sets the horizontal scale.  The default scale is 1.0, meaning that each
         * pixel in the heightfield is 1x1 panda units wide.
         */
        """
        pass

    def setMaxTriangles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_triangles(const HeightfieldTesselator self, int n)
        
        /**
         * Sets the max triangles per geom.
         */
        """
        pass

    def setPolyCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_poly_count(const HeightfieldTesselator self, int n)
        
        /**
         * Sets the polygon-count target.  The tesselator usually manages to come
         * within about 20% of the target, plus or minus.
         */
        """
        pass

    def setVerticalScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertical_scale(const HeightfieldTesselator self, double v)
        
        /**
         * Sets the vertical scale.  The default scale is 255.0, meaning that each as
         * the gray value ranges from (0-1), the elevation ranges from (0-255) feet.
         */
        """
        pass

    def setVisibilityRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_visibility_radius(const HeightfieldTesselator self, int r)
        
        /**
         * Sets the visibility radius.  Polygons that are completely outside the
         * radius (relative to the focal point) are cropped away.  The cropping is
         * imperfect (all approximations are conservative), so this should be used in
         * conjunction with a far clipping plane, fog, or some other visibility
         * limiting mechanism.  The units are in pixels.
         */
        """
        pass

    def set_focal_point(self, const_HeightfieldTesselator_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_focal_point(const HeightfieldTesselator self, int x, int y)
        
        /**
         * Sets the focal point.  The tesselator generates high-resolution terrain
         * around the focal point, and progressively lower and lower resolution
         * terrain as you get farther away.  The units are in pixels.
         */
        """
        pass

    def set_heightfield(self, const_HeightfieldTesselator_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_heightfield(const HeightfieldTesselator self, const Filename filename)
        
        /**
         * Loads the specified greyscale image file into the heightfield.
         */
        """
        pass

    def set_horizontal_scale(self, const_HeightfieldTesselator_self, double_h): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_horizontal_scale(const HeightfieldTesselator self, double h)
        
        /**
         * Sets the horizontal scale.  The default scale is 1.0, meaning that each
         * pixel in the heightfield is 1x1 panda units wide.
         */
        """
        pass

    def set_max_triangles(self, const_HeightfieldTesselator_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_triangles(const HeightfieldTesselator self, int n)
        
        /**
         * Sets the max triangles per geom.
         */
        """
        pass

    def set_poly_count(self, const_HeightfieldTesselator_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_poly_count(const HeightfieldTesselator self, int n)
        
        /**
         * Sets the polygon-count target.  The tesselator usually manages to come
         * within about 20% of the target, plus or minus.
         */
        """
        pass

    def set_vertical_scale(self, const_HeightfieldTesselator_self, double_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertical_scale(const HeightfieldTesselator self, double v)
        
        /**
         * Sets the vertical scale.  The default scale is 255.0, meaning that each as
         * the gray value ranges from (0-1), the elevation ranges from (0-255) feet.
         */
        """
        pass

    def set_visibility_radius(self, const_HeightfieldTesselator_self, int_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_visibility_radius(const HeightfieldTesselator self, int r)
        
        /**
         * Sets the visibility radius.  Polygons that are completely outside the
         * radius (relative to the focal point) are cropped away.  The cropping is
         * imperfect (all approximations are conservative), so this should be used in
         * conjunction with a far clipping plane, fog, or some other visibility
         * limiting mechanism.  The units are in pixels.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.HeightfieldTesselator' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.HeightfieldTesselator' objects>"
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.HeightfieldTesselator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BC730>'
        'generate': None, # (!) real value is "<method 'generate' of 'panda3d.core.HeightfieldTesselator' objects>"
        'getElevation': None, # (!) real value is "<method 'getElevation' of 'panda3d.core.HeightfieldTesselator' objects>"
        'get_elevation': None, # (!) real value is "<method 'get_elevation' of 'panda3d.core.HeightfieldTesselator' objects>"
        'heightfield': None, # (!) real value is "<method 'heightfield' of 'panda3d.core.HeightfieldTesselator' objects>"
        'setFocalPoint': None, # (!) real value is "<method 'setFocalPoint' of 'panda3d.core.HeightfieldTesselator' objects>"
        'setHeightfield': None, # (!) real value is "<method 'setHeightfield' of 'panda3d.core.HeightfieldTesselator' objects>"
        'setHorizontalScale': None, # (!) real value is "<method 'setHorizontalScale' of 'panda3d.core.HeightfieldTesselator' objects>"
        'setMaxTriangles': None, # (!) real value is "<method 'setMaxTriangles' of 'panda3d.core.HeightfieldTesselator' objects>"
        'setPolyCount': None, # (!) real value is "<method 'setPolyCount' of 'panda3d.core.HeightfieldTesselator' objects>"
        'setVerticalScale': None, # (!) real value is "<method 'setVerticalScale' of 'panda3d.core.HeightfieldTesselator' objects>"
        'setVisibilityRadius': None, # (!) real value is "<method 'setVisibilityRadius' of 'panda3d.core.HeightfieldTesselator' objects>"
        'set_focal_point': None, # (!) real value is "<method 'set_focal_point' of 'panda3d.core.HeightfieldTesselator' objects>"
        'set_heightfield': None, # (!) real value is "<method 'set_heightfield' of 'panda3d.core.HeightfieldTesselator' objects>"
        'set_horizontal_scale': None, # (!) real value is "<method 'set_horizontal_scale' of 'panda3d.core.HeightfieldTesselator' objects>"
        'set_max_triangles': None, # (!) real value is "<method 'set_max_triangles' of 'panda3d.core.HeightfieldTesselator' objects>"
        'set_poly_count': None, # (!) real value is "<method 'set_poly_count' of 'panda3d.core.HeightfieldTesselator' objects>"
        'set_vertical_scale': None, # (!) real value is "<method 'set_vertical_scale' of 'panda3d.core.HeightfieldTesselator' objects>"
        'set_visibility_radius': None, # (!) real value is "<method 'set_visibility_radius' of 'panda3d.core.HeightfieldTesselator' objects>"
    }


