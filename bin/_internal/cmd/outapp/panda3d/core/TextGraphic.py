# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TextGraphic(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This defines a special model that has been constructed for the purposes of
     * embedding an arbitrary graphic image within a text paragraph.
     *
     * It can be any arbitrary model, though it should be built along the same
     * scale as the text, and it should probably be at least mostly two-
     * dimensional.  Typically, this means it should be constructed in the X-Z
     * plane, and it should have a maximum vertical (Z) height of 1.0.
     *
     * The frame specifies an arbitrary bounding volume in the form (left, right,
     * bottom, top).  This indicates the amount of space that will be reserved
     * within the paragraph.  The actual model is not actually required to fit
     * within this rectangle, but if it does not, it may visually overlap with
     * nearby text.
     */
    """
    def getFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame(TextGraphic self)
        
        /**
         * Returns the frame specified for the graphic.  This is the amount of space
         * that will be reserved for the graphic when it is embedded in a text
         * paragraph, in the form (left, right, bottom, top).
         *
         * The actual graphic, as rendered by the NodePath specified via set_model(),
         * should more or less fit within this rectangle.  It is not required to fit
         * completely within it, but if it does not, it may visually overlap with
         * nearby text.
         */
        """
        pass

    def getInstanceFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_instance_flag(TextGraphic self)
        
        /**
         * Returns the instance_flag.  See set_instance_flag().
         */
        """
        pass

    def getModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_model(TextGraphic self)
        
        /**
         * Returns the NodePath associated with the graphic, that renders the desired
         * image.
         */
        """
        pass

    def get_frame(self, TextGraphic_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame(TextGraphic self)
        
        /**
         * Returns the frame specified for the graphic.  This is the amount of space
         * that will be reserved for the graphic when it is embedded in a text
         * paragraph, in the form (left, right, bottom, top).
         *
         * The actual graphic, as rendered by the NodePath specified via set_model(),
         * should more or less fit within this rectangle.  It is not required to fit
         * completely within it, but if it does not, it may visually overlap with
         * nearby text.
         */
        """
        pass

    def get_instance_flag(self, TextGraphic_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_instance_flag(TextGraphic self)
        
        /**
         * Returns the instance_flag.  See set_instance_flag().
         */
        """
        pass

    def get_model(self, TextGraphic_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_model(TextGraphic self)
        
        /**
         * Returns the NodePath associated with the graphic, that renders the desired
         * image.
         */
        """
        pass

    def setFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame(const TextGraphic self, const LVecBase4f frame)
        set_frame(const TextGraphic self, float left, float right, float bottom, float top)
        
        /**
         * Specifies the (left, right, bottom, top) bounding frame for the graphic.
         * See get_frame().
         */
        
        /**
         * Specifies the (left, right, bottom, top) bounding frame for the graphic.
         * See get_frame().
         */
        """
        pass

    def setInstanceFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_instance_flag(const TextGraphic self, bool instance_flag)
        
        /**
         * Sets the instance_flag.  When this is true, the graphic is directly
         * instanced to the scene graph whenever it appears; when it is false, the
         * graphic is copied.  The default is false, which is best for most
         * applications.  You might need to set it true for special kinds of
         * "graphics" like interactive elements, for instance a PGEntry.
         */
        """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_model(const TextGraphic self, const NodePath model)
        
        /**
         * Changes the NodePath associated with the graphic.  This NodePath should
         * contain geometry that will render the desired graphic image.
         */
        """
        pass

    def set_frame(self, const_TextGraphic_self, const_LVecBase4f_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame(const TextGraphic self, const LVecBase4f frame)
        set_frame(const TextGraphic self, float left, float right, float bottom, float top)
        
        /**
         * Specifies the (left, right, bottom, top) bounding frame for the graphic.
         * See get_frame().
         */
        
        /**
         * Specifies the (left, right, bottom, top) bounding frame for the graphic.
         * See get_frame().
         */
        """
        pass

    def set_instance_flag(self, const_TextGraphic_self, bool_instance_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_instance_flag(const TextGraphic self, bool instance_flag)
        
        /**
         * Sets the instance_flag.  When this is true, the graphic is directly
         * instanced to the scene graph whenever it appears; when it is false, the
         * graphic is copied.  The default is false, which is best for most
         * applications.  You might need to set it true for special kinds of
         * "graphics" like interactive elements, for instance a PGEntry.
         */
        """
        pass

    def set_model(self, const_TextGraphic_self, const_NodePath_model): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_model(const TextGraphic self, const NodePath model)
        
        /**
         * Changes the NodePath associated with the graphic.  This NodePath should
         * contain geometry that will render the desired graphic image.
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

    frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    instance_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TextGraphic' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TextGraphic' objects>"
        '__doc__': '/**\n * This defines a special model that has been constructed for the purposes of\n * embedding an arbitrary graphic image within a text paragraph.\n *\n * It can be any arbitrary model, though it should be built along the same\n * scale as the text, and it should probably be at least mostly two-\n * dimensional.  Typically, this means it should be constructed in the X-Z\n * plane, and it should have a maximum vertical (Z) height of 1.0.\n *\n * The frame specifies an arbitrary bounding volume in the form (left, right,\n * bottom, top).  This indicates the amount of space that will be reserved\n * within the paragraph.  The actual model is not actually required to fit\n * within this rectangle, but if it does not, it may visually overlap with\n * nearby text.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextGraphic' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35EE60>'
        'frame': None, # (!) real value is "<attribute 'frame' of 'panda3d.core.TextGraphic' objects>"
        'getFrame': None, # (!) real value is "<method 'getFrame' of 'panda3d.core.TextGraphic' objects>"
        'getInstanceFlag': None, # (!) real value is "<method 'getInstanceFlag' of 'panda3d.core.TextGraphic' objects>"
        'getModel': None, # (!) real value is "<method 'getModel' of 'panda3d.core.TextGraphic' objects>"
        'get_frame': None, # (!) real value is "<method 'get_frame' of 'panda3d.core.TextGraphic' objects>"
        'get_instance_flag': None, # (!) real value is "<method 'get_instance_flag' of 'panda3d.core.TextGraphic' objects>"
        'get_model': None, # (!) real value is "<method 'get_model' of 'panda3d.core.TextGraphic' objects>"
        'instance_flag': None, # (!) real value is "<attribute 'instance_flag' of 'panda3d.core.TextGraphic' objects>"
        'model': None, # (!) real value is "<attribute 'model' of 'panda3d.core.TextGraphic' objects>"
        'setFrame': None, # (!) real value is "<method 'setFrame' of 'panda3d.core.TextGraphic' objects>"
        'setInstanceFlag': None, # (!) real value is "<method 'setInstanceFlag' of 'panda3d.core.TextGraphic' objects>"
        'setModel': None, # (!) real value is "<method 'setModel' of 'panda3d.core.TextGraphic' objects>"
        'set_frame': None, # (!) real value is "<method 'set_frame' of 'panda3d.core.TextGraphic' objects>"
        'set_instance_flag': None, # (!) real value is "<method 'set_instance_flag' of 'panda3d.core.TextGraphic' objects>"
        'set_model': None, # (!) real value is "<method 'set_model' of 'panda3d.core.TextGraphic' objects>"
    }


