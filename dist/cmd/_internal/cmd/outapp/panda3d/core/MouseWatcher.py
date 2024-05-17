# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

from .MouseWatcherBase import MouseWatcherBase

class MouseWatcher(DataNode, MouseWatcherBase):
    """
    /**
     * This TFormer maintains a list of rectangular regions on the screen that are
     * considered special mouse regions; typically these will be click buttons.
     * When the mouse passes in or out of one of these regions, or when a button
     * is clicked while the mouse is in one of these regions, an event is thrown.
     *
     * Mouse events may also be suppressed from the rest of the datagraph in these
     * special regions.
     *
     * This class can also implement a software mouse pointer by automatically
     * generating a transform to apply to a piece of geometry placed under the 2-d
     * scene graph.  It will move the geometry around according to the mouse's
     * known position.
     *
     * Finally, this class can keep a record of the mouse trail.  This is useful
     * if you want to know, not just where the mouse is, but the exact sequence of
     * movements it took to get there.  This information is mainly useful for
     * gesture-recognition code.  To use trail logging, you need to enable the
     * generation of pointer events in the GraphicsWindowInputDevice and set the
     * trail log duration in the MouseWatcher.  Otherwise, the trail log will be
     * empty.
     */
    """
    def addGroup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_group(const MouseWatcher self, MouseWatcherGroup group)
        
        /**
         * Adds the indicated group of regions to the set of regions the MouseWatcher
         * will monitor each frame.
         *
         * Since the MouseWatcher itself inherits from MouseWatcherBase, this
         * operation is normally not necessary--you can simply add the Regions you
         * care about one at a time.  Adding a complete group is useful when you may
         * want to explicitly remove the regions as a group later.
         *
         * Returns true if the group was successfully added, or false if it was
         * already on the list.
         */
        """
        pass

    def add_group(self, const_MouseWatcher_self, MouseWatcherGroup_group): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_group(const MouseWatcher self, MouseWatcherGroup group)
        
        /**
         * Adds the indicated group of regions to the set of regions the MouseWatcher
         * will monitor each frame.
         *
         * Since the MouseWatcher itself inherits from MouseWatcherBase, this
         * operation is normally not necessary--you can simply add the Regions you
         * care about one at a time.  Adding a complete group is useful when you may
         * want to explicitly remove the regions as a group later.
         *
         * Returns true if the group was successfully added, or false if it was
         * already on the list.
         */
        """
        pass

    def clearDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_display_region(const MouseWatcher self)
        
        /**
         * Removes the display region constraint from the MouseWatcher, and restores
         * it to the default behavior of watching the whole window.
         */
        """
        pass

    def clearGeometry(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_geometry(const MouseWatcher self)
        
        /**
         * Stops the use of the software cursor set up via set_geometry().
         */
        """
        pass

    def clearInactivityTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_inactivity_timeout(const MouseWatcher self)
        
        /**
         * Removes the inactivity timeout and restores the MouseWatcher to its default
         * behavior of allowing a key to be held indefinitely.
         */
        """
        pass

    def clearTrailLog(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_trail_log(const MouseWatcher self)
        
        /**
         * Clears the mouse trail log.  This does not prevent further accumulation of
         * the log given future events.
         */
        """
        pass

    def clearTrailNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_trail_node(const MouseWatcher self)
        
        /**
         * If you have previously fetched the trail node using get_trail_node, then
         * the MouseWatcher is continually updating the trail node every frame.  Using
         * clear_trail_node causes the MouseWatcher to forget the trail node and stop
         * updating it.
         */
        """
        pass

    def clear_display_region(self, const_MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_display_region(const MouseWatcher self)
        
        /**
         * Removes the display region constraint from the MouseWatcher, and restores
         * it to the default behavior of watching the whole window.
         */
        """
        pass

    def clear_geometry(self, const_MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_geometry(const MouseWatcher self)
        
        /**
         * Stops the use of the software cursor set up via set_geometry().
         */
        """
        pass

    def clear_inactivity_timeout(self, const_MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_inactivity_timeout(const MouseWatcher self)
        
        /**
         * Removes the inactivity timeout and restores the MouseWatcher to its default
         * behavior of allowing a key to be held indefinitely.
         */
        """
        pass

    def clear_trail_log(self, const_MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_trail_log(const MouseWatcher self)
        
        /**
         * Clears the mouse trail log.  This does not prevent further accumulation of
         * the log given future events.
         */
        """
        pass

    def clear_trail_node(self, const_MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_trail_node(const MouseWatcher self)
        
        /**
         * If you have previously fetched the trail node using get_trail_node, then
         * the MouseWatcher is continually updating the trail node every frame.  Using
         * clear_trail_node causes the MouseWatcher to forget the trail node and stop
         * updating it.
         */
        """
        pass

    def getButtonDownPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_button_down_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when a
         * button is depressed.  See set_button_down_pattern().
         */
        """
        pass

    def getButtonRepeatPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_button_repeat_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are names are generated
         * when a button is continuously held and generates keyrepeat "down" events.
         * See set_button_repeat_pattern().
         */
        """
        pass

    def getButtonUpPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_button_up_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when a
         * button is released.  See set_button_down_pattern().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_region(MouseWatcher self)
        
        /**
         * Returns the display region the MouseWatcher is constrained to by
         * set_display_region(), or NULL if it is not constrained.
         */
        """
        pass

    def getEnterPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_enter_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when the
         * mouse enters a region.  This is different from within_pattern, in that a
         * mouse is only "entered" in the topmost region at a given time, while it
         * might be "within" multiple nested regions.
         */
        """
        pass

    def getExtraHandler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_extra_handler(MouseWatcher self)
        
        /**
         * As an optimization for the C++ Gui, an extra handler can be registered with
         * a mouseWatcher so that events can be dealt with much sooner.
         */
        """
        pass

    def getFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame(MouseWatcher self)
        
        /**
         * Returns the frame of the MouseWatcher.  See set_frame().
         */
        """
        pass

    def getGeometry(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geometry(MouseWatcher self)
        
        /**
         * Returns the node that has been set as the software mouse pointer, or NULL
         * if no node has been set.  See has_geometry() and set_geometry().
         */
        """
        pass

    def getGroup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_group(MouseWatcher self, int n)
        
        /**
         * Returns the nth group added to the MouseWatcher via add_group().
         */
        """
        pass

    def getGroups(self, *args, **kwargs): # real signature unknown
        pass

    def getInactivityTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inactivity_timeout(MouseWatcher self)
        
        /**
         * Returns the inactivity timeout that has been set.  It is an error to call
         * this if has_inactivity_timeout() returns false.
         */
        """
        pass

    def getInactivityTimeoutEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inactivity_timeout_event(MouseWatcher self)
        
        /**
         * Returns the event string that will be generated when the inactivity timeout
         * counter expires.  See set_inactivity_timeout().
         */
        """
        pass

    def getLeavePattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_leave_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when the
         * mouse leaves a region.  This is different from without_pattern, in that a
         * mouse is only "entered" in the topmost region at a given time, while it
         * might be "within" multiple nested regions.
         */
        """
        pass

    def getModifierButtons(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modifier_buttons(MouseWatcher self)
        
        /**
         * Returns the set of buttons that are being monitored as modifier buttons, as
         * well as their current state.
         */
        """
        pass

    def getMouse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mouse(MouseWatcher self)
        
        /**
         * It is only valid to call this if has_mouse() returns true.  If so, this
         * returns the current position of the mouse within the window.
         */
        """
        pass

    def getMouseX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mouse_x(MouseWatcher self)
        
        /**
         * It is only valid to call this if has_mouse() returns true.  If so, this
         * returns the current X position of the mouse within the window.
         */
        """
        pass

    def getMouseY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mouse_y(MouseWatcher self)
        
        /**
         * It is only valid to call this if has_mouse() returns true.  If so, this
         * returns the current Y position of the mouse within the window.
         */
        """
        pass

    def getNumGroups(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_groups(MouseWatcher self)
        
        /**
         * Returns the number of separate groups added to the MouseWatcher via
         * add_group().
         */
        """
        pass

    def getOverRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_over_region(MouseWatcher self)
        get_over_region(MouseWatcher self, const LPoint2f pos)
        get_over_region(MouseWatcher self, float x, float y)
        
        /**
         * Returns the smallest region the mouse is currently over, or NULL if it is
         * over no region.
         */
        
        /**
         * Returns the smallest region the indicated point is over, or NULL if it is
         * over no region.
         */
        
        /**
         * Returns the preferred region the mouse is over.  In the case of overlapping
         * regions, the region with the largest sort order is preferred; if two
         * regions have the same sort order, then the smaller region is preferred.
         */
        """
        pass

    def getTrailLog(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_trail_log(MouseWatcher self)
        
        /**
         * Obtain the mouse trail log.  This is a PointerEventList.  Does not make a
         * copy, therefore, this PointerEventList will be updated each time
         * process_events gets called.
         *
         * To use trail logging, you need to enable the generation of pointer events
         * in the GraphicsWindowInputDevice and set the trail log duration in the
         * MouseWatcher.  Otherwise, the trail log will be empty.
         */
        """
        pass

    def getTrailNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_trail_node(const MouseWatcher self)
        
        /**
         * Returns a GeomNode that represents the mouse trail.  The intent is that you
         * should reparent this GeomNode to Render2D, and then forget about it.  The
         * MouseWatcher will continually update the trail node.  There is only one
         * trail node, it does not create a new one each time you call get_trail_node.
         *
         * This is not a particularly beautiful way to render a mouse trail.  It is
         * intended more for debugging purposes than for finished applications.  Even
         * so, It is suggested that you might want to apply a line thickness and
         * antialias mode to the line --- doing so makes it look a lot better.
         */
        """
        pass

    def getWithinPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_within_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when the
         * mouse wanders over a region.  This is different from enter_pattern, in that
         * a mouse is only "entered" in the topmost region at a given time, while it
         * might be "within" multiple nested regions.
         */
        """
        pass

    def getWithoutPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_without_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when the
         * mouse wanders out of a region.  This is different from leave_pattern, in
         * that a mouse is only "entered" in the topmost region at a given time, while
         * it might be "within" multiple nested regions.
         */
        """
        pass

    def get_button_down_pattern(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_button_down_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when a
         * button is depressed.  See set_button_down_pattern().
         */
        """
        pass

    def get_button_repeat_pattern(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_button_repeat_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are names are generated
         * when a button is continuously held and generates keyrepeat "down" events.
         * See set_button_repeat_pattern().
         */
        """
        pass

    def get_button_up_pattern(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_button_up_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when a
         * button is released.  See set_button_down_pattern().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_display_region(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_region(MouseWatcher self)
        
        /**
         * Returns the display region the MouseWatcher is constrained to by
         * set_display_region(), or NULL if it is not constrained.
         */
        """
        pass

    def get_enter_pattern(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_enter_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when the
         * mouse enters a region.  This is different from within_pattern, in that a
         * mouse is only "entered" in the topmost region at a given time, while it
         * might be "within" multiple nested regions.
         */
        """
        pass

    def get_extra_handler(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_extra_handler(MouseWatcher self)
        
        /**
         * As an optimization for the C++ Gui, an extra handler can be registered with
         * a mouseWatcher so that events can be dealt with much sooner.
         */
        """
        pass

    def get_frame(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame(MouseWatcher self)
        
        /**
         * Returns the frame of the MouseWatcher.  See set_frame().
         */
        """
        pass

    def get_geometry(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geometry(MouseWatcher self)
        
        /**
         * Returns the node that has been set as the software mouse pointer, or NULL
         * if no node has been set.  See has_geometry() and set_geometry().
         */
        """
        pass

    def get_group(self, MouseWatcher_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_group(MouseWatcher self, int n)
        
        /**
         * Returns the nth group added to the MouseWatcher via add_group().
         */
        """
        pass

    def get_groups(self, *args, **kwargs): # real signature unknown
        pass

    def get_inactivity_timeout(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inactivity_timeout(MouseWatcher self)
        
        /**
         * Returns the inactivity timeout that has been set.  It is an error to call
         * this if has_inactivity_timeout() returns false.
         */
        """
        pass

    def get_inactivity_timeout_event(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inactivity_timeout_event(MouseWatcher self)
        
        /**
         * Returns the event string that will be generated when the inactivity timeout
         * counter expires.  See set_inactivity_timeout().
         */
        """
        pass

    def get_leave_pattern(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_leave_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when the
         * mouse leaves a region.  This is different from without_pattern, in that a
         * mouse is only "entered" in the topmost region at a given time, while it
         * might be "within" multiple nested regions.
         */
        """
        pass

    def get_modifier_buttons(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modifier_buttons(MouseWatcher self)
        
        /**
         * Returns the set of buttons that are being monitored as modifier buttons, as
         * well as their current state.
         */
        """
        pass

    def get_mouse(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mouse(MouseWatcher self)
        
        /**
         * It is only valid to call this if has_mouse() returns true.  If so, this
         * returns the current position of the mouse within the window.
         */
        """
        pass

    def get_mouse_x(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mouse_x(MouseWatcher self)
        
        /**
         * It is only valid to call this if has_mouse() returns true.  If so, this
         * returns the current X position of the mouse within the window.
         */
        """
        pass

    def get_mouse_y(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mouse_y(MouseWatcher self)
        
        /**
         * It is only valid to call this if has_mouse() returns true.  If so, this
         * returns the current Y position of the mouse within the window.
         */
        """
        pass

    def get_num_groups(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_groups(MouseWatcher self)
        
        /**
         * Returns the number of separate groups added to the MouseWatcher via
         * add_group().
         */
        """
        pass

    def get_over_region(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_over_region(MouseWatcher self)
        get_over_region(MouseWatcher self, const LPoint2f pos)
        get_over_region(MouseWatcher self, float x, float y)
        
        /**
         * Returns the smallest region the mouse is currently over, or NULL if it is
         * over no region.
         */
        
        /**
         * Returns the smallest region the indicated point is over, or NULL if it is
         * over no region.
         */
        
        /**
         * Returns the preferred region the mouse is over.  In the case of overlapping
         * regions, the region with the largest sort order is preferred; if two
         * regions have the same sort order, then the smaller region is preferred.
         */
        """
        pass

    def get_trail_log(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_trail_log(MouseWatcher self)
        
        /**
         * Obtain the mouse trail log.  This is a PointerEventList.  Does not make a
         * copy, therefore, this PointerEventList will be updated each time
         * process_events gets called.
         *
         * To use trail logging, you need to enable the generation of pointer events
         * in the GraphicsWindowInputDevice and set the trail log duration in the
         * MouseWatcher.  Otherwise, the trail log will be empty.
         */
        """
        pass

    def get_trail_node(self, const_MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_trail_node(const MouseWatcher self)
        
        /**
         * Returns a GeomNode that represents the mouse trail.  The intent is that you
         * should reparent this GeomNode to Render2D, and then forget about it.  The
         * MouseWatcher will continually update the trail node.  There is only one
         * trail node, it does not create a new one each time you call get_trail_node.
         *
         * This is not a particularly beautiful way to render a mouse trail.  It is
         * intended more for debugging purposes than for finished applications.  Even
         * so, It is suggested that you might want to apply a line thickness and
         * antialias mode to the line --- doing so makes it look a lot better.
         */
        """
        pass

    def get_within_pattern(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_within_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when the
         * mouse wanders over a region.  This is different from enter_pattern, in that
         * a mouse is only "entered" in the topmost region at a given time, while it
         * might be "within" multiple nested regions.
         */
        """
        pass

    def get_without_pattern(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_without_pattern(MouseWatcher self)
        
        /**
         * Returns the string that indicates how event names are generated when the
         * mouse wanders out of a region.  This is different from leave_pattern, in
         * that a mouse is only "entered" in the topmost region at a given time, while
         * it might be "within" multiple nested regions.
         */
        """
        pass

    def hasDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_display_region(MouseWatcher self)
        
        /**
         * Returns true if the MouseWatcher has been constrained to a particular
         * region of the screen via set_display_region(), or false otherwise.  If this
         * returns true, get_display_region() may be used to return the particular
         * region.
         */
        """
        pass

    def hasGeometry(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_geometry(MouseWatcher self)
        
        /**
         * Returns true if a software mouse pointer has been setup via set_geometry(),
         * or false otherwise.  See set_geometry().
         */
        """
        pass

    def hasInactivityTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_inactivity_timeout(MouseWatcher self)
        
        /**
         * Returns true if an inactivity timeout has been set, false otherwise.
         */
        """
        pass

    def hasMouse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_mouse(MouseWatcher self)
        
        /**
         * Returns true if the mouse is anywhere within the window, false otherwise.
         * Also see is_mouse_open().
         */
        """
        pass

    def has_display_region(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_display_region(MouseWatcher self)
        
        /**
         * Returns true if the MouseWatcher has been constrained to a particular
         * region of the screen via set_display_region(), or false otherwise.  If this
         * returns true, get_display_region() may be used to return the particular
         * region.
         */
        """
        pass

    def has_geometry(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_geometry(MouseWatcher self)
        
        /**
         * Returns true if a software mouse pointer has been setup via set_geometry(),
         * or false otherwise.  See set_geometry().
         */
        """
        pass

    def has_inactivity_timeout(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_inactivity_timeout(MouseWatcher self)
        
        /**
         * Returns true if an inactivity timeout has been set, false otherwise.
         */
        """
        pass

    def has_mouse(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_mouse(MouseWatcher self)
        
        /**
         * Returns true if the mouse is anywhere within the window, false otherwise.
         * Also see is_mouse_open().
         */
        """
        pass

    def isButtonDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_button_down(MouseWatcher self, ButtonHandle button)
        
        /**
         * Returns true if the indicated button is currently being held down, false
         * otherwise.
         */
        """
        pass

    def isMouseOpen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_mouse_open(MouseWatcher self)
        
        /**
         * Returns true if the mouse is within the window and not over some particular
         * MouseWatcherRegion that is marked to suppress mouse events; that is, that
         * the mouse is in open space within the window.
         */
        """
        pass

    def isOverRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_over_region(MouseWatcher self)
        is_over_region(MouseWatcher self, const LPoint2f pos)
        is_over_region(MouseWatcher self, float x, float y)
        
        /**
         * Returns true if the mouse is over any rectangular region, false otherwise.
         */
        
        /**
         * Returns true if the mouse is over any rectangular region, false otherwise.
         */
        
        /**
         * Returns true if the mouse is over any rectangular region, false otherwise.
         */
        """
        pass

    def is_button_down(self, MouseWatcher_self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_button_down(MouseWatcher self, ButtonHandle button)
        
        /**
         * Returns true if the indicated button is currently being held down, false
         * otherwise.
         */
        """
        pass

    def is_mouse_open(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_mouse_open(MouseWatcher self)
        
        /**
         * Returns true if the mouse is within the window and not over some particular
         * MouseWatcherRegion that is marked to suppress mouse events; that is, that
         * the mouse is in open space within the window.
         */
        """
        pass

    def is_over_region(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_over_region(MouseWatcher self)
        is_over_region(MouseWatcher self, const LPoint2f pos)
        is_over_region(MouseWatcher self, float x, float y)
        
        /**
         * Returns true if the mouse is over any rectangular region, false otherwise.
         */
        
        /**
         * Returns true if the mouse is over any rectangular region, false otherwise.
         */
        
        /**
         * Returns true if the mouse is over any rectangular region, false otherwise.
         */
        """
        pass

    def noteActivity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        note_activity(const MouseWatcher self)
        
        /**
         * Can be used in conjunction with the inactivity timeout to inform the
         * MouseWatcher that the user has just performed some action which proves
         * he/she is present.  It may be necessary to call this for external events,
         * such as joystick action, that the MouseWatcher might otherwise not know
         * about.  This will reset the current inactivity timer.  When the inactivity
         * timer reaches the length of time specified by set_inactivity_timeout(),
         * with no keyboard or mouse activity and no calls to note_activity(), then
         * any buttons held will be automatically released.
         */
        """
        pass

    def note_activity(self, const_MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        note_activity(const MouseWatcher self)
        
        /**
         * Can be used in conjunction with the inactivity timeout to inform the
         * MouseWatcher that the user has just performed some action which proves
         * he/she is present.  It may be necessary to call this for external events,
         * such as joystick action, that the MouseWatcher might otherwise not know
         * about.  This will reset the current inactivity timer.  When the inactivity
         * timer reaches the length of time specified by set_inactivity_timeout(),
         * with no keyboard or mouse activity and no calls to note_activity(), then
         * any buttons held will be automatically released.
         */
        """
        pass

    def numTrailRecent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        num_trail_recent(MouseWatcher self)
        
        /**
         * This counter indicates how many events were added to the trail log this
         * frame.  The trail log is updated once per frame, during the process_events
         * operation.
         */
        """
        pass

    def num_trail_recent(self, MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        num_trail_recent(MouseWatcher self)
        
        /**
         * This counter indicates how many events were added to the trail log this
         * frame.  The trail log is updated once per frame, during the process_events
         * operation.
         */
        """
        pass

    def removeGroup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_group(const MouseWatcher self, MouseWatcherGroup group)
        
        /**
         * Removes the indicated group from the set of extra groups associated with
         * the MouseWatcher.  Returns true if successful, or false if the group was
         * already removed or was never added via add_group().
         */
        """
        pass

    def removeRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_region(const MouseWatcher self, MouseWatcherRegion region)
        
        /**
         * Removes the indicated region from the group.  Returns true if it was
         * successfully removed, or false if it wasn't there in the first place.
         */
        """
        pass

    def remove_group(self, const_MouseWatcher_self, MouseWatcherGroup_group): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_group(const MouseWatcher self, MouseWatcherGroup group)
        
        /**
         * Removes the indicated group from the set of extra groups associated with
         * the MouseWatcher.  Returns true if successful, or false if the group was
         * already removed or was never added via add_group().
         */
        """
        pass

    def remove_region(self, const_MouseWatcher_self, MouseWatcherRegion_region): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_region(const MouseWatcher self, MouseWatcherRegion region)
        
        /**
         * Removes the indicated region from the group.  Returns true if it was
         * successfully removed, or false if it wasn't there in the first place.
         */
        """
        pass

    def replaceGroup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        replace_group(const MouseWatcher self, MouseWatcherGroup old_group, MouseWatcherGroup new_group)
        
        /**
         * Atomically removes old_group from the MouseWatcher, and replaces it with
         * new_group.  Presumably old_group and new_group might have some regions in
         * common; these are handled properly.
         *
         * If old_group is not already present, simply adds new_group and returns
         * false.  Otherwise, removes old_group and adds new_group, and then returns
         * true.
         */
        """
        pass

    def replace_group(self, const_MouseWatcher_self, MouseWatcherGroup_old_group, MouseWatcherGroup_new_group): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        replace_group(const MouseWatcher self, MouseWatcherGroup old_group, MouseWatcherGroup new_group)
        
        /**
         * Atomically removes old_group from the MouseWatcher, and replaces it with
         * new_group.  Presumably old_group and new_group might have some regions in
         * common; these are handled properly.
         *
         * If old_group is not already present, simply adds new_group and returns
         * false.  Otherwise, removes old_group and adds new_group, and then returns
         * true.
         */
        """
        pass

    def setButtonDownPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_button_down_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when a button is depressed.  This is a string that may contain any of the
         * following:
         *
         * %r  - the name of the region the mouse is over %b  - the name of the button
         * pressed.
         *
         * The event name will be based on the in_pattern string specified here, with
         * all occurrences of the above strings replaced with the corresponding
         * values.
         */
        """
        pass

    def setButtonRepeatPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_button_repeat_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when a button is continuously held and generates keyrepeat "down" events.
         * This is a string that may contain any of the following:
         *
         * %r  - the name of the region the mouse is over %b  - the name of the button
         * pressed.
         *
         * The event name will be based on the in_pattern string specified here, with
         * all occurrences of the above strings replaced with the corresponding
         * values.
         */
        """
        pass

    def setButtonUpPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_button_up_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when a button is released.  See set_button_down_pattern().
         */
        """
        pass

    def setDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_display_region(const MouseWatcher self, DisplayRegion dr)
        
        /**
         * Constrains the MouseWatcher to watching the mouse within a particular
         * indicated region of the screen.  DataNodes parented under the MouseWatcher
         * will observe the mouse and keyboard events only when the mouse is within
         * the indicated region, and the observed range will be from -1 .. 1 across
         * the region.
         *
         * Do not delete the DisplayRegion while it is owned by the MouseWatcher.
         */
        """
        pass

    def setEnterPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_enter_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when the mouse enters a region.  This is different from within_pattern, in
         * that a mouse is only "entered" in the topmost region at a given time, while
         * it might be "within" multiple nested regions.
         */
        """
        pass

    def setExtraHandler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_extra_handler(const MouseWatcher self, EventHandler eh)
        
        /**
         * As an optimization for the C++ Gui, an extra handler can be registered with
         * a mouseWatcher so that events can be dealt with much sooner.
         */
        """
        pass

    def setFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame(const MouseWatcher self, const LVecBase4f frame)
        set_frame(const MouseWatcher self, float left, float right, float bottom, float top)
        
        /**
         * Sets the frame of the MouseWatcher.  See the next flavor of this method for
         * a more verbose explanation.
         */
        
        /**
         * Sets the frame of the MouseWatcher.  This determines the coordinate space
         * in which the MouseWatcherRegions should be expected to live.  Normally,
         * this is left at -1, 1, -1, 1, which is the default setting, and matches the
         * mouse coordinate range.
         *
         * Whatever values you specify here indicate the shape of the full screen, and
         * the MouseWatcherRegions will be given in coordinate space matching it.  For
         * instance, if you specify (0, 1, 0, 1), then a MouseWatcherRegion with the
         * frame (0, 1, 0, .5) will cover the lower half of the screen.
         */
        """
        pass

    def setGeometry(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_geometry(const MouseWatcher self, PandaNode node)
        
        /**
         * Sets the node that will be transformed each frame by the mouse's
         * coordinates.  It will also be hidden when the mouse goes outside the
         * window.  This can be used to implement a software mouse pointer for when a
         * hardware (or system) mouse pointer is unavailable.
         */
        """
        pass

    def setInactivityTimeout(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_inactivity_timeout(const MouseWatcher self, double timeout)
        
        /**
         * Sets an inactivity timeout on the mouse activity.  When this timeout (in
         * seconds) is exceeded with no keyboard or mouse activity, all currently-held
         * buttons are automatically released.  This is intended to help protect
         * against people who inadvertently (or intentionally) leave a keyboard key
         * stuck down and then wander away from the keyboard.
         *
         * Also, when this timeout expires, the event specified by
         * set_inactivity_timeout_event() will be generated.
         */
        """
        pass

    def setInactivityTimeoutEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_inactivity_timeout_event(const MouseWatcher self, str event)
        
        /**
         * Specifies the event string that will be generated when the inactivity
         * timeout counter expires.  See set_inactivity_timeout().
         */
        """
        pass

    def setLeavePattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_leave_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when the mouse leaves a region.  This is different from without_pattern, in
         * that a mouse is only "entered" in the topmost region at a given time, while
         * it might be "within" multiple nested regions.
         */
        """
        pass

    def setModifierButtons(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_modifier_buttons(const MouseWatcher self, const ModifierButtons mods)
        
        /**
         * Sets the buttons that should be monitored as modifier buttons for
         * generating events to the MouseWatcherRegions.
         */
        """
        pass

    def setTrailLogDuration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_trail_log_duration(const MouseWatcher self, double duration)
        
        /**
         * If the duration is nonzero, causes the MouseWatcher to log the mouse's
         * trail.  Events older than the specified duration are discarded.  If the
         * duration is zero, logging is disabled.
         */
        """
        pass

    def setWithinPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_within_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when the mouse wanders over a region.  This is different from
         * enter_pattern, in that a mouse is only "entered" in the topmost region at a
         * given time, while it might be "within" multiple nested regions.
         */
        """
        pass

    def setWithoutPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_without_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when the mouse wanders out of a region.  This is different from
         * leave_pattern, in that a mouse is only "entered" in the topmost region at a
         * given time, while it might be "within" multiple nested regions.
         */
        """
        pass

    def set_button_down_pattern(self, const_MouseWatcher_self, str_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_button_down_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when a button is depressed.  This is a string that may contain any of the
         * following:
         *
         * %r  - the name of the region the mouse is over %b  - the name of the button
         * pressed.
         *
         * The event name will be based on the in_pattern string specified here, with
         * all occurrences of the above strings replaced with the corresponding
         * values.
         */
        """
        pass

    def set_button_repeat_pattern(self, const_MouseWatcher_self, str_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_button_repeat_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when a button is continuously held and generates keyrepeat "down" events.
         * This is a string that may contain any of the following:
         *
         * %r  - the name of the region the mouse is over %b  - the name of the button
         * pressed.
         *
         * The event name will be based on the in_pattern string specified here, with
         * all occurrences of the above strings replaced with the corresponding
         * values.
         */
        """
        pass

    def set_button_up_pattern(self, const_MouseWatcher_self, str_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_button_up_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when a button is released.  See set_button_down_pattern().
         */
        """
        pass

    def set_display_region(self, const_MouseWatcher_self, DisplayRegion_dr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_display_region(const MouseWatcher self, DisplayRegion dr)
        
        /**
         * Constrains the MouseWatcher to watching the mouse within a particular
         * indicated region of the screen.  DataNodes parented under the MouseWatcher
         * will observe the mouse and keyboard events only when the mouse is within
         * the indicated region, and the observed range will be from -1 .. 1 across
         * the region.
         *
         * Do not delete the DisplayRegion while it is owned by the MouseWatcher.
         */
        """
        pass

    def set_enter_pattern(self, const_MouseWatcher_self, str_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_enter_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when the mouse enters a region.  This is different from within_pattern, in
         * that a mouse is only "entered" in the topmost region at a given time, while
         * it might be "within" multiple nested regions.
         */
        """
        pass

    def set_extra_handler(self, const_MouseWatcher_self, EventHandler_eh): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_extra_handler(const MouseWatcher self, EventHandler eh)
        
        /**
         * As an optimization for the C++ Gui, an extra handler can be registered with
         * a mouseWatcher so that events can be dealt with much sooner.
         */
        """
        pass

    def set_frame(self, const_MouseWatcher_self, const_LVecBase4f_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame(const MouseWatcher self, const LVecBase4f frame)
        set_frame(const MouseWatcher self, float left, float right, float bottom, float top)
        
        /**
         * Sets the frame of the MouseWatcher.  See the next flavor of this method for
         * a more verbose explanation.
         */
        
        /**
         * Sets the frame of the MouseWatcher.  This determines the coordinate space
         * in which the MouseWatcherRegions should be expected to live.  Normally,
         * this is left at -1, 1, -1, 1, which is the default setting, and matches the
         * mouse coordinate range.
         *
         * Whatever values you specify here indicate the shape of the full screen, and
         * the MouseWatcherRegions will be given in coordinate space matching it.  For
         * instance, if you specify (0, 1, 0, 1), then a MouseWatcherRegion with the
         * frame (0, 1, 0, .5) will cover the lower half of the screen.
         */
        """
        pass

    def set_geometry(self, const_MouseWatcher_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_geometry(const MouseWatcher self, PandaNode node)
        
        /**
         * Sets the node that will be transformed each frame by the mouse's
         * coordinates.  It will also be hidden when the mouse goes outside the
         * window.  This can be used to implement a software mouse pointer for when a
         * hardware (or system) mouse pointer is unavailable.
         */
        """
        pass

    def set_inactivity_timeout(self, const_MouseWatcher_self, double_timeout): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_inactivity_timeout(const MouseWatcher self, double timeout)
        
        /**
         * Sets an inactivity timeout on the mouse activity.  When this timeout (in
         * seconds) is exceeded with no keyboard or mouse activity, all currently-held
         * buttons are automatically released.  This is intended to help protect
         * against people who inadvertently (or intentionally) leave a keyboard key
         * stuck down and then wander away from the keyboard.
         *
         * Also, when this timeout expires, the event specified by
         * set_inactivity_timeout_event() will be generated.
         */
        """
        pass

    def set_inactivity_timeout_event(self, const_MouseWatcher_self, str_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_inactivity_timeout_event(const MouseWatcher self, str event)
        
        /**
         * Specifies the event string that will be generated when the inactivity
         * timeout counter expires.  See set_inactivity_timeout().
         */
        """
        pass

    def set_leave_pattern(self, const_MouseWatcher_self, str_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_leave_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when the mouse leaves a region.  This is different from without_pattern, in
         * that a mouse is only "entered" in the topmost region at a given time, while
         * it might be "within" multiple nested regions.
         */
        """
        pass

    def set_modifier_buttons(self, const_MouseWatcher_self, const_ModifierButtons_mods): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_modifier_buttons(const MouseWatcher self, const ModifierButtons mods)
        
        /**
         * Sets the buttons that should be monitored as modifier buttons for
         * generating events to the MouseWatcherRegions.
         */
        """
        pass

    def set_trail_log_duration(self, const_MouseWatcher_self, double_duration): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_trail_log_duration(const MouseWatcher self, double duration)
        
        /**
         * If the duration is nonzero, causes the MouseWatcher to log the mouse's
         * trail.  Events older than the specified duration are discarded.  If the
         * duration is zero, logging is disabled.
         */
        """
        pass

    def set_within_pattern(self, const_MouseWatcher_self, str_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_within_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when the mouse wanders over a region.  This is different from
         * enter_pattern, in that a mouse is only "entered" in the topmost region at a
         * given time, while it might be "within" multiple nested regions.
         */
        """
        pass

    def set_without_pattern(self, const_MouseWatcher_self, str_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_without_pattern(const MouseWatcher self, str pattern)
        
        /**
         * Sets the pattern string that indicates how the event names are generated
         * when the mouse wanders out of a region.  This is different from
         * leave_pattern, in that a mouse is only "entered" in the topmost region at a
         * given time, while it might be "within" multiple nested regions.
         */
        """
        pass

    def upcastToDataNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DataNode(const MouseWatcher self)
        
        upcast from MouseWatcher to DataNode
        """
        pass

    def upcastToMouseWatcherBase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_MouseWatcherBase(const MouseWatcher self)
        
        upcast from MouseWatcher to MouseWatcherBase
        """
        pass

    def upcast_to_DataNode(self, const_MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DataNode(const MouseWatcher self)
        
        upcast from MouseWatcher to DataNode
        """
        pass

    def upcast_to_MouseWatcherBase(self, const_MouseWatcher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_MouseWatcherBase(const MouseWatcher self)
        
        upcast from MouseWatcher to MouseWatcherBase
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
        '__doc__': "/**\n * This TFormer maintains a list of rectangular regions on the screen that are\n * considered special mouse regions; typically these will be click buttons.\n * When the mouse passes in or out of one of these regions, or when a button\n * is clicked while the mouse is in one of these regions, an event is thrown.\n *\n * Mouse events may also be suppressed from the rest of the datagraph in these\n * special regions.\n *\n * This class can also implement a software mouse pointer by automatically\n * generating a transform to apply to a piece of geometry placed under the 2-d\n * scene graph.  It will move the geometry around according to the mouse's\n * known position.\n *\n * Finally, this class can keep a record of the mouse trail.  This is useful\n * if you want to know, not just where the mouse is, but the exact sequence of\n * movements it took to get there.  This information is mainly useful for\n * gesture-recognition code.  To use trail logging, you need to enable the\n * generation of pointer events in the GraphicsWindowInputDevice and set the\n * trail log duration in the MouseWatcher.  Otherwise, the trail log will be\n * empty.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseWatcher' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE366BB0>'
        'addGroup': None, # (!) real value is "<method 'addGroup' of 'panda3d.core.MouseWatcher' objects>"
        'add_group': None, # (!) real value is "<method 'add_group' of 'panda3d.core.MouseWatcher' objects>"
        'clearDisplayRegion': None, # (!) real value is "<method 'clearDisplayRegion' of 'panda3d.core.MouseWatcher' objects>"
        'clearGeometry': None, # (!) real value is "<method 'clearGeometry' of 'panda3d.core.MouseWatcher' objects>"
        'clearInactivityTimeout': None, # (!) real value is "<method 'clearInactivityTimeout' of 'panda3d.core.MouseWatcher' objects>"
        'clearTrailLog': None, # (!) real value is "<method 'clearTrailLog' of 'panda3d.core.MouseWatcher' objects>"
        'clearTrailNode': None, # (!) real value is "<method 'clearTrailNode' of 'panda3d.core.MouseWatcher' objects>"
        'clear_display_region': None, # (!) real value is "<method 'clear_display_region' of 'panda3d.core.MouseWatcher' objects>"
        'clear_geometry': None, # (!) real value is "<method 'clear_geometry' of 'panda3d.core.MouseWatcher' objects>"
        'clear_inactivity_timeout': None, # (!) real value is "<method 'clear_inactivity_timeout' of 'panda3d.core.MouseWatcher' objects>"
        'clear_trail_log': None, # (!) real value is "<method 'clear_trail_log' of 'panda3d.core.MouseWatcher' objects>"
        'clear_trail_node': None, # (!) real value is "<method 'clear_trail_node' of 'panda3d.core.MouseWatcher' objects>"
        'getButtonDownPattern': None, # (!) real value is "<method 'getButtonDownPattern' of 'panda3d.core.MouseWatcher' objects>"
        'getButtonRepeatPattern': None, # (!) real value is "<method 'getButtonRepeatPattern' of 'panda3d.core.MouseWatcher' objects>"
        'getButtonUpPattern': None, # (!) real value is "<method 'getButtonUpPattern' of 'panda3d.core.MouseWatcher' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE366BB0>)>'
        'getDisplayRegion': None, # (!) real value is "<method 'getDisplayRegion' of 'panda3d.core.MouseWatcher' objects>"
        'getEnterPattern': None, # (!) real value is "<method 'getEnterPattern' of 'panda3d.core.MouseWatcher' objects>"
        'getExtraHandler': None, # (!) real value is "<method 'getExtraHandler' of 'panda3d.core.MouseWatcher' objects>"
        'getFrame': None, # (!) real value is "<method 'getFrame' of 'panda3d.core.MouseWatcher' objects>"
        'getGeometry': None, # (!) real value is "<method 'getGeometry' of 'panda3d.core.MouseWatcher' objects>"
        'getGroup': None, # (!) real value is "<method 'getGroup' of 'panda3d.core.MouseWatcher' objects>"
        'getGroups': None, # (!) real value is "<method 'getGroups' of 'panda3d.core.MouseWatcher' objects>"
        'getInactivityTimeout': None, # (!) real value is "<method 'getInactivityTimeout' of 'panda3d.core.MouseWatcher' objects>"
        'getInactivityTimeoutEvent': None, # (!) real value is "<method 'getInactivityTimeoutEvent' of 'panda3d.core.MouseWatcher' objects>"
        'getLeavePattern': None, # (!) real value is "<method 'getLeavePattern' of 'panda3d.core.MouseWatcher' objects>"
        'getModifierButtons': None, # (!) real value is "<method 'getModifierButtons' of 'panda3d.core.MouseWatcher' objects>"
        'getMouse': None, # (!) real value is "<method 'getMouse' of 'panda3d.core.MouseWatcher' objects>"
        'getMouseX': None, # (!) real value is "<method 'getMouseX' of 'panda3d.core.MouseWatcher' objects>"
        'getMouseY': None, # (!) real value is "<method 'getMouseY' of 'panda3d.core.MouseWatcher' objects>"
        'getNumGroups': None, # (!) real value is "<method 'getNumGroups' of 'panda3d.core.MouseWatcher' objects>"
        'getOverRegion': None, # (!) real value is "<method 'getOverRegion' of 'panda3d.core.MouseWatcher' objects>"
        'getTrailLog': None, # (!) real value is "<method 'getTrailLog' of 'panda3d.core.MouseWatcher' objects>"
        'getTrailNode': None, # (!) real value is "<method 'getTrailNode' of 'panda3d.core.MouseWatcher' objects>"
        'getWithinPattern': None, # (!) real value is "<method 'getWithinPattern' of 'panda3d.core.MouseWatcher' objects>"
        'getWithoutPattern': None, # (!) real value is "<method 'getWithoutPattern' of 'panda3d.core.MouseWatcher' objects>"
        'get_button_down_pattern': None, # (!) real value is "<method 'get_button_down_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'get_button_repeat_pattern': None, # (!) real value is "<method 'get_button_repeat_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'get_button_up_pattern': None, # (!) real value is "<method 'get_button_up_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE366BB0>)>'
        'get_display_region': None, # (!) real value is "<method 'get_display_region' of 'panda3d.core.MouseWatcher' objects>"
        'get_enter_pattern': None, # (!) real value is "<method 'get_enter_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'get_extra_handler': None, # (!) real value is "<method 'get_extra_handler' of 'panda3d.core.MouseWatcher' objects>"
        'get_frame': None, # (!) real value is "<method 'get_frame' of 'panda3d.core.MouseWatcher' objects>"
        'get_geometry': None, # (!) real value is "<method 'get_geometry' of 'panda3d.core.MouseWatcher' objects>"
        'get_group': None, # (!) real value is "<method 'get_group' of 'panda3d.core.MouseWatcher' objects>"
        'get_groups': None, # (!) real value is "<method 'get_groups' of 'panda3d.core.MouseWatcher' objects>"
        'get_inactivity_timeout': None, # (!) real value is "<method 'get_inactivity_timeout' of 'panda3d.core.MouseWatcher' objects>"
        'get_inactivity_timeout_event': None, # (!) real value is "<method 'get_inactivity_timeout_event' of 'panda3d.core.MouseWatcher' objects>"
        'get_leave_pattern': None, # (!) real value is "<method 'get_leave_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'get_modifier_buttons': None, # (!) real value is "<method 'get_modifier_buttons' of 'panda3d.core.MouseWatcher' objects>"
        'get_mouse': None, # (!) real value is "<method 'get_mouse' of 'panda3d.core.MouseWatcher' objects>"
        'get_mouse_x': None, # (!) real value is "<method 'get_mouse_x' of 'panda3d.core.MouseWatcher' objects>"
        'get_mouse_y': None, # (!) real value is "<method 'get_mouse_y' of 'panda3d.core.MouseWatcher' objects>"
        'get_num_groups': None, # (!) real value is "<method 'get_num_groups' of 'panda3d.core.MouseWatcher' objects>"
        'get_over_region': None, # (!) real value is "<method 'get_over_region' of 'panda3d.core.MouseWatcher' objects>"
        'get_trail_log': None, # (!) real value is "<method 'get_trail_log' of 'panda3d.core.MouseWatcher' objects>"
        'get_trail_node': None, # (!) real value is "<method 'get_trail_node' of 'panda3d.core.MouseWatcher' objects>"
        'get_within_pattern': None, # (!) real value is "<method 'get_within_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'get_without_pattern': None, # (!) real value is "<method 'get_without_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'hasDisplayRegion': None, # (!) real value is "<method 'hasDisplayRegion' of 'panda3d.core.MouseWatcher' objects>"
        'hasGeometry': None, # (!) real value is "<method 'hasGeometry' of 'panda3d.core.MouseWatcher' objects>"
        'hasInactivityTimeout': None, # (!) real value is "<method 'hasInactivityTimeout' of 'panda3d.core.MouseWatcher' objects>"
        'hasMouse': None, # (!) real value is "<method 'hasMouse' of 'panda3d.core.MouseWatcher' objects>"
        'has_display_region': None, # (!) real value is "<method 'has_display_region' of 'panda3d.core.MouseWatcher' objects>"
        'has_geometry': None, # (!) real value is "<method 'has_geometry' of 'panda3d.core.MouseWatcher' objects>"
        'has_inactivity_timeout': None, # (!) real value is "<method 'has_inactivity_timeout' of 'panda3d.core.MouseWatcher' objects>"
        'has_mouse': None, # (!) real value is "<method 'has_mouse' of 'panda3d.core.MouseWatcher' objects>"
        'isButtonDown': None, # (!) real value is "<method 'isButtonDown' of 'panda3d.core.MouseWatcher' objects>"
        'isMouseOpen': None, # (!) real value is "<method 'isMouseOpen' of 'panda3d.core.MouseWatcher' objects>"
        'isOverRegion': None, # (!) real value is "<method 'isOverRegion' of 'panda3d.core.MouseWatcher' objects>"
        'is_button_down': None, # (!) real value is "<method 'is_button_down' of 'panda3d.core.MouseWatcher' objects>"
        'is_mouse_open': None, # (!) real value is "<method 'is_mouse_open' of 'panda3d.core.MouseWatcher' objects>"
        'is_over_region': None, # (!) real value is "<method 'is_over_region' of 'panda3d.core.MouseWatcher' objects>"
        'noteActivity': None, # (!) real value is "<method 'noteActivity' of 'panda3d.core.MouseWatcher' objects>"
        'note_activity': None, # (!) real value is "<method 'note_activity' of 'panda3d.core.MouseWatcher' objects>"
        'numTrailRecent': None, # (!) real value is "<method 'numTrailRecent' of 'panda3d.core.MouseWatcher' objects>"
        'num_trail_recent': None, # (!) real value is "<method 'num_trail_recent' of 'panda3d.core.MouseWatcher' objects>"
        'removeGroup': None, # (!) real value is "<method 'removeGroup' of 'panda3d.core.MouseWatcher' objects>"
        'removeRegion': None, # (!) real value is "<method 'removeRegion' of 'panda3d.core.MouseWatcher' objects>"
        'remove_group': None, # (!) real value is "<method 'remove_group' of 'panda3d.core.MouseWatcher' objects>"
        'remove_region': None, # (!) real value is "<method 'remove_region' of 'panda3d.core.MouseWatcher' objects>"
        'replaceGroup': None, # (!) real value is "<method 'replaceGroup' of 'panda3d.core.MouseWatcher' objects>"
        'replace_group': None, # (!) real value is "<method 'replace_group' of 'panda3d.core.MouseWatcher' objects>"
        'setButtonDownPattern': None, # (!) real value is "<method 'setButtonDownPattern' of 'panda3d.core.MouseWatcher' objects>"
        'setButtonRepeatPattern': None, # (!) real value is "<method 'setButtonRepeatPattern' of 'panda3d.core.MouseWatcher' objects>"
        'setButtonUpPattern': None, # (!) real value is "<method 'setButtonUpPattern' of 'panda3d.core.MouseWatcher' objects>"
        'setDisplayRegion': None, # (!) real value is "<method 'setDisplayRegion' of 'panda3d.core.MouseWatcher' objects>"
        'setEnterPattern': None, # (!) real value is "<method 'setEnterPattern' of 'panda3d.core.MouseWatcher' objects>"
        'setExtraHandler': None, # (!) real value is "<method 'setExtraHandler' of 'panda3d.core.MouseWatcher' objects>"
        'setFrame': None, # (!) real value is "<method 'setFrame' of 'panda3d.core.MouseWatcher' objects>"
        'setGeometry': None, # (!) real value is "<method 'setGeometry' of 'panda3d.core.MouseWatcher' objects>"
        'setInactivityTimeout': None, # (!) real value is "<method 'setInactivityTimeout' of 'panda3d.core.MouseWatcher' objects>"
        'setInactivityTimeoutEvent': None, # (!) real value is "<method 'setInactivityTimeoutEvent' of 'panda3d.core.MouseWatcher' objects>"
        'setLeavePattern': None, # (!) real value is "<method 'setLeavePattern' of 'panda3d.core.MouseWatcher' objects>"
        'setModifierButtons': None, # (!) real value is "<method 'setModifierButtons' of 'panda3d.core.MouseWatcher' objects>"
        'setTrailLogDuration': None, # (!) real value is "<method 'setTrailLogDuration' of 'panda3d.core.MouseWatcher' objects>"
        'setWithinPattern': None, # (!) real value is "<method 'setWithinPattern' of 'panda3d.core.MouseWatcher' objects>"
        'setWithoutPattern': None, # (!) real value is "<method 'setWithoutPattern' of 'panda3d.core.MouseWatcher' objects>"
        'set_button_down_pattern': None, # (!) real value is "<method 'set_button_down_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'set_button_repeat_pattern': None, # (!) real value is "<method 'set_button_repeat_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'set_button_up_pattern': None, # (!) real value is "<method 'set_button_up_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'set_display_region': None, # (!) real value is "<method 'set_display_region' of 'panda3d.core.MouseWatcher' objects>"
        'set_enter_pattern': None, # (!) real value is "<method 'set_enter_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'set_extra_handler': None, # (!) real value is "<method 'set_extra_handler' of 'panda3d.core.MouseWatcher' objects>"
        'set_frame': None, # (!) real value is "<method 'set_frame' of 'panda3d.core.MouseWatcher' objects>"
        'set_geometry': None, # (!) real value is "<method 'set_geometry' of 'panda3d.core.MouseWatcher' objects>"
        'set_inactivity_timeout': None, # (!) real value is "<method 'set_inactivity_timeout' of 'panda3d.core.MouseWatcher' objects>"
        'set_inactivity_timeout_event': None, # (!) real value is "<method 'set_inactivity_timeout_event' of 'panda3d.core.MouseWatcher' objects>"
        'set_leave_pattern': None, # (!) real value is "<method 'set_leave_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'set_modifier_buttons': None, # (!) real value is "<method 'set_modifier_buttons' of 'panda3d.core.MouseWatcher' objects>"
        'set_trail_log_duration': None, # (!) real value is "<method 'set_trail_log_duration' of 'panda3d.core.MouseWatcher' objects>"
        'set_within_pattern': None, # (!) real value is "<method 'set_within_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'set_without_pattern': None, # (!) real value is "<method 'set_without_pattern' of 'panda3d.core.MouseWatcher' objects>"
        'upcastToDataNode': None, # (!) real value is "<method 'upcastToDataNode' of 'panda3d.core.MouseWatcher' objects>"
        'upcastToMouseWatcherBase': None, # (!) real value is "<method 'upcastToMouseWatcherBase' of 'panda3d.core.MouseWatcher' objects>"
        'upcast_to_DataNode': None, # (!) real value is "<method 'upcast_to_DataNode' of 'panda3d.core.MouseWatcher' objects>"
        'upcast_to_MouseWatcherBase': None, # (!) real value is "<method 'upcast_to_MouseWatcherBase' of 'panda3d.core.MouseWatcher' objects>"
    }


