# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PGItem import PGItem

class PGVirtualFrame(PGItem):
    """
    /**
     * This represents a frame that is rendered as a window onto another (possibly
     * much larger) canvas.  You can only see the portion of the canvas that is
     * below the window at any given time.
     *
     * This works simply by automatically defining a scissor effect to be applied
     * to a special child node, called the canvas_node, of the PGVirtualFrame
     * node.  Every object that is parented to the canvas_node will be clipped by
     * the scissor effect.  Also, you can modify the canvas_transform through
     * convenience methods here, which actually modifies the transform on the
     * canvas_node.
     *
     * The net effect is that the virtual canvas is arbitrarily large, and we can
     * peek at it through the scissor region, and scroll through different parts
     * of it by modifying the canvas_transform.
     *
     * See PGScrollFrame for a specialization of this class that handles the
     * traditional scrolling canvas, with scroll bars.
     */
    """
    def clearClipFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_clip_frame(const PGVirtualFrame self)
        
        /**
         * Removes the clip frame from the item.  This disables clipping.
         */
        """
        pass

    def clear_clip_frame(self, const_PGVirtualFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_clip_frame(const PGVirtualFrame self)
        
        /**
         * Removes the clip frame from the item.  This disables clipping.
         */
        """
        pass

    def getCanvasNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_canvas_node(PGVirtualFrame self)
        
        /**
         * Returns the special node that holds all of the children that appear in the
         * virtual canvas.
         */
        """
        pass

    def getCanvasParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_canvas_parent(PGVirtualFrame self)
        
        /**
         * Returns the parent node of the canvas_node.
         */
        """
        pass

    def getCanvasTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_canvas_transform(PGVirtualFrame self)
        
        /**
         * Returns the transform of the virtual canvas.  This transform is applied to
         * all child nodes of the canvas_node.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClipFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clip_frame(PGVirtualFrame self)
        
        /**
         * Returns the bounding rectangle of the clip frame.  See set_clip_frame().
         * If has_clip_frame() is false, this returns the item's actual frame.
         */
        """
        pass

    def get_canvas_node(self, PGVirtualFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_canvas_node(PGVirtualFrame self)
        
        /**
         * Returns the special node that holds all of the children that appear in the
         * virtual canvas.
         */
        """
        pass

    def get_canvas_parent(self, PGVirtualFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_canvas_parent(PGVirtualFrame self)
        
        /**
         * Returns the parent node of the canvas_node.
         */
        """
        pass

    def get_canvas_transform(self, PGVirtualFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_canvas_transform(PGVirtualFrame self)
        
        /**
         * Returns the transform of the virtual canvas.  This transform is applied to
         * all child nodes of the canvas_node.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_clip_frame(self, PGVirtualFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clip_frame(PGVirtualFrame self)
        
        /**
         * Returns the bounding rectangle of the clip frame.  See set_clip_frame().
         * If has_clip_frame() is false, this returns the item's actual frame.
         */
        """
        pass

    def hasClipFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_clip_frame(PGVirtualFrame self)
        
        /**
         * Returns true if the clip frame has been set; see set_clip_frame().  If it
         * has not been set, objects in the virtual frame will not be clipped.
         */
        """
        pass

    def has_clip_frame(self, PGVirtualFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_clip_frame(PGVirtualFrame self)
        
        /**
         * Returns true if the clip frame has been set; see set_clip_frame().  If it
         * has not been set, objects in the virtual frame will not be clipped.
         */
        """
        pass

    def setCanvasTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_canvas_transform(const PGVirtualFrame self, const TransformState transform)
        
        /**
         * Changes the transform of the virtual canvas.  This transform is applied to
         * all child nodes of the canvas_node.
         */
        """
        pass

    def setClipFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clip_frame(const PGVirtualFrame self, const LVecBase4f clip_frame)
        set_clip_frame(const PGVirtualFrame self, float left, float right, float bottom, float top)
        
        /**
         * Sets the bounding rectangle of the clip frame.  This is the size of the
         * small window through which we can see the virtual canvas.  Normally, this
         * is the same size as the actual frame or smaller (typically it is smaller by
         * the size of the bevel, or to make room for scroll bars).
         */
        
        /**
         * Sets the bounding rectangle of the clip frame.  This is the size of the
         * small window through which we can see the virtual canvas.  Normally, this
         * is the same size as the actual frame or smaller (typically it is smaller by
         * the size of the bevel, or to make room for scroll bars).
         */
        """
        pass

    def setup(self, const_PGVirtualFrame_self, float_width, float_height): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup(const PGVirtualFrame self, float width, float height)
        
        /**
         * Creates a PGVirtualFrame with the indicated dimensions.
         */
        """
        pass

    def set_canvas_transform(self, const_PGVirtualFrame_self, const_TransformState_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_canvas_transform(const PGVirtualFrame self, const TransformState transform)
        
        /**
         * Changes the transform of the virtual canvas.  This transform is applied to
         * all child nodes of the canvas_node.
         */
        """
        pass

    def set_clip_frame(self, const_PGVirtualFrame_self, const_LVecBase4f_clip_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clip_frame(const PGVirtualFrame self, const LVecBase4f clip_frame)
        set_clip_frame(const PGVirtualFrame self, float left, float right, float bottom, float top)
        
        /**
         * Sets the bounding rectangle of the clip frame.  This is the size of the
         * small window through which we can see the virtual canvas.  Normally, this
         * is the same size as the actual frame or smaller (typically it is smaller by
         * the size of the bevel, or to make room for scroll bars).
         */
        
        /**
         * Sets the bounding rectangle of the clip frame.  This is the size of the
         * small window through which we can see the virtual canvas.  Normally, this
         * is the same size as the actual frame or smaller (typically it is smaller by
         * the size of the bevel, or to make room for scroll bars).
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
        '__doc__': '/**\n * This represents a frame that is rendered as a window onto another (possibly\n * much larger) canvas.  You can only see the portion of the canvas that is\n * below the window at any given time.\n *\n * This works simply by automatically defining a scissor effect to be applied\n * to a special child node, called the canvas_node, of the PGVirtualFrame\n * node.  Every object that is parented to the canvas_node will be clipped by\n * the scissor effect.  Also, you can modify the canvas_transform through\n * convenience methods here, which actually modifies the transform on the\n * canvas_node.\n *\n * The net effect is that the virtual canvas is arbitrarily large, and we can\n * peek at it through the scissor region, and scroll through different parts\n * of it by modifying the canvas_transform.\n *\n * See PGScrollFrame for a specialization of this class that handles the\n * traditional scrolling canvas, with scroll bars.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PGVirtualFrame' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE384AB0>'
        'clearClipFrame': None, # (!) real value is "<method 'clearClipFrame' of 'panda3d.core.PGVirtualFrame' objects>"
        'clear_clip_frame': None, # (!) real value is "<method 'clear_clip_frame' of 'panda3d.core.PGVirtualFrame' objects>"
        'getCanvasNode': None, # (!) real value is "<method 'getCanvasNode' of 'panda3d.core.PGVirtualFrame' objects>"
        'getCanvasParent': None, # (!) real value is "<method 'getCanvasParent' of 'panda3d.core.PGVirtualFrame' objects>"
        'getCanvasTransform': None, # (!) real value is "<method 'getCanvasTransform' of 'panda3d.core.PGVirtualFrame' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE384AB0>)>'
        'getClipFrame': None, # (!) real value is "<method 'getClipFrame' of 'panda3d.core.PGVirtualFrame' objects>"
        'get_canvas_node': None, # (!) real value is "<method 'get_canvas_node' of 'panda3d.core.PGVirtualFrame' objects>"
        'get_canvas_parent': None, # (!) real value is "<method 'get_canvas_parent' of 'panda3d.core.PGVirtualFrame' objects>"
        'get_canvas_transform': None, # (!) real value is "<method 'get_canvas_transform' of 'panda3d.core.PGVirtualFrame' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE384AB0>)>'
        'get_clip_frame': None, # (!) real value is "<method 'get_clip_frame' of 'panda3d.core.PGVirtualFrame' objects>"
        'hasClipFrame': None, # (!) real value is "<method 'hasClipFrame' of 'panda3d.core.PGVirtualFrame' objects>"
        'has_clip_frame': None, # (!) real value is "<method 'has_clip_frame' of 'panda3d.core.PGVirtualFrame' objects>"
        'setCanvasTransform': None, # (!) real value is "<method 'setCanvasTransform' of 'panda3d.core.PGVirtualFrame' objects>"
        'setClipFrame': None, # (!) real value is "<method 'setClipFrame' of 'panda3d.core.PGVirtualFrame' objects>"
        'set_canvas_transform': None, # (!) real value is "<method 'set_canvas_transform' of 'panda3d.core.PGVirtualFrame' objects>"
        'set_clip_frame': None, # (!) real value is "<method 'set_clip_frame' of 'panda3d.core.PGVirtualFrame' objects>"
        'setup': None, # (!) real value is "<method 'setup' of 'panda3d.core.PGVirtualFrame' objects>"
    }


