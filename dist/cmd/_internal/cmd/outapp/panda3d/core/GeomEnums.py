# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class GeomEnums(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class exists just to provide scoping for the various enumerated types
     * used by Geom, GeomVertexData, GeomVertexArrayData, GeomPrimitive, and other
     * related classes.
     */
    """
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

    ATHardware = 2
    ATNone = 0
    ATPanda = 1
    AT_hardware = 2
    AT_none = 0
    AT_panda = 1
    CClipPoint = 2
    CColor = 5
    CIndex = 6
    CMatrix = 8
    CMorphDelta = 7
    CNormal = 9
    COther = 0
    CPoint = 1
    CTexcoord = 4
    CVector = 3
    C_clip_point = 2
    C_color = 5
    C_index = 6
    C_matrix = 8
    C_morph_delta = 7
    C_normal = 9
    C_other = 0
    C_point = 1
    C_texcoord = 4
    C_vector = 3
    DtoolClassDict = {
        'ATHardware': 2,
        'ATNone': 0,
        'ATPanda': 1,
        'AT_hardware': 2,
        'AT_none': 0,
        'AT_panda': 1,
        'CClipPoint': 2,
        'CColor': 5,
        'CIndex': 6,
        'CMatrix': 8,
        'CMorphDelta': 7,
        'CNormal': 9,
        'COther': 0,
        'CPoint': 1,
        'CTexcoord': 4,
        'CVector': 3,
        'C_clip_point': 2,
        'C_color': 5,
        'C_index': 6,
        'C_matrix': 8,
        'C_morph_delta': 7,
        'C_normal': 9,
        'C_other': 0,
        'C_point': 1,
        'C_texcoord': 4,
        'C_vector': 3,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'GRAdjacency': 1048576,
        'GRCompositeBits': 7168,
        'GRFlatFirstVertex': 8192,
        'GRFlatLastVertex': 16384,
        'GRIndexedBits': 65537,
        'GRIndexedOther': 65536,
        'GRIndexedPoint': 1,
        'GRLineStrip': 4096,
        'GRPerPointSize': 8,
        'GRPoint': 2,
        'GRPointAspectRatio': 32,
        'GRPointBits': 1022,
        'GRPointPerspective': 16,
        'GRPointRotate': 128,
        'GRPointScale': 64,
        'GRPointSprite': 256,
        'GRPointSpriteTexMatrix': 512,
        'GRPointUniformSize': 4,
        'GRRenderModePoint': 524288,
        'GRRenderModeWireframe': 262144,
        'GRShadeModelBits': 24576,
        'GRStripCutIndex': 131072,
        'GRTriangleFan': 2048,
        'GRTriangleStrip': 1024,
        'GR_adjacency': 1048576,
        'GR_composite_bits': 7168,
        'GR_flat_first_vertex': 8192,
        'GR_flat_last_vertex': 16384,
        'GR_indexed_bits': 65537,
        'GR_indexed_other': 65536,
        'GR_indexed_point': 1,
        'GR_line_strip': 4096,
        'GR_per_point_size': 8,
        'GR_point': 2,
        'GR_point_aspect_ratio': 32,
        'GR_point_bits': 1022,
        'GR_point_perspective': 16,
        'GR_point_rotate': 128,
        'GR_point_scale': 64,
        'GR_point_sprite': 256,
        'GR_point_sprite_tex_matrix': 512,
        'GR_point_uniform_size': 4,
        'GR_render_mode_point': 524288,
        'GR_render_mode_wireframe': 262144,
        'GR_shade_model_bits': 24576,
        'GR_strip_cut_index': 131072,
        'GR_triangle_fan': 2048,
        'GR_triangle_strip': 1024,
        'NTFloat32': 5,
        'NTFloat64': 6,
        'NTInt16': 9,
        'NTInt32': 10,
        'NTInt8': 8,
        'NTPackedDabc': 4,
        'NTPackedDcba': 3,
        'NTPackedUfloat': 11,
        'NTStdfloat': 7,
        'NTUint16': 1,
        'NTUint32': 2,
        'NTUint8': 0,
        'NT_float32': 5,
        'NT_float64': 6,
        'NT_int16': 9,
        'NT_int32': 10,
        'NT_int8': 8,
        'NT_packed_dabc': 4,
        'NT_packed_dcba': 3,
        'NT_packed_ufloat': 11,
        'NT_stdfloat': 7,
        'NT_uint16': 1,
        'NT_uint32': 2,
        'NT_uint8': 0,
        'PTLines': 2,
        'PTNone': 0,
        'PTPatches': 4,
        'PTPoints': 3,
        'PTPolygons': 1,
        'PT_lines': 2,
        'PT_none': 0,
        'PT_patches': 4,
        'PT_points': 3,
        'PT_polygons': 1,
        'SMFlatFirstVertex': 2,
        'SMFlatLastVertex': 3,
        'SMSmooth': 1,
        'SMUniform': 0,
        'SM_flat_first_vertex': 2,
        'SM_flat_last_vertex': 3,
        'SM_smooth': 1,
        'SM_uniform': 0,
        'UHClient': 0,
        'UHDynamic': 2,
        'UHStatic': 3,
        'UHStream': 1,
        'UHUnspecified': 4,
        'UH_client': 0,
        'UH_dynamic': 2,
        'UH_static': 3,
        'UH_stream': 1,
        'UH_unspecified': 4,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomEnums' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomEnums' objects>"
        '__doc__': '/**\n * This class exists just to provide scoping for the various enumerated types\n * used by Geom, GeomVertexData, GeomVertexArrayData, GeomPrimitive, and other\n * related classes.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomEnums' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F99E0>'
    }
    GRAdjacency = 1048576
    GRCompositeBits = 7168
    GRFlatFirstVertex = 8192
    GRFlatLastVertex = 16384
    GRIndexedBits = 65537
    GRIndexedOther = 65536
    GRIndexedPoint = 1
    GRLineStrip = 4096
    GRPerPointSize = 8
    GRPoint = 2
    GRPointAspectRatio = 32
    GRPointBits = 1022
    GRPointPerspective = 16
    GRPointRotate = 128
    GRPointScale = 64
    GRPointSprite = 256
    GRPointSpriteTexMatrix = 512
    GRPointUniformSize = 4
    GRRenderModePoint = 524288
    GRRenderModeWireframe = 262144
    GRShadeModelBits = 24576
    GRStripCutIndex = 131072
    GRTriangleFan = 2048
    GRTriangleStrip = 1024
    GR_adjacency = 1048576
    GR_composite_bits = 7168
    GR_flat_first_vertex = 8192
    GR_flat_last_vertex = 16384
    GR_indexed_bits = 65537
    GR_indexed_other = 65536
    GR_indexed_point = 1
    GR_line_strip = 4096
    GR_per_point_size = 8
    GR_point = 2
    GR_point_aspect_ratio = 32
    GR_point_bits = 1022
    GR_point_perspective = 16
    GR_point_rotate = 128
    GR_point_scale = 64
    GR_point_sprite = 256
    GR_point_sprite_tex_matrix = 512
    GR_point_uniform_size = 4
    GR_render_mode_point = 524288
    GR_render_mode_wireframe = 262144
    GR_shade_model_bits = 24576
    GR_strip_cut_index = 131072
    GR_triangle_fan = 2048
    GR_triangle_strip = 1024
    NTFloat32 = 5
    NTFloat64 = 6
    NTInt16 = 9
    NTInt32 = 10
    NTInt8 = 8
    NTPackedDabc = 4
    NTPackedDcba = 3
    NTPackedUfloat = 11
    NTStdfloat = 7
    NTUint16 = 1
    NTUint32 = 2
    NTUint8 = 0
    NT_float32 = 5
    NT_float64 = 6
    NT_int16 = 9
    NT_int32 = 10
    NT_int8 = 8
    NT_packed_dabc = 4
    NT_packed_dcba = 3
    NT_packed_ufloat = 11
    NT_stdfloat = 7
    NT_uint16 = 1
    NT_uint32 = 2
    NT_uint8 = 0
    PTLines = 2
    PTNone = 0
    PTPatches = 4
    PTPoints = 3
    PTPolygons = 1
    PT_lines = 2
    PT_none = 0
    PT_patches = 4
    PT_points = 3
    PT_polygons = 1
    SMFlatFirstVertex = 2
    SMFlatLastVertex = 3
    SMSmooth = 1
    SMUniform = 0
    SM_flat_first_vertex = 2
    SM_flat_last_vertex = 3
    SM_smooth = 1
    SM_uniform = 0
    UHClient = 0
    UHDynamic = 2
    UHStatic = 3
    UHStream = 1
    UHUnspecified = 4
    UH_client = 0
    UH_dynamic = 2
    UH_static = 3
    UH_stream = 1
    UH_unspecified = 4


