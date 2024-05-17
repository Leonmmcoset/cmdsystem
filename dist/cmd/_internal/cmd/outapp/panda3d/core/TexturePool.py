# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TexturePool(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is the preferred interface for loading textures from image files.  It
     * unifies all references to the same filename, so that multiple models that
     * reference the same textures don't waste texture memory unnecessarily.
     */
    """
    def addTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_texture(Texture texture)
        
        /**
         * Adds the indicated already-loaded texture to the pool.  The texture must
         * have a filename set for its name.  The texture will always replace any
         * previously-loaded texture in the pool that had the same filename.
         */
        """
        pass

    def add_texture(self, Texture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_texture(Texture texture)
        
        /**
         * Adds the indicated already-loaded texture to the pool.  The texture must
         * have a filename set for its name.  The texture will always replace any
         * previously-loaded texture in the pool that had the same filename.
         */
        """
        pass

    def clearFakeTextureImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_fake_texture_image()
        
        /**
         * Restores normal behavior of loading the textures actually requested.
         */
        """
        pass

    def clear_fake_texture_image(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_fake_texture_image()
        
        /**
         * Restores normal behavior of loading the textures actually requested.
         */
        """
        pass

    def findAllTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_textures(str name)
        
        /**
         * Returns the set of all textures found in the pool that match the indicated
         * name (which may contain wildcards).
         */
        """
        pass

    def findTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_texture(str name)
        
        /**
         * Returns the first texture found in the pool that matches the indicated name
         * (which may contain wildcards).  Returns the texture if it is found, or NULL
         * if it is not.
         */
        """
        pass

    def find_all_textures(self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_textures(str name)
        
        /**
         * Returns the set of all textures found in the pool that match the indicated
         * name (which may contain wildcards).
         */
        """
        pass

    def find_texture(self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_texture(str name)
        
        /**
         * Returns the first texture found in the pool that matches the indicated name
         * (which may contain wildcards).  Returns the texture if it is found, or NULL
         * if it is not.
         */
        """
        pass

    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those textures in the pool that have a reference count of
         * exactly 1; i.e.  only those textures that are not being used outside of the
         * pool.  Returns the number of textures released.
         */
        """
        pass

    def garbage_collect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those textures in the pool that have a reference count of
         * exactly 1; i.e.  only those textures that are not being used outside of the
         * pool.  Returns the number of textures released.
         */
        """
        pass

    def getAlphaScaleMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_scale_map()
        
        /**
         * Returns a standard Texture object that has been created with
         * Texture::generate_alpha_scale_map().
         *
         * This Texture object is used internally by Panda to apply an alpha scale to
         * an object (instead of munging its vertices) when
         * gsg->get_alpha_scale_via_texture() returns true.
         */
        """
        pass

    def getFakeTextureImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fake_texture_image()
        
        /**
         * Returns the filename that was specified with a previous call to
         * set_fake_texture_image().
         */
        """
        pass

    def getNormalizationCubeMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_normalization_cube_map(int size)
        
        /**
         * Returns a standard Texture object that has been created with
         * Texture::generate_normalization_cube_map().  This Texture may be shared by
         * any application code requiring a normalization cube map.  It will be at
         * least as large as the specified size, though it may be larger.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(const Filename filename)
        get_texture(const Filename filename, const Filename alpha_filename, int primary_file_num_channels, int alpha_file_channel, bool read_mipmaps)
        get_texture(const Filename filename, int primary_file_num_channels, bool read_mipmaps)
        
        /**
         * Returns the texture that has already been previously loaded, or NULL
         * otherwise.
         */
        
        /**
         * Returns the texture that has already been previously loaded, or NULL
         * otherwise.
         */
        """
        pass

    def get_alpha_scale_map(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_scale_map()
        
        /**
         * Returns a standard Texture object that has been created with
         * Texture::generate_alpha_scale_map().
         *
         * This Texture object is used internally by Panda to apply an alpha scale to
         * an object (instead of munging its vertices) when
         * gsg->get_alpha_scale_via_texture() returns true.
         */
        """
        pass

    def get_fake_texture_image(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fake_texture_image()
        
        /**
         * Returns the filename that was specified with a previous call to
         * set_fake_texture_image().
         */
        """
        pass

    def get_normalization_cube_map(self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_normalization_cube_map(int size)
        
        /**
         * Returns a standard Texture object that has been created with
         * Texture::generate_normalization_cube_map().  This Texture may be shared by
         * any application code requiring a normalization cube map.  It will be at
         * least as large as the specified size, though it may be larger.
         */
        """
        pass

    def get_texture(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(const Filename filename)
        get_texture(const Filename filename, const Filename alpha_filename, int primary_file_num_channels, int alpha_file_channel, bool read_mipmaps)
        get_texture(const Filename filename, int primary_file_num_channels, bool read_mipmaps)
        
        /**
         * Returns the texture that has already been previously loaded, or NULL
         * otherwise.
         */
        
        /**
         * Returns the texture that has already been previously loaded, or NULL
         * otherwise.
         */
        """
        pass

    def hasFakeTextureImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_fake_texture_image()
        
        /**
         * Returns true if fake_texture_image mode has been enabled, false if we are
         * in the normal mode.
         */
        """
        pass

    def hasTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_texture(const Filename filename)
        
        /**
         * Returns true if the texture has ever been loaded, false otherwise.
         */
        """
        pass

    def has_fake_texture_image(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_fake_texture_image()
        
        /**
         * Returns true if fake_texture_image mode has been enabled, false if we are
         * in the normal mode.
         */
        """
        pass

    def has_texture(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_texture(const Filename filename)
        
        /**
         * Returns true if the texture has ever been loaded, false otherwise.
         */
        """
        pass

    def listContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_contents()
        list_contents(ostream out)
        
        /**
         * Lists the contents of the texture pool to the indicated output stream.
         */
        
        /**
         * Lists the contents of the texture pool to cout
         */
        """
        pass

    def list_contents(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_contents()
        list_contents(ostream out)
        
        /**
         * Lists the contents of the texture pool to the indicated output stream.
         */
        
        /**
         * Lists the contents of the texture pool to cout
         */
        """
        pass

    def load2dTextureArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_2d_texture_array(const Filename filename_pattern, bool read_mipmaps, const LoaderOptions options)
        
        /**
         * Loads a 2-D texture array that is specified with a series of n pages, all
         * numbered in sequence, and beginning with index 0.  The filename should
         * include a sequence of one or more hash characters ("#") which will be
         * filled in with the index number of each level.
         *
         * If read_mipmaps is true, the filename should contain an additional hash
         * mark.  The first hash mark will be filled in with the mipmap level number,
         * and the second with the index number of each 2-d level.
         */
        """
        pass

    def load3dTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_3d_texture(const Filename filename_pattern, bool read_mipmaps, const LoaderOptions options)
        
        /**
         * Loads a 3-D texture that is specified with a series of n pages, all
         * numbered in sequence, and beginning with index 0.  The filename should
         * include a sequence of one or more hash characters ("#") which will be
         * filled in with the index number of each level.
         *
         * If read_mipmaps is true, the filename should contain an additional hash
         * mark.  The first hash mark will be filled in with the mipmap level number,
         * and the second with the index number of each 3-d level.
         */
        """
        pass

    def loadCubeMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_cube_map(const Filename filename_pattern, bool read_mipmaps, const LoaderOptions options)
        
        /**
         * Loads a cube map texture that is specified with a series of 6 pages,
         * numbered 0 through 5.  The filename should include a sequence of one or
         * more hash characters ("#") which will be filled in with the index number of
         * each pagee.
         *
         * If read_mipmaps is true, the filename should contain an additional hash
         * mark.  The first hash mark will be filled in with the mipmap level number,
         * and the second with the face number, 0 through 5.
         */
        """
        pass

    def loadTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_texture(const Filename filename)
        load_texture(const Filename filename, const Filename alpha_filename, int primary_file_num_channels, int alpha_file_channel, bool read_mipmaps, const LoaderOptions options)
        load_texture(const Filename filename, int primary_file_num_channels, bool read_mipmaps, const LoaderOptions options)
        
        /**
         * Loads the given filename up into a texture, if it has not already been
         * loaded, and returns the new texture.  If a texture with the same filename
         * was previously loaded, returns that one instead.  If the texture file
         * cannot be found, returns NULL.
         *
         * If read_mipmaps is true, the filename should contain a hash mark ('#'),
         * which will be filled in with the mipmap level number; and the texture will
         * be defined with a series of images, one for each mipmap level.
         */
        
        /**
         * Loads the given filename up into a texture, if it has not already been
         * loaded, and returns the new texture.  If a texture with the same filename
         * was previously loaded, returns that one instead.  If the texture file
         * cannot be found, returns NULL.
         *
         * If read_mipmaps is true, both filenames should contain a hash mark ('#'),
         * which will be filled in with the mipmap level number; and the texture will
         * be defined with a series of images, two for each mipmap level.
         */
        """
        pass

    def load_2d_texture_array(self, const_Filename_filename_pattern, bool_read_mipmaps, const_LoaderOptions_options): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_2d_texture_array(const Filename filename_pattern, bool read_mipmaps, const LoaderOptions options)
        
        /**
         * Loads a 2-D texture array that is specified with a series of n pages, all
         * numbered in sequence, and beginning with index 0.  The filename should
         * include a sequence of one or more hash characters ("#") which will be
         * filled in with the index number of each level.
         *
         * If read_mipmaps is true, the filename should contain an additional hash
         * mark.  The first hash mark will be filled in with the mipmap level number,
         * and the second with the index number of each 2-d level.
         */
        """
        pass

    def load_3d_texture(self, const_Filename_filename_pattern, bool_read_mipmaps, const_LoaderOptions_options): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_3d_texture(const Filename filename_pattern, bool read_mipmaps, const LoaderOptions options)
        
        /**
         * Loads a 3-D texture that is specified with a series of n pages, all
         * numbered in sequence, and beginning with index 0.  The filename should
         * include a sequence of one or more hash characters ("#") which will be
         * filled in with the index number of each level.
         *
         * If read_mipmaps is true, the filename should contain an additional hash
         * mark.  The first hash mark will be filled in with the mipmap level number,
         * and the second with the index number of each 3-d level.
         */
        """
        pass

    def load_cube_map(self, const_Filename_filename_pattern, bool_read_mipmaps, const_LoaderOptions_options): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_cube_map(const Filename filename_pattern, bool read_mipmaps, const LoaderOptions options)
        
        /**
         * Loads a cube map texture that is specified with a series of 6 pages,
         * numbered 0 through 5.  The filename should include a sequence of one or
         * more hash characters ("#") which will be filled in with the index number of
         * each pagee.
         *
         * If read_mipmaps is true, the filename should contain an additional hash
         * mark.  The first hash mark will be filled in with the mipmap level number,
         * and the second with the face number, 0 through 5.
         */
        """
        pass

    def load_texture(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_texture(const Filename filename)
        load_texture(const Filename filename, const Filename alpha_filename, int primary_file_num_channels, int alpha_file_channel, bool read_mipmaps, const LoaderOptions options)
        load_texture(const Filename filename, int primary_file_num_channels, bool read_mipmaps, const LoaderOptions options)
        
        /**
         * Loads the given filename up into a texture, if it has not already been
         * loaded, and returns the new texture.  If a texture with the same filename
         * was previously loaded, returns that one instead.  If the texture file
         * cannot be found, returns NULL.
         *
         * If read_mipmaps is true, the filename should contain a hash mark ('#'),
         * which will be filled in with the mipmap level number; and the texture will
         * be defined with a series of images, one for each mipmap level.
         */
        
        /**
         * Loads the given filename up into a texture, if it has not already been
         * loaded, and returns the new texture.  If a texture with the same filename
         * was previously loaded, returns that one instead.  If the texture file
         * cannot be found, returns NULL.
         *
         * If read_mipmaps is true, both filenames should contain a hash mark ('#'),
         * which will be filled in with the mipmap level number; and the texture will
         * be defined with a series of images, two for each mipmap level.
         */
        """
        pass

    def makeTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_texture(str extension)
        
        /**
         * Creates a new Texture object of the appropriate type for the indicated
         * filename extension, according to the types that have been registered via
         * register_texture_type().
         */
        """
        pass

    def make_texture(self, str_extension): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_texture(str extension)
        
        /**
         * Creates a new Texture object of the appropriate type for the indicated
         * filename extension, according to the types that have been registered via
         * register_texture_type().
         */
        """
        pass

    def rehash(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rehash()
        
        /**
         * Should be called when the model-path changes, to blow away the cache of
         * texture pathnames found along the model-path.
         */
        """
        pass

    def releaseAllTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_textures()
        
        /**
         * Releases all textures in the pool and restores the pool to the empty state.
         */
        """
        pass

    def releaseTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_texture(Texture texture)
        
        /**
         * Removes the indicated texture from the pool, indicating it will never be
         * loaded again; the texture may then be freed.  If this function is never
         * called, a reference count will be maintained on every texture every loaded,
         * and textures will never be freed.
         *
         * The texture's name should not have been changed during its lifetime, or
         * this function may fail to locate it in the pool.
         */
        """
        pass

    def release_all_textures(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_textures()
        
        /**
         * Releases all textures in the pool and restores the pool to the empty state.
         */
        """
        pass

    def release_texture(self, Texture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_texture(Texture texture)
        
        /**
         * Removes the indicated texture from the pool, indicating it will never be
         * loaded again; the texture may then be freed.  If this function is never
         * called, a reference count will be maintained on every texture every loaded,
         * and textures will never be freed.
         *
         * The texture's name should not have been changed during its lifetime, or
         * this function may fail to locate it in the pool.
         */
        """
        pass

    def setFakeTextureImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fake_texture_image(const Filename filename)
        
        /**
         * Sets a bogus filename that will be loaded in lieu of any textures requested
         * from this point on.
         */
        """
        pass

    def set_fake_texture_image(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fake_texture_image(const Filename filename)
        
        /**
         * Sets a bogus filename that will be loaded in lieu of any textures requested
         * from this point on.
         */
        """
        pass

    def verifyTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        verify_texture(const Filename filename)
        
        /**
         * Loads the given filename up into a texture, if it has not already been
         * loaded, and returns true to indicate success, or false to indicate failure.
         * If this returns true, it is guaranteed that a subsequent call to
         * load_texture() with the same texture name will return a valid Texture
         * pointer.
         */
        """
        pass

    def verify_texture(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        verify_texture(const Filename filename)
        
        /**
         * Loads the given filename up into a texture, if it has not already been
         * loaded, and returns true to indicate success, or false to indicate failure.
         * If this returns true, it is guaranteed that a subsequent call to
         * load_texture() with the same texture name will return a valid Texture
         * pointer.
         */
        """
        pass

    def write(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ostream out)
        
        /**
         * Lists the contents of the texture pool to the indicated output stream.  For
         * debugging.
         */
        """
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
        '__doc__': "/**\n * This is the preferred interface for loading textures from image files.  It\n * unifies all references to the same filename, so that multiple models that\n * reference the same textures don't waste texture memory unnecessarily.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TexturePool' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE301350>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TexturePool' objects>"
        'addTexture': None, # (!) real value is '<staticmethod(<built-in method addTexture of type object at 0x00007FFCFE301350>)>'
        'add_texture': None, # (!) real value is '<staticmethod(<built-in method add_texture of type object at 0x00007FFCFE301350>)>'
        'clearFakeTextureImage': None, # (!) real value is '<staticmethod(<built-in method clearFakeTextureImage of type object at 0x00007FFCFE301350>)>'
        'clear_fake_texture_image': None, # (!) real value is '<staticmethod(<built-in method clear_fake_texture_image of type object at 0x00007FFCFE301350>)>'
        'findAllTextures': None, # (!) real value is '<staticmethod(<built-in method findAllTextures of type object at 0x00007FFCFE301350>)>'
        'findTexture': None, # (!) real value is '<staticmethod(<built-in method findTexture of type object at 0x00007FFCFE301350>)>'
        'find_all_textures': None, # (!) real value is '<staticmethod(<built-in method find_all_textures of type object at 0x00007FFCFE301350>)>'
        'find_texture': None, # (!) real value is '<staticmethod(<built-in method find_texture of type object at 0x00007FFCFE301350>)>'
        'garbageCollect': None, # (!) real value is '<staticmethod(<built-in method garbageCollect of type object at 0x00007FFCFE301350>)>'
        'garbage_collect': None, # (!) real value is '<staticmethod(<built-in method garbage_collect of type object at 0x00007FFCFE301350>)>'
        'getAlphaScaleMap': None, # (!) real value is '<staticmethod(<built-in method getAlphaScaleMap of type object at 0x00007FFCFE301350>)>'
        'getFakeTextureImage': None, # (!) real value is '<staticmethod(<built-in method getFakeTextureImage of type object at 0x00007FFCFE301350>)>'
        'getNormalizationCubeMap': None, # (!) real value is '<staticmethod(<built-in method getNormalizationCubeMap of type object at 0x00007FFCFE301350>)>'
        'getTexture': None, # (!) real value is '<staticmethod(<built-in method getTexture of type object at 0x00007FFCFE301350>)>'
        'get_alpha_scale_map': None, # (!) real value is '<staticmethod(<built-in method get_alpha_scale_map of type object at 0x00007FFCFE301350>)>'
        'get_fake_texture_image': None, # (!) real value is '<staticmethod(<built-in method get_fake_texture_image of type object at 0x00007FFCFE301350>)>'
        'get_normalization_cube_map': None, # (!) real value is '<staticmethod(<built-in method get_normalization_cube_map of type object at 0x00007FFCFE301350>)>'
        'get_texture': None, # (!) real value is '<staticmethod(<built-in method get_texture of type object at 0x00007FFCFE301350>)>'
        'hasFakeTextureImage': None, # (!) real value is '<staticmethod(<built-in method hasFakeTextureImage of type object at 0x00007FFCFE301350>)>'
        'hasTexture': None, # (!) real value is '<staticmethod(<built-in method hasTexture of type object at 0x00007FFCFE301350>)>'
        'has_fake_texture_image': None, # (!) real value is '<staticmethod(<built-in method has_fake_texture_image of type object at 0x00007FFCFE301350>)>'
        'has_texture': None, # (!) real value is '<staticmethod(<built-in method has_texture of type object at 0x00007FFCFE301350>)>'
        'listContents': None, # (!) real value is '<staticmethod(<built-in method listContents of type object at 0x00007FFCFE301350>)>'
        'list_contents': None, # (!) real value is '<staticmethod(<built-in method list_contents of type object at 0x00007FFCFE301350>)>'
        'load2dTextureArray': None, # (!) real value is '<staticmethod(<built-in method load2dTextureArray of type object at 0x00007FFCFE301350>)>'
        'load3dTexture': None, # (!) real value is '<staticmethod(<built-in method load3dTexture of type object at 0x00007FFCFE301350>)>'
        'loadCubeMap': None, # (!) real value is '<staticmethod(<built-in method loadCubeMap of type object at 0x00007FFCFE301350>)>'
        'loadTexture': None, # (!) real value is '<staticmethod(<built-in method loadTexture of type object at 0x00007FFCFE301350>)>'
        'load_2d_texture_array': None, # (!) real value is '<staticmethod(<built-in method load_2d_texture_array of type object at 0x00007FFCFE301350>)>'
        'load_3d_texture': None, # (!) real value is '<staticmethod(<built-in method load_3d_texture of type object at 0x00007FFCFE301350>)>'
        'load_cube_map': None, # (!) real value is '<staticmethod(<built-in method load_cube_map of type object at 0x00007FFCFE301350>)>'
        'load_texture': None, # (!) real value is '<staticmethod(<built-in method load_texture of type object at 0x00007FFCFE301350>)>'
        'makeTexture': None, # (!) real value is '<staticmethod(<built-in method makeTexture of type object at 0x00007FFCFE301350>)>'
        'make_texture': None, # (!) real value is '<staticmethod(<built-in method make_texture of type object at 0x00007FFCFE301350>)>'
        'rehash': None, # (!) real value is '<staticmethod(<built-in method rehash of type object at 0x00007FFCFE301350>)>'
        'releaseAllTextures': None, # (!) real value is '<staticmethod(<built-in method releaseAllTextures of type object at 0x00007FFCFE301350>)>'
        'releaseTexture': None, # (!) real value is '<staticmethod(<built-in method releaseTexture of type object at 0x00007FFCFE301350>)>'
        'release_all_textures': None, # (!) real value is '<staticmethod(<built-in method release_all_textures of type object at 0x00007FFCFE301350>)>'
        'release_texture': None, # (!) real value is '<staticmethod(<built-in method release_texture of type object at 0x00007FFCFE301350>)>'
        'setFakeTextureImage': None, # (!) real value is '<staticmethod(<built-in method setFakeTextureImage of type object at 0x00007FFCFE301350>)>'
        'set_fake_texture_image': None, # (!) real value is '<staticmethod(<built-in method set_fake_texture_image of type object at 0x00007FFCFE301350>)>'
        'verifyTexture': None, # (!) real value is '<staticmethod(<built-in method verifyTexture of type object at 0x00007FFCFE301350>)>'
        'verify_texture': None, # (!) real value is '<staticmethod(<built-in method verify_texture of type object at 0x00007FFCFE301350>)>'
        'write': None, # (!) real value is '<staticmethod(<built-in method write of type object at 0x00007FFCFE301350>)>'
    }


