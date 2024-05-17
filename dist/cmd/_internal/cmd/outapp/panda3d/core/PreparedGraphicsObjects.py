# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class PreparedGraphicsObjects(ReferenceCount):
    """
    /**
     * A table of objects that are saved within the graphics context for reference
     * by handle later.  Generally, this represents things like OpenGL texture
     * objects or display lists (or their equivalent on other platforms).
     *
     * This object simply records the pointers to the context objects created by
     * the individual GSG's; these context objects will contain enough information
     * to reference or release the actual object stored within the graphics
     * context.
     *
     * These tables may potentially be shared between related graphics contexts,
     * hence their storage here in a separate object rather than as a part of the
     * GraphicsStateGuardian.
     */
    """
    def dequeueGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_geom(const PreparedGraphicsObjects self, Geom geom)
        
        /**
         * Removes a geom from the queued list of geoms to be prepared.  Normally it
         * is not necessary to call this, unless you change your mind about preparing
         * it at the last minute, since the geom will automatically be dequeued and
         * prepared at the next frame.
         *
         * The return value is true if the geom is successfully dequeued, false if it
         * had not been queued.
         */
        """
        pass

    def dequeueIndexBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_index_buffer(const PreparedGraphicsObjects self, GeomPrimitive data)
        
        /**
         * Removes a buffer from the queued list of data arrays to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the data will automatically be
         * dequeued and prepared at the next frame.
         *
         * The return value is true if the buffer is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeueSampler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_sampler(const PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Removes a sampler from the queued list of samplers to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the sampler will automatically
         * be dequeued and prepared at the next frame.
         *
         * The return value is true if the sampler is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeueShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_shader(const PreparedGraphicsObjects self, Shader shader)
        
        /**
         * Removes a shader from the queued list of shaders to be prepared.  Normally
         * it is not necessary to call this, unless you change your mind about
         * preparing it at the last minute, since the shader will automatically be
         * dequeued and prepared at the next frame.
         *
         * The return value is true if the shader is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeueShaderBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_shader_buffer(const PreparedGraphicsObjects self, ShaderBuffer data)
        
        /**
         * Removes a buffer from the queued list of data arrays to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the data will automatically be
         * dequeued and prepared at the next frame.
         *
         * The return value is true if the buffer is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeueTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_texture(const PreparedGraphicsObjects self, Texture tex)
        
        /**
         * Removes a texture from the queued list of textures to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the texture will automatically
         * be dequeued and prepared at the next frame.
         *
         * The return value is true if the texture is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeueVertexBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dequeue_vertex_buffer(const PreparedGraphicsObjects self, GeomVertexArrayData data)
        
        /**
         * Removes a buffer from the queued list of data arrays to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the data will automatically be
         * dequeued and prepared at the next frame.
         *
         * The return value is true if the buffer is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeue_geom(self, const_PreparedGraphicsObjects_self, Geom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_geom(const PreparedGraphicsObjects self, Geom geom)
        
        /**
         * Removes a geom from the queued list of geoms to be prepared.  Normally it
         * is not necessary to call this, unless you change your mind about preparing
         * it at the last minute, since the geom will automatically be dequeued and
         * prepared at the next frame.
         *
         * The return value is true if the geom is successfully dequeued, false if it
         * had not been queued.
         */
        """
        pass

    def dequeue_index_buffer(self, const_PreparedGraphicsObjects_self, GeomPrimitive_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_index_buffer(const PreparedGraphicsObjects self, GeomPrimitive data)
        
        /**
         * Removes a buffer from the queued list of data arrays to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the data will automatically be
         * dequeued and prepared at the next frame.
         *
         * The return value is true if the buffer is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeue_sampler(self, const_PreparedGraphicsObjects_self, const_SamplerState_sampler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_sampler(const PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Removes a sampler from the queued list of samplers to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the sampler will automatically
         * be dequeued and prepared at the next frame.
         *
         * The return value is true if the sampler is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeue_shader(self, const_PreparedGraphicsObjects_self, Shader_shader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_shader(const PreparedGraphicsObjects self, Shader shader)
        
        /**
         * Removes a shader from the queued list of shaders to be prepared.  Normally
         * it is not necessary to call this, unless you change your mind about
         * preparing it at the last minute, since the shader will automatically be
         * dequeued and prepared at the next frame.
         *
         * The return value is true if the shader is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeue_shader_buffer(self, const_PreparedGraphicsObjects_self, ShaderBuffer_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_shader_buffer(const PreparedGraphicsObjects self, ShaderBuffer data)
        
        /**
         * Removes a buffer from the queued list of data arrays to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the data will automatically be
         * dequeued and prepared at the next frame.
         *
         * The return value is true if the buffer is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeue_texture(self, const_PreparedGraphicsObjects_self, Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_texture(const PreparedGraphicsObjects self, Texture tex)
        
        /**
         * Removes a texture from the queued list of textures to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the texture will automatically
         * be dequeued and prepared at the next frame.
         *
         * The return value is true if the texture is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def dequeue_vertex_buffer(self, const_PreparedGraphicsObjects_self, GeomVertexArrayData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dequeue_vertex_buffer(const PreparedGraphicsObjects self, GeomVertexArrayData data)
        
        /**
         * Removes a buffer from the queued list of data arrays to be prepared.
         * Normally it is not necessary to call this, unless you change your mind
         * about preparing it at the last minute, since the data will automatically be
         * dequeued and prepared at the next frame.
         *
         * The return value is true if the buffer is successfully dequeued, false if
         * it had not been queued.
         */
        """
        pass

    def enqueueGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enqueue_geom(const PreparedGraphicsObjects self, Geom geom)
        
        /**
         * Indicates that a geom would like to be put on the list to be prepared when
         * the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueueIndexBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enqueue_index_buffer(const PreparedGraphicsObjects self, GeomPrimitive data)
        
        /**
         * Indicates that a buffer would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueueSampler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enqueue_sampler(const PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Indicates that a sampler would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueueShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enqueue_shader(const PreparedGraphicsObjects self, Shader shader)
        
        /**
         * Indicates that a shader would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueueShaderBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enqueue_shader_buffer(const PreparedGraphicsObjects self, ShaderBuffer data)
        
        /**
         * Indicates that a buffer would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueueTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enqueue_texture(const PreparedGraphicsObjects self, Texture tex)
        
        /**
         * Indicates that a texture would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueueVertexBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enqueue_vertex_buffer(const PreparedGraphicsObjects self, GeomVertexArrayData data)
        
        /**
         * Indicates that a buffer would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueue_geom(self, const_PreparedGraphicsObjects_self, Geom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enqueue_geom(const PreparedGraphicsObjects self, Geom geom)
        
        /**
         * Indicates that a geom would like to be put on the list to be prepared when
         * the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueue_index_buffer(self, const_PreparedGraphicsObjects_self, GeomPrimitive_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enqueue_index_buffer(const PreparedGraphicsObjects self, GeomPrimitive data)
        
        /**
         * Indicates that a buffer would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueue_sampler(self, const_PreparedGraphicsObjects_self, const_SamplerState_sampler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enqueue_sampler(const PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Indicates that a sampler would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueue_shader(self, const_PreparedGraphicsObjects_self, Shader_shader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enqueue_shader(const PreparedGraphicsObjects self, Shader shader)
        
        /**
         * Indicates that a shader would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueue_shader_buffer(self, const_PreparedGraphicsObjects_self, ShaderBuffer_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enqueue_shader_buffer(const PreparedGraphicsObjects self, ShaderBuffer data)
        
        /**
         * Indicates that a buffer would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueue_texture(self, const_PreparedGraphicsObjects_self, Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enqueue_texture(const PreparedGraphicsObjects self, Texture tex)
        
        /**
         * Indicates that a texture would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def enqueue_vertex_buffer(self, const_PreparedGraphicsObjects_self, GeomVertexArrayData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enqueue_vertex_buffer(const PreparedGraphicsObjects self, GeomVertexArrayData data)
        
        /**
         * Indicates that a buffer would like to be put on the list to be prepared
         * when the GSG is next ready to do this (presumably at the next frame).
         */
        """
        pass

    def getGraphicsMemoryLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_graphics_memory_limit(PreparedGraphicsObjects self)
        
        /**
         * Returns the artificial cap on graphics memory that will be imposed on this
         * GSG.  See set_graphics_memory_limit().
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(PreparedGraphicsObjects self)
        
        /**
         * Returns the name of the PreparedGraphicsObjects structure.  This is an
         * arbitrary name that serves mainly to uniquify the context for PStats
         * reporting.
         */
        """
        pass

    def getNumPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prepared(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of objects of any kind that have already been prepared
         * on this GSG.
         */
        """
        pass

    def getNumPreparedGeoms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prepared_geoms(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of geoms that have already been prepared on this GSG.
         */
        """
        pass

    def getNumPreparedIndexBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prepared_index_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of index buffers that have already been prepared on this
         * GSG.
         */
        """
        pass

    def getNumPreparedSamplers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prepared_samplers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of samplers that have already been prepared on this GSG.
         */
        """
        pass

    def getNumPreparedShaderBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prepared_shader_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of index buffers that have already been prepared on this
         * GSG.
         */
        """
        pass

    def getNumPreparedShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prepared_shaders(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of shaders that have already been prepared on this GSG.
         */
        """
        pass

    def getNumPreparedTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prepared_textures(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of textures that have already been prepared on this GSG.
         */
        """
        pass

    def getNumPreparedVertexBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prepared_vertex_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of vertex buffers that have already been prepared on
         * this GSG.
         */
        """
        pass

    def getNumQueued(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_queued(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of objects of any kind that have been enqueued to be
         * prepared on this GSG.
         */
        """
        pass

    def getNumQueuedGeoms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_queued_geoms(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of geoms that have been enqueued to be prepared on this
         * GSG.
         */
        """
        pass

    def getNumQueuedIndexBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_queued_index_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of index buffers that have been enqueued to be prepared
         * on this GSG.
         */
        """
        pass

    def getNumQueuedSamplers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_queued_samplers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of samplers that have been enqueued to be prepared on
         * this GSG.
         */
        """
        pass

    def getNumQueuedShaderBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_queued_shader_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of index buffers that have been enqueued to be prepared
         * on this GSG.
         */
        """
        pass

    def getNumQueuedShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_queued_shaders(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of shaders that have been enqueued to be prepared on
         * this GSG.
         */
        """
        pass

    def getNumQueuedTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_queued_textures(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of textures that have been enqueued to be prepared on
         * this GSG.
         */
        """
        pass

    def getNumQueuedVertexBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_queued_vertex_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of vertex buffers that have been enqueued to be prepared
         * on this GSG.
         */
        """
        pass

    def get_graphics_memory_limit(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_graphics_memory_limit(PreparedGraphicsObjects self)
        
        /**
         * Returns the artificial cap on graphics memory that will be imposed on this
         * GSG.  See set_graphics_memory_limit().
         */
        """
        pass

    def get_name(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(PreparedGraphicsObjects self)
        
        /**
         * Returns the name of the PreparedGraphicsObjects structure.  This is an
         * arbitrary name that serves mainly to uniquify the context for PStats
         * reporting.
         */
        """
        pass

    def get_num_prepared(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prepared(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of objects of any kind that have already been prepared
         * on this GSG.
         */
        """
        pass

    def get_num_prepared_geoms(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prepared_geoms(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of geoms that have already been prepared on this GSG.
         */
        """
        pass

    def get_num_prepared_index_buffers(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prepared_index_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of index buffers that have already been prepared on this
         * GSG.
         */
        """
        pass

    def get_num_prepared_samplers(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prepared_samplers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of samplers that have already been prepared on this GSG.
         */
        """
        pass

    def get_num_prepared_shaders(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prepared_shaders(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of shaders that have already been prepared on this GSG.
         */
        """
        pass

    def get_num_prepared_shader_buffers(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prepared_shader_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of index buffers that have already been prepared on this
         * GSG.
         */
        """
        pass

    def get_num_prepared_textures(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prepared_textures(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of textures that have already been prepared on this GSG.
         */
        """
        pass

    def get_num_prepared_vertex_buffers(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prepared_vertex_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of vertex buffers that have already been prepared on
         * this GSG.
         */
        """
        pass

    def get_num_queued(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_queued(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of objects of any kind that have been enqueued to be
         * prepared on this GSG.
         */
        """
        pass

    def get_num_queued_geoms(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_queued_geoms(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of geoms that have been enqueued to be prepared on this
         * GSG.
         */
        """
        pass

    def get_num_queued_index_buffers(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_queued_index_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of index buffers that have been enqueued to be prepared
         * on this GSG.
         */
        """
        pass

    def get_num_queued_samplers(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_queued_samplers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of samplers that have been enqueued to be prepared on
         * this GSG.
         */
        """
        pass

    def get_num_queued_shaders(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_queued_shaders(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of shaders that have been enqueued to be prepared on
         * this GSG.
         */
        """
        pass

    def get_num_queued_shader_buffers(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_queued_shader_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of index buffers that have been enqueued to be prepared
         * on this GSG.
         */
        """
        pass

    def get_num_queued_textures(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_queued_textures(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of textures that have been enqueued to be prepared on
         * this GSG.
         */
        """
        pass

    def get_num_queued_vertex_buffers(self, PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_queued_vertex_buffers(PreparedGraphicsObjects self)
        
        /**
         * Returns the number of vertex buffers that have been enqueued to be prepared
         * on this GSG.
         */
        """
        pass

    def isGeomPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_geom_prepared(PreparedGraphicsObjects self, const Geom geom)
        
        /**
         * Returns true if the vertex buffer has been prepared on this GSG, false
         * otherwise.
         */
        """
        pass

    def isGeomQueued(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_geom_queued(PreparedGraphicsObjects self, const Geom geom)
        
        /**
         * Returns true if the geom has been queued on this GSG, false otherwise.
         */
        """
        pass

    def isIndexBufferPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_index_buffer_prepared(PreparedGraphicsObjects self, const GeomPrimitive data)
        
        /**
         * Returns true if the index buffer has been prepared on this GSG, false
         * otherwise.
         */
        """
        pass

    def isIndexBufferQueued(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_index_buffer_queued(PreparedGraphicsObjects self, const GeomPrimitive data)
        
        /**
         * Returns true if the index buffer has been queued on this GSG, false
         * otherwise.
         */
        """
        pass

    def isSamplerPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_sampler_prepared(PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Returns true if the sampler has been prepared on this GSG, false otherwise.
         */
        """
        pass

    def isSamplerQueued(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_sampler_queued(PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Returns true if the sampler has been queued on this GSG, false otherwise.
         */
        """
        pass

    def isShaderBufferPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_shader_buffer_prepared(PreparedGraphicsObjects self, const ShaderBuffer data)
        
        /**
         * Returns true if the index buffer has been prepared on this GSG, false
         * otherwise.
         */
        """
        pass

    def isShaderBufferQueued(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_shader_buffer_queued(PreparedGraphicsObjects self, const ShaderBuffer data)
        
        /**
         * Returns true if the index buffer has been queued on this GSG, false
         * otherwise.
         */
        """
        pass

    def isShaderPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_shader_prepared(PreparedGraphicsObjects self, const Shader shader)
        
        /**
         * Returns true if the shader has been prepared on this GSG, false otherwise.
         */
        """
        pass

    def isShaderQueued(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_shader_queued(PreparedGraphicsObjects self, const Shader shader)
        
        /**
         * Returns true if the shader has been queued on this GSG, false otherwise.
         */
        """
        pass

    def isTexturePrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_texture_prepared(PreparedGraphicsObjects self, const Texture tex)
        
        /**
         * Returns true if the texture has been prepared on this GSG, false otherwise.
         */
        """
        pass

    def isTextureQueued(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_texture_queued(PreparedGraphicsObjects self, const Texture tex)
        
        /**
         * Returns true if the texture has been queued on this GSG, false otherwise.
         */
        """
        pass

    def isVertexBufferPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_vertex_buffer_prepared(PreparedGraphicsObjects self, const GeomVertexArrayData data)
        
        /**
         * Returns true if the vertex buffer has been prepared on this GSG, false
         * otherwise.
         */
        """
        pass

    def isVertexBufferQueued(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_vertex_buffer_queued(PreparedGraphicsObjects self, const GeomVertexArrayData data)
        
        /**
         * Returns true if the vertex buffer has been queued on this GSG, false
         * otherwise.
         */
        """
        pass

    def is_geom_prepared(self, PreparedGraphicsObjects_self, const_Geom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_geom_prepared(PreparedGraphicsObjects self, const Geom geom)
        
        /**
         * Returns true if the vertex buffer has been prepared on this GSG, false
         * otherwise.
         */
        """
        pass

    def is_geom_queued(self, PreparedGraphicsObjects_self, const_Geom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_geom_queued(PreparedGraphicsObjects self, const Geom geom)
        
        /**
         * Returns true if the geom has been queued on this GSG, false otherwise.
         */
        """
        pass

    def is_index_buffer_prepared(self, PreparedGraphicsObjects_self, const_GeomPrimitive_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_index_buffer_prepared(PreparedGraphicsObjects self, const GeomPrimitive data)
        
        /**
         * Returns true if the index buffer has been prepared on this GSG, false
         * otherwise.
         */
        """
        pass

    def is_index_buffer_queued(self, PreparedGraphicsObjects_self, const_GeomPrimitive_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_index_buffer_queued(PreparedGraphicsObjects self, const GeomPrimitive data)
        
        /**
         * Returns true if the index buffer has been queued on this GSG, false
         * otherwise.
         */
        """
        pass

    def is_sampler_prepared(self, PreparedGraphicsObjects_self, const_SamplerState_sampler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_sampler_prepared(PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Returns true if the sampler has been prepared on this GSG, false otherwise.
         */
        """
        pass

    def is_sampler_queued(self, PreparedGraphicsObjects_self, const_SamplerState_sampler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_sampler_queued(PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Returns true if the sampler has been queued on this GSG, false otherwise.
         */
        """
        pass

    def is_shader_buffer_prepared(self, PreparedGraphicsObjects_self, const_ShaderBuffer_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_shader_buffer_prepared(PreparedGraphicsObjects self, const ShaderBuffer data)
        
        /**
         * Returns true if the index buffer has been prepared on this GSG, false
         * otherwise.
         */
        """
        pass

    def is_shader_buffer_queued(self, PreparedGraphicsObjects_self, const_ShaderBuffer_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_shader_buffer_queued(PreparedGraphicsObjects self, const ShaderBuffer data)
        
        /**
         * Returns true if the index buffer has been queued on this GSG, false
         * otherwise.
         */
        """
        pass

    def is_shader_prepared(self, PreparedGraphicsObjects_self, const_Shader_shader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_shader_prepared(PreparedGraphicsObjects self, const Shader shader)
        
        /**
         * Returns true if the shader has been prepared on this GSG, false otherwise.
         */
        """
        pass

    def is_shader_queued(self, PreparedGraphicsObjects_self, const_Shader_shader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_shader_queued(PreparedGraphicsObjects self, const Shader shader)
        
        /**
         * Returns true if the shader has been queued on this GSG, false otherwise.
         */
        """
        pass

    def is_texture_prepared(self, PreparedGraphicsObjects_self, const_Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_texture_prepared(PreparedGraphicsObjects self, const Texture tex)
        
        /**
         * Returns true if the texture has been prepared on this GSG, false otherwise.
         */
        """
        pass

    def is_texture_queued(self, PreparedGraphicsObjects_self, const_Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_texture_queued(PreparedGraphicsObjects self, const Texture tex)
        
        /**
         * Returns true if the texture has been queued on this GSG, false otherwise.
         */
        """
        pass

    def is_vertex_buffer_prepared(self, PreparedGraphicsObjects_self, const_GeomVertexArrayData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_vertex_buffer_prepared(PreparedGraphicsObjects self, const GeomVertexArrayData data)
        
        /**
         * Returns true if the vertex buffer has been prepared on this GSG, false
         * otherwise.
         */
        """
        pass

    def is_vertex_buffer_queued(self, PreparedGraphicsObjects_self, const_GeomVertexArrayData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_vertex_buffer_queued(PreparedGraphicsObjects self, const GeomVertexArrayData data)
        
        /**
         * Returns true if the vertex buffer has been queued on this GSG, false
         * otherwise.
         */
        """
        pass

    def prepareGeomNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_geom_now(const PreparedGraphicsObjects self, Geom geom, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new GeomContext for the indicated geom and returns
         * it.  This assumes that the GraphicsStateGuardian is the currently active
         * rendering context and that it is ready to accept new geoms.  If this is not
         * necessarily the case, you should use enqueue_geom() instead.
         *
         * Normally, this function is not called directly.  Call Geom::prepare_now()
         * instead.
         *
         * The GeomContext contains all of the pertinent information needed by the GSG
         * to keep track of this one particular geom, and will exist as long as the
         * geom is ready to be rendered.
         *
         * When either the Geom or the PreparedGraphicsObjects object destructs, the
         * GeomContext will be deleted.
         */
        """
        pass

    def prepareIndexBufferNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_index_buffer_now(const PreparedGraphicsObjects self, GeomPrimitive data, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new IndexBufferContext for the indicated data and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new datas.  If this
         * is not necessarily the case, you should use enqueue_index_buffer() instead.
         *
         * Normally, this function is not called directly.  Call Data::prepare_now()
         * instead.
         *
         * The IndexBufferContext contains all of the pertinent information needed by
         * the GSG to keep track of this one particular data, and will exist as long
         * as the data is ready to be rendered.
         *
         * When either the Data or the PreparedGraphicsObjects object destructs, the
         * IndexBufferContext will be deleted.
         */
        """
        pass

    def prepareShaderBufferNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_shader_buffer_now(const PreparedGraphicsObjects self, ShaderBuffer data, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new BufferContext for the indicated data and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new datas.  If this
         * is not necessarily the case, you should use enqueue_shader_buffer() instead.
         *
         * Normally, this function is not called directly.  Call Data::prepare_now()
         * instead.
         *
         * The BufferContext contains all of the pertinent information needed by
         * the GSG to keep track of this one particular data, and will exist as long
         * as the data is ready to be rendered.
         *
         * When either the Data or the PreparedGraphicsObjects object destructs, the
         * BufferContext will be deleted.
         */
        """
        pass

    def prepareShaderNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_shader_now(const PreparedGraphicsObjects self, Shader shader, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new ShaderContext for the indicated shader and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new shaders.  If
         * this is not necessarily the case, you should use enqueue_shader() instead.
         *
         * Normally, this function is not called directly.  Call Shader::prepare_now()
         * instead.
         *
         * The ShaderContext contains all of the pertinent information needed by the
         * GSG to keep track of this one particular shader, and will exist as long as
         * the shader is ready to be rendered.
         *
         * When either the Shader or the PreparedGraphicsObjects object destructs, the
         * ShaderContext will be deleted.
         */
        """
        pass

    def prepareTextureNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_texture_now(const PreparedGraphicsObjects self, Texture tex, int view, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new TextureContext for the indicated texture and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new textures.  If
         * this is not necessarily the case, you should use enqueue_texture() instead.
         *
         * Normally, this function is not called directly.  Call
         * Texture::prepare_now() instead.
         *
         * The TextureContext contains all of the pertinent information needed by the
         * GSG to keep track of this one particular texture, and will exist as long as
         * the texture is ready to be rendered.
         *
         * When either the Texture or the PreparedGraphicsObjects object destructs,
         * the TextureContext will be deleted.
         */
        """
        pass

    def prepareVertexBufferNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_vertex_buffer_now(const PreparedGraphicsObjects self, GeomVertexArrayData data, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new VertexBufferContext for the indicated data and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new datas.  If this
         * is not necessarily the case, you should use enqueue_vertex_buffer()
         * instead.
         *
         * Normally, this function is not called directly.  Call Data::prepare_now()
         * instead.
         *
         * The VertexBufferContext contains all of the pertinent information needed by
         * the GSG to keep track of this one particular data, and will exist as long
         * as the data is ready to be rendered.
         *
         * When either the Data or the PreparedGraphicsObjects object destructs, the
         * VertexBufferContext will be deleted.
         */
        """
        pass

    def prepare_geom_now(self, const_PreparedGraphicsObjects_self, Geom_geom, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_geom_now(const PreparedGraphicsObjects self, Geom geom, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new GeomContext for the indicated geom and returns
         * it.  This assumes that the GraphicsStateGuardian is the currently active
         * rendering context and that it is ready to accept new geoms.  If this is not
         * necessarily the case, you should use enqueue_geom() instead.
         *
         * Normally, this function is not called directly.  Call Geom::prepare_now()
         * instead.
         *
         * The GeomContext contains all of the pertinent information needed by the GSG
         * to keep track of this one particular geom, and will exist as long as the
         * geom is ready to be rendered.
         *
         * When either the Geom or the PreparedGraphicsObjects object destructs, the
         * GeomContext will be deleted.
         */
        """
        pass

    def prepare_index_buffer_now(self, const_PreparedGraphicsObjects_self, GeomPrimitive_data, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_index_buffer_now(const PreparedGraphicsObjects self, GeomPrimitive data, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new IndexBufferContext for the indicated data and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new datas.  If this
         * is not necessarily the case, you should use enqueue_index_buffer() instead.
         *
         * Normally, this function is not called directly.  Call Data::prepare_now()
         * instead.
         *
         * The IndexBufferContext contains all of the pertinent information needed by
         * the GSG to keep track of this one particular data, and will exist as long
         * as the data is ready to be rendered.
         *
         * When either the Data or the PreparedGraphicsObjects object destructs, the
         * IndexBufferContext will be deleted.
         */
        """
        pass

    def prepare_shader_buffer_now(self, const_PreparedGraphicsObjects_self, ShaderBuffer_data, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_shader_buffer_now(const PreparedGraphicsObjects self, ShaderBuffer data, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new BufferContext for the indicated data and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new datas.  If this
         * is not necessarily the case, you should use enqueue_shader_buffer() instead.
         *
         * Normally, this function is not called directly.  Call Data::prepare_now()
         * instead.
         *
         * The BufferContext contains all of the pertinent information needed by
         * the GSG to keep track of this one particular data, and will exist as long
         * as the data is ready to be rendered.
         *
         * When either the Data or the PreparedGraphicsObjects object destructs, the
         * BufferContext will be deleted.
         */
        """
        pass

    def prepare_shader_now(self, const_PreparedGraphicsObjects_self, Shader_shader, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_shader_now(const PreparedGraphicsObjects self, Shader shader, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new ShaderContext for the indicated shader and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new shaders.  If
         * this is not necessarily the case, you should use enqueue_shader() instead.
         *
         * Normally, this function is not called directly.  Call Shader::prepare_now()
         * instead.
         *
         * The ShaderContext contains all of the pertinent information needed by the
         * GSG to keep track of this one particular shader, and will exist as long as
         * the shader is ready to be rendered.
         *
         * When either the Shader or the PreparedGraphicsObjects object destructs, the
         * ShaderContext will be deleted.
         */
        """
        pass

    def prepare_texture_now(self, const_PreparedGraphicsObjects_self, Texture_tex, int_view, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_texture_now(const PreparedGraphicsObjects self, Texture tex, int view, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new TextureContext for the indicated texture and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new textures.  If
         * this is not necessarily the case, you should use enqueue_texture() instead.
         *
         * Normally, this function is not called directly.  Call
         * Texture::prepare_now() instead.
         *
         * The TextureContext contains all of the pertinent information needed by the
         * GSG to keep track of this one particular texture, and will exist as long as
         * the texture is ready to be rendered.
         *
         * When either the Texture or the PreparedGraphicsObjects object destructs,
         * the TextureContext will be deleted.
         */
        """
        pass

    def prepare_vertex_buffer_now(self, const_PreparedGraphicsObjects_self, GeomVertexArrayData_data, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_vertex_buffer_now(const PreparedGraphicsObjects self, GeomVertexArrayData data, GraphicsStateGuardianBase gsg)
        
        /**
         * Immediately creates a new VertexBufferContext for the indicated data and
         * returns it.  This assumes that the GraphicsStateGuardian is the currently
         * active rendering context and that it is ready to accept new datas.  If this
         * is not necessarily the case, you should use enqueue_vertex_buffer()
         * instead.
         *
         * Normally, this function is not called directly.  Call Data::prepare_now()
         * instead.
         *
         * The VertexBufferContext contains all of the pertinent information needed by
         * the GSG to keep track of this one particular data, and will exist as long
         * as the data is ready to be rendered.
         *
         * When either the Data or the PreparedGraphicsObjects object destructs, the
         * VertexBufferContext will be deleted.
         */
        """
        pass

    def releaseAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all(const PreparedGraphicsObjects self)
        
        /**
         * Releases all prepared objects of all kinds at once.
         */
        """
        pass

    def releaseAllGeoms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_geoms(const PreparedGraphicsObjects self)
        
        /**
         * Releases all geoms at once.  This will force them to be reloaded into geom
         * memory for all GSG's that share this object.  Returns the number of geoms
         * released.
         */
        """
        pass

    def releaseAllIndexBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_index_buffers(const PreparedGraphicsObjects self)
        
        /**
         * Releases all datas at once.  This will force them to be reloaded into data
         * memory for all GSG's that share this object.  Returns the number of datas
         * released.
         */
        """
        pass

    def releaseAllSamplers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_samplers(const PreparedGraphicsObjects self)
        
        /**
         * Releases all samplers at once.  This will force them to be reloaded for all
         * GSG's that share this object.  Returns the number of samplers released.
         */
        """
        pass

    def releaseAllShaderBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_shader_buffers(const PreparedGraphicsObjects self)
        
        /**
         * Releases all datas at once.  This will force them to be reloaded into data
         * memory for all GSG's that share this object.  Returns the number of datas
         * released.
         */
        """
        pass

    def releaseAllShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_shaders(const PreparedGraphicsObjects self)
        
        /**
         * Releases all shaders at once.  This will force them to be reloaded into
         * shader memory for all GSG's that share this object.  Returns the number of
         * shaders released.
         */
        """
        pass

    def releaseAllTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_textures(const PreparedGraphicsObjects self)
        
        /**
         * Releases all textures at once.  This will force them to be reloaded into
         * texture memory for all GSG's that share this object.  Returns the number of
         * textures released.
         */
        """
        pass

    def releaseAllVertexBuffers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_vertex_buffers(const PreparedGraphicsObjects self)
        
        /**
         * Releases all datas at once.  This will force them to be reloaded into data
         * memory for all GSG's that share this object.  Returns the number of datas
         * released.
         */
        """
        pass

    def releaseGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_geom(const PreparedGraphicsObjects self, GeomContext gc)
        
        /**
         * Indicates that a geom context, created by a previous call to
         * prepare_geom(), is no longer needed.  The driver resources will not be
         * freed until some GSG calls update(), indicating it is at a stage where it
         * is ready to release geoms--this prevents conflicts from threading or
         * multiple GSG's sharing geoms (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_geom is called).
         */
        """
        pass

    def releaseIndexBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_index_buffer(const PreparedGraphicsObjects self, IndexBufferContext ibc)
        
        /**
         * Indicates that a data context, created by a previous call to
         * prepare_index_buffer(), is no longer needed.  The driver resources will not
         * be freed until some GSG calls update(), indicating it is at a stage where
         * it is ready to release datas--this prevents conflicts from threading or
         * multiple GSG's sharing datas (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_index_buffer is called).
         */
        """
        pass

    def releaseSampler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_sampler(const PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Indicates that a sampler context, created by a previous call to
         * prepare_sampler(), is no longer needed.  The driver resources will not be
         * freed until some GSG calls update(), indicating it is at a stage where it
         * is ready to release samplers.
         */
        
        /**
         * Releases a sampler if it has already been prepared, or removes it from the
         * preparation queue.
         */
        """
        pass

    def releaseShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_shader(const PreparedGraphicsObjects self, ShaderContext sc)
        
        /**
         * Indicates that a shader context, created by a previous call to
         * prepare_shader(), is no longer needed.  The driver resources will not be
         * freed until some GSG calls update(), indicating it is at a stage where it
         * is ready to release shaders--this prevents conflicts from threading or
         * multiple GSG's sharing shaders (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_shader is called).
         */
        """
        pass

    def releaseShaderBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_shader_buffer(const PreparedGraphicsObjects self, BufferContext bc)
        
        /**
         * Indicates that a data context, created by a previous call to
         * prepare_shader_buffer(), is no longer needed.  The driver resources will not
         * be freed until some GSG calls update(), indicating it is at a stage where
         * it is ready to release datas--this prevents conflicts from threading or
         * multiple GSG's sharing datas (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_shader_buffer is called).
         */
        """
        pass

    def releaseTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_texture(const PreparedGraphicsObjects self, TextureContext tc)
        release_texture(const PreparedGraphicsObjects self, Texture tex)
        
        /**
         * Indicates that a texture context, created by a previous call to
         * prepare_texture(), is no longer needed.  The driver resources will not be
         * freed until some GSG calls update(), indicating it is at a stage where it
         * is ready to release textures--this prevents conflicts from threading or
         * multiple GSG's sharing textures (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_texture is called).
         */
        
        /**
         * Releases a texture if it has already been prepared, or removes it from the
         * preparation queue.
         */
        """
        pass

    def releaseVertexBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_vertex_buffer(const PreparedGraphicsObjects self, VertexBufferContext vbc)
        
        /**
         * Indicates that a data context, created by a previous call to
         * prepare_vertex_buffer(), is no longer needed.  The driver resources will
         * not be freed until some GSG calls update(), indicating it is at a stage
         * where it is ready to release datas--this prevents conflicts from threading
         * or multiple GSG's sharing datas (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_vertex_buffer is called).
         */
        """
        pass

    def release_all(self, const_PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all(const PreparedGraphicsObjects self)
        
        /**
         * Releases all prepared objects of all kinds at once.
         */
        """
        pass

    def release_all_geoms(self, const_PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_geoms(const PreparedGraphicsObjects self)
        
        /**
         * Releases all geoms at once.  This will force them to be reloaded into geom
         * memory for all GSG's that share this object.  Returns the number of geoms
         * released.
         */
        """
        pass

    def release_all_index_buffers(self, const_PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_index_buffers(const PreparedGraphicsObjects self)
        
        /**
         * Releases all datas at once.  This will force them to be reloaded into data
         * memory for all GSG's that share this object.  Returns the number of datas
         * released.
         */
        """
        pass

    def release_all_samplers(self, const_PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_samplers(const PreparedGraphicsObjects self)
        
        /**
         * Releases all samplers at once.  This will force them to be reloaded for all
         * GSG's that share this object.  Returns the number of samplers released.
         */
        """
        pass

    def release_all_shaders(self, const_PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_shaders(const PreparedGraphicsObjects self)
        
        /**
         * Releases all shaders at once.  This will force them to be reloaded into
         * shader memory for all GSG's that share this object.  Returns the number of
         * shaders released.
         */
        """
        pass

    def release_all_shader_buffers(self, const_PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_shader_buffers(const PreparedGraphicsObjects self)
        
        /**
         * Releases all datas at once.  This will force them to be reloaded into data
         * memory for all GSG's that share this object.  Returns the number of datas
         * released.
         */
        """
        pass

    def release_all_textures(self, const_PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_textures(const PreparedGraphicsObjects self)
        
        /**
         * Releases all textures at once.  This will force them to be reloaded into
         * texture memory for all GSG's that share this object.  Returns the number of
         * textures released.
         */
        """
        pass

    def release_all_vertex_buffers(self, const_PreparedGraphicsObjects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_vertex_buffers(const PreparedGraphicsObjects self)
        
        /**
         * Releases all datas at once.  This will force them to be reloaded into data
         * memory for all GSG's that share this object.  Returns the number of datas
         * released.
         */
        """
        pass

    def release_geom(self, const_PreparedGraphicsObjects_self, GeomContext_gc): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_geom(const PreparedGraphicsObjects self, GeomContext gc)
        
        /**
         * Indicates that a geom context, created by a previous call to
         * prepare_geom(), is no longer needed.  The driver resources will not be
         * freed until some GSG calls update(), indicating it is at a stage where it
         * is ready to release geoms--this prevents conflicts from threading or
         * multiple GSG's sharing geoms (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_geom is called).
         */
        """
        pass

    def release_index_buffer(self, const_PreparedGraphicsObjects_self, IndexBufferContext_ibc): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_index_buffer(const PreparedGraphicsObjects self, IndexBufferContext ibc)
        
        /**
         * Indicates that a data context, created by a previous call to
         * prepare_index_buffer(), is no longer needed.  The driver resources will not
         * be freed until some GSG calls update(), indicating it is at a stage where
         * it is ready to release datas--this prevents conflicts from threading or
         * multiple GSG's sharing datas (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_index_buffer is called).
         */
        """
        pass

    def release_sampler(self, const_PreparedGraphicsObjects_self, const_SamplerState_sampler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_sampler(const PreparedGraphicsObjects self, const SamplerState sampler)
        
        /**
         * Indicates that a sampler context, created by a previous call to
         * prepare_sampler(), is no longer needed.  The driver resources will not be
         * freed until some GSG calls update(), indicating it is at a stage where it
         * is ready to release samplers.
         */
        
        /**
         * Releases a sampler if it has already been prepared, or removes it from the
         * preparation queue.
         */
        """
        pass

    def release_shader(self, const_PreparedGraphicsObjects_self, ShaderContext_sc): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_shader(const PreparedGraphicsObjects self, ShaderContext sc)
        
        /**
         * Indicates that a shader context, created by a previous call to
         * prepare_shader(), is no longer needed.  The driver resources will not be
         * freed until some GSG calls update(), indicating it is at a stage where it
         * is ready to release shaders--this prevents conflicts from threading or
         * multiple GSG's sharing shaders (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_shader is called).
         */
        """
        pass

    def release_shader_buffer(self, const_PreparedGraphicsObjects_self, BufferContext_bc): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_shader_buffer(const PreparedGraphicsObjects self, BufferContext bc)
        
        /**
         * Indicates that a data context, created by a previous call to
         * prepare_shader_buffer(), is no longer needed.  The driver resources will not
         * be freed until some GSG calls update(), indicating it is at a stage where
         * it is ready to release datas--this prevents conflicts from threading or
         * multiple GSG's sharing datas (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_shader_buffer is called).
         */
        """
        pass

    def release_texture(self, const_PreparedGraphicsObjects_self, TextureContext_tc): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_texture(const PreparedGraphicsObjects self, TextureContext tc)
        release_texture(const PreparedGraphicsObjects self, Texture tex)
        
        /**
         * Indicates that a texture context, created by a previous call to
         * prepare_texture(), is no longer needed.  The driver resources will not be
         * freed until some GSG calls update(), indicating it is at a stage where it
         * is ready to release textures--this prevents conflicts from threading or
         * multiple GSG's sharing textures (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_texture is called).
         */
        
        /**
         * Releases a texture if it has already been prepared, or removes it from the
         * preparation queue.
         */
        """
        pass

    def release_vertex_buffer(self, const_PreparedGraphicsObjects_self, VertexBufferContext_vbc): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_vertex_buffer(const PreparedGraphicsObjects self, VertexBufferContext vbc)
        
        /**
         * Indicates that a data context, created by a previous call to
         * prepare_vertex_buffer(), is no longer needed.  The driver resources will
         * not be freed until some GSG calls update(), indicating it is at a stage
         * where it is ready to release datas--this prevents conflicts from threading
         * or multiple GSG's sharing datas (we have no way of knowing which graphics
         * context is currently active, or what state it's in, at the time
         * release_vertex_buffer is called).
         */
        """
        pass

    def setGraphicsMemoryLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_graphics_memory_limit(const PreparedGraphicsObjects self, int limit)
        
        /**
         * Sets an artificial cap on graphics memory that will be imposed on this GSG.
         *
         * This limits the total amount of graphics memory, including texture memory
         * and vertex buffer memory, that will be consumed by the GSG, regardless of
         * whether the hardware claims to provide more graphics memory than this.  It
         * is useful to put a ceiling on graphics memory consumed, since some drivers
         * seem to allow the application to consume more memory than the hardware can
         * realistically support.
         */
        """
        pass

    def set_graphics_memory_limit(self, const_PreparedGraphicsObjects_self, int_limit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_graphics_memory_limit(const PreparedGraphicsObjects self, int limit)
        
        /**
         * Sets an artificial cap on graphics memory that will be imposed on this GSG.
         *
         * This limits the total amount of graphics memory, including texture memory
         * and vertex buffer memory, that will be consumed by the GSG, regardless of
         * whether the hardware claims to provide more graphics memory than this.  It
         * is useful to put a ceiling on graphics memory consumed, since some drivers
         * seem to allow the application to consume more memory than the hardware can
         * realistically support.
         */
        """
        pass

    def showGraphicsMemoryLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_graphics_memory_lru(PreparedGraphicsObjects self, ostream out)
        
        /**
         * Writes to the indicated ostream a report of how the various textures and
         * vertex buffers are allocated in the LRU.
         */
        """
        pass

    def showResidencyTrackers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_residency_trackers(PreparedGraphicsObjects self, ostream out)
        
        /**
         * Writes to the indicated ostream a report of how the various textures and
         * vertex buffers are allocated in the LRU.
         */
        """
        pass

    def show_graphics_memory_lru(self, PreparedGraphicsObjects_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_graphics_memory_lru(PreparedGraphicsObjects self, ostream out)
        
        /**
         * Writes to the indicated ostream a report of how the various textures and
         * vertex buffers are allocated in the LRU.
         */
        """
        pass

    def show_residency_trackers(self, PreparedGraphicsObjects_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_residency_trackers(PreparedGraphicsObjects self, ostream out)
        
        /**
         * Writes to the indicated ostream a report of how the various textures and
         * vertex buffers are allocated in the LRU.
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
        '__doc__': "/**\n * A table of objects that are saved within the graphics context for reference\n * by handle later.  Generally, this represents things like OpenGL texture\n * objects or display lists (or their equivalent on other platforms).\n *\n * This object simply records the pointers to the context objects created by\n * the individual GSG's; these context objects will contain enough information\n * to reference or release the actual object stored within the graphics\n * context.\n *\n * These tables may potentially be shared between related graphics contexts,\n * hence their storage here in a separate object rather than as a part of the\n * GraphicsStateGuardian.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FF2B0>'
        'dequeueGeom': None, # (!) real value is "<method 'dequeueGeom' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeueIndexBuffer': None, # (!) real value is "<method 'dequeueIndexBuffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeueSampler': None, # (!) real value is "<method 'dequeueSampler' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeueShader': None, # (!) real value is "<method 'dequeueShader' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeueShaderBuffer': None, # (!) real value is "<method 'dequeueShaderBuffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeueTexture': None, # (!) real value is "<method 'dequeueTexture' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeueVertexBuffer': None, # (!) real value is "<method 'dequeueVertexBuffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeue_geom': None, # (!) real value is "<method 'dequeue_geom' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeue_index_buffer': None, # (!) real value is "<method 'dequeue_index_buffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeue_sampler': None, # (!) real value is "<method 'dequeue_sampler' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeue_shader': None, # (!) real value is "<method 'dequeue_shader' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeue_shader_buffer': None, # (!) real value is "<method 'dequeue_shader_buffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeue_texture': None, # (!) real value is "<method 'dequeue_texture' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'dequeue_vertex_buffer': None, # (!) real value is "<method 'dequeue_vertex_buffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueueGeom': None, # (!) real value is "<method 'enqueueGeom' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueueIndexBuffer': None, # (!) real value is "<method 'enqueueIndexBuffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueueSampler': None, # (!) real value is "<method 'enqueueSampler' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueueShader': None, # (!) real value is "<method 'enqueueShader' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueueShaderBuffer': None, # (!) real value is "<method 'enqueueShaderBuffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueueTexture': None, # (!) real value is "<method 'enqueueTexture' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueueVertexBuffer': None, # (!) real value is "<method 'enqueueVertexBuffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueue_geom': None, # (!) real value is "<method 'enqueue_geom' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueue_index_buffer': None, # (!) real value is "<method 'enqueue_index_buffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueue_sampler': None, # (!) real value is "<method 'enqueue_sampler' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueue_shader': None, # (!) real value is "<method 'enqueue_shader' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueue_shader_buffer': None, # (!) real value is "<method 'enqueue_shader_buffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueue_texture': None, # (!) real value is "<method 'enqueue_texture' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'enqueue_vertex_buffer': None, # (!) real value is "<method 'enqueue_vertex_buffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getGraphicsMemoryLimit': None, # (!) real value is "<method 'getGraphicsMemoryLimit' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumPrepared': None, # (!) real value is "<method 'getNumPrepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumPreparedGeoms': None, # (!) real value is "<method 'getNumPreparedGeoms' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumPreparedIndexBuffers': None, # (!) real value is "<method 'getNumPreparedIndexBuffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumPreparedSamplers': None, # (!) real value is "<method 'getNumPreparedSamplers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumPreparedShaderBuffers': None, # (!) real value is "<method 'getNumPreparedShaderBuffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumPreparedShaders': None, # (!) real value is "<method 'getNumPreparedShaders' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumPreparedTextures': None, # (!) real value is "<method 'getNumPreparedTextures' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumPreparedVertexBuffers': None, # (!) real value is "<method 'getNumPreparedVertexBuffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumQueued': None, # (!) real value is "<method 'getNumQueued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumQueuedGeoms': None, # (!) real value is "<method 'getNumQueuedGeoms' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumQueuedIndexBuffers': None, # (!) real value is "<method 'getNumQueuedIndexBuffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumQueuedSamplers': None, # (!) real value is "<method 'getNumQueuedSamplers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumQueuedShaderBuffers': None, # (!) real value is "<method 'getNumQueuedShaderBuffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumQueuedShaders': None, # (!) real value is "<method 'getNumQueuedShaders' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumQueuedTextures': None, # (!) real value is "<method 'getNumQueuedTextures' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'getNumQueuedVertexBuffers': None, # (!) real value is "<method 'getNumQueuedVertexBuffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_graphics_memory_limit': None, # (!) real value is "<method 'get_graphics_memory_limit' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_prepared': None, # (!) real value is "<method 'get_num_prepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_prepared_geoms': None, # (!) real value is "<method 'get_num_prepared_geoms' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_prepared_index_buffers': None, # (!) real value is "<method 'get_num_prepared_index_buffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_prepared_samplers': None, # (!) real value is "<method 'get_num_prepared_samplers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_prepared_shader_buffers': None, # (!) real value is "<method 'get_num_prepared_shader_buffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_prepared_shaders': None, # (!) real value is "<method 'get_num_prepared_shaders' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_prepared_textures': None, # (!) real value is "<method 'get_num_prepared_textures' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_prepared_vertex_buffers': None, # (!) real value is "<method 'get_num_prepared_vertex_buffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_queued': None, # (!) real value is "<method 'get_num_queued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_queued_geoms': None, # (!) real value is "<method 'get_num_queued_geoms' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_queued_index_buffers': None, # (!) real value is "<method 'get_num_queued_index_buffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_queued_samplers': None, # (!) real value is "<method 'get_num_queued_samplers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_queued_shader_buffers': None, # (!) real value is "<method 'get_num_queued_shader_buffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_queued_shaders': None, # (!) real value is "<method 'get_num_queued_shaders' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_queued_textures': None, # (!) real value is "<method 'get_num_queued_textures' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'get_num_queued_vertex_buffers': None, # (!) real value is "<method 'get_num_queued_vertex_buffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isGeomPrepared': None, # (!) real value is "<method 'isGeomPrepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isGeomQueued': None, # (!) real value is "<method 'isGeomQueued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isIndexBufferPrepared': None, # (!) real value is "<method 'isIndexBufferPrepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isIndexBufferQueued': None, # (!) real value is "<method 'isIndexBufferQueued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isSamplerPrepared': None, # (!) real value is "<method 'isSamplerPrepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isSamplerQueued': None, # (!) real value is "<method 'isSamplerQueued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isShaderBufferPrepared': None, # (!) real value is "<method 'isShaderBufferPrepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isShaderBufferQueued': None, # (!) real value is "<method 'isShaderBufferQueued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isShaderPrepared': None, # (!) real value is "<method 'isShaderPrepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isShaderQueued': None, # (!) real value is "<method 'isShaderQueued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isTexturePrepared': None, # (!) real value is "<method 'isTexturePrepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isTextureQueued': None, # (!) real value is "<method 'isTextureQueued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isVertexBufferPrepared': None, # (!) real value is "<method 'isVertexBufferPrepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'isVertexBufferQueued': None, # (!) real value is "<method 'isVertexBufferQueued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_geom_prepared': None, # (!) real value is "<method 'is_geom_prepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_geom_queued': None, # (!) real value is "<method 'is_geom_queued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_index_buffer_prepared': None, # (!) real value is "<method 'is_index_buffer_prepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_index_buffer_queued': None, # (!) real value is "<method 'is_index_buffer_queued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_sampler_prepared': None, # (!) real value is "<method 'is_sampler_prepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_sampler_queued': None, # (!) real value is "<method 'is_sampler_queued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_shader_buffer_prepared': None, # (!) real value is "<method 'is_shader_buffer_prepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_shader_buffer_queued': None, # (!) real value is "<method 'is_shader_buffer_queued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_shader_prepared': None, # (!) real value is "<method 'is_shader_prepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_shader_queued': None, # (!) real value is "<method 'is_shader_queued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_texture_prepared': None, # (!) real value is "<method 'is_texture_prepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_texture_queued': None, # (!) real value is "<method 'is_texture_queued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_vertex_buffer_prepared': None, # (!) real value is "<method 'is_vertex_buffer_prepared' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'is_vertex_buffer_queued': None, # (!) real value is "<method 'is_vertex_buffer_queued' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepareGeomNow': None, # (!) real value is "<method 'prepareGeomNow' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepareIndexBufferNow': None, # (!) real value is "<method 'prepareIndexBufferNow' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepareShaderBufferNow': None, # (!) real value is "<method 'prepareShaderBufferNow' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepareShaderNow': None, # (!) real value is "<method 'prepareShaderNow' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepareTextureNow': None, # (!) real value is "<method 'prepareTextureNow' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepareVertexBufferNow': None, # (!) real value is "<method 'prepareVertexBufferNow' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepare_geom_now': None, # (!) real value is "<method 'prepare_geom_now' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepare_index_buffer_now': None, # (!) real value is "<method 'prepare_index_buffer_now' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepare_shader_buffer_now': None, # (!) real value is "<method 'prepare_shader_buffer_now' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepare_shader_now': None, # (!) real value is "<method 'prepare_shader_now' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepare_texture_now': None, # (!) real value is "<method 'prepare_texture_now' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'prepare_vertex_buffer_now': None, # (!) real value is "<method 'prepare_vertex_buffer_now' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseAll': None, # (!) real value is "<method 'releaseAll' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseAllGeoms': None, # (!) real value is "<method 'releaseAllGeoms' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseAllIndexBuffers': None, # (!) real value is "<method 'releaseAllIndexBuffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseAllSamplers': None, # (!) real value is "<method 'releaseAllSamplers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseAllShaderBuffers': None, # (!) real value is "<method 'releaseAllShaderBuffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseAllShaders': None, # (!) real value is "<method 'releaseAllShaders' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseAllTextures': None, # (!) real value is "<method 'releaseAllTextures' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseAllVertexBuffers': None, # (!) real value is "<method 'releaseAllVertexBuffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseGeom': None, # (!) real value is "<method 'releaseGeom' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseIndexBuffer': None, # (!) real value is "<method 'releaseIndexBuffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseSampler': None, # (!) real value is "<method 'releaseSampler' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseShader': None, # (!) real value is "<method 'releaseShader' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseShaderBuffer': None, # (!) real value is "<method 'releaseShaderBuffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseTexture': None, # (!) real value is "<method 'releaseTexture' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'releaseVertexBuffer': None, # (!) real value is "<method 'releaseVertexBuffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_all': None, # (!) real value is "<method 'release_all' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_all_geoms': None, # (!) real value is "<method 'release_all_geoms' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_all_index_buffers': None, # (!) real value is "<method 'release_all_index_buffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_all_samplers': None, # (!) real value is "<method 'release_all_samplers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_all_shader_buffers': None, # (!) real value is "<method 'release_all_shader_buffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_all_shaders': None, # (!) real value is "<method 'release_all_shaders' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_all_textures': None, # (!) real value is "<method 'release_all_textures' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_all_vertex_buffers': None, # (!) real value is "<method 'release_all_vertex_buffers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_geom': None, # (!) real value is "<method 'release_geom' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_index_buffer': None, # (!) real value is "<method 'release_index_buffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_sampler': None, # (!) real value is "<method 'release_sampler' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_shader': None, # (!) real value is "<method 'release_shader' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_shader_buffer': None, # (!) real value is "<method 'release_shader_buffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_texture': None, # (!) real value is "<method 'release_texture' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'release_vertex_buffer': None, # (!) real value is "<method 'release_vertex_buffer' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'setGraphicsMemoryLimit': None, # (!) real value is "<method 'setGraphicsMemoryLimit' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'set_graphics_memory_limit': None, # (!) real value is "<method 'set_graphics_memory_limit' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'showGraphicsMemoryLru': None, # (!) real value is "<method 'showGraphicsMemoryLru' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'showResidencyTrackers': None, # (!) real value is "<method 'showResidencyTrackers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'show_graphics_memory_lru': None, # (!) real value is "<method 'show_graphics_memory_lru' of 'panda3d.core.PreparedGraphicsObjects' objects>"
        'show_residency_trackers': None, # (!) real value is "<method 'show_residency_trackers' of 'panda3d.core.PreparedGraphicsObjects' objects>"
    }


