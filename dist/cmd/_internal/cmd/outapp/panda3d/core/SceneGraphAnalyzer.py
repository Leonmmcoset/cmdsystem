# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SceneGraphAnalyzer(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A handy class that can scrub over a scene graph and collect interesting
     * statistics on it.
     */
    """
    def addNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_node(const SceneGraphAnalyzer self, PandaNode node)
        
        /**
         * Adds a new node to the set of data for analysis.  Normally, this would only
         * be called once, and passed the top of the scene graph, but it's possible to
         * repeatedly pass in subgraphs to get an analysis of all the graphs together.
         */
        """
        pass

    def add_node(self, const_SceneGraphAnalyzer_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_node(const SceneGraphAnalyzer self, PandaNode node)
        
        /**
         * Adds a new node to the set of data for analysis.  Normally, this would only
         * be called once, and passed the top of the scene graph, but it's possible to
         * repeatedly pass in subgraphs to get an analysis of all the graphs together.
         */
        """
        pass

    def clear(self, const_SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const SceneGraphAnalyzer self)
        
        /**
         * Resets all of the data in the analyzer in preparation for a new run.
         */
        """
        pass

    def getLodMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lod_mode(SceneGraphAnalyzer self, int lod_mode)
        
        /**
         * Returns the mode in which LODNodes are analyzed.
         */
        """
        pass

    def getNumColors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_colors(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumGeomNodes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_geom_nodes(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumGeoms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_geoms(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumGeomVertexDatas(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_geom_vertex_datas(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumGeomVertexFormats(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_geom_vertex_formats(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumIndividualTris(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_individual_tris(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumInstances(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_instances(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumLines(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_lines(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumLodNodes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_lod_nodes(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumLongNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_long_normals(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumNodes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_nodes(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumNodesWithAttribs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_nodes_with_attribs(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_normals(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumPatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_patches(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_points(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumShortNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_short_normals(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumTexcoords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_texcoords(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_transforms(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumTrianglesInFans(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_triangles_in_fans(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumTrianglesInStrips(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_triangles_in_strips(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumTrifans(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_trifans(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumTris(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_tris(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumTristrips(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_tristrips(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getNumVerticesInPatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices_in_patches(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getTextureBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_bytes(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getTotalNormalLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_normal_length(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def getVertexDataSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_data_size(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_lod_mode(self, SceneGraphAnalyzer_self, int_lod_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lod_mode(SceneGraphAnalyzer self, int lod_mode)
        
        /**
         * Returns the mode in which LODNodes are analyzed.
         */
        """
        pass

    def get_num_colors(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_colors(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_geoms(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_geoms(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_geom_nodes(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_geom_nodes(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_geom_vertex_datas(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_geom_vertex_datas(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_geom_vertex_formats(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_geom_vertex_formats(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_individual_tris(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_individual_tris(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_instances(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_instances(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_lines(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_lines(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_lod_nodes(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_lod_nodes(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_long_normals(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_long_normals(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_nodes(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_nodes(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_nodes_with_attribs(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_nodes_with_attribs(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_normals(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_normals(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_patches(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_patches(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_points(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_points(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_short_normals(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_short_normals(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_texcoords(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_texcoords(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_transforms(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_transforms(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_triangles_in_fans(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_triangles_in_fans(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_triangles_in_strips(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_triangles_in_strips(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_trifans(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_trifans(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_tris(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_tris(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_tristrips(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_tristrips(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_vertices(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_num_vertices_in_patches(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices_in_patches(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_texture_bytes(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_bytes(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_total_normal_length(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_normal_length(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def get_vertex_data_size(self, SceneGraphAnalyzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_data_size(SceneGraphAnalyzer self)
        
        /**
         *
         */
        """
        pass

    def setLodMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lod_mode(const SceneGraphAnalyzer self, int lod_mode)
        
        /**
         * Specifies the mode in which LODNodes are analyzed.
         */
        """
        pass

    def set_lod_mode(self, const_SceneGraphAnalyzer_self, int_lod_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lod_mode(const SceneGraphAnalyzer self, int lod_mode)
        
        /**
         * Specifies the mode in which LODNodes are analyzed.
         */
        """
        pass

    def write(self, SceneGraphAnalyzer_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(SceneGraphAnalyzer self, ostream out, int indent_level)
        
        /**
         * Describes all the data collected.
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'LMAll': 2,
        'LMHighest': 1,
        'LMLowest': 0,
        'LMNone': 3,
        'LM_all': 2,
        'LM_highest': 1,
        'LM_lowest': 0,
        'LM_none': 3,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        '__doc__': '/**\n * A handy class that can scrub over a scene graph and collect interesting\n * statistics on it.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE288E90>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'addNode': None, # (!) real value is "<method 'addNode' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'add_node': None, # (!) real value is "<method 'add_node' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getLodMode': None, # (!) real value is "<method 'getLodMode' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumColors': None, # (!) real value is "<method 'getNumColors' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumGeomNodes': None, # (!) real value is "<method 'getNumGeomNodes' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumGeomVertexDatas': None, # (!) real value is "<method 'getNumGeomVertexDatas' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumGeomVertexFormats': None, # (!) real value is "<method 'getNumGeomVertexFormats' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumGeoms': None, # (!) real value is "<method 'getNumGeoms' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumIndividualTris': None, # (!) real value is "<method 'getNumIndividualTris' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumInstances': None, # (!) real value is "<method 'getNumInstances' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumLines': None, # (!) real value is "<method 'getNumLines' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumLodNodes': None, # (!) real value is "<method 'getNumLodNodes' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumLongNormals': None, # (!) real value is "<method 'getNumLongNormals' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumNodes': None, # (!) real value is "<method 'getNumNodes' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumNodesWithAttribs': None, # (!) real value is "<method 'getNumNodesWithAttribs' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumNormals': None, # (!) real value is "<method 'getNumNormals' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumPatches': None, # (!) real value is "<method 'getNumPatches' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumPoints': None, # (!) real value is "<method 'getNumPoints' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumShortNormals': None, # (!) real value is "<method 'getNumShortNormals' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumTexcoords': None, # (!) real value is "<method 'getNumTexcoords' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumTransforms': None, # (!) real value is "<method 'getNumTransforms' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumTrianglesInFans': None, # (!) real value is "<method 'getNumTrianglesInFans' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumTrianglesInStrips': None, # (!) real value is "<method 'getNumTrianglesInStrips' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumTrifans': None, # (!) real value is "<method 'getNumTrifans' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumTris': None, # (!) real value is "<method 'getNumTris' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumTristrips': None, # (!) real value is "<method 'getNumTristrips' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumVertices': None, # (!) real value is "<method 'getNumVertices' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getNumVerticesInPatches': None, # (!) real value is "<method 'getNumVerticesInPatches' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getTextureBytes': None, # (!) real value is "<method 'getTextureBytes' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getTotalNormalLength': None, # (!) real value is "<method 'getTotalNormalLength' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'getVertexDataSize': None, # (!) real value is "<method 'getVertexDataSize' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_lod_mode': None, # (!) real value is "<method 'get_lod_mode' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_colors': None, # (!) real value is "<method 'get_num_colors' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_geom_nodes': None, # (!) real value is "<method 'get_num_geom_nodes' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_geom_vertex_datas': None, # (!) real value is "<method 'get_num_geom_vertex_datas' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_geom_vertex_formats': None, # (!) real value is "<method 'get_num_geom_vertex_formats' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_geoms': None, # (!) real value is "<method 'get_num_geoms' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_individual_tris': None, # (!) real value is "<method 'get_num_individual_tris' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_instances': None, # (!) real value is "<method 'get_num_instances' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_lines': None, # (!) real value is "<method 'get_num_lines' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_lod_nodes': None, # (!) real value is "<method 'get_num_lod_nodes' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_long_normals': None, # (!) real value is "<method 'get_num_long_normals' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_nodes': None, # (!) real value is "<method 'get_num_nodes' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_nodes_with_attribs': None, # (!) real value is "<method 'get_num_nodes_with_attribs' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_normals': None, # (!) real value is "<method 'get_num_normals' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_patches': None, # (!) real value is "<method 'get_num_patches' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_points': None, # (!) real value is "<method 'get_num_points' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_short_normals': None, # (!) real value is "<method 'get_num_short_normals' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_texcoords': None, # (!) real value is "<method 'get_num_texcoords' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_transforms': None, # (!) real value is "<method 'get_num_transforms' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_triangles_in_fans': None, # (!) real value is "<method 'get_num_triangles_in_fans' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_triangles_in_strips': None, # (!) real value is "<method 'get_num_triangles_in_strips' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_trifans': None, # (!) real value is "<method 'get_num_trifans' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_tris': None, # (!) real value is "<method 'get_num_tris' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_tristrips': None, # (!) real value is "<method 'get_num_tristrips' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_vertices': None, # (!) real value is "<method 'get_num_vertices' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_num_vertices_in_patches': None, # (!) real value is "<method 'get_num_vertices_in_patches' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_texture_bytes': None, # (!) real value is "<method 'get_texture_bytes' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_total_normal_length': None, # (!) real value is "<method 'get_total_normal_length' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'get_vertex_data_size': None, # (!) real value is "<method 'get_vertex_data_size' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'setLodMode': None, # (!) real value is "<method 'setLodMode' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'set_lod_mode': None, # (!) real value is "<method 'set_lod_mode' of 'panda3d.core.SceneGraphAnalyzer' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.SceneGraphAnalyzer' objects>"
    }
    LMAll = 2
    LMHighest = 1
    LMLowest = 0
    LMNone = 3
    LM_all = 2
    LM_highest = 1
    LM_lowest = 0
    LM_none = 3


