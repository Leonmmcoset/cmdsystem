# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class ShaderTerrainMesh(PandaNode):
    """
    /**
     * @brief Terrain Renderer class utilizing the GPU
     * @details This class provides functionality to render heightfields of large
     *   sizes utilizing the GPU. Internally a quadtree is used to generate the LODs.
     *   The final terrain is then rendered using instancing on the GPU. This makes
     *   it possible to use very large heightfields (8192+) with very reasonable
     *   performance. The terrain provides options to control the LOD using a
     *   target triangle width, see ShaderTerrainMesh::set_target_triangle_width().
     *
     *   Because the Terrain is rendered entirely on the GPU, it needs a special
     *   vertex shader. There is a default vertex shader available, which you can
     *   use in your own shaders. IMPORTANT: If you don't set an appropriate shader
     *   on the terrain, nothing will be visible.
     */
    """
    def generate(self, const_ShaderTerrainMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate(const ShaderTerrainMesh self)
        
        /**
         * @brief Generates the terrain mesh
         * @details This generates the terrain mesh, initializing all chunks of the
         *   internal used quadtree. At this point, a heightfield and a chunk size should
         *   have been set, otherwise an error is thrown.
         *
         *   If anything goes wrong, like a missing heightfield, then an error is printed
         *   and false is returned.
         *
         * @return true if the terrain was initialized, false if an error occured
         */
        """
        pass

    def getChunkSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_chunk_size(ShaderTerrainMesh self)
        
        /**
         * @brief Returns the chunk size
         * @details This returns the chunk size, previously set with set_chunk_size()
         * @return Chunk size
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGeneratePatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_generate_patches(ShaderTerrainMesh self)
        
        /**
         * @brief Returns whether to generate patches
         * @details This returns whether patches are generated, previously set with
         *   set_generate_patches()
         *
         * @return Whether to generate patches
         */
        """
        pass

    def getHeightfield(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_heightfield(ShaderTerrainMesh self)
        
        /**
         * @brief Returns the heightfield
         * @details This returns the terrain heightfield, previously set with
         *   set_heightfield()
         *
         * @return Path to the heightfield
         */
        """
        pass

    def getTargetTriangleWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_target_triangle_width(ShaderTerrainMesh self)
        
        /**
         * @brief Returns the target triangle width
         * @details This returns the target triangle width, previously set with
         *   ShaderTerrainMesh::set_target_triangle_width()
         *
         * @return Target triangle width
         */
        """
        pass

    def getUpdateEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_update_enabled(ShaderTerrainMesh self)
        
        /**
         * @brief Returns whether the terrain is getting updated
         * @details This returns whether the terrain is getting updates, previously set with
         *   set_update_enabled()
         *
         * @return Whether to update the terrain
         */
        """
        pass

    def get_chunk_size(self, ShaderTerrainMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_chunk_size(ShaderTerrainMesh self)
        
        /**
         * @brief Returns the chunk size
         * @details This returns the chunk size, previously set with set_chunk_size()
         * @return Chunk size
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_generate_patches(self, ShaderTerrainMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_generate_patches(ShaderTerrainMesh self)
        
        /**
         * @brief Returns whether to generate patches
         * @details This returns whether patches are generated, previously set with
         *   set_generate_patches()
         *
         * @return Whether to generate patches
         */
        """
        pass

    def get_heightfield(self, ShaderTerrainMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_heightfield(ShaderTerrainMesh self)
        
        /**
         * @brief Returns the heightfield
         * @details This returns the terrain heightfield, previously set with
         *   set_heightfield()
         *
         * @return Path to the heightfield
         */
        """
        pass

    def get_target_triangle_width(self, ShaderTerrainMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_target_triangle_width(ShaderTerrainMesh self)
        
        /**
         * @brief Returns the target triangle width
         * @details This returns the target triangle width, previously set with
         *   ShaderTerrainMesh::set_target_triangle_width()
         *
         * @return Target triangle width
         */
        """
        pass

    def get_update_enabled(self, ShaderTerrainMesh_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_update_enabled(ShaderTerrainMesh self)
        
        /**
         * @brief Returns whether the terrain is getting updated
         * @details This returns whether the terrain is getting updates, previously set with
         *   set_update_enabled()
         *
         * @return Whether to update the terrain
         */
        """
        pass

    def setChunkSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_chunk_size(const ShaderTerrainMesh self, int chunk_size)
        
        /**
         * @brief Sets the chunk size
         * @details This sets the chunk size of the terrain. A chunk is basically the
         *   smallest unit in LOD. If the chunk size is too small, the terrain will
         *   perform bad, since there will be way too many chunks. If the chunk size
         *   is too big, you will not get proper LOD, and might also get bad performance.
         *
         *   For terrains of the size 4096x4096 or 8192x8192, a chunk size of 32 seems
         *   to produce good results. For smaller resolutions, you should try out a
         *   size of 16 or even 8 for very small terrains.
         *
         *   The amount of chunks generated for the last level equals to
         *   (heightfield_size / chunk_size) ** 2. The chunk size has to be a power
         *   of two.
         *
         * @param chunk_size Size of the chunks, has to be a power of two
         */
        """
        pass

    def setGeneratePatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_generate_patches(const ShaderTerrainMesh self, bool generate_patches)
        
        /**
         * @brief Sets whether to generate patches
         * @details If this option is set to true, GeomPatches will be used instead of
         *   GeomTriangles. This is required when the terrain is used with tesselation
         *   shaders, since patches are required for tesselation, whereas triangles
         *   are required for regular rendering.
         *
         *   If this option is set to true while not using a tesselation shader, the
         *   terrain will not get rendered, or even produce errors. The same applies
         *   when this is option is not set, but the terrain is used with tesselation
         *   shaders.
         *
         * @param generate_patches [description]
         */
        """
        pass

    def setHeightfield(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_heightfield(const ShaderTerrainMesh self, Texture heightfield)
        
        /**
         * @brief Sets the heightfield texture
         * @details This sets the heightfield texture. It should be 16bit
         *   single channel, and have a power-of-two resolution greater than 32.
         *   Common sizes are 2048x2048 or 4096x4096.
         *
         *   You should call generate() after setting the heightfield.
         *
         * @param filename Heightfield texture
         */
        """
        pass

    def setTargetTriangleWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_target_triangle_width(const ShaderTerrainMesh self, float target_triangle_width)
        
        /**
         * @brief Sets the desired triangle width
         * @details This sets the desired width a triangle should have in pixels.
         *   A value of 10.0 for example will make the terrain tesselate everything
         *   in a way that each triangle edge roughly is 10 pixels wide.
         *   Of course this will not always accurately match, however you can use this
         *   setting to control the LOD algorithm of the terrain.
         *
         * @param target_triangle_width Desired triangle width in pixels
         */
        """
        pass

    def setUpdateEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_update_enabled(const ShaderTerrainMesh self, bool update_enabled)
        
        /**
         * @brief Sets whether to enable terrain updates
         * @details This flag controls whether the terrain should be updated. If this value
         *   is set to false, no updating of the terrain will happen. This can be useful
         *   to debug the culling algorithm used by the terrain.
         *
         * @param update_enabled Whether to update the terrain
         */
        """
        pass

    def set_chunk_size(self, const_ShaderTerrainMesh_self, int_chunk_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_chunk_size(const ShaderTerrainMesh self, int chunk_size)
        
        /**
         * @brief Sets the chunk size
         * @details This sets the chunk size of the terrain. A chunk is basically the
         *   smallest unit in LOD. If the chunk size is too small, the terrain will
         *   perform bad, since there will be way too many chunks. If the chunk size
         *   is too big, you will not get proper LOD, and might also get bad performance.
         *
         *   For terrains of the size 4096x4096 or 8192x8192, a chunk size of 32 seems
         *   to produce good results. For smaller resolutions, you should try out a
         *   size of 16 or even 8 for very small terrains.
         *
         *   The amount of chunks generated for the last level equals to
         *   (heightfield_size / chunk_size) ** 2. The chunk size has to be a power
         *   of two.
         *
         * @param chunk_size Size of the chunks, has to be a power of two
         */
        """
        pass

    def set_generate_patches(self, const_ShaderTerrainMesh_self, bool_generate_patches): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_generate_patches(const ShaderTerrainMesh self, bool generate_patches)
        
        /**
         * @brief Sets whether to generate patches
         * @details If this option is set to true, GeomPatches will be used instead of
         *   GeomTriangles. This is required when the terrain is used with tesselation
         *   shaders, since patches are required for tesselation, whereas triangles
         *   are required for regular rendering.
         *
         *   If this option is set to true while not using a tesselation shader, the
         *   terrain will not get rendered, or even produce errors. The same applies
         *   when this is option is not set, but the terrain is used with tesselation
         *   shaders.
         *
         * @param generate_patches [description]
         */
        """
        pass

    def set_heightfield(self, const_ShaderTerrainMesh_self, Texture_heightfield): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_heightfield(const ShaderTerrainMesh self, Texture heightfield)
        
        /**
         * @brief Sets the heightfield texture
         * @details This sets the heightfield texture. It should be 16bit
         *   single channel, and have a power-of-two resolution greater than 32.
         *   Common sizes are 2048x2048 or 4096x4096.
         *
         *   You should call generate() after setting the heightfield.
         *
         * @param filename Heightfield texture
         */
        """
        pass

    def set_target_triangle_width(self, const_ShaderTerrainMesh_self, float_target_triangle_width): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_target_triangle_width(const ShaderTerrainMesh self, float target_triangle_width)
        
        /**
         * @brief Sets the desired triangle width
         * @details This sets the desired width a triangle should have in pixels.
         *   A value of 10.0 for example will make the terrain tesselate everything
         *   in a way that each triangle edge roughly is 10 pixels wide.
         *   Of course this will not always accurately match, however you can use this
         *   setting to control the LOD algorithm of the terrain.
         *
         * @param target_triangle_width Desired triangle width in pixels
         */
        """
        pass

    def set_update_enabled(self, const_ShaderTerrainMesh_self, bool_update_enabled): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_update_enabled(const ShaderTerrainMesh self, bool update_enabled)
        
        /**
         * @brief Sets whether to enable terrain updates
         * @details This flag controls whether the terrain should be updated. If this value
         *   is set to false, no updating of the terrain will happen. This can be useful
         *   to debug the culling algorithm used by the terrain.
         *
         * @param update_enabled Whether to update the terrain
         */
        """
        pass

    def uvToWorld(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uv_to_world(ShaderTerrainMesh self, const LPoint2f coord)
        uv_to_world(ShaderTerrainMesh self, float u, float v)
        
        /**
         * @see ShaderTerrainMesh::uv_to_world(LTexCoord)
         */
        
        /**
         * @brief Transforms a texture coordinate to world space
         * @details This transforms a texture coordinatefrom uv-space (0 to 1) to world
         *   space. This takes the terrains transform into account, and also samples the
         *   heightmap. This method should be called after generate().
         *
         * @param coord Coordinate in uv-space from 0, 0 to 1, 1
         * @return World-Space point
         */
        """
        pass

    def uv_to_world(self, ShaderTerrainMesh_self, const_LPoint2f_coord): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uv_to_world(ShaderTerrainMesh self, const LPoint2f coord)
        uv_to_world(ShaderTerrainMesh self, float u, float v)
        
        /**
         * @see ShaderTerrainMesh::uv_to_world(LTexCoord)
         */
        
        /**
         * @brief Transforms a texture coordinate to world space
         * @details This transforms a texture coordinatefrom uv-space (0 to 1) to world
         *   space. This takes the terrains transform into account, and also samples the
         *   heightmap. This method should be called after generate().
         *
         * @param coord Coordinate in uv-space from 0, 0 to 1, 1
         * @return World-Space point
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    chunk_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generate_patches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    heightfield = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_triangle_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    update_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * @brief Terrain Renderer class utilizing the GPU\n * @details This class provides functionality to render heightfields of large\n *   sizes utilizing the GPU. Internally a quadtree is used to generate the LODs.\n *   The final terrain is then rendered using instancing on the GPU. This makes\n *   it possible to use very large heightfields (8192+) with very reasonable\n *   performance. The terrain provides options to control the LOD using a\n *   target triangle width, see ShaderTerrainMesh::set_target_triangle_width().\n *\n *   Because the Terrain is rendered entirely on the GPU, it needs a special\n *   vertex shader. There is a default vertex shader available, which you can\n *   use in your own shaders. IMPORTANT: If you don't set an appropriate shader\n *   on the terrain, nothing will be visible.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ShaderTerrainMesh' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BD3E0>'
        'chunk_size': None, # (!) real value is "<attribute 'chunk_size' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'generate': None, # (!) real value is "<method 'generate' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'generate_patches': None, # (!) real value is "<attribute 'generate_patches' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'getChunkSize': None, # (!) real value is "<method 'getChunkSize' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BD3E0>)>'
        'getGeneratePatches': None, # (!) real value is "<method 'getGeneratePatches' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'getHeightfield': None, # (!) real value is "<method 'getHeightfield' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'getTargetTriangleWidth': None, # (!) real value is "<method 'getTargetTriangleWidth' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'getUpdateEnabled': None, # (!) real value is "<method 'getUpdateEnabled' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'get_chunk_size': None, # (!) real value is "<method 'get_chunk_size' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BD3E0>)>'
        'get_generate_patches': None, # (!) real value is "<method 'get_generate_patches' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'get_heightfield': None, # (!) real value is "<method 'get_heightfield' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'get_target_triangle_width': None, # (!) real value is "<method 'get_target_triangle_width' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'get_update_enabled': None, # (!) real value is "<method 'get_update_enabled' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'heightfield': None, # (!) real value is "<attribute 'heightfield' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'setChunkSize': None, # (!) real value is "<method 'setChunkSize' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'setGeneratePatches': None, # (!) real value is "<method 'setGeneratePatches' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'setHeightfield': None, # (!) real value is "<method 'setHeightfield' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'setTargetTriangleWidth': None, # (!) real value is "<method 'setTargetTriangleWidth' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'setUpdateEnabled': None, # (!) real value is "<method 'setUpdateEnabled' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'set_chunk_size': None, # (!) real value is "<method 'set_chunk_size' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'set_generate_patches': None, # (!) real value is "<method 'set_generate_patches' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'set_heightfield': None, # (!) real value is "<method 'set_heightfield' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'set_target_triangle_width': None, # (!) real value is "<method 'set_target_triangle_width' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'set_update_enabled': None, # (!) real value is "<method 'set_update_enabled' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'target_triangle_width': None, # (!) real value is "<attribute 'target_triangle_width' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'update_enabled': None, # (!) real value is "<attribute 'update_enabled' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'uvToWorld': None, # (!) real value is "<method 'uvToWorld' of 'panda3d.core.ShaderTerrainMesh' objects>"
        'uv_to_world': None, # (!) real value is "<method 'uv_to_world' of 'panda3d.core.ShaderTerrainMesh' objects>"
    }


