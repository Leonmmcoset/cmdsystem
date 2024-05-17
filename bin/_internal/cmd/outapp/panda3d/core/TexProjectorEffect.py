# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderEffect import RenderEffect

class TexProjectorEffect(RenderEffect):
    """
    /**
     * This effect automatically applies a computed texture matrix to the
     * specified texture stage, according to the relative position of two
     * specified nodes.
     *
     * The relative transform from the "from" node to the "to" node is applied
     * directly to the texture matrix each frame.  If the "to" node happens to be
     * a LensNode, its lens projection matrix is applied as well.
     *
     * This can be used to apply a number of special effects.  Fundamentally, it
     * may simply be used to provide a separate PandaNode that may be adjusted
     * (e.g.  via a LerpInterval) in order to easily apply a linear transformation
     * to an object's texture coordinates (rather than having to explicitly call
     * NodePath.set_tex_transform() each frame).
     *
     * In a more sophisticated case, the TexProjectorEffect is particularly useful
     * in conjunction with a TexGenAttrib that specifies a mode of
     * M_world_position (which copies the world position of each vertex to the
     * texture coordinates).  Then the TexProjector can be used to convert these
     * world coordinates to the relative coordinates of a particular node, causing
     * (for instance) a texture to appear to follow a node around as it moves
     * through the world.  With a LensNode, you can project a texture onto the
     * walls, for instance to apply a flashlight effect or an image-based shadow.
     */
    """
    def addStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_stage(TexProjectorEffect self, TextureStage stage, const NodePath from, const NodePath to, int lens_index)
        
        /**
         * Returns a new TexProjectorEffect just like this one, with the indicated
         * projection for the given stage.  If this stage already exists, its
         * projection definition is replaced.
         *
         * The relative transform between the "from" and the "to" nodes is
         * automatically applied to the texture transform each frame.
         *
         * Furthermore, if the "to" node is a LensNode, its projection matrix is also
         * applied to the texture transform.  In this case, the lens_index may be used
         * to select the particular lens that should be used.
         */
        """
        pass

    def add_stage(self, TexProjectorEffect_self, TextureStage_stage, const_NodePath_from, const_NodePath_to, int_lens_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_stage(TexProjectorEffect self, TextureStage stage, const NodePath from, const NodePath to, int lens_index)
        
        /**
         * Returns a new TexProjectorEffect just like this one, with the indicated
         * projection for the given stage.  If this stage already exists, its
         * projection definition is replaced.
         *
         * The relative transform between the "from" and the "to" nodes is
         * automatically applied to the texture transform each frame.
         *
         * Furthermore, if the "to" node is a LensNode, its projection matrix is also
         * applied to the texture transform.  In this case, the lens_index may be used
         * to select the particular lens that should be used.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_from(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns the "from" node associated with the TexProjectorEffect on the
         * indicated stage.  The relative transform between the "from" and the "to"
         * nodes is automatically applied to the texture transform each frame.
         */
        """
        pass

    def getLensIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lens_index(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns the lens_index associated with the TexProjectorEffect on the
         * indicated stage.  This is only used if the "to" node is a LensNode, in
         * which case it specifies the particular lens that should be used.
         */
        """
        pass

    def getTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_to(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns the "to" node associated with the TexProjectorEffect on the
         * indicated stage.  The relative transform between the "from" and the "to"
         * nodes is automatically applied to the texture transform each frame.
         *
         * Furthermore, if the "to" node is a LensNode, its projection matrix is also
         * applied to the texture transform.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_from(self, TexProjectorEffect_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_from(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns the "from" node associated with the TexProjectorEffect on the
         * indicated stage.  The relative transform between the "from" and the "to"
         * nodes is automatically applied to the texture transform each frame.
         */
        """
        pass

    def get_lens_index(self, TexProjectorEffect_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lens_index(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns the lens_index associated with the TexProjectorEffect on the
         * indicated stage.  This is only used if the "to" node is a LensNode, in
         * which case it specifies the particular lens that should be used.
         */
        """
        pass

    def get_to(self, TexProjectorEffect_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_to(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns the "to" node associated with the TexProjectorEffect on the
         * indicated stage.  The relative transform between the "from" and the "to"
         * nodes is automatically applied to the texture transform each frame.
         *
         * Furthermore, if the "to" node is a LensNode, its projection matrix is also
         * applied to the texture transform.
         */
        """
        pass

    def hasStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_stage(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns true if there is a transform associated with the indicated stage,
         * or false otherwise (in which case get_transform(stage) will return the
         * identity transform).
         */
        """
        pass

    def has_stage(self, TexProjectorEffect_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_stage(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns true if there is a transform associated with the indicated stage,
         * or false otherwise (in which case get_transform(stage) will return the
         * identity transform).
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(TexProjectorEffect self)
        
        /**
         * Returns true if no stages are defined in the TexProjectorEffect, false if
         * at least one is.
         */
        """
        pass

    def is_empty(self, TexProjectorEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(TexProjectorEffect self)
        
        /**
         * Returns true if no stages are defined in the TexProjectorEffect, false if
         * at least one is.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        
        /**
         * Constructs a TexProjectorEffect that modifies no stages at all.
         */
        """
        pass

    def removeStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_stage(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns a new TexProjectorEffect just like this one, with the indicated
         * stage removed.
         */
        """
        pass

    def remove_stage(self, TexProjectorEffect_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_stage(TexProjectorEffect self, TextureStage stage)
        
        /**
         * Returns a new TexProjectorEffect just like this one, with the indicated
         * stage removed.
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
        '__doc__': '/**\n * This effect automatically applies a computed texture matrix to the\n * specified texture stage, according to the relative position of two\n * specified nodes.\n *\n * The relative transform from the "from" node to the "to" node is applied\n * directly to the texture matrix each frame.  If the "to" node happens to be\n * a LensNode, its lens projection matrix is applied as well.\n *\n * This can be used to apply a number of special effects.  Fundamentally, it\n * may simply be used to provide a separate PandaNode that may be adjusted\n * (e.g.  via a LerpInterval) in order to easily apply a linear transformation\n * to an object\'s texture coordinates (rather than having to explicitly call\n * NodePath.set_tex_transform() each frame).\n *\n * In a more sophisticated case, the TexProjectorEffect is particularly useful\n * in conjunction with a TexGenAttrib that specifies a mode of\n * M_world_position (which copies the world position of each vertex to the\n * texture coordinates).  Then the TexProjector can be used to convert these\n * world coordinates to the relative coordinates of a particular node, causing\n * (for instance) a texture to appear to follow a node around as it moves\n * through the world.  With a LensNode, you can project a texture onto the\n * walls, for instance to apply a flashlight effect or an image-based shadow.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TexProjectorEffect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE29A560>'
        'addStage': None, # (!) real value is "<method 'addStage' of 'panda3d.core.TexProjectorEffect' objects>"
        'add_stage': None, # (!) real value is "<method 'add_stage' of 'panda3d.core.TexProjectorEffect' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE29A560>)>'
        'getFrom': None, # (!) real value is "<method 'getFrom' of 'panda3d.core.TexProjectorEffect' objects>"
        'getLensIndex': None, # (!) real value is "<method 'getLensIndex' of 'panda3d.core.TexProjectorEffect' objects>"
        'getTo': None, # (!) real value is "<method 'getTo' of 'panda3d.core.TexProjectorEffect' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE29A560>)>'
        'get_from': None, # (!) real value is "<method 'get_from' of 'panda3d.core.TexProjectorEffect' objects>"
        'get_lens_index': None, # (!) real value is "<method 'get_lens_index' of 'panda3d.core.TexProjectorEffect' objects>"
        'get_to': None, # (!) real value is "<method 'get_to' of 'panda3d.core.TexProjectorEffect' objects>"
        'hasStage': None, # (!) real value is "<method 'hasStage' of 'panda3d.core.TexProjectorEffect' objects>"
        'has_stage': None, # (!) real value is "<method 'has_stage' of 'panda3d.core.TexProjectorEffect' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.TexProjectorEffect' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.TexProjectorEffect' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE29A560>)>'
        'removeStage': None, # (!) real value is "<method 'removeStage' of 'panda3d.core.TexProjectorEffect' objects>"
        'remove_stage': None, # (!) real value is "<method 'remove_stage' of 'panda3d.core.TexProjectorEffect' objects>"
    }


