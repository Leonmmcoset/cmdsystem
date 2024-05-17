# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class ScissorAttrib(RenderAttrib):
    """
    /**
     * This restricts rendering to within a rectangular region of the scene,
     * without otherwise affecting the viewport or lens properties.  Geometry that
     * falls outside the scissor region is not rendered.  It is akin to the OpenGL
     * glScissor() function.
     *
     * The ScissorAttrib always specifies its region relative to its enclosing
     * DisplayRegion, in screen space, and performs no culling.
     *
     * See ScissorEffect if you wish to define a region relative to 2-D or 3-D
     * coordinates in the scene graph, with culling.
     */
    """
    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame(ScissorAttrib self)
        
        /**
         * Returns the left, right, bottom, top coordinates of the scissor frame.
         * This defines a frame within the current DisplayRegion, where 0,0 is the
         * lower-left corner of the DisplayRegion, and 1,1 is the upper-right corner.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_frame(self, ScissorAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame(ScissorAttrib self)
        
        /**
         * Returns the left, right, bottom, top coordinates of the scissor frame.
         * This defines a frame within the current DisplayRegion, where 0,0 is the
         * lower-left corner of the DisplayRegion, and 1,1 is the upper-right corner.
         */
        """
        pass

    def isOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_off(ScissorAttrib self)
        
        /**
         * Returns true if the ScissorAttrib is an 'off' ScissorAttrib, indicating
         * that scissor testing is disabled.
         */
        """
        pass

    def is_off(self, ScissorAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_off(ScissorAttrib self)
        
        /**
         * Returns true if the ScissorAttrib is an 'off' ScissorAttrib, indicating
         * that scissor testing is disabled.
         */
        """
        pass

    def make(self, const_LVecBase4f_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(const LVecBase4f frame)
        make(float left, float right, float bottom, float top)
        
        /**
         * Constructs a ScissorAttrib that restricts rendering to the indicated frame
         * within the current DisplayRegion.  (0,0) is the lower-left corner of the
         * DisplayRegion, and (1,1) is the upper-right corner.
         */
        
        /**
         * Constructs a ScissorAttrib that restricts rendering to the indicated frame
         * within the current DisplayRegion.  (0,0) is the lower-left corner of the
         * DisplayRegion, and (1,1) is the upper-right corner.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def makeOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new ScissorAttrib object that removes the scissor region and
         * fills the DisplayRegion.
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new ScissorAttrib object that removes the scissor region and
         * fills the DisplayRegion.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 22
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This restricts rendering to within a rectangular region of the scene,\n * without otherwise affecting the viewport or lens properties.  Geometry that\n * falls outside the scissor region is not rendered.  It is akin to the OpenGL\n * glScissor() function.\n *\n * The ScissorAttrib always specifies its region relative to its enclosing\n * DisplayRegion, in screen space, and performs no culling.\n *\n * See ScissorEffect if you wish to define a region relative to 2-D or 3-D\n * coordinates in the scene graph, with culling.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ScissorAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE29AE70>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.ScissorAttrib'>"
        'frame': None, # (!) real value is "<attribute 'frame' of 'panda3d.core.ScissorAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE29AE70>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE29AE70>)>'
        'getFrame': None, # (!) real value is "<method 'getFrame' of 'panda3d.core.ScissorAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE29AE70>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE29AE70>)>'
        'get_frame': None, # (!) real value is "<method 'get_frame' of 'panda3d.core.ScissorAttrib' objects>"
        'isOff': None, # (!) real value is "<method 'isOff' of 'panda3d.core.ScissorAttrib' objects>"
        'is_off': None, # (!) real value is "<method 'is_off' of 'panda3d.core.ScissorAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE29AE70>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE29AE70>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE29AE70>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE29AE70>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE29AE70>)>'
    }


