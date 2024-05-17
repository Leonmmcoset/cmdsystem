# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ShaderPool(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is the preferred interface for loading shaders for the TextNode
     * system.  It is similar to ModelPool and TexturePool in that it unifies
     * references to the same filename.
     */
    """
    def addShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_shader(const Filename filename, Shader shader)
        
        /**
         * Adds the indicated already-loaded shader to the pool.  The shader will
         * always replace any previously-loaded shader in the pool that had the same
         * filename.
         */
        """
        pass

    def add_shader(self, const_Filename_filename, Shader_shader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_shader(const Filename filename, Shader shader)
        
        /**
         * Adds the indicated already-loaded shader to the pool.  The shader will
         * always replace any previously-loaded shader in the pool that had the same
         * filename.
         */
        """
        pass

    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those shaders in the pool that have a reference count of
         * exactly 1; i.e.  only those shaders that are not being used outside of the
         * pool.  Returns the number of shaders released.
         */
        """
        pass

    def garbage_collect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those shaders in the pool that have a reference count of
         * exactly 1; i.e.  only those shaders that are not being used outside of the
         * pool.  Returns the number of shaders released.
         */
        """
        pass

    def hasShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_shader(const Filename filename)
        
        /**
         * Returns true if the shader has ever been loaded, false otherwise.
         */
        """
        pass

    def has_shader(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_shader(const Filename filename)
        
        /**
         * Returns true if the shader has ever been loaded, false otherwise.
         */
        """
        pass

    def listContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_contents(ostream out)
        
        /**
         * Lists the contents of the shader pool to the indicated output stream.
         */
        """
        pass

    def list_contents(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_contents(ostream out)
        
        /**
         * Lists the contents of the shader pool to the indicated output stream.
         */
        """
        pass

    def loadShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_shader(const Filename filename)
        
        /**
         * Loads the given filename up into a shader, if it has not already been
         * loaded, and returns the new shader.  If a shader with the same filename was
         * previously loaded, returns that one instead.  If the shader file cannot be
         * found, returns NULL.
         */
        """
        pass

    def load_shader(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_shader(const Filename filename)
        
        /**
         * Loads the given filename up into a shader, if it has not already been
         * loaded, and returns the new shader.  If a shader with the same filename was
         * previously loaded, returns that one instead.  If the shader file cannot be
         * found, returns NULL.
         */
        """
        pass

    def releaseAllShaders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_shaders()
        
        /**
         * Releases all shaders in the pool and restores the pool to the empty state.
         */
        """
        pass

    def releaseShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_shader(const Filename filename)
        
        /**
         * Removes the indicated shader from the pool, indicating it will never be
         * loaded again; the shader may then be freed.  If this function is never
         * called, a reference count will be maintained on every shader every loaded,
         * and shaders will never be freed.
         */
        """
        pass

    def release_all_shaders(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_shaders()
        
        /**
         * Releases all shaders in the pool and restores the pool to the empty state.
         */
        """
        pass

    def release_shader(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_shader(const Filename filename)
        
        /**
         * Removes the indicated shader from the pool, indicating it will never be
         * loaded again; the shader may then be freed.  If this function is never
         * called, a reference count will be maintained on every shader every loaded,
         * and shaders will never be freed.
         */
        """
        pass

    def verifyShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        verify_shader(const Filename filename)
        
        /**
         * Loads the given filename up into a shader, if it has not already been
         * loaded, and returns true to indicate success, or false to indicate failure.
         * If this returns true, it is guaranteed that a subsequent call to
         * load_shader() with the same shader name will return a valid Shader pointer.
         */
        """
        pass

    def verify_shader(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        verify_shader(const Filename filename)
        
        /**
         * Loads the given filename up into a shader, if it has not already been
         * loaded, and returns true to indicate success, or false to indicate failure.
         * If this returns true, it is guaranteed that a subsequent call to
         * load_shader() with the same shader name will return a valid Shader pointer.
         */
        """
        pass

    def write(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ostream out)
        
        /**
         * Lists the contents of the shader pool to the indicated output stream.
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
        '__doc__': '/**\n * This is the preferred interface for loading shaders for the TextNode\n * system.  It is similar to ModelPool and TexturePool in that it unifies\n * references to the same filename.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ShaderPool' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE29B3E0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ShaderPool' objects>"
        'addShader': None, # (!) real value is '<staticmethod(<built-in method addShader of type object at 0x00007FFCFE29B3E0>)>'
        'add_shader': None, # (!) real value is '<staticmethod(<built-in method add_shader of type object at 0x00007FFCFE29B3E0>)>'
        'garbageCollect': None, # (!) real value is '<staticmethod(<built-in method garbageCollect of type object at 0x00007FFCFE29B3E0>)>'
        'garbage_collect': None, # (!) real value is '<staticmethod(<built-in method garbage_collect of type object at 0x00007FFCFE29B3E0>)>'
        'hasShader': None, # (!) real value is '<staticmethod(<built-in method hasShader of type object at 0x00007FFCFE29B3E0>)>'
        'has_shader': None, # (!) real value is '<staticmethod(<built-in method has_shader of type object at 0x00007FFCFE29B3E0>)>'
        'listContents': None, # (!) real value is '<staticmethod(<built-in method listContents of type object at 0x00007FFCFE29B3E0>)>'
        'list_contents': None, # (!) real value is '<staticmethod(<built-in method list_contents of type object at 0x00007FFCFE29B3E0>)>'
        'loadShader': None, # (!) real value is '<staticmethod(<built-in method loadShader of type object at 0x00007FFCFE29B3E0>)>'
        'load_shader': None, # (!) real value is '<staticmethod(<built-in method load_shader of type object at 0x00007FFCFE29B3E0>)>'
        'releaseAllShaders': None, # (!) real value is '<staticmethod(<built-in method releaseAllShaders of type object at 0x00007FFCFE29B3E0>)>'
        'releaseShader': None, # (!) real value is '<staticmethod(<built-in method releaseShader of type object at 0x00007FFCFE29B3E0>)>'
        'release_all_shaders': None, # (!) real value is '<staticmethod(<built-in method release_all_shaders of type object at 0x00007FFCFE29B3E0>)>'
        'release_shader': None, # (!) real value is '<staticmethod(<built-in method release_shader of type object at 0x00007FFCFE29B3E0>)>'
        'verifyShader': None, # (!) real value is '<staticmethod(<built-in method verifyShader of type object at 0x00007FFCFE29B3E0>)>'
        'verify_shader': None, # (!) real value is '<staticmethod(<built-in method verify_shader of type object at 0x00007FFCFE29B3E0>)>'
        'write': None, # (!) real value is '<staticmethod(<built-in method write of type object at 0x00007FFCFE29B3E0>)>'
    }


