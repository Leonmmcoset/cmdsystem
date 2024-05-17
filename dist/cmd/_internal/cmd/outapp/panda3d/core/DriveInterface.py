# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .MouseInterfaceNode import MouseInterfaceNode

class DriveInterface(MouseInterfaceNode):
    """
    /**
     * This is a TFormer, similar to Trackball, that moves around a transform
     * matrix in response to mouse input.  The basic motion is on a horizontal
     * plane, as if driving a vehicle.
     */
    """
    def forceDgraph(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        force_dgraph(const DriveInterface self)
        
        /**
         * This is a special kludge for DriveInterface to allow us to avoid the one-
         * frame latency after a collision.  It forces an immediate partial data flow
         * for all data graph nodes below this node, causing all data nodes that
         * depend on this matrix to be updated immediately.
         */
        """
        pass

    def force_dgraph(self, const_DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        force_dgraph(const DriveInterface self)
        
        /**
         * This is a special kludge for DriveInterface to allow us to avoid the one-
         * frame latency after a collision.  It forces an immediate partial data flow
         * for all data graph nodes below this node, causing all data nodes that
         * depend on this matrix to be updated immediately.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getForceMouse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_force_mouse(DriveInterface self)
        
        /**
         * Returns the current setting of the force_mouse flag.  See
         * set_force_mouse().
         */
        """
        pass

    def getForwardSpeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_forward_speed(DriveInterface self)
        
        /**
         * Returns the speed of full forward motion, when the mouse is at the very top
         * of the window.  This is in units (e.g.  feet) per second.
         */
        """
        pass

    def getH(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_h(DriveInterface self)
        """
        pass

    def getHorizontalDeadZone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_horizontal_dead_zone(DriveInterface self)
        
        /**
         * Returns the size of the vertical bar in the center of the screen that
         * represents the "dead zone" of horizontal motion: the region in which the
         * mouse does not report horizontal motion.  This is in a fraction of the
         * window width, so 0.5 will set a dead zone as large as half the screen.
         */
        """
        pass

    def getHorizontalRampDownTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_horizontal_ramp_down_time(DriveInterface self)
        
        /**
         * Returns the amount of time, in seconds, it takes between the time a left or
         * right arrow key is released and the time it registers no motion.
         */
        """
        pass

    def getHorizontalRampUpTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_horizontal_ramp_up_time(DriveInterface self)
        
        /**
         * Returns the amount of time, in seconds, it takes between the time a left or
         * right arrow key is pressed and the time it registers full rotation.
         */
        """
        pass

    def getHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hpr(DriveInterface self)
        
        /**
         * Returns the driver's orientation.
         */
        """
        pass

    def getIgnoreMouse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ignore_mouse(DriveInterface self)
        
        /**
         * Returns the current setting of the ignore_mouse flag.  See
         * set_ignore_mouse().
         */
        """
        pass

    def getMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mat(const DriveInterface self)
        
        /**
         * Returns the current transform.
         */
        """
        pass

    def getP(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_p(DriveInterface self)
        """
        pass

    def getPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos(DriveInterface self)
        
        /**
         * Returns the driver's position.
         */
        """
        pass

    def getR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_r(DriveInterface self)
        """
        pass

    def getReverseSpeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reverse_speed(DriveInterface self)
        
        /**
         * Returns the speed of full reverse motion, when the mouse is at the very
         * bottom of the window.  This is in units (e.g.  feet) per second.
         */
        """
        pass

    def getRotateSpeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rotate_speed(DriveInterface self)
        
        /**
         * Returns the maximum rate at which the user can rotate left or right, when
         * the mouse is at the very edge of the window.  This is in degrees per
         * second.
         */
        """
        pass

    def getRotSpeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rot_speed(DriveInterface self)
        
        /**
         * Returns the rot_speed of the previous update in units/sec
         */
        """
        pass

    def getSpeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_speed(DriveInterface self)
        
        /**
         * Returns the speed of the previous update in units/sec
         */
        """
        pass

    def getStopThisFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stop_this_frame(DriveInterface self)
        
        /**
         * Returns the current setting of the stop_this_frame flag.  See
         * set_stop_this_frame().
         */
        """
        pass

    def getVerticalDeadZone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertical_dead_zone(DriveInterface self)
        
        /**
         * Returns the size of the horizontal bar in the center of the screen that
         * represents the "dead zone" of vertical motion: the region in which the
         * mouse does not report vertical motion.  This is in a fraction of the window
         * height, so 0.5 will set a dead zone as large as half the screen.
         */
        """
        pass

    def getVerticalRampDownTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertical_ramp_down_time(DriveInterface self)
        
        /**
         * Returns the amount of time, in seconds, it takes between the time an up or
         * down arrow key is released and the time it registers no motion.
         */
        """
        pass

    def getVerticalRampUpTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertical_ramp_up_time(DriveInterface self)
        
        /**
         * Returns the amount of time, in seconds, it takes between the time an up or
         * down arrow key is pressed and the time it registers full forward or
         * backward motion.
         */
        """
        pass

    def getX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x(DriveInterface self)
        """
        pass

    def getY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y(DriveInterface self)
        """
        pass

    def getZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_z(DriveInterface self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_force_mouse(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_force_mouse(DriveInterface self)
        
        /**
         * Returns the current setting of the force_mouse flag.  See
         * set_force_mouse().
         */
        """
        pass

    def get_forward_speed(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_forward_speed(DriveInterface self)
        
        /**
         * Returns the speed of full forward motion, when the mouse is at the very top
         * of the window.  This is in units (e.g.  feet) per second.
         */
        """
        pass

    def get_h(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_h(DriveInterface self)
        """
        pass

    def get_horizontal_dead_zone(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_horizontal_dead_zone(DriveInterface self)
        
        /**
         * Returns the size of the vertical bar in the center of the screen that
         * represents the "dead zone" of horizontal motion: the region in which the
         * mouse does not report horizontal motion.  This is in a fraction of the
         * window width, so 0.5 will set a dead zone as large as half the screen.
         */
        """
        pass

    def get_horizontal_ramp_down_time(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_horizontal_ramp_down_time(DriveInterface self)
        
        /**
         * Returns the amount of time, in seconds, it takes between the time a left or
         * right arrow key is released and the time it registers no motion.
         */
        """
        pass

    def get_horizontal_ramp_up_time(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_horizontal_ramp_up_time(DriveInterface self)
        
        /**
         * Returns the amount of time, in seconds, it takes between the time a left or
         * right arrow key is pressed and the time it registers full rotation.
         */
        """
        pass

    def get_hpr(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hpr(DriveInterface self)
        
        /**
         * Returns the driver's orientation.
         */
        """
        pass

    def get_ignore_mouse(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ignore_mouse(DriveInterface self)
        
        /**
         * Returns the current setting of the ignore_mouse flag.  See
         * set_ignore_mouse().
         */
        """
        pass

    def get_mat(self, const_DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mat(const DriveInterface self)
        
        /**
         * Returns the current transform.
         */
        """
        pass

    def get_p(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_p(DriveInterface self)
        """
        pass

    def get_pos(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos(DriveInterface self)
        
        /**
         * Returns the driver's position.
         */
        """
        pass

    def get_r(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_r(DriveInterface self)
        """
        pass

    def get_reverse_speed(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reverse_speed(DriveInterface self)
        
        /**
         * Returns the speed of full reverse motion, when the mouse is at the very
         * bottom of the window.  This is in units (e.g.  feet) per second.
         */
        """
        pass

    def get_rotate_speed(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rotate_speed(DriveInterface self)
        
        /**
         * Returns the maximum rate at which the user can rotate left or right, when
         * the mouse is at the very edge of the window.  This is in degrees per
         * second.
         */
        """
        pass

    def get_rot_speed(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rot_speed(DriveInterface self)
        
        /**
         * Returns the rot_speed of the previous update in units/sec
         */
        """
        pass

    def get_speed(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_speed(DriveInterface self)
        
        /**
         * Returns the speed of the previous update in units/sec
         */
        """
        pass

    def get_stop_this_frame(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stop_this_frame(DriveInterface self)
        
        /**
         * Returns the current setting of the stop_this_frame flag.  See
         * set_stop_this_frame().
         */
        """
        pass

    def get_vertical_dead_zone(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertical_dead_zone(DriveInterface self)
        
        /**
         * Returns the size of the horizontal bar in the center of the screen that
         * represents the "dead zone" of vertical motion: the region in which the
         * mouse does not report vertical motion.  This is in a fraction of the window
         * height, so 0.5 will set a dead zone as large as half the screen.
         */
        """
        pass

    def get_vertical_ramp_down_time(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertical_ramp_down_time(DriveInterface self)
        
        /**
         * Returns the amount of time, in seconds, it takes between the time an up or
         * down arrow key is released and the time it registers no motion.
         */
        """
        pass

    def get_vertical_ramp_up_time(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertical_ramp_up_time(DriveInterface self)
        
        /**
         * Returns the amount of time, in seconds, it takes between the time an up or
         * down arrow key is pressed and the time it registers full forward or
         * backward motion.
         */
        """
        pass

    def get_x(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x(DriveInterface self)
        """
        pass

    def get_y(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y(DriveInterface self)
        """
        pass

    def get_z(self, DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_z(DriveInterface self)
        """
        pass

    def reset(self, const_DriveInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const DriveInterface self)
        
        /**
         * Reinitializes the driver to the origin and resets any knowledge about
         * buttons being held down.
         */
        """
        pass

    def setForceMouse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_force_mouse(const DriveInterface self, bool force_mouse)
        
        /**
         * Changes the state of the force_mouse flag.  If this flag is true, the mouse
         * button need not be held down in order to drive the avatar around.
         */
        """
        pass

    def setForceRoll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_force_roll(const DriveInterface self, float force_roll)
        
        /**
         * This function is no longer used and does nothing.  It will be removed soon.
         */
        """
        pass

    def setForwardSpeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_forward_speed(const DriveInterface self, float speed)
        
        /**
         * Sets the speed of full forward motion, when the mouse is at the very top of
         * the window.  This is in units (e.g.  feet) per second.
         */
        """
        pass

    def setH(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_h(const DriveInterface self, float h)
        """
        pass

    def setHorizontalDeadZone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_horizontal_dead_zone(const DriveInterface self, float zone)
        
        /**
         * Sets the size of the vertical bar in the center of the screen that
         * represents the "dead zone" of horizontal motion: the region in which the
         * mouse does not report horizontal motion.  This is in a fraction of the
         * window width, so 0.5 will set a dead zone as large as half the screen.
         */
        """
        pass

    def setHorizontalRampDownTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_horizontal_ramp_down_time(const DriveInterface self, float ramp_down_time)
        
        /**
         * Sets the amount of time, in seconds, it takes between the time a left or
         * right arrow key is released and the time it registers no motion.
         */
        """
        pass

    def setHorizontalRampUpTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_horizontal_ramp_up_time(const DriveInterface self, float ramp_up_time)
        
        /**
         * Sets the amount of time, in seconds, it takes between the time a left or
         * right arrow key is pressed and the time it registers full rotation.
         */
        """
        pass

    def setHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_hpr(const DriveInterface self, const LVecBase3f hpr)
        set_hpr(const DriveInterface self, float h, float p, float r)
        
        /**
         * Directly sets the driver's orientation.
         */
        """
        pass

    def setIgnoreMouse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ignore_mouse(const DriveInterface self, bool ignore_mouse)
        
        /**
         * Changes the state of the ignore_mouse flag.  If this flag is true, the
         * DriveInterface will ignore mouse down button events (but still recognize
         * mouse up button events); the user will not be able to start the
         * DriveInterface going again if it is stopped, but if the user is currently
         * holding down a mouse button it will not stop immediately until the user
         * eventually releases the button.
         */
        """
        pass

    def setMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mat(const DriveInterface self, const LMatrix4f mat)
        
        /**
         * Stores the indicated transform in the DriveInterface.
         */
        """
        pass

    def setP(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_p(const DriveInterface self, float p)
        """
        pass

    def setPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos(const DriveInterface self, const LVecBase3f vec)
        set_pos(const DriveInterface self, float x, float y, float z)
        
        /**
         * Directly sets the driver's position.
         */
        """
        pass

    def setR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_r(const DriveInterface self, float r)
        """
        pass

    def setReverseSpeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_reverse_speed(const DriveInterface self, float speed)
        
        /**
         * Sets the speed of full reverse motion, when the mouse is at the very bottom
         * of the window.  This is in units (e.g.  feet) per second.
         */
        """
        pass

    def setRotateSpeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rotate_speed(const DriveInterface self, float speed)
        
        /**
         * Sets the maximum rate at which the user can rotate left or right, when the
         * mouse is at the very edge of the window.  This is in degrees per second.
         */
        """
        pass

    def setStopThisFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_stop_this_frame(const DriveInterface self, bool stop_this_frame)
        
        /**
         * If stop_this_frame is true, the next time the frame is computed no motion
         * will be allowed, and then the flag is reset to false.  This can be used to
         * prevent too much movement when we know a long time has artificially
         * elapsed, for instance when we take a screenshot, without munging the clock
         * for everything else.
         */
        """
        pass

    def setVerticalDeadZone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertical_dead_zone(const DriveInterface self, float zone)
        
        /**
         * Sets the size of the horizontal bar in the center of the screen that
         * represents the "dead zone" of vertical motion: the region in which the
         * mouse does not report vertical motion.  This is in a fraction of the window
         * height, so 0.5 will set a dead zone as large as half the screen.
         */
        """
        pass

    def setVerticalRampDownTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertical_ramp_down_time(const DriveInterface self, float ramp_down_time)
        
        /**
         * Sets the amount of time, in seconds, it takes between the time an up or
         * down arrow key is released and the time it registers no motion.
         */
        """
        pass

    def setVerticalRampUpTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertical_ramp_up_time(const DriveInterface self, float ramp_up_time)
        
        /**
         * Sets the amount of time, in seconds, it takes between the time an up or
         * down arrow key is pressed and the time it registers full forward or
         * backward motion.
         */
        """
        pass

    def setX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_x(const DriveInterface self, float x)
        """
        pass

    def setY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_y(const DriveInterface self, float y)
        """
        pass

    def setZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_z(const DriveInterface self, float z)
        """
        pass

    def set_force_mouse(self, const_DriveInterface_self, bool_force_mouse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_force_mouse(const DriveInterface self, bool force_mouse)
        
        /**
         * Changes the state of the force_mouse flag.  If this flag is true, the mouse
         * button need not be held down in order to drive the avatar around.
         */
        """
        pass

    def set_force_roll(self, const_DriveInterface_self, float_force_roll): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_force_roll(const DriveInterface self, float force_roll)
        
        /**
         * This function is no longer used and does nothing.  It will be removed soon.
         */
        """
        pass

    def set_forward_speed(self, const_DriveInterface_self, float_speed): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_forward_speed(const DriveInterface self, float speed)
        
        /**
         * Sets the speed of full forward motion, when the mouse is at the very top of
         * the window.  This is in units (e.g.  feet) per second.
         */
        """
        pass

    def set_h(self, const_DriveInterface_self, float_h): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_h(const DriveInterface self, float h)
        """
        pass

    def set_horizontal_dead_zone(self, const_DriveInterface_self, float_zone): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_horizontal_dead_zone(const DriveInterface self, float zone)
        
        /**
         * Sets the size of the vertical bar in the center of the screen that
         * represents the "dead zone" of horizontal motion: the region in which the
         * mouse does not report horizontal motion.  This is in a fraction of the
         * window width, so 0.5 will set a dead zone as large as half the screen.
         */
        """
        pass

    def set_horizontal_ramp_down_time(self, const_DriveInterface_self, float_ramp_down_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_horizontal_ramp_down_time(const DriveInterface self, float ramp_down_time)
        
        /**
         * Sets the amount of time, in seconds, it takes between the time a left or
         * right arrow key is released and the time it registers no motion.
         */
        """
        pass

    def set_horizontal_ramp_up_time(self, const_DriveInterface_self, float_ramp_up_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_horizontal_ramp_up_time(const DriveInterface self, float ramp_up_time)
        
        /**
         * Sets the amount of time, in seconds, it takes between the time a left or
         * right arrow key is pressed and the time it registers full rotation.
         */
        """
        pass

    def set_hpr(self, const_DriveInterface_self, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hpr(const DriveInterface self, const LVecBase3f hpr)
        set_hpr(const DriveInterface self, float h, float p, float r)
        
        /**
         * Directly sets the driver's orientation.
         */
        """
        pass

    def set_ignore_mouse(self, const_DriveInterface_self, bool_ignore_mouse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ignore_mouse(const DriveInterface self, bool ignore_mouse)
        
        /**
         * Changes the state of the ignore_mouse flag.  If this flag is true, the
         * DriveInterface will ignore mouse down button events (but still recognize
         * mouse up button events); the user will not be able to start the
         * DriveInterface going again if it is stopped, but if the user is currently
         * holding down a mouse button it will not stop immediately until the user
         * eventually releases the button.
         */
        """
        pass

    def set_mat(self, const_DriveInterface_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mat(const DriveInterface self, const LMatrix4f mat)
        
        /**
         * Stores the indicated transform in the DriveInterface.
         */
        """
        pass

    def set_p(self, const_DriveInterface_self, float_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_p(const DriveInterface self, float p)
        """
        pass

    def set_pos(self, const_DriveInterface_self, const_LVecBase3f_vec): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos(const DriveInterface self, const LVecBase3f vec)
        set_pos(const DriveInterface self, float x, float y, float z)
        
        /**
         * Directly sets the driver's position.
         */
        """
        pass

    def set_r(self, const_DriveInterface_self, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_r(const DriveInterface self, float r)
        """
        pass

    def set_reverse_speed(self, const_DriveInterface_self, float_speed): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_reverse_speed(const DriveInterface self, float speed)
        
        /**
         * Sets the speed of full reverse motion, when the mouse is at the very bottom
         * of the window.  This is in units (e.g.  feet) per second.
         */
        """
        pass

    def set_rotate_speed(self, const_DriveInterface_self, float_speed): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rotate_speed(const DriveInterface self, float speed)
        
        /**
         * Sets the maximum rate at which the user can rotate left or right, when the
         * mouse is at the very edge of the window.  This is in degrees per second.
         */
        """
        pass

    def set_stop_this_frame(self, const_DriveInterface_self, bool_stop_this_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_stop_this_frame(const DriveInterface self, bool stop_this_frame)
        
        /**
         * If stop_this_frame is true, the next time the frame is computed no motion
         * will be allowed, and then the flag is reset to false.  This can be used to
         * prevent too much movement when we know a long time has artificially
         * elapsed, for instance when we take a screenshot, without munging the clock
         * for everything else.
         */
        """
        pass

    def set_vertical_dead_zone(self, const_DriveInterface_self, float_zone): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertical_dead_zone(const DriveInterface self, float zone)
        
        /**
         * Sets the size of the horizontal bar in the center of the screen that
         * represents the "dead zone" of vertical motion: the region in which the
         * mouse does not report vertical motion.  This is in a fraction of the window
         * height, so 0.5 will set a dead zone as large as half the screen.
         */
        """
        pass

    def set_vertical_ramp_down_time(self, const_DriveInterface_self, float_ramp_down_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertical_ramp_down_time(const DriveInterface self, float ramp_down_time)
        
        /**
         * Sets the amount of time, in seconds, it takes between the time an up or
         * down arrow key is released and the time it registers no motion.
         */
        """
        pass

    def set_vertical_ramp_up_time(self, const_DriveInterface_self, float_ramp_up_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertical_ramp_up_time(const DriveInterface self, float ramp_up_time)
        
        /**
         * Sets the amount of time, in seconds, it takes between the time an up or
         * down arrow key is pressed and the time it registers full forward or
         * backward motion.
         */
        """
        pass

    def set_x(self, const_DriveInterface_self, float_x): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_x(const DriveInterface self, float x)
        """
        pass

    def set_y(self, const_DriveInterface_self, float_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_y(const DriveInterface self, float y)
        """
        pass

    def set_z(self, const_DriveInterface_self, float_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_z(const DriveInterface self, float z)
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.DriveInterface' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.DriveInterface' objects>"
        '__doc__': '/**\n * This is a TFormer, similar to Trackball, that moves around a transform\n * matrix in response to mouse input.  The basic motion is on a horizontal\n * plane, as if driving a vehicle.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DriveInterface' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3662A0>'
        'forceDgraph': None, # (!) real value is "<method 'forceDgraph' of 'panda3d.core.DriveInterface' objects>"
        'force_dgraph': None, # (!) real value is "<method 'force_dgraph' of 'panda3d.core.DriveInterface' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3662A0>)>'
        'getForceMouse': None, # (!) real value is "<method 'getForceMouse' of 'panda3d.core.DriveInterface' objects>"
        'getForwardSpeed': None, # (!) real value is "<method 'getForwardSpeed' of 'panda3d.core.DriveInterface' objects>"
        'getH': None, # (!) real value is "<method 'getH' of 'panda3d.core.DriveInterface' objects>"
        'getHorizontalDeadZone': None, # (!) real value is "<method 'getHorizontalDeadZone' of 'panda3d.core.DriveInterface' objects>"
        'getHorizontalRampDownTime': None, # (!) real value is "<method 'getHorizontalRampDownTime' of 'panda3d.core.DriveInterface' objects>"
        'getHorizontalRampUpTime': None, # (!) real value is "<method 'getHorizontalRampUpTime' of 'panda3d.core.DriveInterface' objects>"
        'getHpr': None, # (!) real value is "<method 'getHpr' of 'panda3d.core.DriveInterface' objects>"
        'getIgnoreMouse': None, # (!) real value is "<method 'getIgnoreMouse' of 'panda3d.core.DriveInterface' objects>"
        'getMat': None, # (!) real value is "<method 'getMat' of 'panda3d.core.DriveInterface' objects>"
        'getP': None, # (!) real value is "<method 'getP' of 'panda3d.core.DriveInterface' objects>"
        'getPos': None, # (!) real value is "<method 'getPos' of 'panda3d.core.DriveInterface' objects>"
        'getR': None, # (!) real value is "<method 'getR' of 'panda3d.core.DriveInterface' objects>"
        'getReverseSpeed': None, # (!) real value is "<method 'getReverseSpeed' of 'panda3d.core.DriveInterface' objects>"
        'getRotSpeed': None, # (!) real value is "<method 'getRotSpeed' of 'panda3d.core.DriveInterface' objects>"
        'getRotateSpeed': None, # (!) real value is "<method 'getRotateSpeed' of 'panda3d.core.DriveInterface' objects>"
        'getSpeed': None, # (!) real value is "<method 'getSpeed' of 'panda3d.core.DriveInterface' objects>"
        'getStopThisFrame': None, # (!) real value is "<method 'getStopThisFrame' of 'panda3d.core.DriveInterface' objects>"
        'getVerticalDeadZone': None, # (!) real value is "<method 'getVerticalDeadZone' of 'panda3d.core.DriveInterface' objects>"
        'getVerticalRampDownTime': None, # (!) real value is "<method 'getVerticalRampDownTime' of 'panda3d.core.DriveInterface' objects>"
        'getVerticalRampUpTime': None, # (!) real value is "<method 'getVerticalRampUpTime' of 'panda3d.core.DriveInterface' objects>"
        'getX': None, # (!) real value is "<method 'getX' of 'panda3d.core.DriveInterface' objects>"
        'getY': None, # (!) real value is "<method 'getY' of 'panda3d.core.DriveInterface' objects>"
        'getZ': None, # (!) real value is "<method 'getZ' of 'panda3d.core.DriveInterface' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3662A0>)>'
        'get_force_mouse': None, # (!) real value is "<method 'get_force_mouse' of 'panda3d.core.DriveInterface' objects>"
        'get_forward_speed': None, # (!) real value is "<method 'get_forward_speed' of 'panda3d.core.DriveInterface' objects>"
        'get_h': None, # (!) real value is "<method 'get_h' of 'panda3d.core.DriveInterface' objects>"
        'get_horizontal_dead_zone': None, # (!) real value is "<method 'get_horizontal_dead_zone' of 'panda3d.core.DriveInterface' objects>"
        'get_horizontal_ramp_down_time': None, # (!) real value is "<method 'get_horizontal_ramp_down_time' of 'panda3d.core.DriveInterface' objects>"
        'get_horizontal_ramp_up_time': None, # (!) real value is "<method 'get_horizontal_ramp_up_time' of 'panda3d.core.DriveInterface' objects>"
        'get_hpr': None, # (!) real value is "<method 'get_hpr' of 'panda3d.core.DriveInterface' objects>"
        'get_ignore_mouse': None, # (!) real value is "<method 'get_ignore_mouse' of 'panda3d.core.DriveInterface' objects>"
        'get_mat': None, # (!) real value is "<method 'get_mat' of 'panda3d.core.DriveInterface' objects>"
        'get_p': None, # (!) real value is "<method 'get_p' of 'panda3d.core.DriveInterface' objects>"
        'get_pos': None, # (!) real value is "<method 'get_pos' of 'panda3d.core.DriveInterface' objects>"
        'get_r': None, # (!) real value is "<method 'get_r' of 'panda3d.core.DriveInterface' objects>"
        'get_reverse_speed': None, # (!) real value is "<method 'get_reverse_speed' of 'panda3d.core.DriveInterface' objects>"
        'get_rot_speed': None, # (!) real value is "<method 'get_rot_speed' of 'panda3d.core.DriveInterface' objects>"
        'get_rotate_speed': None, # (!) real value is "<method 'get_rotate_speed' of 'panda3d.core.DriveInterface' objects>"
        'get_speed': None, # (!) real value is "<method 'get_speed' of 'panda3d.core.DriveInterface' objects>"
        'get_stop_this_frame': None, # (!) real value is "<method 'get_stop_this_frame' of 'panda3d.core.DriveInterface' objects>"
        'get_vertical_dead_zone': None, # (!) real value is "<method 'get_vertical_dead_zone' of 'panda3d.core.DriveInterface' objects>"
        'get_vertical_ramp_down_time': None, # (!) real value is "<method 'get_vertical_ramp_down_time' of 'panda3d.core.DriveInterface' objects>"
        'get_vertical_ramp_up_time': None, # (!) real value is "<method 'get_vertical_ramp_up_time' of 'panda3d.core.DriveInterface' objects>"
        'get_x': None, # (!) real value is "<method 'get_x' of 'panda3d.core.DriveInterface' objects>"
        'get_y': None, # (!) real value is "<method 'get_y' of 'panda3d.core.DriveInterface' objects>"
        'get_z': None, # (!) real value is "<method 'get_z' of 'panda3d.core.DriveInterface' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.DriveInterface' objects>"
        'setForceMouse': None, # (!) real value is "<method 'setForceMouse' of 'panda3d.core.DriveInterface' objects>"
        'setForceRoll': None, # (!) real value is "<method 'setForceRoll' of 'panda3d.core.DriveInterface' objects>"
        'setForwardSpeed': None, # (!) real value is "<method 'setForwardSpeed' of 'panda3d.core.DriveInterface' objects>"
        'setH': None, # (!) real value is "<method 'setH' of 'panda3d.core.DriveInterface' objects>"
        'setHorizontalDeadZone': None, # (!) real value is "<method 'setHorizontalDeadZone' of 'panda3d.core.DriveInterface' objects>"
        'setHorizontalRampDownTime': None, # (!) real value is "<method 'setHorizontalRampDownTime' of 'panda3d.core.DriveInterface' objects>"
        'setHorizontalRampUpTime': None, # (!) real value is "<method 'setHorizontalRampUpTime' of 'panda3d.core.DriveInterface' objects>"
        'setHpr': None, # (!) real value is "<method 'setHpr' of 'panda3d.core.DriveInterface' objects>"
        'setIgnoreMouse': None, # (!) real value is "<method 'setIgnoreMouse' of 'panda3d.core.DriveInterface' objects>"
        'setMat': None, # (!) real value is "<method 'setMat' of 'panda3d.core.DriveInterface' objects>"
        'setP': None, # (!) real value is "<method 'setP' of 'panda3d.core.DriveInterface' objects>"
        'setPos': None, # (!) real value is "<method 'setPos' of 'panda3d.core.DriveInterface' objects>"
        'setR': None, # (!) real value is "<method 'setR' of 'panda3d.core.DriveInterface' objects>"
        'setReverseSpeed': None, # (!) real value is "<method 'setReverseSpeed' of 'panda3d.core.DriveInterface' objects>"
        'setRotateSpeed': None, # (!) real value is "<method 'setRotateSpeed' of 'panda3d.core.DriveInterface' objects>"
        'setStopThisFrame': None, # (!) real value is "<method 'setStopThisFrame' of 'panda3d.core.DriveInterface' objects>"
        'setVerticalDeadZone': None, # (!) real value is "<method 'setVerticalDeadZone' of 'panda3d.core.DriveInterface' objects>"
        'setVerticalRampDownTime': None, # (!) real value is "<method 'setVerticalRampDownTime' of 'panda3d.core.DriveInterface' objects>"
        'setVerticalRampUpTime': None, # (!) real value is "<method 'setVerticalRampUpTime' of 'panda3d.core.DriveInterface' objects>"
        'setX': None, # (!) real value is "<method 'setX' of 'panda3d.core.DriveInterface' objects>"
        'setY': None, # (!) real value is "<method 'setY' of 'panda3d.core.DriveInterface' objects>"
        'setZ': None, # (!) real value is "<method 'setZ' of 'panda3d.core.DriveInterface' objects>"
        'set_force_mouse': None, # (!) real value is "<method 'set_force_mouse' of 'panda3d.core.DriveInterface' objects>"
        'set_force_roll': None, # (!) real value is "<method 'set_force_roll' of 'panda3d.core.DriveInterface' objects>"
        'set_forward_speed': None, # (!) real value is "<method 'set_forward_speed' of 'panda3d.core.DriveInterface' objects>"
        'set_h': None, # (!) real value is "<method 'set_h' of 'panda3d.core.DriveInterface' objects>"
        'set_horizontal_dead_zone': None, # (!) real value is "<method 'set_horizontal_dead_zone' of 'panda3d.core.DriveInterface' objects>"
        'set_horizontal_ramp_down_time': None, # (!) real value is "<method 'set_horizontal_ramp_down_time' of 'panda3d.core.DriveInterface' objects>"
        'set_horizontal_ramp_up_time': None, # (!) real value is "<method 'set_horizontal_ramp_up_time' of 'panda3d.core.DriveInterface' objects>"
        'set_hpr': None, # (!) real value is "<method 'set_hpr' of 'panda3d.core.DriveInterface' objects>"
        'set_ignore_mouse': None, # (!) real value is "<method 'set_ignore_mouse' of 'panda3d.core.DriveInterface' objects>"
        'set_mat': None, # (!) real value is "<method 'set_mat' of 'panda3d.core.DriveInterface' objects>"
        'set_p': None, # (!) real value is "<method 'set_p' of 'panda3d.core.DriveInterface' objects>"
        'set_pos': None, # (!) real value is "<method 'set_pos' of 'panda3d.core.DriveInterface' objects>"
        'set_r': None, # (!) real value is "<method 'set_r' of 'panda3d.core.DriveInterface' objects>"
        'set_reverse_speed': None, # (!) real value is "<method 'set_reverse_speed' of 'panda3d.core.DriveInterface' objects>"
        'set_rotate_speed': None, # (!) real value is "<method 'set_rotate_speed' of 'panda3d.core.DriveInterface' objects>"
        'set_stop_this_frame': None, # (!) real value is "<method 'set_stop_this_frame' of 'panda3d.core.DriveInterface' objects>"
        'set_vertical_dead_zone': None, # (!) real value is "<method 'set_vertical_dead_zone' of 'panda3d.core.DriveInterface' objects>"
        'set_vertical_ramp_down_time': None, # (!) real value is "<method 'set_vertical_ramp_down_time' of 'panda3d.core.DriveInterface' objects>"
        'set_vertical_ramp_up_time': None, # (!) real value is "<method 'set_vertical_ramp_up_time' of 'panda3d.core.DriveInterface' objects>"
        'set_x': None, # (!) real value is "<method 'set_x' of 'panda3d.core.DriveInterface' objects>"
        'set_y': None, # (!) real value is "<method 'set_y' of 'panda3d.core.DriveInterface' objects>"
        'set_z': None, # (!) real value is "<method 'set_z' of 'panda3d.core.DriveInterface' objects>"
    }


