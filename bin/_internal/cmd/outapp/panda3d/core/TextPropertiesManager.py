# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TextPropertiesManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This defines all of the TextProperties structures that might be referenced
     * by name from an embedded text string.
     *
     * A text string, as rendered by a TextNode, can contain embedded references
     * to one of the TextProperties defined here, by enclosing the name between \1
     * (ASCII 0x01) characters; this causes a "push" to the named state.  All text
     * following the closing \1 character will then be rendered in the new state.
     * The next \2 (ASCII 0x02) character will then restore the previous state for
     * subsequent text.
     *
     * For instance, "x\1up\1n\2 + y" indicates that the character "x" will be
     * rendered in the normal state, the character "n" will be rendered in the
     * "up" state, and then " + y" will be rendered in the normal state again.
     *
     * This can also be used to define arbitrary models that can serve as embedded
     * graphic images in a text paragraph.  This works similarly; the convention
     * is to create a TextGraphic that describes the graphic image, and then
     * associate it here via the set_graphic() call.  Then "\5name\5" will embed
     * the named graphic.
     */
    """
    def clearGraphic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_graphic(const TextPropertiesManager self, str name)
        
        /**
         * Removes the named TextGraphic structure from the manager.
         */
        """
        pass

    def clearProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_properties(const TextPropertiesManager self, str name)
        
        /**
         * Removes the named TextProperties structure from the manager.
         */
        """
        pass

    def clear_graphic(self, const_TextPropertiesManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_graphic(const TextPropertiesManager self, str name)
        
        /**
         * Removes the named TextGraphic structure from the manager.
         */
        """
        pass

    def clear_properties(self, const_TextPropertiesManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_properties(const TextPropertiesManager self, str name)
        
        /**
         * Removes the named TextProperties structure from the manager.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the pointer to the global TextPropertiesManager object.
         */
        """
        pass

    def getGraphic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_graphic(const TextPropertiesManager self, str name)
        
        /**
         * Returns the TextGraphic associated with the indicated name.  If there was
         * not previously a TextGraphic associated with this name, a warning is
         * printed and then a default TextGraphic structure is associated with the
         * name, and returned.
         *
         * Call has_graphic() instead to check whether a particular name has been
         * defined.
         */
        """
        pass

    def getProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_properties(const TextPropertiesManager self, str name)
        
        /**
         * Returns the TextProperties associated with the indicated name.  If there
         * was not previously a TextProperties associated with this name, a warning is
         * printed and then a default TextProperties structure is associated with the
         * name, and returned.
         *
         * Call has_properties() instead to check whether a particular name has been
         * defined.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the pointer to the global TextPropertiesManager object.
         */
        """
        pass

    def get_graphic(self, const_TextPropertiesManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_graphic(const TextPropertiesManager self, str name)
        
        /**
         * Returns the TextGraphic associated with the indicated name.  If there was
         * not previously a TextGraphic associated with this name, a warning is
         * printed and then a default TextGraphic structure is associated with the
         * name, and returned.
         *
         * Call has_graphic() instead to check whether a particular name has been
         * defined.
         */
        """
        pass

    def get_properties(self, const_TextPropertiesManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_properties(const TextPropertiesManager self, str name)
        
        /**
         * Returns the TextProperties associated with the indicated name.  If there
         * was not previously a TextProperties associated with this name, a warning is
         * printed and then a default TextProperties structure is associated with the
         * name, and returned.
         *
         * Call has_properties() instead to check whether a particular name has been
         * defined.
         */
        """
        pass

    def hasGraphic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_graphic(TextPropertiesManager self, str name)
        
        /**
         * Returns true if a TextGraphic structure has been associated with the
         * indicated name, false otherwise.  Normally this means set_graphic() has
         * been called with this name, but because get_graphic() will implicitly
         * create a default TextGraphic structure, it may also mean simply that
         * get_graphic() has been called with the indicated name.
         */
        """
        pass

    def hasProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_properties(TextPropertiesManager self, str name)
        
        /**
         * Returns true if a TextProperties structure has been associated with the
         * indicated name, false otherwise.  Normally this means set_properties() has
         * been called with this name, but because get_properties() will implicitly
         * create a default TextProperties structure, it may also mean simply that
         * get_properties() has been called with the indicated name.
         */
        """
        pass

    def has_graphic(self, TextPropertiesManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_graphic(TextPropertiesManager self, str name)
        
        /**
         * Returns true if a TextGraphic structure has been associated with the
         * indicated name, false otherwise.  Normally this means set_graphic() has
         * been called with this name, but because get_graphic() will implicitly
         * create a default TextGraphic structure, it may also mean simply that
         * get_graphic() has been called with the indicated name.
         */
        """
        pass

    def has_properties(self, TextPropertiesManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_properties(TextPropertiesManager self, str name)
        
        /**
         * Returns true if a TextProperties structure has been associated with the
         * indicated name, false otherwise.  Normally this means set_properties() has
         * been called with this name, but because get_properties() will implicitly
         * create a default TextProperties structure, it may also mean simply that
         * get_properties() has been called with the indicated name.
         */
        """
        pass

    def setGraphic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_graphic(const TextPropertiesManager self, str name, const NodePath model)
        set_graphic(const TextPropertiesManager self, str name, const TextGraphic graphic)
        
        /**
         * Defines the TextGraphic associated with the indicated name.  When the name
         * is subsequently encountered in text embedded between \5 characters in a
         * TextNode string, the specified graphic will be embedded in the text at that
         * point.
         *
         * If there was already a TextGraphic structure associated with this name, it
         * is quietly replaced with the new definition.
         */
        
        /**
         * This flavor of set_graphic implicitly creates a frame for the model using
         * the model's actual computed bounding volume, as derived from
         * NodePath::calc_tight_bounds().  Create a TextGraphic object first if you
         * want to have explicit control of the frame.
         */
        """
        pass

    def setProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_properties(const TextPropertiesManager self, str name, const TextProperties properties)
        
        /**
         * Defines the TextProperties associated with the indicated name.  When the
         * name is subsequently encountered in text embedded between \1 characters in
         * a TextNode string, the following text will be rendered with these
         * properties.
         *
         * If there was already a TextProperties structure associated with this name,
         * it is quietly replaced with the new definition.
         */
        """
        pass

    def set_graphic(self, const_TextPropertiesManager_self, str_name, const_NodePath_model): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_graphic(const TextPropertiesManager self, str name, const NodePath model)
        set_graphic(const TextPropertiesManager self, str name, const TextGraphic graphic)
        
        /**
         * Defines the TextGraphic associated with the indicated name.  When the name
         * is subsequently encountered in text embedded between \5 characters in a
         * TextNode string, the specified graphic will be embedded in the text at that
         * point.
         *
         * If there was already a TextGraphic structure associated with this name, it
         * is quietly replaced with the new definition.
         */
        
        /**
         * This flavor of set_graphic implicitly creates a frame for the model using
         * the model's actual computed bounding volume, as derived from
         * NodePath::calc_tight_bounds().  Create a TextGraphic object first if you
         * want to have explicit control of the frame.
         */
        """
        pass

    def set_properties(self, const_TextPropertiesManager_self, str_name, const_TextProperties_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_properties(const TextPropertiesManager self, str name, const TextProperties properties)
        
        /**
         * Defines the TextProperties associated with the indicated name.  When the
         * name is subsequently encountered in text embedded between \1 characters in
         * a TextNode string, the following text will be rendered with these
         * properties.
         *
         * If there was already a TextProperties structure associated with this name,
         * it is quietly replaced with the new definition.
         */
        """
        pass

    def write(self, TextPropertiesManager_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TextPropertiesManager self, ostream out, int indent_level)
        
        /**
         *
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
        '__doc__': '/**\n * This defines all of the TextProperties structures that might be referenced\n * by name from an embedded text string.\n *\n * A text string, as rendered by a TextNode, can contain embedded references\n * to one of the TextProperties defined here, by enclosing the name between \\1\n * (ASCII 0x01) characters; this causes a "push" to the named state.  All text\n * following the closing \\1 character will then be rendered in the new state.\n * The next \\2 (ASCII 0x02) character will then restore the previous state for\n * subsequent text.\n *\n * For instance, "x\\1up\\1n\\2 + y" indicates that the character "x" will be\n * rendered in the normal state, the character "n" will be rendered in the\n * "up" state, and then " + y" will be rendered in the normal state again.\n *\n * This can also be used to define arbitrary models that can serve as embedded\n * graphic images in a text paragraph.  This works similarly; the convention\n * is to create a TextGraphic that describes the graphic image, and then\n * associate it here via the set_graphic() call.  Then "\\5name\\5" will embed\n * the named graphic.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextPropertiesManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35F030>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TextPropertiesManager' objects>"
        'clearGraphic': None, # (!) real value is "<method 'clearGraphic' of 'panda3d.core.TextPropertiesManager' objects>"
        'clearProperties': None, # (!) real value is "<method 'clearProperties' of 'panda3d.core.TextPropertiesManager' objects>"
        'clear_graphic': None, # (!) real value is "<method 'clear_graphic' of 'panda3d.core.TextPropertiesManager' objects>"
        'clear_properties': None, # (!) real value is "<method 'clear_properties' of 'panda3d.core.TextPropertiesManager' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE35F030>)>'
        'getGraphic': None, # (!) real value is "<method 'getGraphic' of 'panda3d.core.TextPropertiesManager' objects>"
        'getProperties': None, # (!) real value is "<method 'getProperties' of 'panda3d.core.TextPropertiesManager' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE35F030>)>'
        'get_graphic': None, # (!) real value is "<method 'get_graphic' of 'panda3d.core.TextPropertiesManager' objects>"
        'get_properties': None, # (!) real value is "<method 'get_properties' of 'panda3d.core.TextPropertiesManager' objects>"
        'hasGraphic': None, # (!) real value is "<method 'hasGraphic' of 'panda3d.core.TextPropertiesManager' objects>"
        'hasProperties': None, # (!) real value is "<method 'hasProperties' of 'panda3d.core.TextPropertiesManager' objects>"
        'has_graphic': None, # (!) real value is "<method 'has_graphic' of 'panda3d.core.TextPropertiesManager' objects>"
        'has_properties': None, # (!) real value is "<method 'has_properties' of 'panda3d.core.TextPropertiesManager' objects>"
        'setGraphic': None, # (!) real value is "<method 'setGraphic' of 'panda3d.core.TextPropertiesManager' objects>"
        'setProperties': None, # (!) real value is "<method 'setProperties' of 'panda3d.core.TextPropertiesManager' objects>"
        'set_graphic': None, # (!) real value is "<method 'set_graphic' of 'panda3d.core.TextPropertiesManager' objects>"
        'set_properties': None, # (!) real value is "<method 'set_properties' of 'panda3d.core.TextPropertiesManager' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TextPropertiesManager' objects>"
    }


