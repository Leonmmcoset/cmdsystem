# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

class AnalogNode(DataNode):
    """
    /**
     * This is the primary interface to analog controls like sliders and joysticks
     * associated with a ClientBase.  This creates a node that connects to the
     * named analog device, if it exists, and provides hooks to the user to read
     * the state of any of the sequentially numbered controls associated with that
     * device.
     *
     * Each control can return a value ranging from -1 to 1, reflecting the
     * current position of the control within its total range of motion.
     *
     * The user may choose up to two analog controls to place on the data graph as
     * the two channels of an xy datagram, similarly to the way a mouse places its
     * position data.  In this way, an AnalogNode may be used in place of a mouse.
     */
    """
    def clearOutput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_output(const AnalogNode self, int channel)
        
        /**
         * Removes the output to the data graph associated with the indicated channel.
         * See set_output().
         */
        """
        pass

    def clear_output(self, const_AnalogNode_self, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_output(const AnalogNode self, int channel)
        
        /**
         * Removes the output to the data graph associated with the indicated channel.
         * See set_output().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getControlState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_control_state(AnalogNode self, int index)
        
        /**
         * Returns the current position of indicated analog control identified by its
         * index number, or 0.0 if the control is unknown.  The normal range of a
         * single control is -1.0 to 1.0.
         */
        """
        pass

    def getNumControls(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_controls(AnalogNode self)
        
        /**
         * Returns the number of analog controls known to the AnalogNode.  This number
         * may change as more controls are discovered.
         */
        """
        pass

    def getOutput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_output(AnalogNode self, int channel)
        
        /**
         * Returns the analog control index that is output to the data graph on the
         * indicated channel, or -1 if no control is output on that channel.  See
         * set_output().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_control_state(self, AnalogNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_control_state(AnalogNode self, int index)
        
        /**
         * Returns the current position of indicated analog control identified by its
         * index number, or 0.0 if the control is unknown.  The normal range of a
         * single control is -1.0 to 1.0.
         */
        """
        pass

    def get_num_controls(self, AnalogNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_controls(AnalogNode self)
        
        /**
         * Returns the number of analog controls known to the AnalogNode.  This number
         * may change as more controls are discovered.
         */
        """
        pass

    def get_output(self, AnalogNode_self, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_output(AnalogNode self, int channel)
        
        /**
         * Returns the analog control index that is output to the data graph on the
         * indicated channel, or -1 if no control is output on that channel.  See
         * set_output().
         */
        """
        pass

    def isControlKnown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_control_known(AnalogNode self, int index)
        
        /**
         * Returns true if the state of the indicated analog control is known, or
         * false if we have never heard anything about this particular control.
         */
        """
        pass

    def isOutputFlipped(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_output_flipped(AnalogNode self, int channel)
        
        /**
         * Returns true if the analog control index that is output to the data graph
         * on the indicated channel is flipped.  See set_output().
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(AnalogNode self)
        
        /**
         * Returns true if the AnalogNode is valid and connected to a server, false
         * otherwise.
         */
        """
        pass

    def is_control_known(self, AnalogNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_control_known(AnalogNode self, int index)
        
        /**
         * Returns true if the state of the indicated analog control is known, or
         * false if we have never heard anything about this particular control.
         */
        """
        pass

    def is_output_flipped(self, AnalogNode_self, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_output_flipped(AnalogNode self, int channel)
        
        /**
         * Returns true if the analog control index that is output to the data graph
         * on the indicated channel is flipped.  See set_output().
         */
        """
        pass

    def is_valid(self, AnalogNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(AnalogNode self)
        
        /**
         * Returns true if the AnalogNode is valid and connected to a server, false
         * otherwise.
         */
        """
        pass

    def setOutput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_output(const AnalogNode self, int channel, int index, bool flip)
        
        /**
         * Causes a particular analog control to be placed in the data graph for the
         * indicated channel.  Normally, a mouse uses channels 0 and 1 for the X and Y
         * information, respectively; channels 0, 1, and 2 are available.  If flip is
         * true, the analog control value will be reversed before outputting it.
         */
        """
        pass

    def set_output(self, const_AnalogNode_self, int_channel, int_index, bool_flip): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_output(const AnalogNode self, int channel, int index, bool flip)
        
        /**
         * Causes a particular analog control to be placed in the data graph for the
         * indicated channel.  Normally, a mouse uses channels 0 and 1 for the X and Y
         * information, respectively; channels 0, 1, and 2 are available.  If flip is
         * true, the analog control value will be reversed before outputting it.
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AnalogNode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AnalogNode' objects>"
        '__doc__': '/**\n * This is the primary interface to analog controls like sliders and joysticks\n * associated with a ClientBase.  This creates a node that connects to the\n * named analog device, if it exists, and provides hooks to the user to read\n * the state of any of the sequentially numbered controls associated with that\n * device.\n *\n * Each control can return a value ranging from -1 to 1, reflecting the\n * current position of the control within its total range of motion.\n *\n * The user may choose up to two analog controls to place on the data graph as\n * the two channels of an xy datagram, similarly to the way a mouse places its\n * position data.  In this way, an AnalogNode may be used in place of a mouse.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnalogNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D6A10>'
        'clearOutput': None, # (!) real value is "<method 'clearOutput' of 'panda3d.core.AnalogNode' objects>"
        'clear_output': None, # (!) real value is "<method 'clear_output' of 'panda3d.core.AnalogNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D6A10>)>'
        'getControlState': None, # (!) real value is "<method 'getControlState' of 'panda3d.core.AnalogNode' objects>"
        'getNumControls': None, # (!) real value is "<method 'getNumControls' of 'panda3d.core.AnalogNode' objects>"
        'getOutput': None, # (!) real value is "<method 'getOutput' of 'panda3d.core.AnalogNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D6A10>)>'
        'get_control_state': None, # (!) real value is "<method 'get_control_state' of 'panda3d.core.AnalogNode' objects>"
        'get_num_controls': None, # (!) real value is "<method 'get_num_controls' of 'panda3d.core.AnalogNode' objects>"
        'get_output': None, # (!) real value is "<method 'get_output' of 'panda3d.core.AnalogNode' objects>"
        'isControlKnown': None, # (!) real value is "<method 'isControlKnown' of 'panda3d.core.AnalogNode' objects>"
        'isOutputFlipped': None, # (!) real value is "<method 'isOutputFlipped' of 'panda3d.core.AnalogNode' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.AnalogNode' objects>"
        'is_control_known': None, # (!) real value is "<method 'is_control_known' of 'panda3d.core.AnalogNode' objects>"
        'is_output_flipped': None, # (!) real value is "<method 'is_output_flipped' of 'panda3d.core.AnalogNode' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.AnalogNode' objects>"
        'setOutput': None, # (!) real value is "<method 'setOutput' of 'panda3d.core.AnalogNode' objects>"
        'set_output': None, # (!) real value is "<method 'set_output' of 'panda3d.core.AnalogNode' objects>"
    }


