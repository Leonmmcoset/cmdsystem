# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class FontPool(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is the preferred interface for loading fonts for the TextNode system.
     * It is similar to ModelPool and TexturePool in that it unifies references to
     * the same filename.
     */
    """
    def addFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_font(str filename, TextFont font)
        
        /**
         * Adds the indicated already-loaded font to the pool.  The font will always
         * replace any previously-loaded font in the pool that had the same filename.
         */
        """
        pass

    def add_font(self, str_filename, TextFont_font): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_font(str filename, TextFont font)
        
        /**
         * Adds the indicated already-loaded font to the pool.  The font will always
         * replace any previously-loaded font in the pool that had the same filename.
         */
        """
        pass

    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those fonts in the pool that have a reference count of
         * exactly 1; i.e.  only those fonts that are not being used outside of the
         * pool.  Returns the number of fonts released.
         */
        """
        pass

    def garbage_collect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those fonts in the pool that have a reference count of
         * exactly 1; i.e.  only those fonts that are not being used outside of the
         * pool.  Returns the number of fonts released.
         */
        """
        pass

    def hasFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_font(str filename)
        
        /**
         * Returns true if the font has ever been loaded, false otherwise.
         */
        """
        pass

    def has_font(self, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_font(str filename)
        
        /**
         * Returns true if the font has ever been loaded, false otherwise.
         */
        """
        pass

    def listContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_contents(ostream out)
        
        /**
         * Lists the contents of the font pool to the indicated output stream.
         */
        """
        pass

    def list_contents(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_contents(ostream out)
        
        /**
         * Lists the contents of the font pool to the indicated output stream.
         */
        """
        pass

    def loadFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_font(str filename)
        
        /**
         * Loads the given filename up into a font, if it has not already been loaded,
         * and returns the new font.  If a font with the same filename was previously
         * loaded, returns that one instead.  If the font file cannot be found,
         * returns NULL.
         */
        """
        pass

    def load_font(self, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_font(str filename)
        
        /**
         * Loads the given filename up into a font, if it has not already been loaded,
         * and returns the new font.  If a font with the same filename was previously
         * loaded, returns that one instead.  If the font file cannot be found,
         * returns NULL.
         */
        """
        pass

    def releaseAllFonts(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_fonts()
        
        /**
         * Releases all fonts in the pool and restores the pool to the empty state.
         */
        """
        pass

    def releaseFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_font(str filename)
        
        /**
         * Removes the indicated font from the pool, indicating it will never be
         * loaded again; the font may then be freed.  If this function is never
         * called, a reference count will be maintained on every font every loaded,
         * and fonts will never be freed.
         */
        """
        pass

    def release_all_fonts(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_fonts()
        
        /**
         * Releases all fonts in the pool and restores the pool to the empty state.
         */
        """
        pass

    def release_font(self, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_font(str filename)
        
        /**
         * Removes the indicated font from the pool, indicating it will never be
         * loaded again; the font may then be freed.  If this function is never
         * called, a reference count will be maintained on every font every loaded,
         * and fonts will never be freed.
         */
        """
        pass

    def verifyFont(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        verify_font(str filename)
        
        /**
         * Loads the given filename up into a font, if it has not already been loaded,
         * and returns true to indicate success, or false to indicate failure.  If
         * this returns true, it is guaranteed that a subsequent call to load_font()
         * with the same font name will return a valid Font pointer.
         */
        """
        pass

    def verify_font(self, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        verify_font(str filename)
        
        /**
         * Loads the given filename up into a font, if it has not already been loaded,
         * and returns true to indicate success, or false to indicate failure.  If
         * this returns true, it is guaranteed that a subsequent call to load_font()
         * with the same font name will return a valid Font pointer.
         */
        """
        pass

    def write(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ostream out)
        
        /**
         * Lists the contents of the font pool to the indicated output stream.
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
        '__doc__': '/**\n * This is the preferred interface for loading fonts for the TextNode system.\n * It is similar to ModelPool and TexturePool in that it unifies references to\n * the same filename.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FontPool' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35E720>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.FontPool' objects>"
        'addFont': None, # (!) real value is '<staticmethod(<built-in method addFont of type object at 0x00007FFCFE35E720>)>'
        'add_font': None, # (!) real value is '<staticmethod(<built-in method add_font of type object at 0x00007FFCFE35E720>)>'
        'garbageCollect': None, # (!) real value is '<staticmethod(<built-in method garbageCollect of type object at 0x00007FFCFE35E720>)>'
        'garbage_collect': None, # (!) real value is '<staticmethod(<built-in method garbage_collect of type object at 0x00007FFCFE35E720>)>'
        'hasFont': None, # (!) real value is '<staticmethod(<built-in method hasFont of type object at 0x00007FFCFE35E720>)>'
        'has_font': None, # (!) real value is '<staticmethod(<built-in method has_font of type object at 0x00007FFCFE35E720>)>'
        'listContents': None, # (!) real value is '<staticmethod(<built-in method listContents of type object at 0x00007FFCFE35E720>)>'
        'list_contents': None, # (!) real value is '<staticmethod(<built-in method list_contents of type object at 0x00007FFCFE35E720>)>'
        'loadFont': None, # (!) real value is '<staticmethod(<built-in method loadFont of type object at 0x00007FFCFE35E720>)>'
        'load_font': None, # (!) real value is '<staticmethod(<built-in method load_font of type object at 0x00007FFCFE35E720>)>'
        'releaseAllFonts': None, # (!) real value is '<staticmethod(<built-in method releaseAllFonts of type object at 0x00007FFCFE35E720>)>'
        'releaseFont': None, # (!) real value is '<staticmethod(<built-in method releaseFont of type object at 0x00007FFCFE35E720>)>'
        'release_all_fonts': None, # (!) real value is '<staticmethod(<built-in method release_all_fonts of type object at 0x00007FFCFE35E720>)>'
        'release_font': None, # (!) real value is '<staticmethod(<built-in method release_font of type object at 0x00007FFCFE35E720>)>'
        'verifyFont': None, # (!) real value is '<staticmethod(<built-in method verifyFont of type object at 0x00007FFCFE35E720>)>'
        'verify_font': None, # (!) real value is '<staticmethod(<built-in method verify_font of type object at 0x00007FFCFE35E720>)>'
        'write': None, # (!) real value is '<staticmethod(<built-in method write of type object at 0x00007FFCFE35E720>)>'
    }


