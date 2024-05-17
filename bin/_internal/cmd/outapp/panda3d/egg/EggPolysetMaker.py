# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggBinMaker import EggBinMaker

class EggPolysetMaker(EggBinMaker):
    """
    /**
     * A specialization on EggBinMaker for making polysets that share the same
     * basic rendering characteristic.  This really just defines the example
     * functions described in the leading comment to EggBinMaker.
     *
     * It makes some common assumptions about how polysets should be grouped; if
     * these are not sufficient, you can always rederive your own further
     * specialization of this class.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def setProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_properties(const EggPolysetMaker self, int properties)
        
        /**
         * Sets the set of properties that determines which polygons are allowed to be
         * grouped together into a single polyset.  This is the bitwise 'or' of all
         * the properties that matter.  If this is 0, all polygons (within a given
         * group) will be lumped into a common polyset regardless of their properties.
         */
        """
        pass

    def set_properties(self, const_EggPolysetMaker_self, int_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_properties(const EggPolysetMaker self, int properties)
        
        /**
         * Sets the set of properties that determines which polygons are allowed to be
         * grouped together into a single polyset.  This is the bitwise 'or' of all
         * the properties that matter.  If this is 0, all polygons (within a given
         * group) will be lumped into a common polyset regardless of their properties.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BNNone = 0
    BNPolyset = 1
    BN_none = 0
    BN_polyset = 1
    DtoolClassDict = {
        'BNNone': 0,
        'BNPolyset': 1,
        'BN_none': 0,
        'BN_polyset': 1,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'PBface': 512,
        'PHasMaterial': 4,
        'PHasPolyColor': 16,
        'PHasPolyNormal': 64,
        'PHasTexture': 1,
        'PHasVertexColor': 256,
        'PHasVertexNormal': 128,
        'PMaterial': 8,
        'PPolyColor': 32,
        'PTexture': 2,
        'P_bface': 512,
        'P_has_material': 4,
        'P_has_poly_color': 16,
        'P_has_poly_normal': 64,
        'P_has_texture': 1,
        'P_has_vertex_color': 256,
        'P_has_vertex_normal': 128,
        'P_material': 8,
        'P_poly_color': 32,
        'P_texture': 2,
        '__doc__': '/**\n * A specialization on EggBinMaker for making polysets that share the same\n * basic rendering characteristic.  This really just defines the example\n * functions described in the leading comment to EggBinMaker.\n *\n * It makes some common assumptions about how polysets should be grouped; if\n * these are not sufficient, you can always rederive your own further\n * specialization of this class.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggPolysetMaker' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D0C60>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D0C60>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D0C60>)>'
        'setProperties': None, # (!) real value is "<method 'setProperties' of 'panda3d.egg.EggPolysetMaker' objects>"
        'set_properties': None, # (!) real value is "<method 'set_properties' of 'panda3d.egg.EggPolysetMaker' objects>"
    }
    PBface = 512
    PHasMaterial = 4
    PHasPolyColor = 16
    PHasPolyNormal = 64
    PHasTexture = 1
    PHasVertexColor = 256
    PHasVertexNormal = 128
    PMaterial = 8
    PPolyColor = 32
    PTexture = 2
    P_bface = 512
    P_has_material = 4
    P_has_poly_color = 16
    P_has_poly_normal = 64
    P_has_texture = 1
    P_has_vertex_color = 256
    P_has_vertex_normal = 128
    P_material = 8
    P_poly_color = 32
    P_texture = 2


