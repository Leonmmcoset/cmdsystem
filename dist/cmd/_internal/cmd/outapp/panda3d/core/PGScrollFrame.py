# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PGVirtualFrame import PGVirtualFrame

class PGScrollFrame(PGVirtualFrame):
    """
    /**
     * This is a special kind of frame that pretends to be much larger than it
     * actually is.  You can scroll through the frame, as if you're looking
     * through a window at the larger frame beneath.  All children of this frame
     * node are scrolled and clipped as if they were children of the larger,
     * virtual frame.
     *
     * This is implemented as a specialization of PGVirtualFrame, which handles
     * the meat of the virtual canvas.  This class adds automatic support for
     * scroll bars, and restricts the virtual transform to translate only (no
     * scale or rotate).
     */
    """
    def clearHorizontalSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_horizontal_slider(const PGScrollFrame self)
        
        /**
         * Removes the horizontal scroll bar from control of the frame.  It is your
         * responsibility to actually remove or hide the object itself.
         */
        """
        pass

    def clearVerticalSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_vertical_slider(const PGScrollFrame self)
        
        /**
         * Removes the vertical scroll bar from control of the frame.  It is your
         * responsibility to actually remove or hide the object itself.
         */
        """
        pass

    def clearVirtualFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_virtual_frame(const PGScrollFrame self)
        
        /**
         * Removes the virtual frame from the item.  This effectively sets the virtual
         * frame to the same size as the clip frame.  Scrolling will no longer be
         * possible.
         */
        """
        pass

    def clear_horizontal_slider(self, const_PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_horizontal_slider(const PGScrollFrame self)
        
        /**
         * Removes the horizontal scroll bar from control of the frame.  It is your
         * responsibility to actually remove or hide the object itself.
         */
        """
        pass

    def clear_vertical_slider(self, const_PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_vertical_slider(const PGScrollFrame self)
        
        /**
         * Removes the vertical scroll bar from control of the frame.  It is your
         * responsibility to actually remove or hide the object itself.
         */
        """
        pass

    def clear_virtual_frame(self, const_PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_virtual_frame(const PGScrollFrame self)
        
        /**
         * Removes the virtual frame from the item.  This effectively sets the virtual
         * frame to the same size as the clip frame.  Scrolling will no longer be
         * possible.
         */
        """
        pass

    def getAutoHide(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_hide(PGScrollFrame self)
        
        /**
         * Returns the auto_hide flag.  See set_auto_hide().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHorizontalSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_horizontal_slider(PGScrollFrame self)
        
        /**
         * Returns the PGSliderBar that serves as the horizontal scroll bar for this
         * frame, if any, or NULL if it is not set.
         */
        """
        pass

    def getManagePieces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_manage_pieces(PGScrollFrame self)
        
        /**
         * Returns the manage_pieces flag.  See set_manage_pieces().
         */
        """
        pass

    def getVerticalSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertical_slider(PGScrollFrame self)
        
        /**
         * Returns the PGSliderBar that serves as the vertical scroll bar for this
         * frame, if any, or NULL if it is not set.
         */
        """
        pass

    def getVirtualFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_virtual_frame(PGScrollFrame self)
        
        /**
         * Returns the bounding rectangle of the virtual frame.  See
         * set_virtual_frame().  If has_virtual_frame() is false, this returns the
         * item's clip frame.
         */
        """
        pass

    def get_auto_hide(self, PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_hide(PGScrollFrame self)
        
        /**
         * Returns the auto_hide flag.  See set_auto_hide().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_horizontal_slider(self, PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_horizontal_slider(PGScrollFrame self)
        
        /**
         * Returns the PGSliderBar that serves as the horizontal scroll bar for this
         * frame, if any, or NULL if it is not set.
         */
        """
        pass

    def get_manage_pieces(self, PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_manage_pieces(PGScrollFrame self)
        
        /**
         * Returns the manage_pieces flag.  See set_manage_pieces().
         */
        """
        pass

    def get_vertical_slider(self, PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertical_slider(PGScrollFrame self)
        
        /**
         * Returns the PGSliderBar that serves as the vertical scroll bar for this
         * frame, if any, or NULL if it is not set.
         */
        """
        pass

    def get_virtual_frame(self, PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_virtual_frame(PGScrollFrame self)
        
        /**
         * Returns the bounding rectangle of the virtual frame.  See
         * set_virtual_frame().  If has_virtual_frame() is false, this returns the
         * item's clip frame.
         */
        """
        pass

    def hasVirtualFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_virtual_frame(PGScrollFrame self)
        
        /**
         * Returns true if the virtual frame has a bounding rectangle; see
         * set_virtual_frame().  Most PGScrollFrame objects will have a virtual frame.
         */
        """
        pass

    def has_virtual_frame(self, PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_virtual_frame(PGScrollFrame self)
        
        /**
         * Returns true if the virtual frame has a bounding rectangle; see
         * set_virtual_frame().  Most PGScrollFrame objects will have a virtual frame.
         */
        """
        pass

    def recompute(self, const_PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute(const PGScrollFrame self)
        
        /**
         * Forces the PGScrollFrame to recompute itself right now.  Normally this
         * should not be required.
         */
        """
        pass

    def remanage(self, const_PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remanage(const PGScrollFrame self)
        
        /**
         * Manages the position and size of the scroll bars.  Normally this should not
         * need to be called directly.
         */
        """
        pass

    def setAutoHide(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_hide(const PGScrollFrame self, bool auto_hide)
        
        /**
         * Sets the auto_hide flag.  When this is true, the two scroll bars are
         * automatically hidden if they are not needed (that is, if the virtual frame
         * would fit within the clip frame without them), and they are automatically
         * shown when they are needed.
         *
         * Setting this flag true forces the manage_pieces flag to also be set true.
         */
        """
        pass

    def setHorizontalSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_horizontal_slider(const PGScrollFrame self, PGSliderBar horizontal_slider)
        
        /**
         * Sets the PGSliderBar object that will serve as the horizontal scroll bar
         * for this frame.  It is your responsibility to parent this slider bar to the
         * frame and move it to the appropriate place.
         */
        """
        pass

    def setManagePieces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_manage_pieces(const PGScrollFrame self, bool manage_pieces)
        
        /**
         * Sets the manage_pieces flag.  When this is true, the sub-pieces of the
         * scroll frame--that is, the two scroll bars--are automatically positioned
         * and/or resized when the scroll frame's overall frame is changed.  They are
         * also automatically resized to fill in the gap when one or the other is
         * hidden.
         */
        """
        pass

    def setup(self, const_PGScrollFrame_self, float_width, float_height, float_left, float_right, float_bottom, float_top, float_slider_width, float_bevel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup(const PGScrollFrame self, float width, float height, float left, float right, float bottom, float top, float slider_width, float bevel)
        
        /**
         * Creates a PGScrollFrame with the indicated dimensions, and the indicated
         * virtual frame.
         */
        """
        pass

    def setVerticalSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertical_slider(const PGScrollFrame self, PGSliderBar vertical_slider)
        
        /**
         * Sets the PGSliderBar object that will serve as the vertical scroll bar for
         * this frame.  It is your responsibility to parent this slider bar to the
         * frame and move it to the appropriate place.
         */
        """
        pass

    def setVirtualFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_virtual_frame(const PGScrollFrame self, const LVecBase4f virtual_frame)
        set_virtual_frame(const PGScrollFrame self, float left, float right, float bottom, float top)
        
        /**
         * Sets the bounding rectangle of the virtual frame.  This is the size of the
         * large, virtual canvas which we can see only a portion of at any given time.
         */
        
        /**
         * Sets the bounding rectangle of the virtual frame.  This is the size of the
         * large, virtual canvas which we can see only a portion of at any given time.
         */
        """
        pass

    def set_auto_hide(self, const_PGScrollFrame_self, bool_auto_hide): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_hide(const PGScrollFrame self, bool auto_hide)
        
        /**
         * Sets the auto_hide flag.  When this is true, the two scroll bars are
         * automatically hidden if they are not needed (that is, if the virtual frame
         * would fit within the clip frame without them), and they are automatically
         * shown when they are needed.
         *
         * Setting this flag true forces the manage_pieces flag to also be set true.
         */
        """
        pass

    def set_horizontal_slider(self, const_PGScrollFrame_self, PGSliderBar_horizontal_slider): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_horizontal_slider(const PGScrollFrame self, PGSliderBar horizontal_slider)
        
        /**
         * Sets the PGSliderBar object that will serve as the horizontal scroll bar
         * for this frame.  It is your responsibility to parent this slider bar to the
         * frame and move it to the appropriate place.
         */
        """
        pass

    def set_manage_pieces(self, const_PGScrollFrame_self, bool_manage_pieces): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_manage_pieces(const PGScrollFrame self, bool manage_pieces)
        
        /**
         * Sets the manage_pieces flag.  When this is true, the sub-pieces of the
         * scroll frame--that is, the two scroll bars--are automatically positioned
         * and/or resized when the scroll frame's overall frame is changed.  They are
         * also automatically resized to fill in the gap when one or the other is
         * hidden.
         */
        """
        pass

    def set_vertical_slider(self, const_PGScrollFrame_self, PGSliderBar_vertical_slider): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertical_slider(const PGScrollFrame self, PGSliderBar vertical_slider)
        
        /**
         * Sets the PGSliderBar object that will serve as the vertical scroll bar for
         * this frame.  It is your responsibility to parent this slider bar to the
         * frame and move it to the appropriate place.
         */
        """
        pass

    def set_virtual_frame(self, const_PGScrollFrame_self, const_LVecBase4f_virtual_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_virtual_frame(const PGScrollFrame self, const LVecBase4f virtual_frame)
        set_virtual_frame(const PGScrollFrame self, float left, float right, float bottom, float top)
        
        /**
         * Sets the bounding rectangle of the virtual frame.  This is the size of the
         * large, virtual canvas which we can see only a portion of at any given time.
         */
        
        /**
         * Sets the bounding rectangle of the virtual frame.  This is the size of the
         * large, virtual canvas which we can see only a portion of at any given time.
         */
        """
        pass

    def upcastToPGVirtualFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_PGVirtualFrame(const PGScrollFrame self)
        
        upcast from PGScrollFrame to PGVirtualFrame
        """
        pass

    def upcast_to_PGVirtualFrame(self, const_PGScrollFrame_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_PGVirtualFrame(const PGScrollFrame self)
        
        upcast from PGScrollFrame to PGVirtualFrame
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
        '__doc__': "/**\n * This is a special kind of frame that pretends to be much larger than it\n * actually is.  You can scroll through the frame, as if you're looking\n * through a window at the larger frame beneath.  All children of this frame\n * node are scrolled and clipped as if they were children of the larger,\n * virtual frame.\n *\n * This is implemented as a specialization of PGVirtualFrame, which handles\n * the meat of the virtual canvas.  This class adds automatic support for\n * scroll bars, and restricts the virtual transform to translate only (no\n * scale or rotate).\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PGScrollFrame' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE384E50>'
        'clearHorizontalSlider': None, # (!) real value is "<method 'clearHorizontalSlider' of 'panda3d.core.PGScrollFrame' objects>"
        'clearVerticalSlider': None, # (!) real value is "<method 'clearVerticalSlider' of 'panda3d.core.PGScrollFrame' objects>"
        'clearVirtualFrame': None, # (!) real value is "<method 'clearVirtualFrame' of 'panda3d.core.PGScrollFrame' objects>"
        'clear_horizontal_slider': None, # (!) real value is "<method 'clear_horizontal_slider' of 'panda3d.core.PGScrollFrame' objects>"
        'clear_vertical_slider': None, # (!) real value is "<method 'clear_vertical_slider' of 'panda3d.core.PGScrollFrame' objects>"
        'clear_virtual_frame': None, # (!) real value is "<method 'clear_virtual_frame' of 'panda3d.core.PGScrollFrame' objects>"
        'getAutoHide': None, # (!) real value is "<method 'getAutoHide' of 'panda3d.core.PGScrollFrame' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE384E50>)>'
        'getHorizontalSlider': None, # (!) real value is "<method 'getHorizontalSlider' of 'panda3d.core.PGScrollFrame' objects>"
        'getManagePieces': None, # (!) real value is "<method 'getManagePieces' of 'panda3d.core.PGScrollFrame' objects>"
        'getVerticalSlider': None, # (!) real value is "<method 'getVerticalSlider' of 'panda3d.core.PGScrollFrame' objects>"
        'getVirtualFrame': None, # (!) real value is "<method 'getVirtualFrame' of 'panda3d.core.PGScrollFrame' objects>"
        'get_auto_hide': None, # (!) real value is "<method 'get_auto_hide' of 'panda3d.core.PGScrollFrame' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE384E50>)>'
        'get_horizontal_slider': None, # (!) real value is "<method 'get_horizontal_slider' of 'panda3d.core.PGScrollFrame' objects>"
        'get_manage_pieces': None, # (!) real value is "<method 'get_manage_pieces' of 'panda3d.core.PGScrollFrame' objects>"
        'get_vertical_slider': None, # (!) real value is "<method 'get_vertical_slider' of 'panda3d.core.PGScrollFrame' objects>"
        'get_virtual_frame': None, # (!) real value is "<method 'get_virtual_frame' of 'panda3d.core.PGScrollFrame' objects>"
        'hasVirtualFrame': None, # (!) real value is "<method 'hasVirtualFrame' of 'panda3d.core.PGScrollFrame' objects>"
        'has_virtual_frame': None, # (!) real value is "<method 'has_virtual_frame' of 'panda3d.core.PGScrollFrame' objects>"
        'recompute': None, # (!) real value is "<method 'recompute' of 'panda3d.core.PGScrollFrame' objects>"
        'remanage': None, # (!) real value is "<method 'remanage' of 'panda3d.core.PGScrollFrame' objects>"
        'setAutoHide': None, # (!) real value is "<method 'setAutoHide' of 'panda3d.core.PGScrollFrame' objects>"
        'setHorizontalSlider': None, # (!) real value is "<method 'setHorizontalSlider' of 'panda3d.core.PGScrollFrame' objects>"
        'setManagePieces': None, # (!) real value is "<method 'setManagePieces' of 'panda3d.core.PGScrollFrame' objects>"
        'setVerticalSlider': None, # (!) real value is "<method 'setVerticalSlider' of 'panda3d.core.PGScrollFrame' objects>"
        'setVirtualFrame': None, # (!) real value is "<method 'setVirtualFrame' of 'panda3d.core.PGScrollFrame' objects>"
        'set_auto_hide': None, # (!) real value is "<method 'set_auto_hide' of 'panda3d.core.PGScrollFrame' objects>"
        'set_horizontal_slider': None, # (!) real value is "<method 'set_horizontal_slider' of 'panda3d.core.PGScrollFrame' objects>"
        'set_manage_pieces': None, # (!) real value is "<method 'set_manage_pieces' of 'panda3d.core.PGScrollFrame' objects>"
        'set_vertical_slider': None, # (!) real value is "<method 'set_vertical_slider' of 'panda3d.core.PGScrollFrame' objects>"
        'set_virtual_frame': None, # (!) real value is "<method 'set_virtual_frame' of 'panda3d.core.PGScrollFrame' objects>"
        'setup': None, # (!) real value is "<method 'setup' of 'panda3d.core.PGScrollFrame' objects>"
        'upcastToPGVirtualFrame': None, # (!) real value is "<method 'upcastToPGVirtualFrame' of 'panda3d.core.PGScrollFrame' objects>"
        'upcast_to_PGVirtualFrame': None, # (!) real value is "<method 'upcast_to_PGVirtualFrame' of 'panda3d.core.PGScrollFrame' objects>"
    }


