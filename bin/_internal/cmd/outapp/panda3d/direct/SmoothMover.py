# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class SmoothMover(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class handles smoothing of sampled motion points over time, e.g.  for
     * smoothing the apparent movement of remote avatars, whose positions are sent
     * via occasional telemetry updates.
     *
     * It can operate in any of three modes: off, in which it does not smooth any
     * motion but provides the last position it was told; smoothing only, in which
     * it smooths motion information but never tries to anticipate where the
     * avatar might be going; or full prediction, in which it smooths motion as
     * well as tries to predict the avatar's position in lead of the last position
     * update.  The assumption is that all SmoothMovers in the world will be
     * operating in the same mode together.
     */
    """
    def applySmoothHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_smooth_hpr(SmoothMover self, NodePath node)
        
        /**
         * Applies the smoothed orientation to the indicated NodePath.  This is
         * equivalent to calling node.set_hpr(smooth_mover->get_smooth_hpr()).  It
         * exists as an optimization only, to avoid the overhead of passing the return
         * value through Python.
         */
        """
        pass

    def applySmoothPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_smooth_pos(SmoothMover self, NodePath node)
        
        /**
         * Applies the smoothed position to the indicated NodePath.  This is
         * equivalent to calling node.set_pos(smooth_mover->get_smooth_pos()).  It
         * exists as an optimization only, to avoid the overhead of passing the return
         * value through Python.
         */
        """
        pass

    def applySmoothPosHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_smooth_pos_hpr(SmoothMover self, NodePath pos_node, NodePath hpr_node)
        
        /**
         * Applies the smoothed position and orientation to the indicated NodePath.
         * This is equivalent to calling
         * node.set_pos_hpr(smooth_mover->get_smooth_pos(),
         * smooth_mover->get_smooth_hpr()).  It exists as an optimization only, to
         * avoid the overhead of passing the return value through Python.
         */
        """
        pass

    def apply_smooth_hpr(self, SmoothMover_self, NodePath_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_smooth_hpr(SmoothMover self, NodePath node)
        
        /**
         * Applies the smoothed orientation to the indicated NodePath.  This is
         * equivalent to calling node.set_hpr(smooth_mover->get_smooth_hpr()).  It
         * exists as an optimization only, to avoid the overhead of passing the return
         * value through Python.
         */
        """
        pass

    def apply_smooth_pos(self, SmoothMover_self, NodePath_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_smooth_pos(SmoothMover self, NodePath node)
        
        /**
         * Applies the smoothed position to the indicated NodePath.  This is
         * equivalent to calling node.set_pos(smooth_mover->get_smooth_pos()).  It
         * exists as an optimization only, to avoid the overhead of passing the return
         * value through Python.
         */
        """
        pass

    def apply_smooth_pos_hpr(self, SmoothMover_self, NodePath_pos_node, NodePath_hpr_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_smooth_pos_hpr(SmoothMover self, NodePath pos_node, NodePath hpr_node)
        
        /**
         * Applies the smoothed position and orientation to the indicated NodePath.
         * This is equivalent to calling
         * node.set_pos_hpr(smooth_mover->get_smooth_pos(),
         * smooth_mover->get_smooth_hpr()).  It exists as an optimization only, to
         * avoid the overhead of passing the return value through Python.
         */
        """
        pass

    def clearPositions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_positions(const SmoothMover self, bool reset_velocity)
        
        /**
         * Erases all the old position reports.  This should be done, for instance,
         * prior to teleporting the avatar to a new position; otherwise, the smoother
         * might try to lerp the avatar there.  If reset_velocity is true, the
         * velocity is also reset to 0.
         */
        """
        pass

    def clear_positions(self, const_SmoothMover_self, bool_reset_velocity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_positions(const SmoothMover self, bool reset_velocity)
        
        /**
         * Erases all the old position reports.  This should be done, for instance,
         * prior to teleporting the avatar to a new position; otherwise, the smoother
         * might try to lerp the avatar there.  If reset_velocity is true, the
         * velocity is also reset to 0.
         */
        """
        pass

    def computeAndApplySmoothHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compute_and_apply_smooth_hpr(const SmoothMover self, NodePath hpr_node)
        
        /**
         * A further optimization to reduce Python calls.  This computes the smooth
         * position and applies it to the indicated node or nodes in one call.  The
         * pos_node and hpr_node might be the same NodePath.
         */
        """
        pass

    def computeAndApplySmoothPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compute_and_apply_smooth_pos(const SmoothMover self, NodePath node)
        
        /**
         * A further optimization to reduce Python calls.  This computes the smooth
         * position and applies it to the indicated node in one call.
         */
        """
        pass

    def computeAndApplySmoothPosHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compute_and_apply_smooth_pos_hpr(const SmoothMover self, NodePath pos_node, NodePath hpr_node)
        
        /**
         * A further optimization to reduce Python calls.  This computes the smooth
         * position and applies it to the indicated node or nodes in one call.  The
         * pos_node and hpr_node might be the same NodePath.
         */
        """
        pass

    def computeSmoothPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compute_smooth_position(const SmoothMover self)
        compute_smooth_position(const SmoothMover self, double timestamp)
        
        /**
         * Computes the smoothed position (and orientation) of the mover at the
         * indicated point in time, based on the previous position reports.  After
         * this call has been made, get_smooth_pos() etc.  may be called to retrieve
         * the smoothed position.
         *
         * With no parameter, the function uses ClockObject::get_frame_time() as the
         * default time.
         */
        
        /**
         * Computes the smoothed position (and orientation) of the mover at the
         * indicated point in time, based on the previous position reports.  After
         * this call has been made, get_smooth_pos() etc.  may be called to retrieve
         * the smoothed position.
         *
         * The return value is true if the value has changed (or might have changed)
         * since the last call to compute_smooth_position(), or false if it remains
         * the same.
         */
        """
        pass

    def compute_and_apply_smooth_hpr(self, const_SmoothMover_self, NodePath_hpr_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compute_and_apply_smooth_hpr(const SmoothMover self, NodePath hpr_node)
        
        /**
         * A further optimization to reduce Python calls.  This computes the smooth
         * position and applies it to the indicated node or nodes in one call.  The
         * pos_node and hpr_node might be the same NodePath.
         */
        """
        pass

    def compute_and_apply_smooth_pos(self, const_SmoothMover_self, NodePath_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compute_and_apply_smooth_pos(const SmoothMover self, NodePath node)
        
        /**
         * A further optimization to reduce Python calls.  This computes the smooth
         * position and applies it to the indicated node in one call.
         */
        """
        pass

    def compute_and_apply_smooth_pos_hpr(self, const_SmoothMover_self, NodePath_pos_node, NodePath_hpr_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compute_and_apply_smooth_pos_hpr(const SmoothMover self, NodePath pos_node, NodePath hpr_node)
        
        /**
         * A further optimization to reduce Python calls.  This computes the smooth
         * position and applies it to the indicated node or nodes in one call.  The
         * pos_node and hpr_node might be the same NodePath.
         */
        """
        pass

    def compute_smooth_position(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compute_smooth_position(const SmoothMover self)
        compute_smooth_position(const SmoothMover self, double timestamp)
        
        /**
         * Computes the smoothed position (and orientation) of the mover at the
         * indicated point in time, based on the previous position reports.  After
         * this call has been made, get_smooth_pos() etc.  may be called to retrieve
         * the smoothed position.
         *
         * With no parameter, the function uses ClockObject::get_frame_time() as the
         * default time.
         */
        
        /**
         * Computes the smoothed position (and orientation) of the mover at the
         * indicated point in time, based on the previous position reports.  After
         * this call has been made, get_smooth_pos() etc.  may be called to retrieve
         * the smoothed position.
         *
         * The return value is true if the value has changed (or might have changed)
         * since the last call to compute_smooth_position(), or false if it remains
         * the same.
         */
        """
        pass

    def getAcceptClockSkew(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_accept_clock_skew(const SmoothMover self)
        
        /**
         * Returns the current state of the 'accept clock skew' flag.  See
         * set_accept_clock_skew().
         */
        """
        pass

    def getDefaultToStandingStill(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_to_standing_still(const SmoothMover self)
        
        /**
         * Returns the current state of the 'default to standing still' flag.  See
         * set_default_to_standing_still().
         */
        """
        pass

    def getDelay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_delay(const SmoothMover self)
        
        /**
         * Returns the amount of time, in seconds, to delay the computed position of a
         * SmoothMover.  See set_delay().
         */
        """
        pass

    def getDirectionalVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_directional_velocity(const SmoothMover self)
        
        /**
         * Returns the current state of the 'directional velocity' flag.  See
         * set_directional_velocity().
         */
        """
        pass

    def getExpectedBroadcastPeriod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expected_broadcast_period(const SmoothMover self)
        
        /**
         * Returns the interval at which we expect the SmoothNodes to broadcast their
         * position, in elapsed seconds.  See set_expected_broadcast_period().
         */
        """
        pass

    def getForwardAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_forward_axis(SmoothMover self)
        
        /**
         * Returns the smoothed position as computed by a previous call to
         * compute_smooth_position().
         */
        """
        pass

    def getLatestPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_latest_position(const SmoothMover self)
        
        /**
         * Updates the smooth_pos (and smooth_hpr, etc.) members to reflect the
         * absolute latest position known for this avatar.  This may result in a pop
         * to the most recent position.
         *
         * Returns true if the latest position is known, false otherwise.
         */
        """
        pass

    def getMaxPositionAge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_position_age(const SmoothMover self)
        
        /**
         * Returns the maximum amount of time a position is allowed to remain
         * unchanged before assuming it represents the avatar actually standing still.
         */
        """
        pass

    def getMostRecentTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_most_recent_timestamp(SmoothMover self)
        
        /**
         * Returns most recently recorded timestamp
         */
        """
        pass

    def getPredictionMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prediction_mode(const SmoothMover self)
        
        /**
         * Returns the predictioning mode of all SmoothMovers in the world.  See
         * set_prediction_mode().
         */
        """
        pass

    def getResetVelocityAge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reset_velocity_age(const SmoothMover self)
        
        /**
         * Returns the amount of time that should elapse after the last position
         * report before the velocity is reset to 0.  See set_reset_velocity_age().
         */
        """
        pass

    def getSampleHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sample_hpr(SmoothMover self)
        
        /**
         * Returns the current orientation of the working sample point.  This
         * orientation is updated periodically by set_h(), set_p(), etc., and its
         * current value is copied to the sample point table when mark_position() is
         * called.
         */
        """
        pass

    def getSamplePos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sample_pos(SmoothMover self)
        
        /**
         * Returns the current position of the working sample point.  This position is
         * updated periodically by set_x(), set_y(), etc., and its current value is
         * copied to the sample point table when mark_position() is called.
         */
        """
        pass

    def getSmoothForwardVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_smooth_forward_velocity(SmoothMover self)
        
        /**
         * Returns the speed at which the avatar is moving, in feet per second, along
         * its own forward axis (after applying the avatar's hpr).  This will be a
         * positive number if the avatar is moving forward, and a negative number if
         * it is moving backward.
         */
        """
        pass

    def getSmoothHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_smooth_hpr(SmoothMover self)
        
        /**
         * Returns the smoothed orientation as computed by a previous call to
         * compute_smooth_position().
         */
        """
        pass

    def getSmoothLateralVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_smooth_lateral_velocity(SmoothMover self)
        
        /**
         * Returns the speed at which the avatar is moving, in feet per second, along
         * its own lateral axis (after applying the avatar's hpr).  This will be a
         * positive number if the avatar is moving right, and a negative number if it
         * is moving left.
         */
        """
        pass

    def getSmoothMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_smooth_mode(const SmoothMover self)
        
        /**
         * Returns the smoothing mode of all SmoothMovers in the world.  See
         * set_smooth_mode().
         */
        """
        pass

    def getSmoothPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_smooth_pos(SmoothMover self)
        
        /**
         * Returns the smoothed position as computed by a previous call to
         * compute_smooth_position().
         */
        """
        pass

    def getSmoothRotationalVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_smooth_rotational_velocity(SmoothMover self)
        
        /**
         * Returns the speed at which the avatar is rotating in the horizontal plane
         * (i.e.  heading), in degrees per second.  This may be positive or negative,
         * according to the direction of rotation.
         */
        """
        pass

    def get_accept_clock_skew(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_accept_clock_skew(const SmoothMover self)
        
        /**
         * Returns the current state of the 'accept clock skew' flag.  See
         * set_accept_clock_skew().
         */
        """
        pass

    def get_default_to_standing_still(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_to_standing_still(const SmoothMover self)
        
        /**
         * Returns the current state of the 'default to standing still' flag.  See
         * set_default_to_standing_still().
         */
        """
        pass

    def get_delay(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_delay(const SmoothMover self)
        
        /**
         * Returns the amount of time, in seconds, to delay the computed position of a
         * SmoothMover.  See set_delay().
         */
        """
        pass

    def get_directional_velocity(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_directional_velocity(const SmoothMover self)
        
        /**
         * Returns the current state of the 'directional velocity' flag.  See
         * set_directional_velocity().
         */
        """
        pass

    def get_expected_broadcast_period(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expected_broadcast_period(const SmoothMover self)
        
        /**
         * Returns the interval at which we expect the SmoothNodes to broadcast their
         * position, in elapsed seconds.  See set_expected_broadcast_period().
         */
        """
        pass

    def get_forward_axis(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_forward_axis(SmoothMover self)
        
        /**
         * Returns the smoothed position as computed by a previous call to
         * compute_smooth_position().
         */
        """
        pass

    def get_latest_position(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_latest_position(const SmoothMover self)
        
        /**
         * Updates the smooth_pos (and smooth_hpr, etc.) members to reflect the
         * absolute latest position known for this avatar.  This may result in a pop
         * to the most recent position.
         *
         * Returns true if the latest position is known, false otherwise.
         */
        """
        pass

    def get_max_position_age(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_position_age(const SmoothMover self)
        
        /**
         * Returns the maximum amount of time a position is allowed to remain
         * unchanged before assuming it represents the avatar actually standing still.
         */
        """
        pass

    def get_most_recent_timestamp(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_most_recent_timestamp(SmoothMover self)
        
        /**
         * Returns most recently recorded timestamp
         */
        """
        pass

    def get_prediction_mode(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prediction_mode(const SmoothMover self)
        
        /**
         * Returns the predictioning mode of all SmoothMovers in the world.  See
         * set_prediction_mode().
         */
        """
        pass

    def get_reset_velocity_age(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reset_velocity_age(const SmoothMover self)
        
        /**
         * Returns the amount of time that should elapse after the last position
         * report before the velocity is reset to 0.  See set_reset_velocity_age().
         */
        """
        pass

    def get_sample_hpr(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sample_hpr(SmoothMover self)
        
        /**
         * Returns the current orientation of the working sample point.  This
         * orientation is updated periodically by set_h(), set_p(), etc., and its
         * current value is copied to the sample point table when mark_position() is
         * called.
         */
        """
        pass

    def get_sample_pos(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sample_pos(SmoothMover self)
        
        /**
         * Returns the current position of the working sample point.  This position is
         * updated periodically by set_x(), set_y(), etc., and its current value is
         * copied to the sample point table when mark_position() is called.
         */
        """
        pass

    def get_smooth_forward_velocity(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_smooth_forward_velocity(SmoothMover self)
        
        /**
         * Returns the speed at which the avatar is moving, in feet per second, along
         * its own forward axis (after applying the avatar's hpr).  This will be a
         * positive number if the avatar is moving forward, and a negative number if
         * it is moving backward.
         */
        """
        pass

    def get_smooth_hpr(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_smooth_hpr(SmoothMover self)
        
        /**
         * Returns the smoothed orientation as computed by a previous call to
         * compute_smooth_position().
         */
        """
        pass

    def get_smooth_lateral_velocity(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_smooth_lateral_velocity(SmoothMover self)
        
        /**
         * Returns the speed at which the avatar is moving, in feet per second, along
         * its own lateral axis (after applying the avatar's hpr).  This will be a
         * positive number if the avatar is moving right, and a negative number if it
         * is moving left.
         */
        """
        pass

    def get_smooth_mode(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_smooth_mode(const SmoothMover self)
        
        /**
         * Returns the smoothing mode of all SmoothMovers in the world.  See
         * set_smooth_mode().
         */
        """
        pass

    def get_smooth_pos(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_smooth_pos(SmoothMover self)
        
        /**
         * Returns the smoothed position as computed by a previous call to
         * compute_smooth_position().
         */
        """
        pass

    def get_smooth_rotational_velocity(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_smooth_rotational_velocity(SmoothMover self)
        
        /**
         * Returns the speed at which the avatar is rotating in the horizontal plane
         * (i.e.  heading), in degrees per second.  This may be positive or negative,
         * according to the direction of rotation.
         */
        """
        pass

    def handleWrtReparent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        handle_wrt_reparent(const SmoothMover self, NodePath old_parent, NodePath new_parent)
        
        /**
         * Node is being wrtReparented, update recorded sample positions to reflect
         * new parent
         */
        """
        pass

    def handle_wrt_reparent(self, const_SmoothMover_self, NodePath_old_parent, NodePath_new_parent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        handle_wrt_reparent(const SmoothMover self, NodePath old_parent, NodePath new_parent)
        
        /**
         * Node is being wrtReparented, update recorded sample positions to reflect
         * new parent
         */
        """
        pass

    def hasMostRecentTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_most_recent_timestamp(SmoothMover self)
        
        /**
         * Returns true if we have most recently recorded timestamp
         */
        """
        pass

    def has_most_recent_timestamp(self, SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_most_recent_timestamp(SmoothMover self)
        
        /**
         * Returns true if we have most recently recorded timestamp
         */
        """
        pass

    def markPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mark_position(const SmoothMover self)
        
        /**
         * Stores the position, orientation, and timestamp (if relevant) indicated by
         * previous calls to set_pos(), set_hpr(), and set_timestamp() in a new
         * position report.
         *
         * When compute_smooth_position() is called, it uses these stored position
         * reports to base its computation of the known position.
         */
        """
        pass

    def mark_position(self, const_SmoothMover_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mark_position(const SmoothMover self)
        
        /**
         * Stores the position, orientation, and timestamp (if relevant) indicated by
         * previous calls to set_pos(), set_hpr(), and set_timestamp() in a new
         * position report.
         *
         * When compute_smooth_position() is called, it uses these stored position
         * reports to base its computation of the known position.
         */
        """
        pass

    def output(self, SmoothMover_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(SmoothMover self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setAcceptClockSkew(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_accept_clock_skew(const SmoothMover self, bool flag)
        
        /**
         * Sets the 'accept clock skew' flag.  When this flag is true, clock skew from
         * the other clients will be tolerated by delaying each smooth mover's
         * position an additional amount, on top of that specified by set_delay(),
         * based on the measured average latency for timestamp messages received by
         * the client.
         *
         * In this way, if the other client has significant clock skew with respect to
         * our clock, it will be evident as a large positive or negative average
         * latency for timestamps.  By subtracting out this average latency, we
         * compensate for poor clock sync.
         */
        """
        pass

    def setDefaultToStandingStill(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_default_to_standing_still(const SmoothMover self, bool flag)
        
        /**
         * Sets the flag that indicates whether to assume that the node stopped moving
         * during periods when we don't get enough position updates.  If true, the
         * object will stand still momentarily.  If false, the object will
         * continuously lerp between the position updates that we did get.
         */
        """
        pass

    def setDelay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_delay(const SmoothMover self, double delay)
        
        /**
         * Sets the amount of time, in seconds, to delay the computed position of a
         * SmoothMover.  This is particularly useful when the prediction mode is off,
         * because it can allow the apparent motion of an avatar to appear smooth
         * without relying on prediction, at the cost of introducing additional lag in
         * the avatar's apparent position.
         */
        """
        pass

    def setDirectionalVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_directional_velocity(const SmoothMover self, bool flag)
        
        /**
         * Sets the flag that indicates whether the avatar's direction is considered
         * in computing the velocity.  When this is true, velocity is automatically
         * decomposed into a forward and a lateral velocity (and both may be positive
         * or negative); when it is false, all velocity is always returned as forward
         * velocity (and it is always positive).
         */
        """
        pass

    def setExpectedBroadcastPeriod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_expected_broadcast_period(const SmoothMover self, double period)
        
        /**
         * Sets the interval at which we expect the SmoothNodes to broadcast their
         * position, in elapsed seconds.  This controls the length of time we assume
         * the object has truly stopped, when we receive a long sequence of no
         * updates.
         */
        """
        pass

    def setH(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_h(const SmoothMover self, float h)
        
        /**
         * Sets the heading only.  See set_hpr().
         */
        """
        pass

    def setHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_hpr(const SmoothMover self, const LVecBase3f hpr)
        set_hpr(const SmoothMover self, float h, float p, float r)
        
        /**
         * Specifies the orientation of the SmoothMover at a particular time in the
         * past.  When mark_position() is called, this will be recorded (along with
         * hpr and timestamp) in a position report, which will then be used along with
         * all other position reports to determine the smooth position at any
         * particular instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_hpr(), or false if they are the same.
         */
        
        /**
         * Specifies the orientation of the SmoothMover at a particular time in the
         * past.  When mark_position() is called, this will be recorded (along with
         * hpr and timestamp) in a position report, which will then be used along with
         * all other position reports to determine the smooth position at any
         * particular instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_hpr(), or false if they are the same.
         */
        """
        pass

    def setMaxPositionAge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_position_age(const SmoothMover self, double age)
        
        /**
         * Sets the maximum amount of time a position is allowed to remain unchanged
         * before assuming it represents the avatar actually standing still.
         */
        """
        pass

    def setP(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_p(const SmoothMover self, float p)
        
        /**
         * Sets the pitch only.  See set_hpr().
         */
        """
        pass

    def setPhonyTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_phony_timestamp(const SmoothMover self, double timestamp, bool period_adjust)
        
        /**
         * Lies and specifies that the current position report was received now.  This
         * is usually used for very old position reports for which we're not sure of
         * the actual receipt time.
         */
        """
        pass

    def setPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos(const SmoothMover self, const LVecBase3f pos)
        set_pos(const SmoothMover self, float x, float y, float z)
        
        // These methods are used to specify each position update.  Call the
        // appropriate set_* function(s), as needed, and then call mark_position().
        // The return value of each function is true if the parameter value has
        // changed, or false if it remains the same as last time.
        
        /**
         * Specifies the position of the SmoothMover at a particular time in the past.
         * When mark_position() is called, this will be recorded (along with hpr and
         * timestamp) in a position report, which will then be used along with all
         * other position reports to determine the smooth position at any particular
         * instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_pos(), or false if they are the same.
         */
        
        /**
         * Specifies the position of the SmoothMover at a particular time in the past.
         * When mark_position() is called, this will be recorded (along with hpr and
         * timestamp) in a position report, which will then be used along with all
         * other position reports to determine the smooth position at any particular
         * instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_pos(), or false if they are the same.
         */
        """
        pass

    def setPosHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos_hpr(const SmoothMover self, const LVecBase3f pos, const LVecBase3f hpr)
        set_pos_hpr(const SmoothMover self, float x, float y, float z, float h, float p, float r)
        
        /**
         * Specifies the position and orientation of the SmoothMover at a particular
         * time in the past.  When mark_position() is called, this will be recorded
         * (along with timestamp) in a position report, which will then be used along
         * with all other position reports to determine the smooth position at any
         * particular instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_pos_hpr(), or false if they are the same.
         */
        
        /**
         * Specifies the position of the SmoothMover at a particular time in the past.
         * When mark_position() is called, this will be recorded (along with
         * timestamp) in a position report, which will then be used along with all
         * other position reports to determine the smooth position at any particular
         * instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_pos_hpr(), or false if they are the same.
         */
        """
        pass

    def setPredictionMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_prediction_mode(const SmoothMover self, int mode)
        
        /**
         * Sets the predictioning mode of all SmoothMovers in the world.  If this is
         * PM_off, no prediction will be performed, but smoothing might still be
         * performed.
         */
        """
        pass

    def setR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_r(const SmoothMover self, float r)
        
        /**
         * Sets the roll only.  See set_hpr().
         */
        """
        pass

    def setResetVelocityAge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_reset_velocity_age(const SmoothMover self, double age)
        
        /**
         * Sets the amount of time that should elapse after the last position report
         * before the velocity is reset to 0.  This is similar to max_position_age,
         * but it is only used to determine the resetting of the reported velocity.
         * It should always be greater than or equal to max_position_age.
         */
        """
        pass

    def setSmoothMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_smooth_mode(const SmoothMover self, int mode)
        
        /**
         * Sets the smoothing mode of all SmoothMovers in the world.  If this is
         * SM_off, no smoothing or prediction will be performed, and get_smooth_pos()
         * will simply return the position last set by mark_position().
         */
        """
        pass

    def setTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_timestamp(const SmoothMover self, double timestamp)
        
        /**
         * Specifies the time that the current position report applies.  This should
         * be called, along with set_pos() and set_hpr(), before a call to
         * mark_position().
         */
        """
        pass

    def setX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_x(const SmoothMover self, float x)
        
        /**
         * Sets the X position only.  See set_pos().
         */
        """
        pass

    def setY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_y(const SmoothMover self, float y)
        
        /**
         * Sets the Y position only.  See set_pos().
         */
        """
        pass

    def setZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_z(const SmoothMover self, float z)
        
        /**
         * Sets the Z position only.  See set_pos().
         */
        """
        pass

    def set_accept_clock_skew(self, const_SmoothMover_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_accept_clock_skew(const SmoothMover self, bool flag)
        
        /**
         * Sets the 'accept clock skew' flag.  When this flag is true, clock skew from
         * the other clients will be tolerated by delaying each smooth mover's
         * position an additional amount, on top of that specified by set_delay(),
         * based on the measured average latency for timestamp messages received by
         * the client.
         *
         * In this way, if the other client has significant clock skew with respect to
         * our clock, it will be evident as a large positive or negative average
         * latency for timestamps.  By subtracting out this average latency, we
         * compensate for poor clock sync.
         */
        """
        pass

    def set_default_to_standing_still(self, const_SmoothMover_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_default_to_standing_still(const SmoothMover self, bool flag)
        
        /**
         * Sets the flag that indicates whether to assume that the node stopped moving
         * during periods when we don't get enough position updates.  If true, the
         * object will stand still momentarily.  If false, the object will
         * continuously lerp between the position updates that we did get.
         */
        """
        pass

    def set_delay(self, const_SmoothMover_self, double_delay): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_delay(const SmoothMover self, double delay)
        
        /**
         * Sets the amount of time, in seconds, to delay the computed position of a
         * SmoothMover.  This is particularly useful when the prediction mode is off,
         * because it can allow the apparent motion of an avatar to appear smooth
         * without relying on prediction, at the cost of introducing additional lag in
         * the avatar's apparent position.
         */
        """
        pass

    def set_directional_velocity(self, const_SmoothMover_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_directional_velocity(const SmoothMover self, bool flag)
        
        /**
         * Sets the flag that indicates whether the avatar's direction is considered
         * in computing the velocity.  When this is true, velocity is automatically
         * decomposed into a forward and a lateral velocity (and both may be positive
         * or negative); when it is false, all velocity is always returned as forward
         * velocity (and it is always positive).
         */
        """
        pass

    def set_expected_broadcast_period(self, const_SmoothMover_self, double_period): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_expected_broadcast_period(const SmoothMover self, double period)
        
        /**
         * Sets the interval at which we expect the SmoothNodes to broadcast their
         * position, in elapsed seconds.  This controls the length of time we assume
         * the object has truly stopped, when we receive a long sequence of no
         * updates.
         */
        """
        pass

    def set_h(self, const_SmoothMover_self, float_h): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_h(const SmoothMover self, float h)
        
        /**
         * Sets the heading only.  See set_hpr().
         */
        """
        pass

    def set_hpr(self, const_SmoothMover_self, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hpr(const SmoothMover self, const LVecBase3f hpr)
        set_hpr(const SmoothMover self, float h, float p, float r)
        
        /**
         * Specifies the orientation of the SmoothMover at a particular time in the
         * past.  When mark_position() is called, this will be recorded (along with
         * hpr and timestamp) in a position report, which will then be used along with
         * all other position reports to determine the smooth position at any
         * particular instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_hpr(), or false if they are the same.
         */
        
        /**
         * Specifies the orientation of the SmoothMover at a particular time in the
         * past.  When mark_position() is called, this will be recorded (along with
         * hpr and timestamp) in a position report, which will then be used along with
         * all other position reports to determine the smooth position at any
         * particular instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_hpr(), or false if they are the same.
         */
        """
        pass

    def set_max_position_age(self, const_SmoothMover_self, double_age): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_position_age(const SmoothMover self, double age)
        
        /**
         * Sets the maximum amount of time a position is allowed to remain unchanged
         * before assuming it represents the avatar actually standing still.
         */
        """
        pass

    def set_p(self, const_SmoothMover_self, float_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_p(const SmoothMover self, float p)
        
        /**
         * Sets the pitch only.  See set_hpr().
         */
        """
        pass

    def set_phony_timestamp(self, const_SmoothMover_self, double_timestamp, bool_period_adjust): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_phony_timestamp(const SmoothMover self, double timestamp, bool period_adjust)
        
        /**
         * Lies and specifies that the current position report was received now.  This
         * is usually used for very old position reports for which we're not sure of
         * the actual receipt time.
         */
        """
        pass

    def set_pos(self, const_SmoothMover_self, const_LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos(const SmoothMover self, const LVecBase3f pos)
        set_pos(const SmoothMover self, float x, float y, float z)
        
        // These methods are used to specify each position update.  Call the
        // appropriate set_* function(s), as needed, and then call mark_position().
        // The return value of each function is true if the parameter value has
        // changed, or false if it remains the same as last time.
        
        /**
         * Specifies the position of the SmoothMover at a particular time in the past.
         * When mark_position() is called, this will be recorded (along with hpr and
         * timestamp) in a position report, which will then be used along with all
         * other position reports to determine the smooth position at any particular
         * instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_pos(), or false if they are the same.
         */
        
        /**
         * Specifies the position of the SmoothMover at a particular time in the past.
         * When mark_position() is called, this will be recorded (along with hpr and
         * timestamp) in a position report, which will then be used along with all
         * other position reports to determine the smooth position at any particular
         * instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_pos(), or false if they are the same.
         */
        """
        pass

    def set_pos_hpr(self, const_SmoothMover_self, const_LVecBase3f_pos, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos_hpr(const SmoothMover self, const LVecBase3f pos, const LVecBase3f hpr)
        set_pos_hpr(const SmoothMover self, float x, float y, float z, float h, float p, float r)
        
        /**
         * Specifies the position and orientation of the SmoothMover at a particular
         * time in the past.  When mark_position() is called, this will be recorded
         * (along with timestamp) in a position report, which will then be used along
         * with all other position reports to determine the smooth position at any
         * particular instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_pos_hpr(), or false if they are the same.
         */
        
        /**
         * Specifies the position of the SmoothMover at a particular time in the past.
         * When mark_position() is called, this will be recorded (along with
         * timestamp) in a position report, which will then be used along with all
         * other position reports to determine the smooth position at any particular
         * instant.
         *
         * The return value is true if any parameter has changed since the last call
         * to set_pos_hpr(), or false if they are the same.
         */
        """
        pass

    def set_prediction_mode(self, const_SmoothMover_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_prediction_mode(const SmoothMover self, int mode)
        
        /**
         * Sets the predictioning mode of all SmoothMovers in the world.  If this is
         * PM_off, no prediction will be performed, but smoothing might still be
         * performed.
         */
        """
        pass

    def set_r(self, const_SmoothMover_self, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_r(const SmoothMover self, float r)
        
        /**
         * Sets the roll only.  See set_hpr().
         */
        """
        pass

    def set_reset_velocity_age(self, const_SmoothMover_self, double_age): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_reset_velocity_age(const SmoothMover self, double age)
        
        /**
         * Sets the amount of time that should elapse after the last position report
         * before the velocity is reset to 0.  This is similar to max_position_age,
         * but it is only used to determine the resetting of the reported velocity.
         * It should always be greater than or equal to max_position_age.
         */
        """
        pass

    def set_smooth_mode(self, const_SmoothMover_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_smooth_mode(const SmoothMover self, int mode)
        
        /**
         * Sets the smoothing mode of all SmoothMovers in the world.  If this is
         * SM_off, no smoothing or prediction will be performed, and get_smooth_pos()
         * will simply return the position last set by mark_position().
         */
        """
        pass

    def set_timestamp(self, const_SmoothMover_self, double_timestamp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_timestamp(const SmoothMover self, double timestamp)
        
        /**
         * Specifies the time that the current position report applies.  This should
         * be called, along with set_pos() and set_hpr(), before a call to
         * mark_position().
         */
        """
        pass

    def set_x(self, const_SmoothMover_self, float_x): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_x(const SmoothMover self, float x)
        
        /**
         * Sets the X position only.  See set_pos().
         */
        """
        pass

    def set_y(self, const_SmoothMover_self, float_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_y(const SmoothMover self, float y)
        
        /**
         * Sets the Y position only.  See set_pos().
         */
        """
        pass

    def set_z(self, const_SmoothMover_self, float_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_z(const SmoothMover self, float z)
        
        /**
         * Sets the Z position only.  See set_pos().
         */
        """
        pass

    def write(self, SmoothMover_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(SmoothMover self, ostream out)
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'PMOff': 0,
        'PMOn': 1,
        'PM_off': 0,
        'PM_on': 1,
        'SMOff': 0,
        'SMOn': 1,
        'SM_off': 0,
        'SM_on': 1,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.SmoothMover' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.SmoothMover' objects>"
        '__doc__': "/**\n * This class handles smoothing of sampled motion points over time, e.g.  for\n * smoothing the apparent movement of remote avatars, whose positions are sent\n * via occasional telemetry updates.\n *\n * It can operate in any of three modes: off, in which it does not smooth any\n * motion but provides the last position it was told; smoothing only, in which\n * it smooths motion information but never tries to anticipate where the\n * avatar might be going; or full prediction, in which it smooths motion as\n * well as tries to predict the avatar's position in lead of the last position\n * update.  The assumption is that all SmoothMovers in the world will be\n * operating in the same mode together.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.SmoothMover' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68E3BE0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.direct.SmoothMover' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.direct.SmoothMover' objects>"
        'applySmoothHpr': None, # (!) real value is "<method 'applySmoothHpr' of 'panda3d.direct.SmoothMover' objects>"
        'applySmoothPos': None, # (!) real value is "<method 'applySmoothPos' of 'panda3d.direct.SmoothMover' objects>"
        'applySmoothPosHpr': None, # (!) real value is "<method 'applySmoothPosHpr' of 'panda3d.direct.SmoothMover' objects>"
        'apply_smooth_hpr': None, # (!) real value is "<method 'apply_smooth_hpr' of 'panda3d.direct.SmoothMover' objects>"
        'apply_smooth_pos': None, # (!) real value is "<method 'apply_smooth_pos' of 'panda3d.direct.SmoothMover' objects>"
        'apply_smooth_pos_hpr': None, # (!) real value is "<method 'apply_smooth_pos_hpr' of 'panda3d.direct.SmoothMover' objects>"
        'clearPositions': None, # (!) real value is "<method 'clearPositions' of 'panda3d.direct.SmoothMover' objects>"
        'clear_positions': None, # (!) real value is "<method 'clear_positions' of 'panda3d.direct.SmoothMover' objects>"
        'computeAndApplySmoothHpr': None, # (!) real value is "<method 'computeAndApplySmoothHpr' of 'panda3d.direct.SmoothMover' objects>"
        'computeAndApplySmoothPos': None, # (!) real value is "<method 'computeAndApplySmoothPos' of 'panda3d.direct.SmoothMover' objects>"
        'computeAndApplySmoothPosHpr': None, # (!) real value is "<method 'computeAndApplySmoothPosHpr' of 'panda3d.direct.SmoothMover' objects>"
        'computeSmoothPosition': None, # (!) real value is "<method 'computeSmoothPosition' of 'panda3d.direct.SmoothMover' objects>"
        'compute_and_apply_smooth_hpr': None, # (!) real value is "<method 'compute_and_apply_smooth_hpr' of 'panda3d.direct.SmoothMover' objects>"
        'compute_and_apply_smooth_pos': None, # (!) real value is "<method 'compute_and_apply_smooth_pos' of 'panda3d.direct.SmoothMover' objects>"
        'compute_and_apply_smooth_pos_hpr': None, # (!) real value is "<method 'compute_and_apply_smooth_pos_hpr' of 'panda3d.direct.SmoothMover' objects>"
        'compute_smooth_position': None, # (!) real value is "<method 'compute_smooth_position' of 'panda3d.direct.SmoothMover' objects>"
        'getAcceptClockSkew': None, # (!) real value is "<method 'getAcceptClockSkew' of 'panda3d.direct.SmoothMover' objects>"
        'getDefaultToStandingStill': None, # (!) real value is "<method 'getDefaultToStandingStill' of 'panda3d.direct.SmoothMover' objects>"
        'getDelay': None, # (!) real value is "<method 'getDelay' of 'panda3d.direct.SmoothMover' objects>"
        'getDirectionalVelocity': None, # (!) real value is "<method 'getDirectionalVelocity' of 'panda3d.direct.SmoothMover' objects>"
        'getExpectedBroadcastPeriod': None, # (!) real value is "<method 'getExpectedBroadcastPeriod' of 'panda3d.direct.SmoothMover' objects>"
        'getForwardAxis': None, # (!) real value is "<method 'getForwardAxis' of 'panda3d.direct.SmoothMover' objects>"
        'getLatestPosition': None, # (!) real value is "<method 'getLatestPosition' of 'panda3d.direct.SmoothMover' objects>"
        'getMaxPositionAge': None, # (!) real value is "<method 'getMaxPositionAge' of 'panda3d.direct.SmoothMover' objects>"
        'getMostRecentTimestamp': None, # (!) real value is "<method 'getMostRecentTimestamp' of 'panda3d.direct.SmoothMover' objects>"
        'getPredictionMode': None, # (!) real value is "<method 'getPredictionMode' of 'panda3d.direct.SmoothMover' objects>"
        'getResetVelocityAge': None, # (!) real value is "<method 'getResetVelocityAge' of 'panda3d.direct.SmoothMover' objects>"
        'getSampleHpr': None, # (!) real value is "<method 'getSampleHpr' of 'panda3d.direct.SmoothMover' objects>"
        'getSamplePos': None, # (!) real value is "<method 'getSamplePos' of 'panda3d.direct.SmoothMover' objects>"
        'getSmoothForwardVelocity': None, # (!) real value is "<method 'getSmoothForwardVelocity' of 'panda3d.direct.SmoothMover' objects>"
        'getSmoothHpr': None, # (!) real value is "<method 'getSmoothHpr' of 'panda3d.direct.SmoothMover' objects>"
        'getSmoothLateralVelocity': None, # (!) real value is "<method 'getSmoothLateralVelocity' of 'panda3d.direct.SmoothMover' objects>"
        'getSmoothMode': None, # (!) real value is "<method 'getSmoothMode' of 'panda3d.direct.SmoothMover' objects>"
        'getSmoothPos': None, # (!) real value is "<method 'getSmoothPos' of 'panda3d.direct.SmoothMover' objects>"
        'getSmoothRotationalVelocity': None, # (!) real value is "<method 'getSmoothRotationalVelocity' of 'panda3d.direct.SmoothMover' objects>"
        'get_accept_clock_skew': None, # (!) real value is "<method 'get_accept_clock_skew' of 'panda3d.direct.SmoothMover' objects>"
        'get_default_to_standing_still': None, # (!) real value is "<method 'get_default_to_standing_still' of 'panda3d.direct.SmoothMover' objects>"
        'get_delay': None, # (!) real value is "<method 'get_delay' of 'panda3d.direct.SmoothMover' objects>"
        'get_directional_velocity': None, # (!) real value is "<method 'get_directional_velocity' of 'panda3d.direct.SmoothMover' objects>"
        'get_expected_broadcast_period': None, # (!) real value is "<method 'get_expected_broadcast_period' of 'panda3d.direct.SmoothMover' objects>"
        'get_forward_axis': None, # (!) real value is "<method 'get_forward_axis' of 'panda3d.direct.SmoothMover' objects>"
        'get_latest_position': None, # (!) real value is "<method 'get_latest_position' of 'panda3d.direct.SmoothMover' objects>"
        'get_max_position_age': None, # (!) real value is "<method 'get_max_position_age' of 'panda3d.direct.SmoothMover' objects>"
        'get_most_recent_timestamp': None, # (!) real value is "<method 'get_most_recent_timestamp' of 'panda3d.direct.SmoothMover' objects>"
        'get_prediction_mode': None, # (!) real value is "<method 'get_prediction_mode' of 'panda3d.direct.SmoothMover' objects>"
        'get_reset_velocity_age': None, # (!) real value is "<method 'get_reset_velocity_age' of 'panda3d.direct.SmoothMover' objects>"
        'get_sample_hpr': None, # (!) real value is "<method 'get_sample_hpr' of 'panda3d.direct.SmoothMover' objects>"
        'get_sample_pos': None, # (!) real value is "<method 'get_sample_pos' of 'panda3d.direct.SmoothMover' objects>"
        'get_smooth_forward_velocity': None, # (!) real value is "<method 'get_smooth_forward_velocity' of 'panda3d.direct.SmoothMover' objects>"
        'get_smooth_hpr': None, # (!) real value is "<method 'get_smooth_hpr' of 'panda3d.direct.SmoothMover' objects>"
        'get_smooth_lateral_velocity': None, # (!) real value is "<method 'get_smooth_lateral_velocity' of 'panda3d.direct.SmoothMover' objects>"
        'get_smooth_mode': None, # (!) real value is "<method 'get_smooth_mode' of 'panda3d.direct.SmoothMover' objects>"
        'get_smooth_pos': None, # (!) real value is "<method 'get_smooth_pos' of 'panda3d.direct.SmoothMover' objects>"
        'get_smooth_rotational_velocity': None, # (!) real value is "<method 'get_smooth_rotational_velocity' of 'panda3d.direct.SmoothMover' objects>"
        'handleWrtReparent': None, # (!) real value is "<method 'handleWrtReparent' of 'panda3d.direct.SmoothMover' objects>"
        'handle_wrt_reparent': None, # (!) real value is "<method 'handle_wrt_reparent' of 'panda3d.direct.SmoothMover' objects>"
        'hasMostRecentTimestamp': None, # (!) real value is "<method 'hasMostRecentTimestamp' of 'panda3d.direct.SmoothMover' objects>"
        'has_most_recent_timestamp': None, # (!) real value is "<method 'has_most_recent_timestamp' of 'panda3d.direct.SmoothMover' objects>"
        'markPosition': None, # (!) real value is "<method 'markPosition' of 'panda3d.direct.SmoothMover' objects>"
        'mark_position': None, # (!) real value is "<method 'mark_position' of 'panda3d.direct.SmoothMover' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.direct.SmoothMover' objects>"
        'setAcceptClockSkew': None, # (!) real value is "<method 'setAcceptClockSkew' of 'panda3d.direct.SmoothMover' objects>"
        'setDefaultToStandingStill': None, # (!) real value is "<method 'setDefaultToStandingStill' of 'panda3d.direct.SmoothMover' objects>"
        'setDelay': None, # (!) real value is "<method 'setDelay' of 'panda3d.direct.SmoothMover' objects>"
        'setDirectionalVelocity': None, # (!) real value is "<method 'setDirectionalVelocity' of 'panda3d.direct.SmoothMover' objects>"
        'setExpectedBroadcastPeriod': None, # (!) real value is "<method 'setExpectedBroadcastPeriod' of 'panda3d.direct.SmoothMover' objects>"
        'setH': None, # (!) real value is "<method 'setH' of 'panda3d.direct.SmoothMover' objects>"
        'setHpr': None, # (!) real value is "<method 'setHpr' of 'panda3d.direct.SmoothMover' objects>"
        'setMaxPositionAge': None, # (!) real value is "<method 'setMaxPositionAge' of 'panda3d.direct.SmoothMover' objects>"
        'setP': None, # (!) real value is "<method 'setP' of 'panda3d.direct.SmoothMover' objects>"
        'setPhonyTimestamp': None, # (!) real value is "<method 'setPhonyTimestamp' of 'panda3d.direct.SmoothMover' objects>"
        'setPos': None, # (!) real value is "<method 'setPos' of 'panda3d.direct.SmoothMover' objects>"
        'setPosHpr': None, # (!) real value is "<method 'setPosHpr' of 'panda3d.direct.SmoothMover' objects>"
        'setPredictionMode': None, # (!) real value is "<method 'setPredictionMode' of 'panda3d.direct.SmoothMover' objects>"
        'setR': None, # (!) real value is "<method 'setR' of 'panda3d.direct.SmoothMover' objects>"
        'setResetVelocityAge': None, # (!) real value is "<method 'setResetVelocityAge' of 'panda3d.direct.SmoothMover' objects>"
        'setSmoothMode': None, # (!) real value is "<method 'setSmoothMode' of 'panda3d.direct.SmoothMover' objects>"
        'setTimestamp': None, # (!) real value is "<method 'setTimestamp' of 'panda3d.direct.SmoothMover' objects>"
        'setX': None, # (!) real value is "<method 'setX' of 'panda3d.direct.SmoothMover' objects>"
        'setY': None, # (!) real value is "<method 'setY' of 'panda3d.direct.SmoothMover' objects>"
        'setZ': None, # (!) real value is "<method 'setZ' of 'panda3d.direct.SmoothMover' objects>"
        'set_accept_clock_skew': None, # (!) real value is "<method 'set_accept_clock_skew' of 'panda3d.direct.SmoothMover' objects>"
        'set_default_to_standing_still': None, # (!) real value is "<method 'set_default_to_standing_still' of 'panda3d.direct.SmoothMover' objects>"
        'set_delay': None, # (!) real value is "<method 'set_delay' of 'panda3d.direct.SmoothMover' objects>"
        'set_directional_velocity': None, # (!) real value is "<method 'set_directional_velocity' of 'panda3d.direct.SmoothMover' objects>"
        'set_expected_broadcast_period': None, # (!) real value is "<method 'set_expected_broadcast_period' of 'panda3d.direct.SmoothMover' objects>"
        'set_h': None, # (!) real value is "<method 'set_h' of 'panda3d.direct.SmoothMover' objects>"
        'set_hpr': None, # (!) real value is "<method 'set_hpr' of 'panda3d.direct.SmoothMover' objects>"
        'set_max_position_age': None, # (!) real value is "<method 'set_max_position_age' of 'panda3d.direct.SmoothMover' objects>"
        'set_p': None, # (!) real value is "<method 'set_p' of 'panda3d.direct.SmoothMover' objects>"
        'set_phony_timestamp': None, # (!) real value is "<method 'set_phony_timestamp' of 'panda3d.direct.SmoothMover' objects>"
        'set_pos': None, # (!) real value is "<method 'set_pos' of 'panda3d.direct.SmoothMover' objects>"
        'set_pos_hpr': None, # (!) real value is "<method 'set_pos_hpr' of 'panda3d.direct.SmoothMover' objects>"
        'set_prediction_mode': None, # (!) real value is "<method 'set_prediction_mode' of 'panda3d.direct.SmoothMover' objects>"
        'set_r': None, # (!) real value is "<method 'set_r' of 'panda3d.direct.SmoothMover' objects>"
        'set_reset_velocity_age': None, # (!) real value is "<method 'set_reset_velocity_age' of 'panda3d.direct.SmoothMover' objects>"
        'set_smooth_mode': None, # (!) real value is "<method 'set_smooth_mode' of 'panda3d.direct.SmoothMover' objects>"
        'set_timestamp': None, # (!) real value is "<method 'set_timestamp' of 'panda3d.direct.SmoothMover' objects>"
        'set_x': None, # (!) real value is "<method 'set_x' of 'panda3d.direct.SmoothMover' objects>"
        'set_y': None, # (!) real value is "<method 'set_y' of 'panda3d.direct.SmoothMover' objects>"
        'set_z': None, # (!) real value is "<method 'set_z' of 'panda3d.direct.SmoothMover' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.direct.SmoothMover' objects>"
    }
    PMOff = 0
    PMOn = 1
    PM_off = 0
    PM_on = 1
    SMOff = 0
    SMOn = 1
    SM_off = 0
    SM_on = 1


