# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PGItem import PGItem

class PGSliderBar(PGItem):
    """
    /**
     * This is a particular kind of PGItem that draws a little bar with a slider
     * that moves from left to right indicating a value between the ranges.
     *
     * This is used as an implementation for both DirectSlider and for
     * DirectScrollBar.
     */
    """
    def clearLeftButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_left_button(const PGSliderBar self)
        
        /**
         * Removes the left button object from control of the frame.  It is your
         * responsibility to actually remove or hide the button itself.
         */
        """
        pass

    def clearRightButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_right_button(const PGSliderBar self)
        
        /**
         * Removes the right button object from control of the frame.  It is your
         * responsibility to actually remove or hide the button itself.
         */
        """
        pass

    def clearThumbButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_thumb_button(const PGSliderBar self)
        
        /**
         * Removes the thumb button object from control of the frame.  It is your
         * responsibility to actually remove or hide the button itself.
         */
        """
        pass

    def clear_left_button(self, const_PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_left_button(const PGSliderBar self)
        
        /**
         * Removes the left button object from control of the frame.  It is your
         * responsibility to actually remove or hide the button itself.
         */
        """
        pass

    def clear_right_button(self, const_PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_right_button(const PGSliderBar self)
        
        /**
         * Removes the right button object from control of the frame.  It is your
         * responsibility to actually remove or hide the button itself.
         */
        """
        pass

    def clear_thumb_button(self, const_PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_thumb_button(const PGSliderBar self)
        
        /**
         * Removes the thumb button object from control of the frame.  It is your
         * responsibility to actually remove or hide the button itself.
         */
        """
        pass

    def getAdjustEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_adjust_event(PGSliderBar self)
        
        /**
         * Returns the event name that will be thrown when the slider bar value is
         * adjusted by the user or programmatically.
         */
        """
        pass

    def getAdjustPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_adjust_prefix()
        
        /**
         * Returns the prefix that is used to define the adjust event for all
         * PGSliderBars.  The adjust event is the concatenation of this string
         * followed by get_id().
         */
        """
        pass

    def getAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_axis(PGSliderBar self)
        
        /**
         * Returns the axis of the slider bar's motion.  See set_axis().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLeftButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_left_button(PGSliderBar self)
        
        /**
         * Returns the PGButton that serves as the left scroll button for this slider,
         * if any, or NULL if it is not set.
         */
        """
        pass

    def getManagePieces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_manage_pieces(PGSliderBar self)
        
        /**
         * Returns the manage_pieces flag.  See set_manage_pieces().
         */
        """
        pass

    def getMaxValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_value(PGSliderBar self)
        
        /**
         * Returns the value when the slider is all the way to the right.
         */
        """
        pass

    def getMinValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min_value(PGSliderBar self)
        
        /**
         * Returns the value when the slider is all the way to the left.
         */
        """
        pass

    def getPageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page_size(PGSliderBar self)
        
        /**
         * Returns the value last set by set_page_size().
         */
        """
        pass

    def getRatio(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ratio(PGSliderBar self)
        
        /**
         * Returns the current value of the slider, expressed in the range 0 .. 1.
         */
        """
        pass

    def getResizeThumb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_resize_thumb(PGSliderBar self)
        
        /**
         * Returns the resize_thumb flag.  See set_resize_thumb().
         */
        """
        pass

    def getRightButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right_button(PGSliderBar self)
        
        /**
         * Returns the PGButton that serves as the right scroll button for this
         * slider, if any, or NULL if it is not set.
         */
        """
        pass

    def getScrollSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scroll_size(PGSliderBar self)
        
        /**
         * Returns the value last set by set_scroll_size().
         */
        """
        pass

    def getThumbButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thumb_button(PGSliderBar self)
        
        /**
         * Returns the PGButton that serves as the thumb for this slider, or NULL if
         * it is not set.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(PGSliderBar self)
        
        /**
         * Returns the current value of the slider.
         */
        """
        pass

    def get_adjust_event(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_adjust_event(PGSliderBar self)
        
        /**
         * Returns the event name that will be thrown when the slider bar value is
         * adjusted by the user or programmatically.
         */
        """
        pass

    def get_adjust_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_adjust_prefix()
        
        /**
         * Returns the prefix that is used to define the adjust event for all
         * PGSliderBars.  The adjust event is the concatenation of this string
         * followed by get_id().
         */
        """
        pass

    def get_axis(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_axis(PGSliderBar self)
        
        /**
         * Returns the axis of the slider bar's motion.  See set_axis().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_left_button(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_left_button(PGSliderBar self)
        
        /**
         * Returns the PGButton that serves as the left scroll button for this slider,
         * if any, or NULL if it is not set.
         */
        """
        pass

    def get_manage_pieces(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_manage_pieces(PGSliderBar self)
        
        /**
         * Returns the manage_pieces flag.  See set_manage_pieces().
         */
        """
        pass

    def get_max_value(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_value(PGSliderBar self)
        
        /**
         * Returns the value when the slider is all the way to the right.
         */
        """
        pass

    def get_min_value(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min_value(PGSliderBar self)
        
        /**
         * Returns the value when the slider is all the way to the left.
         */
        """
        pass

    def get_page_size(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page_size(PGSliderBar self)
        
        /**
         * Returns the value last set by set_page_size().
         */
        """
        pass

    def get_ratio(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ratio(PGSliderBar self)
        
        /**
         * Returns the current value of the slider, expressed in the range 0 .. 1.
         */
        """
        pass

    def get_resize_thumb(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_resize_thumb(PGSliderBar self)
        
        /**
         * Returns the resize_thumb flag.  See set_resize_thumb().
         */
        """
        pass

    def get_right_button(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right_button(PGSliderBar self)
        
        /**
         * Returns the PGButton that serves as the right scroll button for this
         * slider, if any, or NULL if it is not set.
         */
        """
        pass

    def get_scroll_size(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scroll_size(PGSliderBar self)
        
        /**
         * Returns the value last set by set_scroll_size().
         */
        """
        pass

    def get_thumb_button(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thumb_button(PGSliderBar self)
        
        /**
         * Returns the PGButton that serves as the thumb for this slider, or NULL if
         * it is not set.
         */
        """
        pass

    def get_value(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(PGSliderBar self)
        
        /**
         * Returns the current value of the slider.
         */
        """
        pass

    def isButtonDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_button_down(PGSliderBar self)
        
        /**
         * Returns true if the user is currently holding down the mouse button to
         * manipulate the slider.  When true, calls to set_ratio() or set_value() will
         * have no effect.
         */
        """
        pass

    def is_button_down(self, PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_button_down(PGSliderBar self)
        
        /**
         * Returns true if the user is currently holding down the mouse button to
         * manipulate the slider.  When true, calls to set_ratio() or set_value() will
         * have no effect.
         */
        """
        pass

    def recompute(self, const_PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute(const PGSliderBar self)
        
        /**
         * Recomputes the position and size of the thumb.  Normally this should not
         * need to be called directly.
         */
        """
        pass

    def remanage(self, const_PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remanage(const PGSliderBar self)
        
        /**
         * Manages the position and size of the scroll bars and the thumb.  Normally
         * this should not need to be called directly.
         */
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const PGSliderBar self, bool active)
        
        /**
         * Sets whether the PGItem is active for mouse watching.  This is not
         * necessarily related to the active/inactive appearance of the item, which is
         * controlled by set_state(), but it does affect whether it responds to mouse
         * events.
         */
        """
        pass

    def setAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_axis(const PGSliderBar self, const LVector3f axis)
        
        /**
         * Specifies the axis of the slider bar's motion.  This should be only one of
         * four vectors: (1, 0, 0), (0, 0, 1), (-1, 0, 0), or (0, 0, -1).
         *
         * This specifies the vector in which the thumb moves when it is moving from
         * the minimum to the maximum value.
         *
         * The axis must be parallel to one of the screen axes, and it must be
         * normalized.  Hence, it may only be one of the above four possibilities;
         * anything else is an error and will result in indeterminate behavior.
         *
         * Normally, you should not try to set the axis directly.
         */
        """
        pass

    def setLeftButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_left_button(const PGSliderBar self, PGButton left_button)
        
        /**
         * Sets the PGButton object that will serve as the left scroll button for this
         * slider.  This button is optional; if present, the user can click on it to
         * move scroll_size units at a time to the left.
         *
         * It is the responsibility of the caller to ensure that the button object is
         * parented to the PGSliderBar node.
         */
        """
        pass

    def setManagePieces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_manage_pieces(const PGSliderBar self, bool manage_pieces)
        
        /**
         * Sets the manage_pieces flag.  When this is true, the sub-pieces of the
         * slider bar--that is, the thumb, and the left and right scroll buttons--are
         * automatically positioned and/or resized when the slider bar's overall frame
         * is changed.
         */
        """
        pass

    def setPageSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_page_size(const PGSliderBar self, float page_size)
        
        /**
         * Specifies the amount of data contained in a single page.  This indicates
         * how much the thumb will jump when the trough is directly clicked; and if
         * resize_thumb is true, it also controls the visible size of the thumb
         * button.
         */
        """
        pass

    def setRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_range(const PGSliderBar self, float min_value, float max_value)
        
        /**
         * Sets the minimum and maxmimum value for the slider.
         */
        """
        pass

    def setRatio(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ratio(const PGSliderBar self, float ratio)
        
        /**
         * Sets the current value of the slider, expressed in the range 0 .. 1.
         */
        """
        pass

    def setResizeThumb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_resize_thumb(const PGSliderBar self, bool resize_thumb)
        
        /**
         * Sets the resize_thumb flag.  When this is true, the thumb button's frame
         * will be adjusted so that its width visually represents the page size.  When
         * this is false, the thumb button will be left alone.
         */
        """
        pass

    def setRightButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_right_button(const PGSliderBar self, PGButton right_button)
        
        /**
         * Sets the PGButton object that will serve as the right scroll button for
         * this slider.  This button is optional; if present, the user can click on it
         * to move scroll_size units at a time to the right.
         *
         * It is the responsibility of the caller to ensure that the button object is
         * parented to the PGSliderBar node.
         */
        """
        pass

    def setScrollSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scroll_size(const PGSliderBar self, float scroll_size)
        
        /**
         * Specifies the amount the slider will move when the user clicks on the left
         * or right buttons.
         */
        """
        pass

    def setThumbButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_thumb_button(const PGSliderBar self, PGButton thumb_button)
        
        /**
         * Sets the PGButton object that will serve as the thumb for this slider.
         * This button visually represents the position of the slider, and can be
         * dragged left and right by the user.
         *
         * It is the responsibility of the caller to ensure that the button object is
         * parented to the PGSliderBar node.
         */
        """
        pass

    def setupScrollBar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_scroll_bar(const PGSliderBar self, bool vertical, float length, float width, float bevel)
        
        /**
         * Creates PGSliderBar that represents a vertical or horizontal scroll bar (if
         * vertical is true or false, respectively), with additional buttons for
         * scrolling, and a range of 0 .. 1.
         *
         * length here is the measurement along the scroll bar, and width is the
         * measurement across the scroll bar, whether it is vertical or horizontal (so
         * for a horizontal scroll bar, the length is actually the x dimension, and
         * the width is the y dimension).
         */
        """
        pass

    def setupSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_slider(const PGSliderBar self, bool vertical, float length, float width, float bevel)
        
        /**
         * Creates PGSliderBar that represents a slider that the user can use to
         * control an analog quantity.
         *
         * This is functionally the same as a scroll bar, but it has a distinctive
         * look.
         */
        """
        pass

    def setup_scroll_bar(self, const_PGSliderBar_self, bool_vertical, float_length, float_width, float_bevel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_scroll_bar(const PGSliderBar self, bool vertical, float length, float width, float bevel)
        
        /**
         * Creates PGSliderBar that represents a vertical or horizontal scroll bar (if
         * vertical is true or false, respectively), with additional buttons for
         * scrolling, and a range of 0 .. 1.
         *
         * length here is the measurement along the scroll bar, and width is the
         * measurement across the scroll bar, whether it is vertical or horizontal (so
         * for a horizontal scroll bar, the length is actually the x dimension, and
         * the width is the y dimension).
         */
        """
        pass

    def setup_slider(self, const_PGSliderBar_self, bool_vertical, float_length, float_width, float_bevel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_slider(const PGSliderBar self, bool vertical, float length, float width, float bevel)
        
        /**
         * Creates PGSliderBar that represents a slider that the user can use to
         * control an analog quantity.
         *
         * This is functionally the same as a scroll bar, but it has a distinctive
         * look.
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const PGSliderBar self, float value)
        
        /**
         * Sets the current value of the slider programmatically.  This should range
         * between get_min_value() and get_max_value().
         */
        """
        pass

    def set_active(self, const_PGSliderBar_self, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const PGSliderBar self, bool active)
        
        /**
         * Sets whether the PGItem is active for mouse watching.  This is not
         * necessarily related to the active/inactive appearance of the item, which is
         * controlled by set_state(), but it does affect whether it responds to mouse
         * events.
         */
        """
        pass

    def set_axis(self, const_PGSliderBar_self, const_LVector3f_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_axis(const PGSliderBar self, const LVector3f axis)
        
        /**
         * Specifies the axis of the slider bar's motion.  This should be only one of
         * four vectors: (1, 0, 0), (0, 0, 1), (-1, 0, 0), or (0, 0, -1).
         *
         * This specifies the vector in which the thumb moves when it is moving from
         * the minimum to the maximum value.
         *
         * The axis must be parallel to one of the screen axes, and it must be
         * normalized.  Hence, it may only be one of the above four possibilities;
         * anything else is an error and will result in indeterminate behavior.
         *
         * Normally, you should not try to set the axis directly.
         */
        """
        pass

    def set_left_button(self, const_PGSliderBar_self, PGButton_left_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_left_button(const PGSliderBar self, PGButton left_button)
        
        /**
         * Sets the PGButton object that will serve as the left scroll button for this
         * slider.  This button is optional; if present, the user can click on it to
         * move scroll_size units at a time to the left.
         *
         * It is the responsibility of the caller to ensure that the button object is
         * parented to the PGSliderBar node.
         */
        """
        pass

    def set_manage_pieces(self, const_PGSliderBar_self, bool_manage_pieces): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_manage_pieces(const PGSliderBar self, bool manage_pieces)
        
        /**
         * Sets the manage_pieces flag.  When this is true, the sub-pieces of the
         * slider bar--that is, the thumb, and the left and right scroll buttons--are
         * automatically positioned and/or resized when the slider bar's overall frame
         * is changed.
         */
        """
        pass

    def set_page_size(self, const_PGSliderBar_self, float_page_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_page_size(const PGSliderBar self, float page_size)
        
        /**
         * Specifies the amount of data contained in a single page.  This indicates
         * how much the thumb will jump when the trough is directly clicked; and if
         * resize_thumb is true, it also controls the visible size of the thumb
         * button.
         */
        """
        pass

    def set_range(self, const_PGSliderBar_self, float_min_value, float_max_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_range(const PGSliderBar self, float min_value, float max_value)
        
        /**
         * Sets the minimum and maxmimum value for the slider.
         */
        """
        pass

    def set_ratio(self, const_PGSliderBar_self, float_ratio): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ratio(const PGSliderBar self, float ratio)
        
        /**
         * Sets the current value of the slider, expressed in the range 0 .. 1.
         */
        """
        pass

    def set_resize_thumb(self, const_PGSliderBar_self, bool_resize_thumb): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_resize_thumb(const PGSliderBar self, bool resize_thumb)
        
        /**
         * Sets the resize_thumb flag.  When this is true, the thumb button's frame
         * will be adjusted so that its width visually represents the page size.  When
         * this is false, the thumb button will be left alone.
         */
        """
        pass

    def set_right_button(self, const_PGSliderBar_self, PGButton_right_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_right_button(const PGSliderBar self, PGButton right_button)
        
        /**
         * Sets the PGButton object that will serve as the right scroll button for
         * this slider.  This button is optional; if present, the user can click on it
         * to move scroll_size units at a time to the right.
         *
         * It is the responsibility of the caller to ensure that the button object is
         * parented to the PGSliderBar node.
         */
        """
        pass

    def set_scroll_size(self, const_PGSliderBar_self, float_scroll_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scroll_size(const PGSliderBar self, float scroll_size)
        
        /**
         * Specifies the amount the slider will move when the user clicks on the left
         * or right buttons.
         */
        """
        pass

    def set_thumb_button(self, const_PGSliderBar_self, PGButton_thumb_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_thumb_button(const PGSliderBar self, PGButton thumb_button)
        
        /**
         * Sets the PGButton object that will serve as the thumb for this slider.
         * This button visually represents the position of the slider, and can be
         * dragged left and right by the user.
         *
         * It is the responsibility of the caller to ensure that the button object is
         * parented to the PGSliderBar node.
         */
        """
        pass

    def set_value(self, const_PGSliderBar_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const PGSliderBar self, float value)
        
        /**
         * Sets the current value of the slider programmatically.  This should range
         * between get_min_value() and get_max_value().
         */
        """
        pass

    def upcastToPGItem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_PGItem(const PGSliderBar self)
        
        upcast from PGSliderBar to PGItem
        """
        pass

    def upcast_to_PGItem(self, const_PGSliderBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_PGItem(const PGSliderBar self)
        
        upcast from PGSliderBar to PGItem
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
        '__doc__': '/**\n * This is a particular kind of PGItem that draws a little bar with a slider\n * that moves from left to right indicating a value between the ranges.\n *\n * This is used as an implementation for both DirectSlider and for\n * DirectScrollBar.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PGSliderBar' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE384C80>'
        'clearLeftButton': None, # (!) real value is "<method 'clearLeftButton' of 'panda3d.core.PGSliderBar' objects>"
        'clearRightButton': None, # (!) real value is "<method 'clearRightButton' of 'panda3d.core.PGSliderBar' objects>"
        'clearThumbButton': None, # (!) real value is "<method 'clearThumbButton' of 'panda3d.core.PGSliderBar' objects>"
        'clear_left_button': None, # (!) real value is "<method 'clear_left_button' of 'panda3d.core.PGSliderBar' objects>"
        'clear_right_button': None, # (!) real value is "<method 'clear_right_button' of 'panda3d.core.PGSliderBar' objects>"
        'clear_thumb_button': None, # (!) real value is "<method 'clear_thumb_button' of 'panda3d.core.PGSliderBar' objects>"
        'getAdjustEvent': None, # (!) real value is "<method 'getAdjustEvent' of 'panda3d.core.PGSliderBar' objects>"
        'getAdjustPrefix': None, # (!) real value is '<staticmethod(<built-in method getAdjustPrefix of type object at 0x00007FFCFE384C80>)>'
        'getAxis': None, # (!) real value is "<method 'getAxis' of 'panda3d.core.PGSliderBar' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE384C80>)>'
        'getLeftButton': None, # (!) real value is "<method 'getLeftButton' of 'panda3d.core.PGSliderBar' objects>"
        'getManagePieces': None, # (!) real value is "<method 'getManagePieces' of 'panda3d.core.PGSliderBar' objects>"
        'getMaxValue': None, # (!) real value is "<method 'getMaxValue' of 'panda3d.core.PGSliderBar' objects>"
        'getMinValue': None, # (!) real value is "<method 'getMinValue' of 'panda3d.core.PGSliderBar' objects>"
        'getPageSize': None, # (!) real value is "<method 'getPageSize' of 'panda3d.core.PGSliderBar' objects>"
        'getRatio': None, # (!) real value is "<method 'getRatio' of 'panda3d.core.PGSliderBar' objects>"
        'getResizeThumb': None, # (!) real value is "<method 'getResizeThumb' of 'panda3d.core.PGSliderBar' objects>"
        'getRightButton': None, # (!) real value is "<method 'getRightButton' of 'panda3d.core.PGSliderBar' objects>"
        'getScrollSize': None, # (!) real value is "<method 'getScrollSize' of 'panda3d.core.PGSliderBar' objects>"
        'getThumbButton': None, # (!) real value is "<method 'getThumbButton' of 'panda3d.core.PGSliderBar' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.PGSliderBar' objects>"
        'get_adjust_event': None, # (!) real value is "<method 'get_adjust_event' of 'panda3d.core.PGSliderBar' objects>"
        'get_adjust_prefix': None, # (!) real value is '<staticmethod(<built-in method get_adjust_prefix of type object at 0x00007FFCFE384C80>)>'
        'get_axis': None, # (!) real value is "<method 'get_axis' of 'panda3d.core.PGSliderBar' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE384C80>)>'
        'get_left_button': None, # (!) real value is "<method 'get_left_button' of 'panda3d.core.PGSliderBar' objects>"
        'get_manage_pieces': None, # (!) real value is "<method 'get_manage_pieces' of 'panda3d.core.PGSliderBar' objects>"
        'get_max_value': None, # (!) real value is "<method 'get_max_value' of 'panda3d.core.PGSliderBar' objects>"
        'get_min_value': None, # (!) real value is "<method 'get_min_value' of 'panda3d.core.PGSliderBar' objects>"
        'get_page_size': None, # (!) real value is "<method 'get_page_size' of 'panda3d.core.PGSliderBar' objects>"
        'get_ratio': None, # (!) real value is "<method 'get_ratio' of 'panda3d.core.PGSliderBar' objects>"
        'get_resize_thumb': None, # (!) real value is "<method 'get_resize_thumb' of 'panda3d.core.PGSliderBar' objects>"
        'get_right_button': None, # (!) real value is "<method 'get_right_button' of 'panda3d.core.PGSliderBar' objects>"
        'get_scroll_size': None, # (!) real value is "<method 'get_scroll_size' of 'panda3d.core.PGSliderBar' objects>"
        'get_thumb_button': None, # (!) real value is "<method 'get_thumb_button' of 'panda3d.core.PGSliderBar' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.PGSliderBar' objects>"
        'isButtonDown': None, # (!) real value is "<method 'isButtonDown' of 'panda3d.core.PGSliderBar' objects>"
        'is_button_down': None, # (!) real value is "<method 'is_button_down' of 'panda3d.core.PGSliderBar' objects>"
        'recompute': None, # (!) real value is "<method 'recompute' of 'panda3d.core.PGSliderBar' objects>"
        'remanage': None, # (!) real value is "<method 'remanage' of 'panda3d.core.PGSliderBar' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.PGSliderBar' objects>"
        'setAxis': None, # (!) real value is "<method 'setAxis' of 'panda3d.core.PGSliderBar' objects>"
        'setLeftButton': None, # (!) real value is "<method 'setLeftButton' of 'panda3d.core.PGSliderBar' objects>"
        'setManagePieces': None, # (!) real value is "<method 'setManagePieces' of 'panda3d.core.PGSliderBar' objects>"
        'setPageSize': None, # (!) real value is "<method 'setPageSize' of 'panda3d.core.PGSliderBar' objects>"
        'setRange': None, # (!) real value is "<method 'setRange' of 'panda3d.core.PGSliderBar' objects>"
        'setRatio': None, # (!) real value is "<method 'setRatio' of 'panda3d.core.PGSliderBar' objects>"
        'setResizeThumb': None, # (!) real value is "<method 'setResizeThumb' of 'panda3d.core.PGSliderBar' objects>"
        'setRightButton': None, # (!) real value is "<method 'setRightButton' of 'panda3d.core.PGSliderBar' objects>"
        'setScrollSize': None, # (!) real value is "<method 'setScrollSize' of 'panda3d.core.PGSliderBar' objects>"
        'setThumbButton': None, # (!) real value is "<method 'setThumbButton' of 'panda3d.core.PGSliderBar' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.core.PGSliderBar' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.PGSliderBar' objects>"
        'set_axis': None, # (!) real value is "<method 'set_axis' of 'panda3d.core.PGSliderBar' objects>"
        'set_left_button': None, # (!) real value is "<method 'set_left_button' of 'panda3d.core.PGSliderBar' objects>"
        'set_manage_pieces': None, # (!) real value is "<method 'set_manage_pieces' of 'panda3d.core.PGSliderBar' objects>"
        'set_page_size': None, # (!) real value is "<method 'set_page_size' of 'panda3d.core.PGSliderBar' objects>"
        'set_range': None, # (!) real value is "<method 'set_range' of 'panda3d.core.PGSliderBar' objects>"
        'set_ratio': None, # (!) real value is "<method 'set_ratio' of 'panda3d.core.PGSliderBar' objects>"
        'set_resize_thumb': None, # (!) real value is "<method 'set_resize_thumb' of 'panda3d.core.PGSliderBar' objects>"
        'set_right_button': None, # (!) real value is "<method 'set_right_button' of 'panda3d.core.PGSliderBar' objects>"
        'set_scroll_size': None, # (!) real value is "<method 'set_scroll_size' of 'panda3d.core.PGSliderBar' objects>"
        'set_thumb_button': None, # (!) real value is "<method 'set_thumb_button' of 'panda3d.core.PGSliderBar' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.core.PGSliderBar' objects>"
        'setupScrollBar': None, # (!) real value is "<method 'setupScrollBar' of 'panda3d.core.PGSliderBar' objects>"
        'setupSlider': None, # (!) real value is "<method 'setupSlider' of 'panda3d.core.PGSliderBar' objects>"
        'setup_scroll_bar': None, # (!) real value is "<method 'setup_scroll_bar' of 'panda3d.core.PGSliderBar' objects>"
        'setup_slider': None, # (!) real value is "<method 'setup_slider' of 'panda3d.core.PGSliderBar' objects>"
        'upcastToPGItem': None, # (!) real value is "<method 'upcastToPGItem' of 'panda3d.core.PGSliderBar' objects>"
        'upcast_to_PGItem': None, # (!) real value is "<method 'upcast_to_PGItem' of 'panda3d.core.PGSliderBar' objects>"
    }


