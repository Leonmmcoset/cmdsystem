# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Namable import Namable

class FisheyeMaker(Namable):
    """
    /**
     * This class is similar to CardMaker, but instead of generating ordinary
     * cards, it generates a circular rose that represents the projection of a 3-D
     * scene through a fisheye lens.  The texture coordinates of the rose are
     * defined so that each 2-D vertex has a 3-D UVW that reflects the
     * corresponding position in 3-D space of that particular vertex.
     *
     * This class is particularly suited for converting cube maps to sphere maps.
     */
    """
    def generate(self, const_FisheyeMaker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate(const FisheyeMaker self)
        
        /**
         * Generates a GeomNode that renders the specified geometry.
         */
        """
        pass

    def reset(self, const_FisheyeMaker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const FisheyeMaker self)
        
        /**
         * Resets all the parameters to their initial defaults.
         */
        """
        pass

    def setFov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fov(const FisheyeMaker self, float fov)
        
        /**
         * Specifies the field of view of the fisheye projection.  A sphere map will
         * have a 360-degree field of view (and this is the default).
         */
        """
        pass

    def setNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_vertices(const FisheyeMaker self, int num_vertices)
        
        /**
         * Specifies the approximate number of vertices to be used to generate the
         * rose.  This is the approximate number of vertices that will be located
         * within the rose's unit circle, not counting the inscribing square (if any).
         * The actual number of vertices used may be +/- 25% of this value.
         */
        """
        pass

    def setReflection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_reflection(const FisheyeMaker self, bool reflection)
        
        /**
         * Sets the flag indicating whether the texture image should be mirrored
         * (true) or normal (false).  When this is true, the 3-D texture coordinates
         * will be reversed so that the image is appropriate for a reflection.  This
         * is the best choice for generating a sphere map from a cube map.  The
         * default is false.
         */
        """
        pass

    def setSquareInscribed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_square_inscribed(const FisheyeMaker self, bool square_inscribed, float square_radius)
        
        /**
         * Sets the flag that indicates whether the rose should be inscribed within a
         * square.  When this is true, an additional square is generated to inscribed
         * the circular rose, with the indicated "radius" (the sides of the square
         * will be 2 * square_radius).  The texture coordinates of the square will
         * uniformly map to the back pole of the cube map.
         *
         * This is mainly useful to provide a good uniform background color for a
         * sphere map so that it does not have a sharp circular edge that might
         * produce artifacts due to numerical imprecision when mapping.
         */
        """
        pass

    def set_fov(self, const_FisheyeMaker_self, float_fov): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fov(const FisheyeMaker self, float fov)
        
        /**
         * Specifies the field of view of the fisheye projection.  A sphere map will
         * have a 360-degree field of view (and this is the default).
         */
        """
        pass

    def set_num_vertices(self, const_FisheyeMaker_self, int_num_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_vertices(const FisheyeMaker self, int num_vertices)
        
        /**
         * Specifies the approximate number of vertices to be used to generate the
         * rose.  This is the approximate number of vertices that will be located
         * within the rose's unit circle, not counting the inscribing square (if any).
         * The actual number of vertices used may be +/- 25% of this value.
         */
        """
        pass

    def set_reflection(self, const_FisheyeMaker_self, bool_reflection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_reflection(const FisheyeMaker self, bool reflection)
        
        /**
         * Sets the flag indicating whether the texture image should be mirrored
         * (true) or normal (false).  When this is true, the 3-D texture coordinates
         * will be reversed so that the image is appropriate for a reflection.  This
         * is the best choice for generating a sphere map from a cube map.  The
         * default is false.
         */
        """
        pass

    def set_square_inscribed(self, const_FisheyeMaker_self, bool_square_inscribed, float_square_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_square_inscribed(const FisheyeMaker self, bool square_inscribed, float square_radius)
        
        /**
         * Sets the flag that indicates whether the rose should be inscribed within a
         * square.  When this is true, an additional square is generated to inscribed
         * the circular rose, with the indicated "radius" (the sides of the square
         * will be 2 * square_radius).  The texture coordinates of the square will
         * uniformly map to the back pole of the cube map.
         *
         * This is mainly useful to provide a good uniform background color for a
         * sphere map so that it does not have a sharp circular edge that might
         * produce artifacts due to numerical imprecision when mapping.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.FisheyeMaker' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.FisheyeMaker' objects>"
        '__doc__': '/**\n * This class is similar to CardMaker, but instead of generating ordinary\n * cards, it generates a circular rose that represents the projection of a 3-D\n * scene through a fisheye lens.  The texture coordinates of the rose are\n * defined so that each 2-D vertex has a 3-D UVW that reflects the\n * corresponding position in 3-D space of that particular vertex.\n *\n * This class is particularly suited for converting cube maps to sphere maps.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FisheyeMaker' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BC1C0>'
        'generate': None, # (!) real value is "<method 'generate' of 'panda3d.core.FisheyeMaker' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.FisheyeMaker' objects>"
        'setFov': None, # (!) real value is "<method 'setFov' of 'panda3d.core.FisheyeMaker' objects>"
        'setNumVertices': None, # (!) real value is "<method 'setNumVertices' of 'panda3d.core.FisheyeMaker' objects>"
        'setReflection': None, # (!) real value is "<method 'setReflection' of 'panda3d.core.FisheyeMaker' objects>"
        'setSquareInscribed': None, # (!) real value is "<method 'setSquareInscribed' of 'panda3d.core.FisheyeMaker' objects>"
        'set_fov': None, # (!) real value is "<method 'set_fov' of 'panda3d.core.FisheyeMaker' objects>"
        'set_num_vertices': None, # (!) real value is "<method 'set_num_vertices' of 'panda3d.core.FisheyeMaker' objects>"
        'set_reflection': None, # (!) real value is "<method 'set_reflection' of 'panda3d.core.FisheyeMaker' objects>"
        'set_square_inscribed': None, # (!) real value is "<method 'set_square_inscribed' of 'panda3d.core.FisheyeMaker' objects>"
    }


