# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class PGItem(PandaNode):
    """
    /**
     * This is the base class for all the various kinds of gui widget objects.
     *
     * It is a Node which corresponds to a rectangular region on the screen, and
     * it may have any number of "state" subgraphs, one of which is rendered at
     * any given time according to its current state.
     *
     * The PGItem node must be parented to the scene graph somewhere beneath a
     * PGTop node in order for this behavior to work.
     */
    """
    def clearFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_frame(const PGItem self)
        
        /**
         * Removes the bounding rectangle from the item.  It will no longer be
         * possible to position the mouse within the item; see set_frame().
         */
        """
        pass

    def clearSound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_sound(const PGItem self, str event)
        
        /**
         * Removes the sound associated with the indicated event.
         */
        """
        pass

    def clearStateDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_state_def(const PGItem self, int state)
        
        /**
         * Resets the NodePath assigned to the indicated state to its initial default,
         * with only a frame representation if appropriate.
         */
        """
        pass

    def clear_frame(self, const_PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_frame(const PGItem self)
        
        /**
         * Removes the bounding rectangle from the item.  It will no longer be
         * possible to position the mouse within the item; see set_frame().
         */
        """
        pass

    def clear_sound(self, const_PGItem_self, str_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_sound(const PGItem self, str event)
        
        /**
         * Removes the sound associated with the indicated event.
         */
        """
        pass

    def clear_state_def(self, const_PGItem_self, int_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_state_def(const PGItem self, int state)
        
        /**
         * Resets the NodePath assigned to the indicated state to its initial default,
         * with only a frame representation if appropriate.
         */
        """
        pass

    def getActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active(PGItem self)
        
        /**
         * Returns whether the PGItem is currently active for mouse events.  See
         * set_active().
         */
        """
        pass

    def getBackgroundFocus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_background_focus(PGItem self)
        
        /**
         * Returns whether background_focus is currently enabled.  See
         * set_background_focus().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getEnterEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_enter_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * mouse enters its frame, but not any nested frames.
         */
        """
        pass

    def getEnterPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_enter_prefix()
        
        /**
         * Returns the prefix that is used to define the enter event for all PGItems.
         * The enter event is the concatenation of this string followed by get_id().
         */
        """
        pass

    def getExitEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_exit_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * mouse exits its frame, or enters a nested frame.
         */
        """
        pass

    def getExitPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_exit_prefix()
        
        /**
         * Returns the prefix that is used to define the exit event for all PGItems.
         * The exit event is the concatenation of this string followed by get_id().
         */
        """
        pass

    def getFocus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_focus(PGItem self)
        
        /**
         * Returns whether the PGItem currently has focus for keyboard events.  See
         * set_focus().
         */
        """
        pass

    def getFocusInEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_focus_in_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item gets the keyboard
         * focus.
         */
        """
        pass

    def getFocusInPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_focus_in_prefix()
        
        /**
         * Returns the prefix that is used to define the focus_in event for all
         * PGItems.  The focus_in event is the concatenation of this string followed
         * by get_id().
         *
         * Unlike most item events, this event is thrown with no parameters.
         */
        """
        pass

    def getFocusItem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_focus_item()
        
        /**
         * Returns the one PGItem in the world that currently has keyboard focus, if
         * any, or NULL if no item has keyboard focus.  Use PGItem::set_focus() to
         * activate or deactivate keyboard focus on a particular item.
         */
        """
        pass

    def getFocusOutEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_focus_out_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item loses the keyboard
         * focus.
         */
        """
        pass

    def getFocusOutPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_focus_out_prefix()
        
        /**
         * Returns the prefix that is used to define the focus_out event for all
         * PGItems.  The focus_out event is the concatenation of this string followed
         * by get_id().
         *
         * Unlike most item events, this event is thrown with no parameters.
         */
        """
        pass

    def getFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame(PGItem self)
        
        /**
         * Returns the bounding rectangle of the item.  See set_frame().  It is an
         * error to call this if has_frame() returns false.
         */
        """
        pass

    def getFrameInvXform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_inv_xform(PGItem self)
        
        /**
         * Returns the inverse of the frame transform matrix
         */
        """
        pass

    def getFrameStyle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_style(const PGItem self, int state)
        
        /**
         * Returns the kind of frame that will be drawn behind the item when it is in
         * the indicated state.
         */
        """
        pass

    def getId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_id(PGItem self)
        
        /**
         * Returns the unique ID assigned to this PGItem.  This will be assigned to
         * the region created with the MouseWatcher, and will thus be used to generate
         * event names.
         */
        """
        pass

    def getKeystrokeEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keystroke_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and any
         * key is pressed by the user.
         */
        """
        pass

    def getKeystrokePrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keystroke_prefix()
        
        /**
         * Returns the prefix that is used to define the keystroke event for all
         * PGItems.  The keystroke event is the concatenation of this string followed
         * by a hyphen and get_id().
         */
        """
        pass

    def getNumStateDefs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_state_defs(PGItem self)
        
        /**
         * Returns one more than the highest-numbered state def that was ever assigned
         * to the PGItem.  The complete set of state defs assigned may then be
         * retrieved by indexing from 0 to (get_num_state_defs() - 1).
         *
         * This is only an upper limit on the actual number of state defs, since there
         * may be holes in the list.
         */
        """
        pass

    def getPressEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_press_event(PGItem self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * indicated mouse or keyboard button is depressed while the mouse is within
         * the frame.
         */
        """
        pass

    def getPressPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_press_prefix()
        
        /**
         * Returns the prefix that is used to define the press event for all PGItems.
         * The press event is the concatenation of this string followed by a button
         * name, followed by a hyphen and get_id().
         */
        """
        pass

    def getReleaseEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_release_event(PGItem self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * indicated mouse or keyboard button, formerly clicked down is within the
         * frame, is released.
         */
        """
        pass

    def getReleasePrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_release_prefix()
        
        /**
         * Returns the prefix that is used to define the release event for all
         * PGItems.  The release event is the concatenation of this string followed by
         * a button name, followed by a hyphen and get_id().
         */
        """
        pass

    def getRepeatEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_repeat_event(PGItem self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * indicated mouse or keyboard button is continuously held down while the
         * mouse is within the frame.
         */
        """
        pass

    def getRepeatPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_repeat_prefix()
        
        /**
         * Returns the prefix that is used to define the repeat event for all PGItems.
         * The repeat event is the concatenation of this string followed by a button
         * name, followed by a hyphen and get_id().
         */
        """
        pass

    def getSound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sound(PGItem self, str event)
        
        /**
         * Returns the sound associated with the indicated event, or NULL if there is
         * no associated sound.
         */
        """
        pass

    def getState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_state(PGItem self)
        
        /**
         * Returns the "state" of this particular PGItem.  See set_state().
         */
        """
        pass

    def getStateDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_state_def(const PGItem self, int state)
        
        /**
         * Returns the Node that is the root of the subgraph that will be drawn when
         * the PGItem is in the indicated state.  The first time this is called for a
         * particular state index, it may create the Node.
         */
        """
        pass

    def getStateDefs(self, *args, **kwargs): # real signature unknown
        pass

    def getSuppressFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_suppress_flags(PGItem self)
        
        /**
         * This is just an interface to get the suppress flags on the underlying
         * MouseWatcherRegion.  See MouseWatcherRegion::get_suppress_flags().
         */
        """
        pass

    def getTextNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_text_node()
        
        /**
         * Returns the TextNode object that will be used by all PGItems to generate
         * default labels given a string.  This can be loaded with the default font,
         * etc.
         */
        """
        pass

    def getWithinEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_within_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * mouse moves within the boundaries of the frame.  This is different from the
         * enter_event in that the mouse is considered within the frame even if it is
         * also within a nested frame.
         */
        """
        pass

    def getWithinPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_within_prefix()
        
        /**
         * Returns the prefix that is used to define the within event for all PGItems.
         * The within event is the concatenation of this string followed by get_id().
         */
        """
        pass

    def getWithoutEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_without_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * mouse moves completely outside the boundaries of the frame.  This is
         * different from the exit_event in that the mouse is considered within the
         * frame even if it is also within a nested frame.
         */
        """
        pass

    def getWithoutPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_without_prefix()
        
        /**
         * Returns the prefix that is used to define the without event for all
         * PGItems.  The without event is the concatenation of this string followed by
         * get_id().
         */
        """
        pass

    def get_active(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active(PGItem self)
        
        /**
         * Returns whether the PGItem is currently active for mouse events.  See
         * set_active().
         */
        """
        pass

    def get_background_focus(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_background_focus(PGItem self)
        
        /**
         * Returns whether background_focus is currently enabled.  See
         * set_background_focus().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_enter_event(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_enter_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * mouse enters its frame, but not any nested frames.
         */
        """
        pass

    def get_enter_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_enter_prefix()
        
        /**
         * Returns the prefix that is used to define the enter event for all PGItems.
         * The enter event is the concatenation of this string followed by get_id().
         */
        """
        pass

    def get_exit_event(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_exit_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * mouse exits its frame, or enters a nested frame.
         */
        """
        pass

    def get_exit_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_exit_prefix()
        
        /**
         * Returns the prefix that is used to define the exit event for all PGItems.
         * The exit event is the concatenation of this string followed by get_id().
         */
        """
        pass

    def get_focus(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_focus(PGItem self)
        
        /**
         * Returns whether the PGItem currently has focus for keyboard events.  See
         * set_focus().
         */
        """
        pass

    def get_focus_in_event(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_focus_in_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item gets the keyboard
         * focus.
         */
        """
        pass

    def get_focus_in_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_focus_in_prefix()
        
        /**
         * Returns the prefix that is used to define the focus_in event for all
         * PGItems.  The focus_in event is the concatenation of this string followed
         * by get_id().
         *
         * Unlike most item events, this event is thrown with no parameters.
         */
        """
        pass

    def get_focus_item(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_focus_item()
        
        /**
         * Returns the one PGItem in the world that currently has keyboard focus, if
         * any, or NULL if no item has keyboard focus.  Use PGItem::set_focus() to
         * activate or deactivate keyboard focus on a particular item.
         */
        """
        pass

    def get_focus_out_event(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_focus_out_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item loses the keyboard
         * focus.
         */
        """
        pass

    def get_focus_out_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_focus_out_prefix()
        
        /**
         * Returns the prefix that is used to define the focus_out event for all
         * PGItems.  The focus_out event is the concatenation of this string followed
         * by get_id().
         *
         * Unlike most item events, this event is thrown with no parameters.
         */
        """
        pass

    def get_frame(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame(PGItem self)
        
        /**
         * Returns the bounding rectangle of the item.  See set_frame().  It is an
         * error to call this if has_frame() returns false.
         */
        """
        pass

    def get_frame_inv_xform(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_inv_xform(PGItem self)
        
        /**
         * Returns the inverse of the frame transform matrix
         */
        """
        pass

    def get_frame_style(self, const_PGItem_self, int_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_style(const PGItem self, int state)
        
        /**
         * Returns the kind of frame that will be drawn behind the item when it is in
         * the indicated state.
         */
        """
        pass

    def get_id(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_id(PGItem self)
        
        /**
         * Returns the unique ID assigned to this PGItem.  This will be assigned to
         * the region created with the MouseWatcher, and will thus be used to generate
         * event names.
         */
        """
        pass

    def get_keystroke_event(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keystroke_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and any
         * key is pressed by the user.
         */
        """
        pass

    def get_keystroke_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keystroke_prefix()
        
        /**
         * Returns the prefix that is used to define the keystroke event for all
         * PGItems.  The keystroke event is the concatenation of this string followed
         * by a hyphen and get_id().
         */
        """
        pass

    def get_num_state_defs(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_state_defs(PGItem self)
        
        /**
         * Returns one more than the highest-numbered state def that was ever assigned
         * to the PGItem.  The complete set of state defs assigned may then be
         * retrieved by indexing from 0 to (get_num_state_defs() - 1).
         *
         * This is only an upper limit on the actual number of state defs, since there
         * may be holes in the list.
         */
        """
        pass

    def get_press_event(self, PGItem_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_press_event(PGItem self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * indicated mouse or keyboard button is depressed while the mouse is within
         * the frame.
         */
        """
        pass

    def get_press_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_press_prefix()
        
        /**
         * Returns the prefix that is used to define the press event for all PGItems.
         * The press event is the concatenation of this string followed by a button
         * name, followed by a hyphen and get_id().
         */
        """
        pass

    def get_release_event(self, PGItem_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_release_event(PGItem self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * indicated mouse or keyboard button, formerly clicked down is within the
         * frame, is released.
         */
        """
        pass

    def get_release_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_release_prefix()
        
        /**
         * Returns the prefix that is used to define the release event for all
         * PGItems.  The release event is the concatenation of this string followed by
         * a button name, followed by a hyphen and get_id().
         */
        """
        pass

    def get_repeat_event(self, PGItem_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_repeat_event(PGItem self, const ButtonHandle button)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * indicated mouse or keyboard button is continuously held down while the
         * mouse is within the frame.
         */
        """
        pass

    def get_repeat_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_repeat_prefix()
        
        /**
         * Returns the prefix that is used to define the repeat event for all PGItems.
         * The repeat event is the concatenation of this string followed by a button
         * name, followed by a hyphen and get_id().
         */
        """
        pass

    def get_sound(self, PGItem_self, str_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sound(PGItem self, str event)
        
        /**
         * Returns the sound associated with the indicated event, or NULL if there is
         * no associated sound.
         */
        """
        pass

    def get_state(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_state(PGItem self)
        
        /**
         * Returns the "state" of this particular PGItem.  See set_state().
         */
        """
        pass

    def get_state_def(self, const_PGItem_self, int_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_state_def(const PGItem self, int state)
        
        /**
         * Returns the Node that is the root of the subgraph that will be drawn when
         * the PGItem is in the indicated state.  The first time this is called for a
         * particular state index, it may create the Node.
         */
        """
        pass

    def get_state_defs(self, *args, **kwargs): # real signature unknown
        pass

    def get_suppress_flags(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_suppress_flags(PGItem self)
        
        /**
         * This is just an interface to get the suppress flags on the underlying
         * MouseWatcherRegion.  See MouseWatcherRegion::get_suppress_flags().
         */
        """
        pass

    def get_text_node(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_text_node()
        
        /**
         * Returns the TextNode object that will be used by all PGItems to generate
         * default labels given a string.  This can be loaded with the default font,
         * etc.
         */
        """
        pass

    def get_within_event(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_within_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * mouse moves within the boundaries of the frame.  This is different from the
         * enter_event in that the mouse is considered within the frame even if it is
         * also within a nested frame.
         */
        """
        pass

    def get_within_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_within_prefix()
        
        /**
         * Returns the prefix that is used to define the within event for all PGItems.
         * The within event is the concatenation of this string followed by get_id().
         */
        """
        pass

    def get_without_event(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_without_event(PGItem self)
        
        /**
         * Returns the event name that will be thrown when the item is active and the
         * mouse moves completely outside the boundaries of the frame.  This is
         * different from the exit_event in that the mouse is considered within the
         * frame even if it is also within a nested frame.
         */
        """
        pass

    def get_without_prefix(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_without_prefix()
        
        /**
         * Returns the prefix that is used to define the without event for all
         * PGItems.  The without event is the concatenation of this string followed by
         * get_id().
         */
        """
        pass

    def hasFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_frame(PGItem self)
        
        /**
         * Returns true if the item has a bounding rectangle; see set_frame().
         */
        """
        pass

    def hasSound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_sound(PGItem self, str event)
        
        /**
         * Returns true if there is a sound associated with the indicated event, or
         * false otherwise.
         */
        """
        pass

    def hasStateDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_state_def(PGItem self, int state)
        
        /**
         * Returns true if get_state_def() has ever been called for the indicated
         * state (thus defining a render subgraph for this state index), false
         * otherwise.
         */
        """
        pass

    def has_frame(self, PGItem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_frame(PGItem self)
        
        /**
         * Returns true if the item has a bounding rectangle; see set_frame().
         */
        """
        pass

    def has_sound(self, PGItem_self, str_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_sound(PGItem self, str event)
        
        /**
         * Returns true if there is a sound associated with the indicated event, or
         * false otherwise.
         */
        """
        pass

    def has_state_def(self, PGItem_self, int_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_state_def(PGItem self, int state)
        
        /**
         * Returns true if get_state_def() has ever been called for the indicated
         * state (thus defining a render subgraph for this state index), false
         * otherwise.
         */
        """
        pass

    def instanceToStateDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        instance_to_state_def(const PGItem self, int state, const NodePath path)
        
        /**
         * Parents an instance of the bottom node of the indicated NodePath to the
         * indicated state index.
         */
        """
        pass

    def instance_to_state_def(self, const_PGItem_self, int_state, const_NodePath_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        instance_to_state_def(const PGItem self, int state, const NodePath path)
        
        /**
         * Parents an instance of the bottom node of the indicated NodePath to the
         * indicated state index.
         */
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const PGItem self, bool active)
        
        /**
         * Sets whether the PGItem is active for mouse watching.  This is not
         * necessarily related to the active/inactive appearance of the item, which is
         * controlled by set_state(), but it does affect whether it responds to mouse
         * events.
         */
        """
        pass

    def setBackgroundFocus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_background_focus(const PGItem self, bool focus)
        
        /**
         * Sets the background_focus flag for this item.  When background_focus is
         * enabled, the item will receive keypress events even if it is not in focus;
         * in fact, even if it is not onscreen.  Unlike normal focus, many items may
         * have background_focus simultaneously.
         */
        """
        pass

    def setFocus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_focus(const PGItem self, bool focus)
        
        /**
         * Sets whether the PGItem currently has keyboard focus.  This simply means
         * that the item may respond to keyboard events as well as to mouse events;
         * precisely what this means is up to the individual item.
         *
         * Only one PGItem in the world is allowed to have focus at any given time.
         * Setting the focus on any other item automatically disables the focus from
         * the previous item.
         */
        """
        pass

    def setFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame(const PGItem self, const LVecBase4f frame)
        set_frame(const PGItem self, float left, float right, float bottom, float top)
        
        /**
         * Sets the bounding rectangle of the item, in local coordinates.  This is the
         * region on screen within which the mouse will be considered to be within the
         * item.  Normally, it should correspond to the bounding rectangle of the
         * visible geometry of the item.
         */
        
        /**
         * Sets the bounding rectangle of the item, in local coordinates.  This is the
         * region on screen within which the mouse will be considered to be within the
         * item.  Normally, it should correspond to the bounding rectangle of the
         * visible geometry of the item.
         */
        """
        pass

    def setFrameStyle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_style(const PGItem self, int state, const PGFrameStyle style)
        
        /**
         * Changes the kind of frame that will be drawn behind the item when it is in
         * the indicated state.
         */
        """
        pass

    def setId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_id(const PGItem self, str id)
        
        /**
         * Set the unique ID assigned to this PGItem.  It is the user's responsibility
         * to ensure that this ID is unique.
         *
         * Normally, this should not need to be called, as the PGItem will assign
         * itself an ID when it is created, but this function allows the user to
         * decide to redefine the ID to be something possibly more meaningful.
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const PGItem self, str name)
        
        /**
         *
         */
        """
        pass

    def setSound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sound(const PGItem self, str event, AudioSound sound)
        
        /**
         * Sets the sound that will be played whenever the indicated event occurs.
         */
        """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_state(const PGItem self, int state)
        
        /**
         * Sets the "state" of this particular PGItem.
         *
         * The PGItem node will render as if it were the subgraph assigned to the
         * corresponding index via set_state_def().
         */
        """
        pass

    def setSuppressFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_suppress_flags(const PGItem self, int suppress_flags)
        
        /**
         * This is just an interface to set the suppress flags on the underlying
         * MouseWatcherRegion.  See MouseWatcherRegion::set_suppress_flags().
         */
        """
        pass

    def setTextNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_text_node(TextNode node)
        
        /**
         * Changes the TextNode object that will be used by all PGItems to generate
         * default labels given a string.  This can be loaded with the default font,
         * etc.
         */
        """
        pass

    def set_active(self, const_PGItem_self, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const PGItem self, bool active)
        
        /**
         * Sets whether the PGItem is active for mouse watching.  This is not
         * necessarily related to the active/inactive appearance of the item, which is
         * controlled by set_state(), but it does affect whether it responds to mouse
         * events.
         */
        """
        pass

    def set_background_focus(self, const_PGItem_self, bool_focus): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_background_focus(const PGItem self, bool focus)
        
        /**
         * Sets the background_focus flag for this item.  When background_focus is
         * enabled, the item will receive keypress events even if it is not in focus;
         * in fact, even if it is not onscreen.  Unlike normal focus, many items may
         * have background_focus simultaneously.
         */
        """
        pass

    def set_focus(self, const_PGItem_self, bool_focus): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_focus(const PGItem self, bool focus)
        
        /**
         * Sets whether the PGItem currently has keyboard focus.  This simply means
         * that the item may respond to keyboard events as well as to mouse events;
         * precisely what this means is up to the individual item.
         *
         * Only one PGItem in the world is allowed to have focus at any given time.
         * Setting the focus on any other item automatically disables the focus from
         * the previous item.
         */
        """
        pass

    def set_frame(self, const_PGItem_self, const_LVecBase4f_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame(const PGItem self, const LVecBase4f frame)
        set_frame(const PGItem self, float left, float right, float bottom, float top)
        
        /**
         * Sets the bounding rectangle of the item, in local coordinates.  This is the
         * region on screen within which the mouse will be considered to be within the
         * item.  Normally, it should correspond to the bounding rectangle of the
         * visible geometry of the item.
         */
        
        /**
         * Sets the bounding rectangle of the item, in local coordinates.  This is the
         * region on screen within which the mouse will be considered to be within the
         * item.  Normally, it should correspond to the bounding rectangle of the
         * visible geometry of the item.
         */
        """
        pass

    def set_frame_style(self, const_PGItem_self, int_state, const_PGFrameStyle_style): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_style(const PGItem self, int state, const PGFrameStyle style)
        
        /**
         * Changes the kind of frame that will be drawn behind the item when it is in
         * the indicated state.
         */
        """
        pass

    def set_id(self, const_PGItem_self, str_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_id(const PGItem self, str id)
        
        /**
         * Set the unique ID assigned to this PGItem.  It is the user's responsibility
         * to ensure that this ID is unique.
         *
         * Normally, this should not need to be called, as the PGItem will assign
         * itself an ID when it is created, but this function allows the user to
         * decide to redefine the ID to be something possibly more meaningful.
         */
        """
        pass

    def set_name(self, const_PGItem_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const PGItem self, str name)
        
        /**
         *
         */
        """
        pass

    def set_sound(self, const_PGItem_self, str_event, AudioSound_sound): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sound(const PGItem self, str event, AudioSound sound)
        
        /**
         * Sets the sound that will be played whenever the indicated event occurs.
         */
        """
        pass

    def set_state(self, const_PGItem_self, int_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_state(const PGItem self, int state)
        
        /**
         * Sets the "state" of this particular PGItem.
         *
         * The PGItem node will render as if it were the subgraph assigned to the
         * corresponding index via set_state_def().
         */
        """
        pass

    def set_suppress_flags(self, const_PGItem_self, int_suppress_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_suppress_flags(const PGItem self, int suppress_flags)
        
        /**
         * This is just an interface to set the suppress flags on the underlying
         * MouseWatcherRegion.  See MouseWatcherRegion::set_suppress_flags().
         */
        """
        pass

    def set_text_node(self, TextNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_text_node(TextNode node)
        
        /**
         * Changes the TextNode object that will be used by all PGItems to generate
         * default labels given a string.  This can be loaded with the default font,
         * etc.
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
        '__doc__': '/**\n * This is the base class for all the various kinds of gui widget objects.\n *\n * It is a Node which corresponds to a rectangular region on the screen, and\n * it may have any number of "state" subgraphs, one of which is rendered at\n * any given time according to its current state.\n *\n * The PGItem node must be parented to the scene graph somewhere beneath a\n * PGTop node in order for this behavior to work.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PGItem' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE383FD0>'
        'clearFrame': None, # (!) real value is "<method 'clearFrame' of 'panda3d.core.PGItem' objects>"
        'clearSound': None, # (!) real value is "<method 'clearSound' of 'panda3d.core.PGItem' objects>"
        'clearStateDef': None, # (!) real value is "<method 'clearStateDef' of 'panda3d.core.PGItem' objects>"
        'clear_frame': None, # (!) real value is "<method 'clear_frame' of 'panda3d.core.PGItem' objects>"
        'clear_sound': None, # (!) real value is "<method 'clear_sound' of 'panda3d.core.PGItem' objects>"
        'clear_state_def': None, # (!) real value is "<method 'clear_state_def' of 'panda3d.core.PGItem' objects>"
        'getActive': None, # (!) real value is "<method 'getActive' of 'panda3d.core.PGItem' objects>"
        'getBackgroundFocus': None, # (!) real value is "<method 'getBackgroundFocus' of 'panda3d.core.PGItem' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE383FD0>)>'
        'getEnterEvent': None, # (!) real value is "<method 'getEnterEvent' of 'panda3d.core.PGItem' objects>"
        'getEnterPrefix': None, # (!) real value is '<staticmethod(<built-in method getEnterPrefix of type object at 0x00007FFCFE383FD0>)>'
        'getExitEvent': None, # (!) real value is "<method 'getExitEvent' of 'panda3d.core.PGItem' objects>"
        'getExitPrefix': None, # (!) real value is '<staticmethod(<built-in method getExitPrefix of type object at 0x00007FFCFE383FD0>)>'
        'getFocus': None, # (!) real value is "<method 'getFocus' of 'panda3d.core.PGItem' objects>"
        'getFocusInEvent': None, # (!) real value is "<method 'getFocusInEvent' of 'panda3d.core.PGItem' objects>"
        'getFocusInPrefix': None, # (!) real value is '<staticmethod(<built-in method getFocusInPrefix of type object at 0x00007FFCFE383FD0>)>'
        'getFocusItem': None, # (!) real value is '<staticmethod(<built-in method getFocusItem of type object at 0x00007FFCFE383FD0>)>'
        'getFocusOutEvent': None, # (!) real value is "<method 'getFocusOutEvent' of 'panda3d.core.PGItem' objects>"
        'getFocusOutPrefix': None, # (!) real value is '<staticmethod(<built-in method getFocusOutPrefix of type object at 0x00007FFCFE383FD0>)>'
        'getFrame': None, # (!) real value is "<method 'getFrame' of 'panda3d.core.PGItem' objects>"
        'getFrameInvXform': None, # (!) real value is "<method 'getFrameInvXform' of 'panda3d.core.PGItem' objects>"
        'getFrameStyle': None, # (!) real value is "<method 'getFrameStyle' of 'panda3d.core.PGItem' objects>"
        'getId': None, # (!) real value is "<method 'getId' of 'panda3d.core.PGItem' objects>"
        'getKeystrokeEvent': None, # (!) real value is "<method 'getKeystrokeEvent' of 'panda3d.core.PGItem' objects>"
        'getKeystrokePrefix': None, # (!) real value is '<staticmethod(<built-in method getKeystrokePrefix of type object at 0x00007FFCFE383FD0>)>'
        'getNumStateDefs': None, # (!) real value is "<method 'getNumStateDefs' of 'panda3d.core.PGItem' objects>"
        'getPressEvent': None, # (!) real value is "<method 'getPressEvent' of 'panda3d.core.PGItem' objects>"
        'getPressPrefix': None, # (!) real value is '<staticmethod(<built-in method getPressPrefix of type object at 0x00007FFCFE383FD0>)>'
        'getReleaseEvent': None, # (!) real value is "<method 'getReleaseEvent' of 'panda3d.core.PGItem' objects>"
        'getReleasePrefix': None, # (!) real value is '<staticmethod(<built-in method getReleasePrefix of type object at 0x00007FFCFE383FD0>)>'
        'getRepeatEvent': None, # (!) real value is "<method 'getRepeatEvent' of 'panda3d.core.PGItem' objects>"
        'getRepeatPrefix': None, # (!) real value is '<staticmethod(<built-in method getRepeatPrefix of type object at 0x00007FFCFE383FD0>)>'
        'getSound': None, # (!) real value is "<method 'getSound' of 'panda3d.core.PGItem' objects>"
        'getState': None, # (!) real value is "<method 'getState' of 'panda3d.core.PGItem' objects>"
        'getStateDef': None, # (!) real value is "<method 'getStateDef' of 'panda3d.core.PGItem' objects>"
        'getStateDefs': None, # (!) real value is "<method 'getStateDefs' of 'panda3d.core.PGItem' objects>"
        'getSuppressFlags': None, # (!) real value is "<method 'getSuppressFlags' of 'panda3d.core.PGItem' objects>"
        'getTextNode': None, # (!) real value is '<staticmethod(<built-in method getTextNode of type object at 0x00007FFCFE383FD0>)>'
        'getWithinEvent': None, # (!) real value is "<method 'getWithinEvent' of 'panda3d.core.PGItem' objects>"
        'getWithinPrefix': None, # (!) real value is '<staticmethod(<built-in method getWithinPrefix of type object at 0x00007FFCFE383FD0>)>'
        'getWithoutEvent': None, # (!) real value is "<method 'getWithoutEvent' of 'panda3d.core.PGItem' objects>"
        'getWithoutPrefix': None, # (!) real value is '<staticmethod(<built-in method getWithoutPrefix of type object at 0x00007FFCFE383FD0>)>'
        'get_active': None, # (!) real value is "<method 'get_active' of 'panda3d.core.PGItem' objects>"
        'get_background_focus': None, # (!) real value is "<method 'get_background_focus' of 'panda3d.core.PGItem' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE383FD0>)>'
        'get_enter_event': None, # (!) real value is "<method 'get_enter_event' of 'panda3d.core.PGItem' objects>"
        'get_enter_prefix': None, # (!) real value is '<staticmethod(<built-in method get_enter_prefix of type object at 0x00007FFCFE383FD0>)>'
        'get_exit_event': None, # (!) real value is "<method 'get_exit_event' of 'panda3d.core.PGItem' objects>"
        'get_exit_prefix': None, # (!) real value is '<staticmethod(<built-in method get_exit_prefix of type object at 0x00007FFCFE383FD0>)>'
        'get_focus': None, # (!) real value is "<method 'get_focus' of 'panda3d.core.PGItem' objects>"
        'get_focus_in_event': None, # (!) real value is "<method 'get_focus_in_event' of 'panda3d.core.PGItem' objects>"
        'get_focus_in_prefix': None, # (!) real value is '<staticmethod(<built-in method get_focus_in_prefix of type object at 0x00007FFCFE383FD0>)>'
        'get_focus_item': None, # (!) real value is '<staticmethod(<built-in method get_focus_item of type object at 0x00007FFCFE383FD0>)>'
        'get_focus_out_event': None, # (!) real value is "<method 'get_focus_out_event' of 'panda3d.core.PGItem' objects>"
        'get_focus_out_prefix': None, # (!) real value is '<staticmethod(<built-in method get_focus_out_prefix of type object at 0x00007FFCFE383FD0>)>'
        'get_frame': None, # (!) real value is "<method 'get_frame' of 'panda3d.core.PGItem' objects>"
        'get_frame_inv_xform': None, # (!) real value is "<method 'get_frame_inv_xform' of 'panda3d.core.PGItem' objects>"
        'get_frame_style': None, # (!) real value is "<method 'get_frame_style' of 'panda3d.core.PGItem' objects>"
        'get_id': None, # (!) real value is "<method 'get_id' of 'panda3d.core.PGItem' objects>"
        'get_keystroke_event': None, # (!) real value is "<method 'get_keystroke_event' of 'panda3d.core.PGItem' objects>"
        'get_keystroke_prefix': None, # (!) real value is '<staticmethod(<built-in method get_keystroke_prefix of type object at 0x00007FFCFE383FD0>)>'
        'get_num_state_defs': None, # (!) real value is "<method 'get_num_state_defs' of 'panda3d.core.PGItem' objects>"
        'get_press_event': None, # (!) real value is "<method 'get_press_event' of 'panda3d.core.PGItem' objects>"
        'get_press_prefix': None, # (!) real value is '<staticmethod(<built-in method get_press_prefix of type object at 0x00007FFCFE383FD0>)>'
        'get_release_event': None, # (!) real value is "<method 'get_release_event' of 'panda3d.core.PGItem' objects>"
        'get_release_prefix': None, # (!) real value is '<staticmethod(<built-in method get_release_prefix of type object at 0x00007FFCFE383FD0>)>'
        'get_repeat_event': None, # (!) real value is "<method 'get_repeat_event' of 'panda3d.core.PGItem' objects>"
        'get_repeat_prefix': None, # (!) real value is '<staticmethod(<built-in method get_repeat_prefix of type object at 0x00007FFCFE383FD0>)>'
        'get_sound': None, # (!) real value is "<method 'get_sound' of 'panda3d.core.PGItem' objects>"
        'get_state': None, # (!) real value is "<method 'get_state' of 'panda3d.core.PGItem' objects>"
        'get_state_def': None, # (!) real value is "<method 'get_state_def' of 'panda3d.core.PGItem' objects>"
        'get_state_defs': None, # (!) real value is "<method 'get_state_defs' of 'panda3d.core.PGItem' objects>"
        'get_suppress_flags': None, # (!) real value is "<method 'get_suppress_flags' of 'panda3d.core.PGItem' objects>"
        'get_text_node': None, # (!) real value is '<staticmethod(<built-in method get_text_node of type object at 0x00007FFCFE383FD0>)>'
        'get_within_event': None, # (!) real value is "<method 'get_within_event' of 'panda3d.core.PGItem' objects>"
        'get_within_prefix': None, # (!) real value is '<staticmethod(<built-in method get_within_prefix of type object at 0x00007FFCFE383FD0>)>'
        'get_without_event': None, # (!) real value is "<method 'get_without_event' of 'panda3d.core.PGItem' objects>"
        'get_without_prefix': None, # (!) real value is '<staticmethod(<built-in method get_without_prefix of type object at 0x00007FFCFE383FD0>)>'
        'hasFrame': None, # (!) real value is "<method 'hasFrame' of 'panda3d.core.PGItem' objects>"
        'hasSound': None, # (!) real value is "<method 'hasSound' of 'panda3d.core.PGItem' objects>"
        'hasStateDef': None, # (!) real value is "<method 'hasStateDef' of 'panda3d.core.PGItem' objects>"
        'has_frame': None, # (!) real value is "<method 'has_frame' of 'panda3d.core.PGItem' objects>"
        'has_sound': None, # (!) real value is "<method 'has_sound' of 'panda3d.core.PGItem' objects>"
        'has_state_def': None, # (!) real value is "<method 'has_state_def' of 'panda3d.core.PGItem' objects>"
        'instanceToStateDef': None, # (!) real value is "<method 'instanceToStateDef' of 'panda3d.core.PGItem' objects>"
        'instance_to_state_def': None, # (!) real value is "<method 'instance_to_state_def' of 'panda3d.core.PGItem' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.PGItem' objects>"
        'setBackgroundFocus': None, # (!) real value is "<method 'setBackgroundFocus' of 'panda3d.core.PGItem' objects>"
        'setFocus': None, # (!) real value is "<method 'setFocus' of 'panda3d.core.PGItem' objects>"
        'setFrame': None, # (!) real value is "<method 'setFrame' of 'panda3d.core.PGItem' objects>"
        'setFrameStyle': None, # (!) real value is "<method 'setFrameStyle' of 'panda3d.core.PGItem' objects>"
        'setId': None, # (!) real value is "<method 'setId' of 'panda3d.core.PGItem' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.PGItem' objects>"
        'setSound': None, # (!) real value is "<method 'setSound' of 'panda3d.core.PGItem' objects>"
        'setState': None, # (!) real value is "<method 'setState' of 'panda3d.core.PGItem' objects>"
        'setSuppressFlags': None, # (!) real value is "<method 'setSuppressFlags' of 'panda3d.core.PGItem' objects>"
        'setTextNode': None, # (!) real value is '<staticmethod(<built-in method setTextNode of type object at 0x00007FFCFE383FD0>)>'
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.PGItem' objects>"
        'set_background_focus': None, # (!) real value is "<method 'set_background_focus' of 'panda3d.core.PGItem' objects>"
        'set_focus': None, # (!) real value is "<method 'set_focus' of 'panda3d.core.PGItem' objects>"
        'set_frame': None, # (!) real value is "<method 'set_frame' of 'panda3d.core.PGItem' objects>"
        'set_frame_style': None, # (!) real value is "<method 'set_frame_style' of 'panda3d.core.PGItem' objects>"
        'set_id': None, # (!) real value is "<method 'set_id' of 'panda3d.core.PGItem' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.PGItem' objects>"
        'set_sound': None, # (!) real value is "<method 'set_sound' of 'panda3d.core.PGItem' objects>"
        'set_state': None, # (!) real value is "<method 'set_state' of 'panda3d.core.PGItem' objects>"
        'set_suppress_flags': None, # (!) real value is "<method 'set_suppress_flags' of 'panda3d.core.PGItem' objects>"
        'set_text_node': None, # (!) real value is '<staticmethod(<built-in method set_text_node of type object at 0x00007FFCFE383FD0>)>'
    }


