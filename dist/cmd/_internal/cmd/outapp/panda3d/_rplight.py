# encoding: utf-8
# module panda3d._rplight
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\_rplight.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


# Variables with simple values

Dtool_PyNativeInterface = 1

# functions

def Dtool_BorrowThisReference(*args, **kwargs): # real signature unknown
    """
    Used to borrow 'this' pointer (to, from)
    Assumes no ownership.
    """
    pass

# classes

class GPUCommand(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * @brief Class for storing data to be transferred to the GPU.
     * @details This class can be seen like a packet, to be transferred to the GPU.
     *   It has a command type, which tells the GPU what to do once it recieved this
     *   "packet". It stores a limited amount of floating point components.
     */
    """
    def getUsesIntegerPacking(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uses_integer_packing()
        
        /**
         * @brief Returns whether integers are packed as floats.
         * @details This returns how integer are packed into the data stream. If the
         *   returned value is true, then integers are packed using their binary
         *   representation converted to floating point format. If the returned value
         *   is false, then integers are packed by simply casting them to float,
         *   e.g. val = (float)i;
         * @return The integer representation flag
         */
        """
        pass

    def get_uses_integer_packing(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uses_integer_packing()
        
        /**
         * @brief Returns whether integers are packed as floats.
         * @details This returns how integer are packed into the data stream. If the
         *   returned value is true, then integers are packed using their binary
         *   representation converted to floating point format. If the returned value
         *   is false, then integers are packed by simply casting them to float,
         *   e.g. val = (float)i;
         * @return The integer representation flag
         */
        """
        pass

    def pushFloat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        push_float(const GPUCommand self, float v)
        
        /**
         * @brief Appends a float to the GPUCommand.
         * @details This adds an integer to the back of the GPUCommand. Its used by all
         *   other push_xxx methods, and simply stores the value, then increments the write
         *   pointer. When the amount of floats exceeds the capacity of the GPUCommand,
         *   an error will be printed, and the method returns without doing anything else.
         *
         * @param v The float to append.
         */
        """
        pass

    def pushInt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        push_int(const GPUCommand self, int v)
        
        /**
         * @brief Appends an integer to the GPUCommand.
         * @details This adds an integer to the back of the GPUCommand. Depending on the
         *   setting in convert_int_to_float, this will either just convert the int to a
         *   float by casting it, or just do a bitwise copy.
         *
         * @param v The integer to append.
         */
        """
        pass

    def pushMat3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        push_mat3(const GPUCommand self, const LMatrix3f v)
        
        /**
         * @brief Appends a floating point 3x3 matrix to the GPUCommand.
         * @details This appends a floating point 3x3 matrix to the GPUCommand, by
         *   pushing all components in row-order to the command. This occupies a space of
         *   9 floats.
         *
         * @param v Matrix to append
         */
        """
        pass

    def pushMat4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        push_mat4(const GPUCommand self, const LMatrix4f v)
        
        /**
         * @brief Appends a floating point 4x4 matrix to the GPUCommand.
         * @details This appends a floating point 4x4 matrix to the GPUCommand, by
         *   pushing all components in row-order to the command. This occupies a space of
         *   16 floats.
         *
         * @param v Matrix to append
         */
        """
        pass

    def pushVec3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        push_vec3(const GPUCommand self, const LVecBase3f v)
        push_vec3(const GPUCommand self, const LVecBase3i v)
        
        /**
         * @brief Appends a 3-component floating point vector to the GPUCommand.
         * @details This appends a 3-component floating point vector to the command.
         *   It basically just calls push_float() for every component, in the order
         *   x, y, z, which causes the vector to occupy the space of 3 floats.
         *
         * @param v Int-Vector to append.
         */
        
        /**
         * @brief Appends a 3-component integer vector to the GPUCommand.
         * @details This appends a 3-component integer vector to the command.
         *   It basically just calls push_int() for every component, in the order
         *   x, y, z, which causes the vector to occupy the space of 3 floats.
         *
         * @param v Int-Vector to append.
         */
        """
        pass

    def pushVec4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        push_vec4(const GPUCommand self, const LVecBase4i v)
        push_vec4(const GPUCommand self, const LVecBase4f v)
        
        /**
         * @brief Appends a 4-component floating point vector to the GPUCommand.
         * @details This appends a 4-component floating point vector to the command.
         *   It basically just calls push_float() for every component, in the order
         *   x, y, z, which causes the vector to occupy the space of 3 floats.
         *
         * @param v Int-Vector to append.
         */
        
        /**
         * @brief Appends a 4-component integer vector to the GPUCommand.
         * @details This appends a 4-component integer vector to the command.
         *   It basically just calls push_int() for every component, in the order
         *   x, y, z, w, which causes the vector to occupy the space of 4 floats.
         *
         * @param v Int-Vector to append.
         */
        """
        pass

    def push_float(self, const_GPUCommand_self, float_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        push_float(const GPUCommand self, float v)
        
        /**
         * @brief Appends a float to the GPUCommand.
         * @details This adds an integer to the back of the GPUCommand. Its used by all
         *   other push_xxx methods, and simply stores the value, then increments the write
         *   pointer. When the amount of floats exceeds the capacity of the GPUCommand,
         *   an error will be printed, and the method returns without doing anything else.
         *
         * @param v The float to append.
         */
        """
        pass

    def push_int(self, const_GPUCommand_self, int_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        push_int(const GPUCommand self, int v)
        
        /**
         * @brief Appends an integer to the GPUCommand.
         * @details This adds an integer to the back of the GPUCommand. Depending on the
         *   setting in convert_int_to_float, this will either just convert the int to a
         *   float by casting it, or just do a bitwise copy.
         *
         * @param v The integer to append.
         */
        """
        pass

    def push_mat3(self, const_GPUCommand_self, const_LMatrix3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        push_mat3(const GPUCommand self, const LMatrix3f v)
        
        /**
         * @brief Appends a floating point 3x3 matrix to the GPUCommand.
         * @details This appends a floating point 3x3 matrix to the GPUCommand, by
         *   pushing all components in row-order to the command. This occupies a space of
         *   9 floats.
         *
         * @param v Matrix to append
         */
        """
        pass

    def push_mat4(self, const_GPUCommand_self, const_LMatrix4f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        push_mat4(const GPUCommand self, const LMatrix4f v)
        
        /**
         * @brief Appends a floating point 4x4 matrix to the GPUCommand.
         * @details This appends a floating point 4x4 matrix to the GPUCommand, by
         *   pushing all components in row-order to the command. This occupies a space of
         *   16 floats.
         *
         * @param v Matrix to append
         */
        """
        pass

    def push_vec3(self, const_GPUCommand_self, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        push_vec3(const GPUCommand self, const LVecBase3f v)
        push_vec3(const GPUCommand self, const LVecBase3i v)
        
        /**
         * @brief Appends a 3-component floating point vector to the GPUCommand.
         * @details This appends a 3-component floating point vector to the command.
         *   It basically just calls push_float() for every component, in the order
         *   x, y, z, which causes the vector to occupy the space of 3 floats.
         *
         * @param v Int-Vector to append.
         */
        
        /**
         * @brief Appends a 3-component integer vector to the GPUCommand.
         * @details This appends a 3-component integer vector to the command.
         *   It basically just calls push_int() for every component, in the order
         *   x, y, z, which causes the vector to occupy the space of 3 floats.
         *
         * @param v Int-Vector to append.
         */
        """
        pass

    def push_vec4(self, const_GPUCommand_self, const_LVecBase4i_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        push_vec4(const GPUCommand self, const LVecBase4i v)
        push_vec4(const GPUCommand self, const LVecBase4f v)
        
        /**
         * @brief Appends a 4-component floating point vector to the GPUCommand.
         * @details This appends a 4-component floating point vector to the command.
         *   It basically just calls push_float() for every component, in the order
         *   x, y, z, which causes the vector to occupy the space of 3 floats.
         *
         * @param v Int-Vector to append.
         */
        
        /**
         * @brief Appends a 4-component integer vector to the GPUCommand.
         * @details This appends a 4-component integer vector to the command.
         *   It basically just calls push_int() for every component, in the order
         *   x, y, z, w, which causes the vector to occupy the space of 4 floats.
         *
         * @param v Int-Vector to append.
         */
        """
        pass

    def write(self, GPUCommand_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(GPUCommand self, ostream out)
        
        /**
         * @brief Prints out the GPUCommand to the console
         * @details This method prints the type, size, and data of the GPUCommand to the
         *   console. This helps for debugging the contents of the GPUCommand. Keep
         *   in mind that integers might be shown in their binary float representation,
         *   depending on the setting in the GPUCommand::convert_int_to_float method.
         */
        """
        pass

    def writeTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_to(const GPUCommand self, const PointerToArray dest, int command_index)
        
        /**
         * @brief Writes the GPU command to a given target.
         * @details This method writes all the data of the GPU command to a given target.
         *   The target should be a pointer to memory being big enough to hold the
         *   data. Presumably #dest will be a handle to texture memory.
         *   The command_index controls the offset where the data will be written
         *   to.
         *
         * @param dest Handle to the memory to write the command to
         * @param command_index Offset to write the command to. The command will write
         *   its data to command_index * GPU_COMMAND_ENTRIES. When writing
         *   the GPUCommand in a GPUCommandList, the command_index will
         *   most likely be the index of the command in the list.
         */
        """
        pass

    def write_to(self, const_GPUCommand_self, const_PointerToArray_dest, int_command_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_to(const GPUCommand self, const PointerToArray dest, int command_index)
        
        /**
         * @brief Writes the GPU command to a given target.
         * @details This method writes all the data of the GPU command to a given target.
         *   The target should be a pointer to memory being big enough to hold the
         *   data. Presumably #dest will be a handle to texture memory.
         *   The command_index controls the offset where the data will be written
         *   to.
         *
         * @param dest Handle to the memory to write the command to
         * @param command_index Offset to write the command to. The command will write
         *   its data to command_index * GPU_COMMAND_ENTRIES. When writing
         *   the GPUCommand in a GPUCommandList, the command_index will
         *   most likely be the index of the command in the list.
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    CMDInvalid = 0
    CMDRemoveLight = 2
    CMDRemoveSources = 4
    CMDStoreLight = 1
    CMDStoreSource = 3
    CMD_invalid = 0
    CMD_remove_light = 2
    CMD_remove_sources = 4
    CMD_store_light = 1
    CMD_store_source = 3
    DtoolClassDict = {
        'CMDInvalid': 0,
        'CMDRemoveLight': 2,
        'CMDRemoveSources': 4,
        'CMDStoreLight': 1,
        'CMDStoreSource': 3,
        'CMD_invalid': 0,
        'CMD_remove_light': 2,
        'CMD_remove_sources': 4,
        'CMD_store_light': 1,
        'CMD_store_source': 3,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d._rplight.GPUCommand' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d._rplight.GPUCommand' objects>"
        '__doc__': '/**\n * @brief Class for storing data to be transferred to the GPU.\n * @details This class can be seen like a packet, to be transferred to the GPU.\n *   It has a command type, which tells the GPU what to do once it recieved this\n *   "packet". It stores a limited amount of floating point components.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.GPUCommand' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E4B60>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d._rplight.GPUCommand' objects>"
        'getUsesIntegerPacking': None, # (!) real value is '<staticmethod(<built-in method getUsesIntegerPacking of type object at 0x00007FFDE44E4B60>)>'
        'get_uses_integer_packing': None, # (!) real value is '<staticmethod(<built-in method get_uses_integer_packing of type object at 0x00007FFDE44E4B60>)>'
        'pushFloat': None, # (!) real value is "<method 'pushFloat' of 'panda3d._rplight.GPUCommand' objects>"
        'pushInt': None, # (!) real value is "<method 'pushInt' of 'panda3d._rplight.GPUCommand' objects>"
        'pushMat3': None, # (!) real value is "<method 'pushMat3' of 'panda3d._rplight.GPUCommand' objects>"
        'pushMat4': None, # (!) real value is "<method 'pushMat4' of 'panda3d._rplight.GPUCommand' objects>"
        'pushVec3': None, # (!) real value is "<method 'pushVec3' of 'panda3d._rplight.GPUCommand' objects>"
        'pushVec4': None, # (!) real value is "<method 'pushVec4' of 'panda3d._rplight.GPUCommand' objects>"
        'push_float': None, # (!) real value is "<method 'push_float' of 'panda3d._rplight.GPUCommand' objects>"
        'push_int': None, # (!) real value is "<method 'push_int' of 'panda3d._rplight.GPUCommand' objects>"
        'push_mat3': None, # (!) real value is "<method 'push_mat3' of 'panda3d._rplight.GPUCommand' objects>"
        'push_mat4': None, # (!) real value is "<method 'push_mat4' of 'panda3d._rplight.GPUCommand' objects>"
        'push_vec3': None, # (!) real value is "<method 'push_vec3' of 'panda3d._rplight.GPUCommand' objects>"
        'push_vec4': None, # (!) real value is "<method 'push_vec4' of 'panda3d._rplight.GPUCommand' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d._rplight.GPUCommand' objects>"
        'writeTo': None, # (!) real value is "<method 'writeTo' of 'panda3d._rplight.GPUCommand' objects>"
        'write_to': None, # (!) real value is "<method 'write_to' of 'panda3d._rplight.GPUCommand' objects>"
    }


class GPUCommandList(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * @brief Class to store a list of commands.
     * @details This is a class to store a list of GPUCommands. It provides
     *   functionality to only provide the a given amount of commands at one time.
     */
    """
    def addCommand(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_command(const GPUCommandList self, const GPUCommand cmd)
        
        /**
         * @brief Pushes a GPUCommand to the command list.
         * @details This adds a new GPUCommand to the list of commands to be processed.
         *
         * @param cmd The command to add
         */
        """
        pass

    def add_command(self, const_GPUCommandList_self, const_GPUCommand_cmd): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_command(const GPUCommandList self, const GPUCommand cmd)
        
        /**
         * @brief Pushes a GPUCommand to the command list.
         * @details This adds a new GPUCommand to the list of commands to be processed.
         *
         * @param cmd The command to add
         */
        """
        pass

    def getNumCommands(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_commands(const GPUCommandList self)
        
        /**
         * @brief Returns the number of commands in this list.
         * @details This returns the amount of commands which are currently stored in this
         *   list, and are waiting to get processed.
         * @return Amount of commands
         */
        """
        pass

    def get_num_commands(self, const_GPUCommandList_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_commands(const GPUCommandList self)
        
        /**
         * @brief Returns the number of commands in this list.
         * @details This returns the amount of commands which are currently stored in this
         *   list, and are waiting to get processed.
         * @return Amount of commands
         */
        """
        pass

    def writeCommandsTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_commands_to(const GPUCommandList self, const PointerToArray dest, int limit)
        
        /**
         * @brief Writes the first n-commands to a destination.
         * @details This takes the first #limit commands, and writes them to the
         *   destination using GPUCommand::write_to. See GPUCommand::write_to for
         *   further information about #dest. The limit controls after how much
         *   commands the processing will be stopped. All commands which got processed
         *   will get removed from the list.
         *
         * @param dest Destination to write to, see GPUCommand::write_to
         * @param limit Maximum amount of commands to process
         *
         * @return Amount of commands processed, between 0 and #limit.
         */
        """
        pass

    def write_commands_to(self, const_GPUCommandList_self, const_PointerToArray_dest, int_limit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_commands_to(const GPUCommandList self, const PointerToArray dest, int limit)
        
        /**
         * @brief Writes the first n-commands to a destination.
         * @details This takes the first #limit commands, and writes them to the
         *   destination using GPUCommand::write_to. See GPUCommand::write_to for
         *   further information about #dest. The limit controls after how much
         *   commands the processing will be stopped. All commands which got processed
         *   will get removed from the list.
         *
         * @param dest Destination to write to, see GPUCommand::write_to
         * @param limit Maximum amount of commands to process
         *
         * @return Amount of commands processed, between 0 and #limit.
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

    num_commands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d._rplight.GPUCommandList' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d._rplight.GPUCommandList' objects>"
        '__doc__': '/**\n * @brief Class to store a list of commands.\n * @details This is a class to store a list of GPUCommands. It provides\n *   functionality to only provide the a given amount of commands at one time.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.GPUCommandList' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E4D30>'
        'addCommand': None, # (!) real value is "<method 'addCommand' of 'panda3d._rplight.GPUCommandList' objects>"
        'add_command': None, # (!) real value is "<method 'add_command' of 'panda3d._rplight.GPUCommandList' objects>"
        'getNumCommands': None, # (!) real value is "<method 'getNumCommands' of 'panda3d._rplight.GPUCommandList' objects>"
        'get_num_commands': None, # (!) real value is "<method 'get_num_commands' of 'panda3d._rplight.GPUCommandList' objects>"
        'num_commands': None, # (!) real value is "<attribute 'num_commands' of 'panda3d._rplight.GPUCommandList' objects>"
        'writeCommandsTo': None, # (!) real value is "<method 'writeCommandsTo' of 'panda3d._rplight.GPUCommandList' objects>"
        'write_commands_to': None, # (!) real value is "<method 'write_commands_to' of 'panda3d._rplight.GPUCommandList' objects>"
    }


class IESDataset(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * @brief This class generates a LUT from IES data.
     * @details This class is used by the IESLoader to generate a LUT texture which
     *   is used in the shaders to perform IES lighting. It takes a set of vertical
     *   and horizontal angles, as well as a set of candela values, which then are
     *   lineary interpolated onto a 2D LUT Texture.
     */
    """
    def generateDatasetTextureInto(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_dataset_texture_into(IESDataset self, Texture dest_tex, int z)
        
        /**
         * @brief Generates the IES LUT
         * @details This generates the LUT into a given dataset texture. The x-axis
         *   referes to the vertical_angle, whereas the y-axis refers to the
         *   horizontal angle.
         *
         * @param dest_tex Texture to write the LUT into
         * @param z Layer to write the LUT into, in case the texture is a 3D Texture or
         *   2D Texture Array.
         */
        """
        pass

    def generate_dataset_texture_into(self, IESDataset_self, Texture_dest_tex, int_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_dataset_texture_into(IESDataset self, Texture dest_tex, int z)
        
        /**
         * @brief Generates the IES LUT
         * @details This generates the LUT into a given dataset texture. The x-axis
         *   referes to the vertical_angle, whereas the y-axis refers to the
         *   horizontal angle.
         *
         * @param dest_tex Texture to write the LUT into
         * @param z Layer to write the LUT into, in case the texture is a 3D Texture or
         *   2D Texture Array.
         */
        """
        pass

    def setCandelaValues(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_candela_values(const IESDataset self, const PointerToArray candela_values)
        
        /**
         * @brief Sets the candela values.
         * @details This sets the candela values of the dataset. They should be an
         *   interleaved 2D array with the dimensions vertical_angles x horizontal_angles.
         *   They also should be normalized by dividing by the maximum entry.
         * @param candela_values Interleaved 2D-vector of candela values.
         */
        """
        pass

    def setHorizontalAngles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_horizontal_angles(const IESDataset self, const PointerToArray horizontal_angles)
        
        /**
         * @brief Sets the horizontal angles of the dataset.
         * @details This sets the list of horizontal angles of the dataset.
         *
         * @param horizontal_angles Vector of all horizontal angles.
         */
        """
        pass

    def setVerticalAngles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertical_angles(const IESDataset self, const PointerToArray vertical_angles)
        
        /**
         * @brief Sets the vertical angles of the dataset.
         * @details This sets the list of vertical angles of the dataset.
         *
         * @param vertical_angles Vector of all vertical angles.
         */
        """
        pass

    def set_candela_values(self, const_IESDataset_self, const_PointerToArray_candela_values): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_candela_values(const IESDataset self, const PointerToArray candela_values)
        
        /**
         * @brief Sets the candela values.
         * @details This sets the candela values of the dataset. They should be an
         *   interleaved 2D array with the dimensions vertical_angles x horizontal_angles.
         *   They also should be normalized by dividing by the maximum entry.
         * @param candela_values Interleaved 2D-vector of candela values.
         */
        """
        pass

    def set_horizontal_angles(self, const_IESDataset_self, const_PointerToArray_horizontal_angles): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_horizontal_angles(const IESDataset self, const PointerToArray horizontal_angles)
        
        /**
         * @brief Sets the horizontal angles of the dataset.
         * @details This sets the list of horizontal angles of the dataset.
         *
         * @param horizontal_angles Vector of all horizontal angles.
         */
        """
        pass

    def set_vertical_angles(self, const_IESDataset_self, const_PointerToArray_vertical_angles): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertical_angles(const IESDataset self, const PointerToArray vertical_angles)
        
        /**
         * @brief Sets the vertical angles of the dataset.
         * @details This sets the list of vertical angles of the dataset.
         *
         * @param vertical_angles Vector of all vertical angles.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d._rplight.IESDataset' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d._rplight.IESDataset' objects>"
        '__doc__': '/**\n * @brief This class generates a LUT from IES data.\n * @details This class is used by the IESLoader to generate a LUT texture which\n *   is used in the shaders to perform IES lighting. It takes a set of vertical\n *   and horizontal angles, as well as a set of candela values, which then are\n *   lineary interpolated onto a 2D LUT Texture.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.IESDataset' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E4F00>'
        'generateDatasetTextureInto': None, # (!) real value is "<method 'generateDatasetTextureInto' of 'panda3d._rplight.IESDataset' objects>"
        'generate_dataset_texture_into': None, # (!) real value is "<method 'generate_dataset_texture_into' of 'panda3d._rplight.IESDataset' objects>"
        'setCandelaValues': None, # (!) real value is "<method 'setCandelaValues' of 'panda3d._rplight.IESDataset' objects>"
        'setHorizontalAngles': None, # (!) real value is "<method 'setHorizontalAngles' of 'panda3d._rplight.IESDataset' objects>"
        'setVerticalAngles': None, # (!) real value is "<method 'setVerticalAngles' of 'panda3d._rplight.IESDataset' objects>"
        'set_candela_values': None, # (!) real value is "<method 'set_candela_values' of 'panda3d._rplight.IESDataset' objects>"
        'set_horizontal_angles': None, # (!) real value is "<method 'set_horizontal_angles' of 'panda3d._rplight.IESDataset' objects>"
        'set_vertical_angles': None, # (!) real value is "<method 'set_vertical_angles' of 'panda3d._rplight.IESDataset' objects>"
    }


class InternalLightManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * @brief Internal class used for handling lights and shadows.
     * @details This is the internal class used by the pipeline to handle all
     *   lights and shadows. It stores references to the lights, manages handling
     *   the light and shadow slots, and also communicates with the GPU with the
     *   GPUCommandQueue to store light and shadow source data.
     */
    """
    def addLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_light(const InternalLightManager self, RPLight light)
        
        /**
         * @brief Adds a new light.
         * @details This adds a new light to the list of lights. This will throw an
         *   error and return if the light is already attached. You may only call
         *   this after the ShadowManager was already set.
         *
         *   While the light is attached, the light manager keeps a reference to it, so
         *   the light does not get destructed.
         *
         *   This also setups the shadows on the light, in case shadows are enabled.
         *   While a light is attached, you can not change whether it casts shadows or not.
         *   To do so, detach the light, change the setting, and re-add the light.
         *
         *   In case no free light slot is available, an error will be printed and no
         *   action will be performed.
         *
         *   If no shadow manager was set, an assertion will be triggered.
         *
         * @param light The light to add.
         */
        """
        pass

    def add_light(self, const_InternalLightManager_self, RPLight_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_light(const InternalLightManager self, RPLight light)
        
        /**
         * @brief Adds a new light.
         * @details This adds a new light to the list of lights. This will throw an
         *   error and return if the light is already attached. You may only call
         *   this after the ShadowManager was already set.
         *
         *   While the light is attached, the light manager keeps a reference to it, so
         *   the light does not get destructed.
         *
         *   This also setups the shadows on the light, in case shadows are enabled.
         *   While a light is attached, you can not change whether it casts shadows or not.
         *   To do so, detach the light, change the setting, and re-add the light.
         *
         *   In case no free light slot is available, an error will be printed and no
         *   action will be performed.
         *
         *   If no shadow manager was set, an assertion will be triggered.
         *
         * @param light The light to add.
         */
        """
        pass

    def getMaxLightIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_light_index(InternalLightManager self)
        
        /**
         * @brief Returns the maximum light index
         * @details This returns the maximum light index (also called slot). Any lights
         *   after that slot are guaranteed to be zero-lights. This is useful when
         *   iterating over the list of lights, because iteration can be stopped when
         *   the maximum light index is reached.
         *
         *   The maximum light index points to the last slot which is used. If no lights
         *   are attached, -1 is returned. If one light is attached at slot 0, the index
         *   is 0, if two are attached at the slots 0 and 1, the index is 1, and so on.
         *
         *   If, for example, two lights are attached at the slots 2 and 5, then the
         *   index will be 5. Keep in mind that the max-index is not an indicator for
         *   how many lights are attached. Also, zero lights still may occur when iterating
         *   over the light lists
         *
         * @return Maximum light index
         */
        """
        pass

    def getNumLights(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_lights(InternalLightManager self)
        
        /**
         * @brief Returns the amount of stored lights.
         * @details This returns the amount of stored lights. This behaves unlike
         *   InternalLightManager::get_max_light_index, and instead returns the true
         *   amount of lights, which is completely unrelated to the amount of used slots.
         *
         * @return Amount of stored lights
         */
        """
        pass

    def getNumShadowSources(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_shadow_sources(InternalLightManager self)
        
        /**
         * @brief Returns the amount of shadow sources.
         * @details This returns the total amount of stored shadow sources. This does
         *   not denote the amount of updated sources, but instead takes into account
         *   all sources, even those out of frustum.
         * @return Amount of shadow sources.
         */
        """
        pass

    def getShadowManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shadow_manager(InternalLightManager self)
        
        /**
         * @brief Returns the internal used ShadowManager
         * @details This returns a handle to the internally used shadow manager
         * @return Shadow manager
         */
        """
        pass

    def get_max_light_index(self, InternalLightManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_light_index(InternalLightManager self)
        
        /**
         * @brief Returns the maximum light index
         * @details This returns the maximum light index (also called slot). Any lights
         *   after that slot are guaranteed to be zero-lights. This is useful when
         *   iterating over the list of lights, because iteration can be stopped when
         *   the maximum light index is reached.
         *
         *   The maximum light index points to the last slot which is used. If no lights
         *   are attached, -1 is returned. If one light is attached at slot 0, the index
         *   is 0, if two are attached at the slots 0 and 1, the index is 1, and so on.
         *
         *   If, for example, two lights are attached at the slots 2 and 5, then the
         *   index will be 5. Keep in mind that the max-index is not an indicator for
         *   how many lights are attached. Also, zero lights still may occur when iterating
         *   over the light lists
         *
         * @return Maximum light index
         */
        """
        pass

    def get_num_lights(self, InternalLightManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_lights(InternalLightManager self)
        
        /**
         * @brief Returns the amount of stored lights.
         * @details This returns the amount of stored lights. This behaves unlike
         *   InternalLightManager::get_max_light_index, and instead returns the true
         *   amount of lights, which is completely unrelated to the amount of used slots.
         *
         * @return Amount of stored lights
         */
        """
        pass

    def get_num_shadow_sources(self, InternalLightManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_shadow_sources(InternalLightManager self)
        
        /**
         * @brief Returns the amount of shadow sources.
         * @details This returns the total amount of stored shadow sources. This does
         *   not denote the amount of updated sources, but instead takes into account
         *   all sources, even those out of frustum.
         * @return Amount of shadow sources.
         */
        """
        pass

    def get_shadow_manager(self, InternalLightManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shadow_manager(InternalLightManager self)
        
        /**
         * @brief Returns the internal used ShadowManager
         * @details This returns a handle to the internally used shadow manager
         * @return Shadow manager
         */
        """
        pass

    def removeLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_light(const InternalLightManager self, RPLight light)
        
        /**
         * @brief Removes a light
         * @details This detaches a light. This prevents it from being rendered, and also
         *   cleans up all resources used by that light. If no reference is kept on the
         *   python side, the light will also get destructed.
         *
         *   If the light was not previously attached with InternalLightManager::add_light,
         *   an error will be triggered and nothing happens.
         *
         *   In case the light was set to cast shadows, all shadow sources are cleaned
         *   up, and their regions in the shadow atlas are freed.
         *
         *   All resources used by the light in the light and shadow storage are also
         *   cleaned up, by emitting cleanup GPUCommands.
         *
         *   If no shadow manager was set, an assertion will be triggered.
         *
         * @param light [description]
         */
        """
        pass

    def remove_light(self, const_InternalLightManager_self, RPLight_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_light(const InternalLightManager self, RPLight light)
        
        /**
         * @brief Removes a light
         * @details This detaches a light. This prevents it from being rendered, and also
         *   cleans up all resources used by that light. If no reference is kept on the
         *   python side, the light will also get destructed.
         *
         *   If the light was not previously attached with InternalLightManager::add_light,
         *   an error will be triggered and nothing happens.
         *
         *   In case the light was set to cast shadows, all shadow sources are cleaned
         *   up, and their regions in the shadow atlas are freed.
         *
         *   All resources used by the light in the light and shadow storage are also
         *   cleaned up, by emitting cleanup GPUCommands.
         *
         *   If no shadow manager was set, an assertion will be triggered.
         *
         * @param light [description]
         */
        """
        pass

    def setCameraPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_camera_pos(const InternalLightManager self, const LPoint3f pos)
        
        /**
         * @brief Sets the camera position
         * @details This sets the camera position, which will be used to determine which
         *   shadow sources have to get updated
         *
         * @param mat View projection mat
         */
        """
        pass

    def setCommandList(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_command_list(const InternalLightManager self, GPUCommandList cmd_list)
        
        /**
         * @brief Sets a handle to the command list
         * @details This sets a handle to the global GPUCommandList. This is required to
         *   emit GPUCommands, which are used for attaching and detaching lights, as well
         *   as shadow source updates.
         *
         *   The cmd_list should be a handle to a GPUCommandList handle, and will be
         *   stored somewhere on the python side most likely. The light manager does not
         *   keep a reference to it, so the python side should make sure to keep one.
         *
         *   Be sure to call this before the InternalLightManager::update() method is
         *   called, otherwise an assertion will get triggered.
         *
         * @param cmd_list The GPUCommandList instance
         */
        """
        pass

    def setShadowManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shadow_manager(const InternalLightManager self, ShadowManager mgr)
        
        /**
         * @brief Sets the handle to the shadow manager
         * @details This sets the handle to the global shadow manager. It is usually
         *   constructed on the python side, so we need to get a handle to it.
         *
         *   The manager should be a handle to a ShadowManager instance, and will be
         *   stored somewhere on the python side most likely. The light manager does not
         *   keep a reference to it, so the python side should make sure to keep one.
         *
         *   Be sure to call this before the InternalLightManager::update() method is
         *   called, otherwise an assertion will get triggered.
         *
         * @param mgr The ShadowManager instance
         */
        """
        pass

    def setShadowUpdateDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shadow_update_distance(const InternalLightManager self, float dist)
        
        /**
         * @brief Sets the maximum shadow update distance
         * @details This controls the maximum distance until which shadows are updated.
         *   If a shadow source is past that distance, it is ignored and no longer recieves
         *   updates until it is in range again
         *
         * @param dist Distance in world space units
         */
        """
        pass

    def set_camera_pos(self, const_InternalLightManager_self, const_LPoint3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_camera_pos(const InternalLightManager self, const LPoint3f pos)
        
        /**
         * @brief Sets the camera position
         * @details This sets the camera position, which will be used to determine which
         *   shadow sources have to get updated
         *
         * @param mat View projection mat
         */
        """
        pass

    def set_command_list(self, const_InternalLightManager_self, GPUCommandList_cmd_list): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_command_list(const InternalLightManager self, GPUCommandList cmd_list)
        
        /**
         * @brief Sets a handle to the command list
         * @details This sets a handle to the global GPUCommandList. This is required to
         *   emit GPUCommands, which are used for attaching and detaching lights, as well
         *   as shadow source updates.
         *
         *   The cmd_list should be a handle to a GPUCommandList handle, and will be
         *   stored somewhere on the python side most likely. The light manager does not
         *   keep a reference to it, so the python side should make sure to keep one.
         *
         *   Be sure to call this before the InternalLightManager::update() method is
         *   called, otherwise an assertion will get triggered.
         *
         * @param cmd_list The GPUCommandList instance
         */
        """
        pass

    def set_shadow_manager(self, const_InternalLightManager_self, ShadowManager_mgr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shadow_manager(const InternalLightManager self, ShadowManager mgr)
        
        /**
         * @brief Sets the handle to the shadow manager
         * @details This sets the handle to the global shadow manager. It is usually
         *   constructed on the python side, so we need to get a handle to it.
         *
         *   The manager should be a handle to a ShadowManager instance, and will be
         *   stored somewhere on the python side most likely. The light manager does not
         *   keep a reference to it, so the python side should make sure to keep one.
         *
         *   Be sure to call this before the InternalLightManager::update() method is
         *   called, otherwise an assertion will get triggered.
         *
         * @param mgr The ShadowManager instance
         */
        """
        pass

    def set_shadow_update_distance(self, const_InternalLightManager_self, float_dist): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shadow_update_distance(const InternalLightManager self, float dist)
        
        /**
         * @brief Sets the maximum shadow update distance
         * @details This controls the maximum distance until which shadows are updated.
         *   If a shadow source is past that distance, it is ignored and no longer recieves
         *   updates until it is in range again
         *
         * @param dist Distance in world space units
         */
        """
        pass

    def update(self, const_InternalLightManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const InternalLightManager self)
        
        /**
         * @brief Main update method
         * @details This is the main update method of the InternalLightManager. It
         *   processes all lights and shadow sources, updates them, and notifies the
         *   GPU about it. This should be called on a per-frame basis.
         *
         *   If the InternalLightManager was not initialized yet, an assertion is thrown.
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

    max_light_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_lights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_shadow_sources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shadow_manager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d._rplight.InternalLightManager' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d._rplight.InternalLightManager' objects>"
        '__doc__': '/**\n * @brief Internal class used for handling lights and shadows.\n * @details This is the internal class used by the pipeline to handle all\n *   lights and shadows. It stores references to the lights, manages handling\n *   the light and shadow slots, and also communicates with the GPU with the\n *   GPUCommandQueue to store light and shadow source data.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.InternalLightManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E5810>'
        'addLight': None, # (!) real value is "<method 'addLight' of 'panda3d._rplight.InternalLightManager' objects>"
        'add_light': None, # (!) real value is "<method 'add_light' of 'panda3d._rplight.InternalLightManager' objects>"
        'getMaxLightIndex': None, # (!) real value is "<method 'getMaxLightIndex' of 'panda3d._rplight.InternalLightManager' objects>"
        'getNumLights': None, # (!) real value is "<method 'getNumLights' of 'panda3d._rplight.InternalLightManager' objects>"
        'getNumShadowSources': None, # (!) real value is "<method 'getNumShadowSources' of 'panda3d._rplight.InternalLightManager' objects>"
        'getShadowManager': None, # (!) real value is "<method 'getShadowManager' of 'panda3d._rplight.InternalLightManager' objects>"
        'get_max_light_index': None, # (!) real value is "<method 'get_max_light_index' of 'panda3d._rplight.InternalLightManager' objects>"
        'get_num_lights': None, # (!) real value is "<method 'get_num_lights' of 'panda3d._rplight.InternalLightManager' objects>"
        'get_num_shadow_sources': None, # (!) real value is "<method 'get_num_shadow_sources' of 'panda3d._rplight.InternalLightManager' objects>"
        'get_shadow_manager': None, # (!) real value is "<method 'get_shadow_manager' of 'panda3d._rplight.InternalLightManager' objects>"
        'max_light_index': None, # (!) real value is "<attribute 'max_light_index' of 'panda3d._rplight.InternalLightManager' objects>"
        'num_lights': None, # (!) real value is "<attribute 'num_lights' of 'panda3d._rplight.InternalLightManager' objects>"
        'num_shadow_sources': None, # (!) real value is "<attribute 'num_shadow_sources' of 'panda3d._rplight.InternalLightManager' objects>"
        'removeLight': None, # (!) real value is "<method 'removeLight' of 'panda3d._rplight.InternalLightManager' objects>"
        'remove_light': None, # (!) real value is "<method 'remove_light' of 'panda3d._rplight.InternalLightManager' objects>"
        'setCameraPos': None, # (!) real value is "<method 'setCameraPos' of 'panda3d._rplight.InternalLightManager' objects>"
        'setCommandList': None, # (!) real value is "<method 'setCommandList' of 'panda3d._rplight.InternalLightManager' objects>"
        'setShadowManager': None, # (!) real value is "<method 'setShadowManager' of 'panda3d._rplight.InternalLightManager' objects>"
        'setShadowUpdateDistance': None, # (!) real value is "<method 'setShadowUpdateDistance' of 'panda3d._rplight.InternalLightManager' objects>"
        'set_camera_pos': None, # (!) real value is "<method 'set_camera_pos' of 'panda3d._rplight.InternalLightManager' objects>"
        'set_command_list': None, # (!) real value is "<method 'set_command_list' of 'panda3d._rplight.InternalLightManager' objects>"
        'set_shadow_manager': None, # (!) real value is "<method 'set_shadow_manager' of 'panda3d._rplight.InternalLightManager' objects>"
        'set_shadow_update_distance': None, # (!) real value is "<method 'set_shadow_update_distance' of 'panda3d._rplight.InternalLightManager' objects>"
        'shadow_manager': None, # (!) real value is "<attribute 'shadow_manager' of 'panda3d._rplight.InternalLightManager' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d._rplight.InternalLightManager' objects>"
    }


class PSSMCameraRig(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * @brief Main class used for handling PSSM
     * @details This is the main class for supporting PSSM, it is used by the PSSM
     *   plugin to compute the position of the splits.
     *
     *   It supports handling a varying amount of cameras, and fitting those cameras
     *   into the main camera frustum, to render distant shadows. It also supports
     *   various optimizations for fitting the frustum, e.g. rotating the sources
     *   to get a better coverage.
     *
     *   It also provides methods to get arrays of data about the used cameras
     *   view-projection matrices and their near and far plane, which is required for
     *   processing the data in the shadow sampling shader.
     *
     *   In this class, there is often referred to "Splits" or also called "Cascades".
     *   These denote the different cameras which are used to split the frustum,
     *   and are a common term related to the PSSM algorithm.
     *
     *   To understand the functionality of this class, a detailed knowledge of the
     *   PSSM algorithm is helpful.
     */
    """
    def getCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_camera(const PSSMCameraRig self, int index)
        
        /**
         * @brief Returns the n-th camera
         * @details This returns the n-th camera of the camera rig, which can be used
         *   for various stuff like showing its frustum, passing it as a shader input,
         *   and so on.
         *
         *   The first camera is the camera which is the camera of the first split,
         *   which is the split closest to the camera. All cameras follow in descending
         *   order until to the last camera, which is the split furthest away from the
         *   camera.
         *
         *   If an invalid index is passed, an assertion is thrown.
         *
         * @param index Index of the camera.
         * @return [description]
         */
        """
        pass

    def getMvpArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mvp_array(const PSSMCameraRig self)
        
        /**
         * @brief Returns a handle to the MVP array
         * @details This returns a handle to the array of view-projection matrices
         *   of the different splits. This can be used for computing shadows. The array
         *   is a PTALMatrix4 and thus can be directly bound to a shader.
         *
         * @return view-projection matrix array
         */
        """
        pass

    def getNearfarArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_nearfar_array(const PSSMCameraRig self)
        
        /**
         * @brief Returns a handle to the near and far planes array
         * @details This returns a handle to the near and far plane array. Each split
         *   has an entry in the array, whereas the x component of the vecto denotes the
         *   near plane, and the y component denotes the far plane of the split.
         *
         *   This is required because the near and far planes of the splits change
         *   constantly. To access them in a shader, the shader needs access to the
         *   array.
         *
         * @return Array of near and far planes
         */
        """
        pass

    def get_camera(self, const_PSSMCameraRig_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_camera(const PSSMCameraRig self, int index)
        
        /**
         * @brief Returns the n-th camera
         * @details This returns the n-th camera of the camera rig, which can be used
         *   for various stuff like showing its frustum, passing it as a shader input,
         *   and so on.
         *
         *   The first camera is the camera which is the camera of the first split,
         *   which is the split closest to the camera. All cameras follow in descending
         *   order until to the last camera, which is the split furthest away from the
         *   camera.
         *
         *   If an invalid index is passed, an assertion is thrown.
         *
         * @param index Index of the camera.
         * @return [description]
         */
        """
        pass

    def get_mvp_array(self, const_PSSMCameraRig_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mvp_array(const PSSMCameraRig self)
        
        /**
         * @brief Returns a handle to the MVP array
         * @details This returns a handle to the array of view-projection matrices
         *   of the different splits. This can be used for computing shadows. The array
         *   is a PTALMatrix4 and thus can be directly bound to a shader.
         *
         * @return view-projection matrix array
         */
        """
        pass

    def get_nearfar_array(self, const_PSSMCameraRig_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_nearfar_array(const PSSMCameraRig self)
        
        /**
         * @brief Returns a handle to the near and far planes array
         * @details This returns a handle to the near and far plane array. Each split
         *   has an entry in the array, whereas the x component of the vecto denotes the
         *   near plane, and the y component denotes the far plane of the split.
         *
         *   This is required because the near and far planes of the splits change
         *   constantly. To access them in a shader, the shader needs access to the
         *   array.
         *
         * @return Array of near and far planes
         */
        """
        pass

    def reparentTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reparent_to(const PSSMCameraRig self, NodePath parent)
        
        /**
         * @brief Reparents the camera rig
         * @details This reparents all cameras to the given parent. Usually the parent
         *   will be ShowBase.render. The parent should be the same node where the
         *   main camera is located in, too.
         *
         *   If an empty parrent is passed, an assertion will get triggered.
         *
         * @param parent Parent node path
         */
        """
        pass

    def reparent_to(self, const_PSSMCameraRig_self, NodePath_parent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reparent_to(const PSSMCameraRig self, NodePath parent)
        
        /**
         * @brief Reparents the camera rig
         * @details This reparents all cameras to the given parent. Usually the parent
         *   will be ShowBase.render. The parent should be the same node where the
         *   main camera is located in, too.
         *
         *   If an empty parrent is passed, an assertion will get triggered.
         *
         * @param parent Parent node path
         */
        """
        pass

    def resetFilmSizeCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_film_size_cache(const PSSMCameraRig self)
        
        /**
         * @brief Resets the film size cache
         * @details In case PSSMCameraRig::set_use_fixed_film_size is used, this resets
         *   the film size cache. This might lead to a small "jump" in the shadows,
         *   because the film size changes, however it leads to a better shadow distribution.
         *
         *   This is the case because when using a fixed film size, the cache will get
         *   bigger and bigger, whenever the camera moves to a grazing angle. However,
         *   when moving back to a normal angle, the film size cache still stores this
         *   big angle, and thus the splits will have a much bigger film size than actualy
         *   required. To prevent this, call this method once in a while, so an optimal
         *   distribution is ensured.
         */
        """
        pass

    def reset_film_size_cache(self, const_PSSMCameraRig_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_film_size_cache(const PSSMCameraRig self)
        
        /**
         * @brief Resets the film size cache
         * @details In case PSSMCameraRig::set_use_fixed_film_size is used, this resets
         *   the film size cache. This might lead to a small "jump" in the shadows,
         *   because the film size changes, however it leads to a better shadow distribution.
         *
         *   This is the case because when using a fixed film size, the cache will get
         *   bigger and bigger, whenever the camera moves to a grazing angle. However,
         *   when moving back to a normal angle, the film size cache still stores this
         *   big angle, and thus the splits will have a much bigger film size than actualy
         *   required. To prevent this, call this method once in a while, so an optimal
         *   distribution is ensured.
         */
        """
        pass

    def setBorderBias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_border_bias(const PSSMCameraRig self, float bias)
        
        /**
         * @brief Sets the border bias for each split
         * @details This sets the border bias for every split. This increases each
         *   splits frustum by multiplying it by (1 + bias), and helps reducing artifacts
         *   at the borders of the splits. Artifacts can occur when the bias is too low,
         *   because then the filtering will go over the bounds of the split, producing
         *   invalid results.
         *
         *   If the bias is below zero, an assertion is thrown.
         *
         * @param bias Border bias
         */
        """
        pass

    def setLogarithmicFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_logarithmic_factor(const PSSMCameraRig self, float factor)
        
        /**
         * @brief Sets the logarithmic factor
         * @details This sets the logarithmic factor, which is the core of the algorithm.
         *   PSSM splits the camera frustum based on a linear and a logarithmic factor.
         *   While a linear factor provides a good distribution, it often is not applicable
         *   for wider distances. A logarithmic distribution provides a better distribution
         *   at distance, but suffers from splitting in the near areas.
         *
         *   The logarithmic factor mixes the logarithmic and linear split distribution,
         *   to get the best of both. A greater factor will make the distribution more
         *   logarithmic, while a smaller factor will make it more linear.
         *
         *   If the factor is below zero, an ssertion is triggered.
         *
         * @param factor The logarithmic factor
         */
        """
        pass

    def setPssmDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pssm_distance(const PSSMCameraRig self, float distance)
        
        /**
         * @brief Sets the maximum pssm distance.
         * @details This sets the maximum distance in world space until which shadows
         *   are rendered. After this distance, no shadows will be rendered.
         *
         *   If the distance is below zero, an assertion is triggered.
         *
         * @param distance Maximum distance in world space
         */
        """
        pass

    def setResolution(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_resolution(const PSSMCameraRig self, int resolution)
        
        /**
         * @brief Sets the resolution of each split
         * @details This sets the resolution of each split. Currently it is equal for
         *   each split. This is required when using PSSMCameraRig::set_use_stable_csm,
         *   to compute how bix a texel is.
         *
         *   It has to match the y-resolution of the pssm shadow map. If an invalid
         *   resolution is triggered, an assertion is thrown.
         *
         * @param resolution The resolution of each split.
         */
        """
        pass

    def setSunDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sun_distance(const PSSMCameraRig self, float distance)
        
        /**
         * @brief Sets the suns distance
         * @details This sets the distance the cameras will have from the cameras frustum.
         *   This prevents far objects from having no shadows, which can occur when these
         *   objects are between the cameras frustum and the sun, but not inside of the
         *   cameras frustum. Setting the sun distance high enough will move the cameras
         *   away from the camera frustum, being able to cover those distant objects too.
         *
         *   If the sun distance is set too high, artifacts will occur due to the reduced
         *   range of depth. If a value below zero is passed, an assertion will get
         *   triggered.
         *
         * @param distance The sun distance
         */
        """
        pass

    def setUseFixedFilmSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_use_fixed_film_size(const PSSMCameraRig self, bool flag)
        
        /**
         * @brief Sets whether to use a fixed film size
         * @details This controls if a fixed film size should be used. This will cause
         *   the camera rig to cache the current film size, and only change it in case
         *   it gets too small. This provides less flickering when moving, because the
         *   film size will stay roughly constant. However, to prevent the cached film
         *   size getting too big, one should call PSSMCameraRig::reset_film_size
         *   once in a while, otherwise there might be a lot of wasted space.
         *
         * @param flag Whether to use a fixed film size
         */
        """
        pass

    def setUseStableCsm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_use_stable_csm(const PSSMCameraRig self, bool flag)
        
        /**
         * @brief Sets whether to use stable CSM snapping.
         * @details This option controls if stable CSM snapping should be used. When the
         *   option is enabled, all splits will snap to their texels, so that when moving,
         *   no flickering will occur. However, this only works when the splits do not
         *   change their film size, rotation and angle.
         *
         * @param flag Whether to use stable CSM snapping
         */
        """
        pass

    def set_border_bias(self, const_PSSMCameraRig_self, float_bias): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_border_bias(const PSSMCameraRig self, float bias)
        
        /**
         * @brief Sets the border bias for each split
         * @details This sets the border bias for every split. This increases each
         *   splits frustum by multiplying it by (1 + bias), and helps reducing artifacts
         *   at the borders of the splits. Artifacts can occur when the bias is too low,
         *   because then the filtering will go over the bounds of the split, producing
         *   invalid results.
         *
         *   If the bias is below zero, an assertion is thrown.
         *
         * @param bias Border bias
         */
        """
        pass

    def set_logarithmic_factor(self, const_PSSMCameraRig_self, float_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_logarithmic_factor(const PSSMCameraRig self, float factor)
        
        /**
         * @brief Sets the logarithmic factor
         * @details This sets the logarithmic factor, which is the core of the algorithm.
         *   PSSM splits the camera frustum based on a linear and a logarithmic factor.
         *   While a linear factor provides a good distribution, it often is not applicable
         *   for wider distances. A logarithmic distribution provides a better distribution
         *   at distance, but suffers from splitting in the near areas.
         *
         *   The logarithmic factor mixes the logarithmic and linear split distribution,
         *   to get the best of both. A greater factor will make the distribution more
         *   logarithmic, while a smaller factor will make it more linear.
         *
         *   If the factor is below zero, an ssertion is triggered.
         *
         * @param factor The logarithmic factor
         */
        """
        pass

    def set_pssm_distance(self, const_PSSMCameraRig_self, float_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pssm_distance(const PSSMCameraRig self, float distance)
        
        /**
         * @brief Sets the maximum pssm distance.
         * @details This sets the maximum distance in world space until which shadows
         *   are rendered. After this distance, no shadows will be rendered.
         *
         *   If the distance is below zero, an assertion is triggered.
         *
         * @param distance Maximum distance in world space
         */
        """
        pass

    def set_resolution(self, const_PSSMCameraRig_self, int_resolution): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_resolution(const PSSMCameraRig self, int resolution)
        
        /**
         * @brief Sets the resolution of each split
         * @details This sets the resolution of each split. Currently it is equal for
         *   each split. This is required when using PSSMCameraRig::set_use_stable_csm,
         *   to compute how bix a texel is.
         *
         *   It has to match the y-resolution of the pssm shadow map. If an invalid
         *   resolution is triggered, an assertion is thrown.
         *
         * @param resolution The resolution of each split.
         */
        """
        pass

    def set_sun_distance(self, const_PSSMCameraRig_self, float_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sun_distance(const PSSMCameraRig self, float distance)
        
        /**
         * @brief Sets the suns distance
         * @details This sets the distance the cameras will have from the cameras frustum.
         *   This prevents far objects from having no shadows, which can occur when these
         *   objects are between the cameras frustum and the sun, but not inside of the
         *   cameras frustum. Setting the sun distance high enough will move the cameras
         *   away from the camera frustum, being able to cover those distant objects too.
         *
         *   If the sun distance is set too high, artifacts will occur due to the reduced
         *   range of depth. If a value below zero is passed, an assertion will get
         *   triggered.
         *
         * @param distance The sun distance
         */
        """
        pass

    def set_use_fixed_film_size(self, const_PSSMCameraRig_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_use_fixed_film_size(const PSSMCameraRig self, bool flag)
        
        /**
         * @brief Sets whether to use a fixed film size
         * @details This controls if a fixed film size should be used. This will cause
         *   the camera rig to cache the current film size, and only change it in case
         *   it gets too small. This provides less flickering when moving, because the
         *   film size will stay roughly constant. However, to prevent the cached film
         *   size getting too big, one should call PSSMCameraRig::reset_film_size
         *   once in a while, otherwise there might be a lot of wasted space.
         *
         * @param flag Whether to use a fixed film size
         */
        """
        pass

    def set_use_stable_csm(self, const_PSSMCameraRig_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_use_stable_csm(const PSSMCameraRig self, bool flag)
        
        /**
         * @brief Sets whether to use stable CSM snapping.
         * @details This option controls if stable CSM snapping should be used. When the
         *   option is enabled, all splits will snap to their texels, so that when moving,
         *   no flickering will occur. However, this only works when the splits do not
         *   change their film size, rotation and angle.
         *
         * @param flag Whether to use stable CSM snapping
         */
        """
        pass

    def update(self, const_PSSMCameraRig_self, NodePath_cam_node, const_LVecBase3f_light_vector): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const PSSMCameraRig self, NodePath cam_node, const LVecBase3f light_vector)
        
        /**
         * @brief Updates the PSSM camera rig
         * @details This updates the rig with an updated camera position, and a given
         *   light vector. This should be called on a per-frame basis. It will reposition
         *   all camera sources to fit the frustum based on the pssm distribution.
         *
         *   The light vector should be the vector from the light source, not the
         *   vector to the light source.
         *
         * @param cam_node Target camera node
         * @param light_vector The vector from the light to any point
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d._rplight.PSSMCameraRig' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d._rplight.PSSMCameraRig' objects>"
        '__doc__': '/**\n * @brief Main class used for handling PSSM\n * @details This is the main class for supporting PSSM, it is used by the PSSM\n *   plugin to compute the position of the splits.\n *\n *   It supports handling a varying amount of cameras, and fitting those cameras\n *   into the main camera frustum, to render distant shadows. It also supports\n *   various optimizations for fitting the frustum, e.g. rotating the sources\n *   to get a better coverage.\n *\n *   It also provides methods to get arrays of data about the used cameras\n *   view-projection matrices and their near and far plane, which is required for\n *   processing the data in the shadow sampling shader.\n *\n *   In this class, there is often referred to "Splits" or also called "Cascades".\n *   These denote the different cameras which are used to split the frustum,\n *   and are a common term related to the PSSM algorithm.\n *\n *   To understand the functionality of this class, a detailed knowledge of the\n *   PSSM algorithm is helpful.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.PSSMCameraRig' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E5BB0>'
        'getCamera': None, # (!) real value is "<method 'getCamera' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'getMvpArray': None, # (!) real value is "<method 'getMvpArray' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'getNearfarArray': None, # (!) real value is "<method 'getNearfarArray' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'get_camera': None, # (!) real value is "<method 'get_camera' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'get_mvp_array': None, # (!) real value is "<method 'get_mvp_array' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'get_nearfar_array': None, # (!) real value is "<method 'get_nearfar_array' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'reparentTo': None, # (!) real value is "<method 'reparentTo' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'reparent_to': None, # (!) real value is "<method 'reparent_to' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'resetFilmSizeCache': None, # (!) real value is "<method 'resetFilmSizeCache' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'reset_film_size_cache': None, # (!) real value is "<method 'reset_film_size_cache' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'setBorderBias': None, # (!) real value is "<method 'setBorderBias' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'setLogarithmicFactor': None, # (!) real value is "<method 'setLogarithmicFactor' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'setPssmDistance': None, # (!) real value is "<method 'setPssmDistance' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'setResolution': None, # (!) real value is "<method 'setResolution' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'setSunDistance': None, # (!) real value is "<method 'setSunDistance' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'setUseFixedFilmSize': None, # (!) real value is "<method 'setUseFixedFilmSize' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'setUseStableCsm': None, # (!) real value is "<method 'setUseStableCsm' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'set_border_bias': None, # (!) real value is "<method 'set_border_bias' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'set_logarithmic_factor': None, # (!) real value is "<method 'set_logarithmic_factor' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'set_pssm_distance': None, # (!) real value is "<method 'set_pssm_distance' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'set_resolution': None, # (!) real value is "<method 'set_resolution' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'set_sun_distance': None, # (!) real value is "<method 'set_sun_distance' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'set_use_fixed_film_size': None, # (!) real value is "<method 'set_use_fixed_film_size' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'set_use_stable_csm': None, # (!) real value is "<method 'set_use_stable_csm' of 'panda3d._rplight.PSSMCameraRig' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d._rplight.PSSMCameraRig' objects>"
    }


class RPLight(__panda3d_core.ReferenceCount):
    """
    /**
     * @brief Base class for Lights
     * @details This is the base class for all lights in the render pipeline. It
     *   stores common properties, and provides methods to modify these.
     *   It also defines some interface functions which subclasses have to implement.
     */
    """
    def clearIesProfile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_ies_profile(const RPLight self)
        
        /**
         * @brief Clears the IES profile
         * @details This clears the IES profile of the light, telling it to no longer
         *   use an IES profile, and instead use the default attenuation.
         */
        """
        pass

    def clear_ies_profile(self, const_RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_ies_profile(const RPLight self)
        
        /**
         * @brief Clears the IES profile
         * @details This clears the IES profile of the light, telling it to no longer
         *   use an IES profile, and instead use the default attenuation.
         */
        """
        pass

    def getCastsShadows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_casts_shadows(RPLight self)
        
        /**
         * @brief Returns whether the light casts shadows
         * @details This returns whether the light casts shadows, the returned value
         *   is the one previously set with RPLight::set_casts_shadows.
         *
         * @return true if the light casts shadows, false otherwise
         */
        """
        pass

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color(RPLight self)
        
        /**
         * @brief Returns the lights color
         * @details This returns the light color, previously set with RPLight::set_color.
         *   This does not include the energy of the light. It might differ from what
         *   was set with set_color, because the color is normalized by dividing it
         *   by its luminance.
         * @return Light-color
         */
        """
        pass

    def getEnergy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_energy(RPLight self)
        
        /**
         * @brief Returns the energy of the light
         * @details This returns the energy of the light, previously set with
         *   RPLight::set_energy.
         *
         * @return energy of the light
         */
        """
        pass

    def getIesProfile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ies_profile(RPLight self)
        
        /**
         * @brief Returns the light's IES profile
         * @details This returns the IES profile of a light, previously set with
         *   RPLight::set_ies_profile. In case no ies profile was set, returns -1.
         *
         * @return IES Profile handle
         */
        """
        pass

    def getLightType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_light_type(RPLight self)
        
        /**
         * @brief Returns the type of the light
         * @details This returns the internal type of the light, which was specified
         *   in the lights constructor. This can be used to distinguish between light
         *   types.
         * @return Type of the light
         */
        """
        pass

    def getNearPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_near_plane(RPLight self)
        
        /**
         * @brief Returns the near plane of the light
         * @details This returns the light's near plane, previously set with
         *   RPLight::set_near_plane. If the light does not cast shadows, this value
         *   is meaningless.
         *
         * @return Near-plane
         */
        """
        pass

    def getPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos(RPLight self)
        
        /**
         * @brief Returns the position of the light
         * @details This returns the position of the light previously set with
         *   RPLight::set_pos(). The returned position is in world space.
         * @return Light-position
         */
        """
        pass

    def getShadowMapResolution(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shadow_map_resolution(RPLight self)
        
        /**
         * @brief Returns the shadow map resolution
         * @details This returns the shadow map resolution of each source of the light.
         *   If the light is not setup to cast shadows, this value is meaningless.
         *   The returned value is the one previously set with RPLight::set_shadow_map_resolution.
         *
         * @return Shadow map resolution in pixels
         */
        """
        pass

    def get_casts_shadows(self, RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_casts_shadows(RPLight self)
        
        /**
         * @brief Returns whether the light casts shadows
         * @details This returns whether the light casts shadows, the returned value
         *   is the one previously set with RPLight::set_casts_shadows.
         *
         * @return true if the light casts shadows, false otherwise
         */
        """
        pass

    def get_color(self, RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(RPLight self)
        
        /**
         * @brief Returns the lights color
         * @details This returns the light color, previously set with RPLight::set_color.
         *   This does not include the energy of the light. It might differ from what
         *   was set with set_color, because the color is normalized by dividing it
         *   by its luminance.
         * @return Light-color
         */
        """
        pass

    def get_energy(self, RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_energy(RPLight self)
        
        /**
         * @brief Returns the energy of the light
         * @details This returns the energy of the light, previously set with
         *   RPLight::set_energy.
         *
         * @return energy of the light
         */
        """
        pass

    def get_ies_profile(self, RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ies_profile(RPLight self)
        
        /**
         * @brief Returns the light's IES profile
         * @details This returns the IES profile of a light, previously set with
         *   RPLight::set_ies_profile. In case no ies profile was set, returns -1.
         *
         * @return IES Profile handle
         */
        """
        pass

    def get_light_type(self, RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_light_type(RPLight self)
        
        /**
         * @brief Returns the type of the light
         * @details This returns the internal type of the light, which was specified
         *   in the lights constructor. This can be used to distinguish between light
         *   types.
         * @return Type of the light
         */
        """
        pass

    def get_near_plane(self, RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_near_plane(RPLight self)
        
        /**
         * @brief Returns the near plane of the light
         * @details This returns the light's near plane, previously set with
         *   RPLight::set_near_plane. If the light does not cast shadows, this value
         *   is meaningless.
         *
         * @return Near-plane
         */
        """
        pass

    def get_pos(self, RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos(RPLight self)
        
        /**
         * @brief Returns the position of the light
         * @details This returns the position of the light previously set with
         *   RPLight::set_pos(). The returned position is in world space.
         * @return Light-position
         */
        """
        pass

    def get_shadow_map_resolution(self, RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shadow_map_resolution(RPLight self)
        
        /**
         * @brief Returns the shadow map resolution
         * @details This returns the shadow map resolution of each source of the light.
         *   If the light is not setup to cast shadows, this value is meaningless.
         *   The returned value is the one previously set with RPLight::set_shadow_map_resolution.
         *
         * @return Shadow map resolution in pixels
         */
        """
        pass

    def hasIesProfile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_ies_profile(RPLight self)
        
        /**
         * @brief Returns whether the light has an IES profile assigned
         * @details This returns whether the light has an IES profile assigned,
         *   previously done with RPLight::set_ies_profile.
         *
         * @return true if the light has an IES profile assigned, false otherwise
         */
        """
        pass

    def has_ies_profile(self, RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_ies_profile(RPLight self)
        
        /**
         * @brief Returns whether the light has an IES profile assigned
         * @details This returns whether the light has an IES profile assigned,
         *   previously done with RPLight::set_ies_profile.
         *
         * @return true if the light has an IES profile assigned, false otherwise
         */
        """
        pass

    def invalidateShadows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invalidate_shadows(const RPLight self)
        
        /**
         * @brief Invalidates the shadows
         * @details This invalidates all shadows of the light, causing them to get
         *   regenerated. This might be the case  when the lights position or similar
         *   changed. This will cause all shadow sources to be updated, emitting a
         *   shadow update. Be careful when calling this method if you don't want all
         *   sources to get updated. If you only have to invalidate a single shadow source,
         *   use `get_shadow_source(n)->set_needs_update(true)`.
         */
        """
        pass

    def invalidate_shadows(self, const_RPLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invalidate_shadows(const RPLight self)
        
        /**
         * @brief Invalidates the shadows
         * @details This invalidates all shadows of the light, causing them to get
         *   regenerated. This might be the case  when the lights position or similar
         *   changed. This will cause all shadow sources to be updated, emitting a
         *   shadow update. Be careful when calling this method if you don't want all
         *   sources to get updated. If you only have to invalidate a single shadow source,
         *   use `get_shadow_source(n)->set_needs_update(true)`.
         */
        """
        pass

    def setCastsShadows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_casts_shadows(const RPLight self, bool flag)
        
        /**
         * @brief Controls whether the light casts shadows
         * @details This sets whether the light casts shadows. You can not change this
         *   while the light is attached. When flag is set to true, the light will be
         *   setup to cast shadows, spawning shadow sources based on the lights type.
         *   If the flag is set to false, the light will be inddicated to cast no shadows.
         *
         * @param flag Whether the light casts shadows
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const RPLight self, const LVecBase3f color)
        set_color(const RPLight self, float r, float g, float b)
        
        /**
         * @brief Sets the lights color
         * @details This sets the lights color. The color should not include the brightness
         *   of the light, you should control that with the energy. The color specifies
         *   the lights "tint" and will get multiplied with its specular and diffuse
         *   contribution.
         *
         *   The color will be normalized by dividing by the colors luminance. Setting
         *   higher values than 1.0 will have no effect.
         *
         * @param color Light color
         */
        
        /**
         * @brief Sets the lights color
         * @details @copydetails RPLight::set_color(const LVecBase3 &color)
         *
         * @param r Red-component of the color
         * @param g Green-component of the color
         * @param b Blue-component of the color
         */
        """
        pass

    def setColorFromTemperature(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_from_temperature(const RPLight self, float temperature)
        
        /**
         * @brief Sets the lights color from a given color temperature
         * @details This sets the lights color, given a temperature. This is more
         *   physically based than setting a user defined color. The color will be
         *   computed from the given temperature.
         *
         * @param temperature Light temperature
         */
        """
        pass

    def setEnergy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_energy(const RPLight self, float energy)
        
        /**
         * @brief Sets the energy of the light
         * @details This sets the energy of the light, which can be seen as the brightness
         *   of the light. It will get multiplied with the normalized color.
         *
         * @param energy energy of the light
         */
        """
        pass

    def setIesProfile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ies_profile(const RPLight self, int profile)
        
        /**
         * @brief Sets the IES profile
         * @details This sets the ies profile of the light. The parameter should be a
         *   handle previously returned by RenderPipeline.load_ies_profile. Using a
         *   value of -1 indicates no ies profile.
         *
         *   Notice that for IES profiles which cover a whole range, you should use an
         *   RPPointLight, whereas for ies profiles which only cover the lower
         *   hemisphere you should use an RPSpotLight for the best performance.
         *
         * @param profile IES Profile handle
         */
        """
        pass

    def setNearPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_near_plane(const RPLight self, float near_plane)
        
        /**
         * @brief Sets the near plane of the light
         * @details This sets the near plane of all shadow sources of the light. It has
         *   no effects if the light does not cast shadows. This prevents artifacts from
         *   objects near to the light. It behaves like Lens::set_near().
         *
         *   It can also help increasing shadow map precision, low near planes will
         *   cause the precision to suffer. Try setting the near plane as big as possible.
         *
         *   If a negative or zero near plane is passed, an assertion is thrown.
         *
         * @param near_plane Near-plane
         */
        """
        pass

    def setPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos(const RPLight self, const LVecBase3f pos)
        set_pos(const RPLight self, float x, float y, float z)
        
        /**
         * @brief Sets the position of the light
         * @details This sets the position of the light in world space. It will cause
         *   the light to get invalidated, and resubmitted to the GPU.
         *
         * @param pos Position in world space
         */
        
        /**
         * @brief Sets the position of the light
         * @details @copydetails RPLight::set_pos(const LVecBase3 &pos)
         *
         * @param x X-component of the position
         * @param y Y-component of the position
         * @param z Z-component of the position
         */
        """
        pass

    def setShadowMapResolution(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shadow_map_resolution(const RPLight self, int resolution)
        
        /**
         * @brief Sets the light's shadow map resolution
         * @details This sets the light's shadow map resolution. This has no effect
         *   when the light is not told to cast shadows (Use RPLight::set_casts_shadows).
         *
         *   When calling this on a light with multiple shadow sources (e.g.
         *   RPPointLight), this controls the resolution of each source. If the light
         *   has 6 shadow sources, and you use a resolution of 512x512, the light's
         *   shadow map will occupy a space of 6 * 512x512 maps in the shadow atlas.
         *
         * @param resolution Resolution of the shadow map in pixels
         */
        """
        pass

    def set_casts_shadows(self, const_RPLight_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_casts_shadows(const RPLight self, bool flag)
        
        /**
         * @brief Controls whether the light casts shadows
         * @details This sets whether the light casts shadows. You can not change this
         *   while the light is attached. When flag is set to true, the light will be
         *   setup to cast shadows, spawning shadow sources based on the lights type.
         *   If the flag is set to false, the light will be inddicated to cast no shadows.
         *
         * @param flag Whether the light casts shadows
         */
        """
        pass

    def set_color(self, const_RPLight_self, const_LVecBase3f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const RPLight self, const LVecBase3f color)
        set_color(const RPLight self, float r, float g, float b)
        
        /**
         * @brief Sets the lights color
         * @details This sets the lights color. The color should not include the brightness
         *   of the light, you should control that with the energy. The color specifies
         *   the lights "tint" and will get multiplied with its specular and diffuse
         *   contribution.
         *
         *   The color will be normalized by dividing by the colors luminance. Setting
         *   higher values than 1.0 will have no effect.
         *
         * @param color Light color
         */
        
        /**
         * @brief Sets the lights color
         * @details @copydetails RPLight::set_color(const LVecBase3 &color)
         *
         * @param r Red-component of the color
         * @param g Green-component of the color
         * @param b Blue-component of the color
         */
        """
        pass

    def set_color_from_temperature(self, const_RPLight_self, float_temperature): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_from_temperature(const RPLight self, float temperature)
        
        /**
         * @brief Sets the lights color from a given color temperature
         * @details This sets the lights color, given a temperature. This is more
         *   physically based than setting a user defined color. The color will be
         *   computed from the given temperature.
         *
         * @param temperature Light temperature
         */
        """
        pass

    def set_energy(self, const_RPLight_self, float_energy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_energy(const RPLight self, float energy)
        
        /**
         * @brief Sets the energy of the light
         * @details This sets the energy of the light, which can be seen as the brightness
         *   of the light. It will get multiplied with the normalized color.
         *
         * @param energy energy of the light
         */
        """
        pass

    def set_ies_profile(self, const_RPLight_self, int_profile): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ies_profile(const RPLight self, int profile)
        
        /**
         * @brief Sets the IES profile
         * @details This sets the ies profile of the light. The parameter should be a
         *   handle previously returned by RenderPipeline.load_ies_profile. Using a
         *   value of -1 indicates no ies profile.
         *
         *   Notice that for IES profiles which cover a whole range, you should use an
         *   RPPointLight, whereas for ies profiles which only cover the lower
         *   hemisphere you should use an RPSpotLight for the best performance.
         *
         * @param profile IES Profile handle
         */
        """
        pass

    def set_near_plane(self, const_RPLight_self, float_near_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_near_plane(const RPLight self, float near_plane)
        
        /**
         * @brief Sets the near plane of the light
         * @details This sets the near plane of all shadow sources of the light. It has
         *   no effects if the light does not cast shadows. This prevents artifacts from
         *   objects near to the light. It behaves like Lens::set_near().
         *
         *   It can also help increasing shadow map precision, low near planes will
         *   cause the precision to suffer. Try setting the near plane as big as possible.
         *
         *   If a negative or zero near plane is passed, an assertion is thrown.
         *
         * @param near_plane Near-plane
         */
        """
        pass

    def set_pos(self, const_RPLight_self, const_LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos(const RPLight self, const LVecBase3f pos)
        set_pos(const RPLight self, float x, float y, float z)
        
        /**
         * @brief Sets the position of the light
         * @details This sets the position of the light in world space. It will cause
         *   the light to get invalidated, and resubmitted to the GPU.
         *
         * @param pos Position in world space
         */
        
        /**
         * @brief Sets the position of the light
         * @details @copydetails RPLight::set_pos(const LVecBase3 &pos)
         *
         * @param x X-component of the position
         * @param y Y-component of the position
         * @param z Z-component of the position
         */
        """
        pass

    def set_shadow_map_resolution(self, const_RPLight_self, int_resolution): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shadow_map_resolution(const RPLight self, int resolution)
        
        /**
         * @brief Sets the light's shadow map resolution
         * @details This sets the light's shadow map resolution. This has no effect
         *   when the light is not told to cast shadows (Use RPLight::set_casts_shadows).
         *
         *   When calling this on a light with multiple shadow sources (e.g.
         *   RPPointLight), this controls the resolution of each source. If the light
         *   has 6 shadow sources, and you use a resolution of 512x512, the light's
         *   shadow map will occupy a space of 6 * 512x512 maps in the shadow atlas.
         *
         * @param resolution Resolution of the shadow map in pixels
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    casts_shadows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    energy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ies_profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    near_plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shadow_map_resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'LTEmpty': 0,
        'LTPointLight': 1,
        'LTSpotLight': 2,
        'LT_empty': 0,
        'LT_point_light': 1,
        'LT_spot_light': 2,
        '__doc__': '/**\n * @brief Base class for Lights\n * @details This is the base class for all lights in the render pipeline. It\n *   stores common properties, and provides methods to modify these.\n *   It also defines some interface functions which subclasses have to implement.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.RPLight' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E50D0>'
        'casts_shadows': None, # (!) real value is "<attribute 'casts_shadows' of 'panda3d._rplight.RPLight' objects>"
        'clearIesProfile': None, # (!) real value is "<method 'clearIesProfile' of 'panda3d._rplight.RPLight' objects>"
        'clear_ies_profile': None, # (!) real value is "<method 'clear_ies_profile' of 'panda3d._rplight.RPLight' objects>"
        'color': None, # (!) real value is "<attribute 'color' of 'panda3d._rplight.RPLight' objects>"
        'energy': None, # (!) real value is "<attribute 'energy' of 'panda3d._rplight.RPLight' objects>"
        'getCastsShadows': None, # (!) real value is "<method 'getCastsShadows' of 'panda3d._rplight.RPLight' objects>"
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d._rplight.RPLight' objects>"
        'getEnergy': None, # (!) real value is "<method 'getEnergy' of 'panda3d._rplight.RPLight' objects>"
        'getIesProfile': None, # (!) real value is "<method 'getIesProfile' of 'panda3d._rplight.RPLight' objects>"
        'getLightType': None, # (!) real value is "<method 'getLightType' of 'panda3d._rplight.RPLight' objects>"
        'getNearPlane': None, # (!) real value is "<method 'getNearPlane' of 'panda3d._rplight.RPLight' objects>"
        'getPos': None, # (!) real value is "<method 'getPos' of 'panda3d._rplight.RPLight' objects>"
        'getShadowMapResolution': None, # (!) real value is "<method 'getShadowMapResolution' of 'panda3d._rplight.RPLight' objects>"
        'get_casts_shadows': None, # (!) real value is "<method 'get_casts_shadows' of 'panda3d._rplight.RPLight' objects>"
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d._rplight.RPLight' objects>"
        'get_energy': None, # (!) real value is "<method 'get_energy' of 'panda3d._rplight.RPLight' objects>"
        'get_ies_profile': None, # (!) real value is "<method 'get_ies_profile' of 'panda3d._rplight.RPLight' objects>"
        'get_light_type': None, # (!) real value is "<method 'get_light_type' of 'panda3d._rplight.RPLight' objects>"
        'get_near_plane': None, # (!) real value is "<method 'get_near_plane' of 'panda3d._rplight.RPLight' objects>"
        'get_pos': None, # (!) real value is "<method 'get_pos' of 'panda3d._rplight.RPLight' objects>"
        'get_shadow_map_resolution': None, # (!) real value is "<method 'get_shadow_map_resolution' of 'panda3d._rplight.RPLight' objects>"
        'hasIesProfile': None, # (!) real value is "<method 'hasIesProfile' of 'panda3d._rplight.RPLight' objects>"
        'has_ies_profile': None, # (!) real value is "<method 'has_ies_profile' of 'panda3d._rplight.RPLight' objects>"
        'ies_profile': None, # (!) real value is "<attribute 'ies_profile' of 'panda3d._rplight.RPLight' objects>"
        'invalidateShadows': None, # (!) real value is "<method 'invalidateShadows' of 'panda3d._rplight.RPLight' objects>"
        'invalidate_shadows': None, # (!) real value is "<method 'invalidate_shadows' of 'panda3d._rplight.RPLight' objects>"
        'light_type': None, # (!) real value is "<attribute 'light_type' of 'panda3d._rplight.RPLight' objects>"
        'near_plane': None, # (!) real value is "<attribute 'near_plane' of 'panda3d._rplight.RPLight' objects>"
        'pos': None, # (!) real value is "<attribute 'pos' of 'panda3d._rplight.RPLight' objects>"
        'setCastsShadows': None, # (!) real value is "<method 'setCastsShadows' of 'panda3d._rplight.RPLight' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d._rplight.RPLight' objects>"
        'setColorFromTemperature': None, # (!) real value is "<method 'setColorFromTemperature' of 'panda3d._rplight.RPLight' objects>"
        'setEnergy': None, # (!) real value is "<method 'setEnergy' of 'panda3d._rplight.RPLight' objects>"
        'setIesProfile': None, # (!) real value is "<method 'setIesProfile' of 'panda3d._rplight.RPLight' objects>"
        'setNearPlane': None, # (!) real value is "<method 'setNearPlane' of 'panda3d._rplight.RPLight' objects>"
        'setPos': None, # (!) real value is "<method 'setPos' of 'panda3d._rplight.RPLight' objects>"
        'setShadowMapResolution': None, # (!) real value is "<method 'setShadowMapResolution' of 'panda3d._rplight.RPLight' objects>"
        'set_casts_shadows': None, # (!) real value is "<method 'set_casts_shadows' of 'panda3d._rplight.RPLight' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d._rplight.RPLight' objects>"
        'set_color_from_temperature': None, # (!) real value is "<method 'set_color_from_temperature' of 'panda3d._rplight.RPLight' objects>"
        'set_energy': None, # (!) real value is "<method 'set_energy' of 'panda3d._rplight.RPLight' objects>"
        'set_ies_profile': None, # (!) real value is "<method 'set_ies_profile' of 'panda3d._rplight.RPLight' objects>"
        'set_near_plane': None, # (!) real value is "<method 'set_near_plane' of 'panda3d._rplight.RPLight' objects>"
        'set_pos': None, # (!) real value is "<method 'set_pos' of 'panda3d._rplight.RPLight' objects>"
        'set_shadow_map_resolution': None, # (!) real value is "<method 'set_shadow_map_resolution' of 'panda3d._rplight.RPLight' objects>"
        'shadow_map_resolution': None, # (!) real value is "<attribute 'shadow_map_resolution' of 'panda3d._rplight.RPLight' objects>"
    }
    LTEmpty = 0
    LTPointLight = 1
    LTSpotLight = 2
    LT_empty = 0
    LT_point_light = 1
    LT_spot_light = 2


class RPPointLight(RPLight):
    """
    /**
     * @brief PointLight class
     * @details This represents a point light, a light which has a position and
     *   radius. Checkout the RenderPipeline documentation for more information
     *   about this type of light.
     */
    """
    def getInnerRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inner_radius(RPPointLight self)
        
        /**
         * @brief Returns the inner radius of the light
         * @details This returns the inner radius of the light, previously set with
         *   RPPointLight::get_inner_radius.
         * @return [description]
         */
        """
        pass

    def getRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_radius(RPPointLight self)
        
        /**
         * @brief Returns the lights radius
         * @details This returns the lights radius previously set with
         *   RPPointLight::set_radius
         * @return Light radius in world space
         */
        """
        pass

    def get_inner_radius(self, RPPointLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inner_radius(RPPointLight self)
        
        /**
         * @brief Returns the inner radius of the light
         * @details This returns the inner radius of the light, previously set with
         *   RPPointLight::get_inner_radius.
         * @return [description]
         */
        """
        pass

    def get_radius(self, RPPointLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radius(RPPointLight self)
        
        /**
         * @brief Returns the lights radius
         * @details This returns the lights radius previously set with
         *   RPPointLight::set_radius
         * @return Light radius in world space
         */
        """
        pass

    def setInnerRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_inner_radius(const RPPointLight self, float inner_radius)
        
        /**
         * @brief Sets the inner radius of the light
         * @details This sets the inner radius of the light. Anything greater than
         *   zero causes the light to get an area light. This has influence on the
         *   specular highlights of the light aswell as the shadows.
         *
         *   The inner radius controls the size of the lights sphere size in world
         *   space units. A radius of 0 means the light has no inner radius, and the
         *   light will be have like an infinite small point light source.
         *   A radius greater than zero will cause the light to behave like it would be
         *   an emissive sphere with the given inner radius emitting light. This is
         *   more physically correct.
         *
         * @param inner_radius Inner-radius in world space
         */
        """
        pass

    def setRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_radius(const RPPointLight self, float radius)
        
        /**
         * @brief Sets the radius of the light
         * @details This sets the radius of the light. It controls the lights
         *   influence. After a distance greater than this radius, the light influence
         *   is zero.
         *
         * @param radius Light radius in world space
         */
        """
        pass

    def set_inner_radius(self, const_RPPointLight_self, float_inner_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_inner_radius(const RPPointLight self, float inner_radius)
        
        /**
         * @brief Sets the inner radius of the light
         * @details This sets the inner radius of the light. Anything greater than
         *   zero causes the light to get an area light. This has influence on the
         *   specular highlights of the light aswell as the shadows.
         *
         *   The inner radius controls the size of the lights sphere size in world
         *   space units. A radius of 0 means the light has no inner radius, and the
         *   light will be have like an infinite small point light source.
         *   A radius greater than zero will cause the light to behave like it would be
         *   an emissive sphere with the given inner radius emitting light. This is
         *   more physically correct.
         *
         * @param inner_radius Inner-radius in world space
         */
        """
        pass

    def set_radius(self, const_RPPointLight_self, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_radius(const RPPointLight self, float radius)
        
        /**
         * @brief Sets the radius of the light
         * @details This sets the radius of the light. It controls the lights
         *   influence. After a distance greater than this radius, the light influence
         *   is zero.
         *
         * @param radius Light radius in world space
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    inner_radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * @brief PointLight class\n * @details This represents a point light, a light which has a position and\n *   radius. Checkout the RenderPipeline documentation for more information\n *   about this type of light.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.RPPointLight' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E59E0>'
        'getInnerRadius': None, # (!) real value is "<method 'getInnerRadius' of 'panda3d._rplight.RPPointLight' objects>"
        'getRadius': None, # (!) real value is "<method 'getRadius' of 'panda3d._rplight.RPPointLight' objects>"
        'get_inner_radius': None, # (!) real value is "<method 'get_inner_radius' of 'panda3d._rplight.RPPointLight' objects>"
        'get_radius': None, # (!) real value is "<method 'get_radius' of 'panda3d._rplight.RPPointLight' objects>"
        'inner_radius': None, # (!) real value is "<attribute 'inner_radius' of 'panda3d._rplight.RPPointLight' objects>"
        'radius': None, # (!) real value is "<attribute 'radius' of 'panda3d._rplight.RPPointLight' objects>"
        'setInnerRadius': None, # (!) real value is "<method 'setInnerRadius' of 'panda3d._rplight.RPPointLight' objects>"
        'setRadius': None, # (!) real value is "<method 'setRadius' of 'panda3d._rplight.RPPointLight' objects>"
        'set_inner_radius': None, # (!) real value is "<method 'set_inner_radius' of 'panda3d._rplight.RPPointLight' objects>"
        'set_radius': None, # (!) real value is "<method 'set_radius' of 'panda3d._rplight.RPPointLight' objects>"
    }


class RPSpotLight(RPLight):
    """
    /**
     * @brief SpotLight class
     * @details This represents a spot light, a light which has a position, radius,
     *   direction and FoV. Checkout the RenderPipeline documentation for more
     *   information about this type of light.
     */
    """
    def getDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_direction(RPSpotLight self)
        """
        pass

    def getFov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fov(RPSpotLight self)
        """
        pass

    def getRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_radius(RPSpotLight self)
        """
        pass

    def get_direction(self, RPSpotLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_direction(RPSpotLight self)
        """
        pass

    def get_fov(self, RPSpotLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fov(RPSpotLight self)
        """
        pass

    def get_radius(self, RPSpotLight_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radius(RPSpotLight self)
        """
        pass

    def lookAt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        look_at(const RPSpotLight self, LVecBase3f point)
        look_at(const RPSpotLight self, float x, float y, float z)
        """
        pass

    def look_at(self, const_RPSpotLight_self, LVecBase3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        look_at(const RPSpotLight self, LVecBase3f point)
        look_at(const RPSpotLight self, float x, float y, float z)
        """
        pass

    def setDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_direction(const RPSpotLight self, LVecBase3f direction)
        set_direction(const RPSpotLight self, float dx, float dy, float dz)
        """
        pass

    def setFov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fov(const RPSpotLight self, float fov)
        """
        pass

    def setRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_radius(const RPSpotLight self, float radius)
        """
        pass

    def set_direction(self, const_RPSpotLight_self, LVecBase3f_direction): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_direction(const RPSpotLight self, LVecBase3f direction)
        set_direction(const RPSpotLight self, float dx, float dy, float dz)
        """
        pass

    def set_fov(self, const_RPSpotLight_self, float_fov): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fov(const RPSpotLight self, float fov)
        """
        pass

    def set_radius(self, const_RPSpotLight_self, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_radius(const RPSpotLight self, float radius)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * @brief SpotLight class\n * @details This represents a spot light, a light which has a position, radius,\n *   direction and FoV. Checkout the RenderPipeline documentation for more\n *   information about this type of light.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.RPSpotLight' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E5D80>'
        'direction': None, # (!) real value is "<attribute 'direction' of 'panda3d._rplight.RPSpotLight' objects>"
        'fov': None, # (!) real value is "<attribute 'fov' of 'panda3d._rplight.RPSpotLight' objects>"
        'getDirection': None, # (!) real value is "<method 'getDirection' of 'panda3d._rplight.RPSpotLight' objects>"
        'getFov': None, # (!) real value is "<method 'getFov' of 'panda3d._rplight.RPSpotLight' objects>"
        'getRadius': None, # (!) real value is "<method 'getRadius' of 'panda3d._rplight.RPSpotLight' objects>"
        'get_direction': None, # (!) real value is "<method 'get_direction' of 'panda3d._rplight.RPSpotLight' objects>"
        'get_fov': None, # (!) real value is "<method 'get_fov' of 'panda3d._rplight.RPSpotLight' objects>"
        'get_radius': None, # (!) real value is "<method 'get_radius' of 'panda3d._rplight.RPSpotLight' objects>"
        'lookAt': None, # (!) real value is "<method 'lookAt' of 'panda3d._rplight.RPSpotLight' objects>"
        'look_at': None, # (!) real value is "<method 'look_at' of 'panda3d._rplight.RPSpotLight' objects>"
        'radius': None, # (!) real value is "<attribute 'radius' of 'panda3d._rplight.RPSpotLight' objects>"
        'setDirection': None, # (!) real value is "<method 'setDirection' of 'panda3d._rplight.RPSpotLight' objects>"
        'setFov': None, # (!) real value is "<method 'setFov' of 'panda3d._rplight.RPSpotLight' objects>"
        'setRadius': None, # (!) real value is "<method 'setRadius' of 'panda3d._rplight.RPSpotLight' objects>"
        'set_direction': None, # (!) real value is "<method 'set_direction' of 'panda3d._rplight.RPSpotLight' objects>"
        'set_fov': None, # (!) real value is "<method 'set_fov' of 'panda3d._rplight.RPSpotLight' objects>"
        'set_radius': None, # (!) real value is "<method 'set_radius' of 'panda3d._rplight.RPSpotLight' objects>"
    }


class ShadowAtlas(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * @brief Class which manages distributing shadow maps in an atlas.
     * @details This class manages the shadow atlas. It handles finding and reserving
     *   space for new shadow maps.
     */
    """
    def getCoverage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coverage(ShadowAtlas self)
        
        /**
         * @brief Returns the amount of used tiles in percentage
         * @details This returns in percentage from 0 to 1 how much space of the atlas
         *   is used right now. A value of 1 means the atlas is completely full, whereas
         *   a value of 0 means the atlas is completely free.
         * @return Atlas usage in percentage
         */
        """
        pass

    def getNumUsedTiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_used_tiles(ShadowAtlas self)
        
        /**
         * @brief Returns the amount of used tiles
         * @details Returns the amount of used tiles in the atlas
         * @return Amount of used tiles
         */
        """
        pass

    def get_coverage(self, ShadowAtlas_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coverage(ShadowAtlas self)
        
        /**
         * @brief Returns the amount of used tiles in percentage
         * @details This returns in percentage from 0 to 1 how much space of the atlas
         *   is used right now. A value of 1 means the atlas is completely full, whereas
         *   a value of 0 means the atlas is completely free.
         * @return Atlas usage in percentage
         */
        """
        pass

    def get_num_used_tiles(self, ShadowAtlas_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_used_tiles(ShadowAtlas self)
        
        /**
         * @brief Returns the amount of used tiles
         * @details Returns the amount of used tiles in the atlas
         * @return Amount of used tiles
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

    coverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_used_tiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d._rplight.ShadowAtlas' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d._rplight.ShadowAtlas' objects>"
        '__doc__': '/**\n * @brief Class which manages distributing shadow maps in an atlas.\n * @details This class manages the shadow atlas. It handles finding and reserving\n *   space for new shadow maps.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.ShadowAtlas' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E52A0>'
        'coverage': None, # (!) real value is "<attribute 'coverage' of 'panda3d._rplight.ShadowAtlas' objects>"
        'getCoverage': None, # (!) real value is "<method 'getCoverage' of 'panda3d._rplight.ShadowAtlas' objects>"
        'getNumUsedTiles': None, # (!) real value is "<method 'getNumUsedTiles' of 'panda3d._rplight.ShadowAtlas' objects>"
        'get_coverage': None, # (!) real value is "<method 'get_coverage' of 'panda3d._rplight.ShadowAtlas' objects>"
        'get_num_used_tiles': None, # (!) real value is "<method 'get_num_used_tiles' of 'panda3d._rplight.ShadowAtlas' objects>"
        'num_used_tiles': None, # (!) real value is "<attribute 'num_used_tiles' of 'panda3d._rplight.ShadowAtlas' objects>"
    }


class ShadowManager(__panda3d_core.ReferenceCount):
    # no doc
    def getAtlas(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_atlas(ShadowManager self)
        
        /**
         * @brief Returns a handle to the shadow atlas.
         * @details This returns a handle to the internal shadow atlas instance. This
         *   is only valid after calling ShadowManager::init. Calling this earlier will
         *   trigger an assertion and undefined behaviour.
         * @return The internal ShadowAtlas instance
         */
        """
        pass

    def getAtlasSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_atlas_size(ShadowManager self)
        
        /**
         * @brief Returns the shadow atlas size.
         * @details This returns the shadow atlas size previously set with
         *   ShadowManager::set_atlas_size.
         * @return Shadow atlas size in pixels
         */
        """
        pass

    def getNumUpdateSlotsLeft(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_update_slots_left(ShadowManager self)
        
        /**
         * @brief Returns how many update slots are left.
         * @details This returns how many update slots are left. You can assume the
         *   next n calls to add_update will succeed, whereas n is the value returned
         *   by this function.
         * @return Number of update slots left.
         */
        """
        pass

    def get_atlas(self, ShadowManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_atlas(ShadowManager self)
        
        /**
         * @brief Returns a handle to the shadow atlas.
         * @details This returns a handle to the internal shadow atlas instance. This
         *   is only valid after calling ShadowManager::init. Calling this earlier will
         *   trigger an assertion and undefined behaviour.
         * @return The internal ShadowAtlas instance
         */
        """
        pass

    def get_atlas_size(self, ShadowManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_atlas_size(ShadowManager self)
        
        /**
         * @brief Returns the shadow atlas size.
         * @details This returns the shadow atlas size previously set with
         *   ShadowManager::set_atlas_size.
         * @return Shadow atlas size in pixels
         */
        """
        pass

    def get_num_update_slots_left(self, ShadowManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_update_slots_left(ShadowManager self)
        
        /**
         * @brief Returns how many update slots are left.
         * @details This returns how many update slots are left. You can assume the
         *   next n calls to add_update will succeed, whereas n is the value returned
         *   by this function.
         * @return Number of update slots left.
         */
        """
        pass

    def init(self, const_ShadowManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        init(const ShadowManager self)
        
        /**
         * @brief Initializes the ShadowManager.
         * @details This initializes the ShadowManager. All properties should have
         *   been set before calling this, otherwise assertions will get triggered.
         *
         *   This setups everything required for rendering shadows, including the
         *   shadow atlas and the various shadow cameras. After calling this method,
         *   no properties can be changed anymore.
         */
        """
        pass

    def setAtlasGraphicsOutput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_atlas_graphics_output(const ShadowManager self, GraphicsOutput graphics_output)
        
        /**
         * @brief Sets the handle to the Shadow targets output
         * @details This sets the handle to the GraphicsOutput of the shadow atlas.
         *   Usually this is RenderTarget.get_internal_buffer(), whereas the RenderTarget
         *   is the target of the ShadowStage.
         *
         *   This is used for creating display regions and attaching cameras to them,
         *   for performing shadow updates.
         *
         *   This has to get called before ShadowManager::init, otherwise an assertion
         *   will be triggered.
         *
         * @param graphics_output [description]
         */
        """
        pass

    def setAtlasSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_atlas_size(const ShadowManager self, int atlas_size)
        
        /**
         * @brief Sets the shadow atlas size
         * @details This sets the desired shadow atlas size. It should be big enough
         *   to store all important shadow sources, with some buffer, because the shadow
         *   maps usually won't be fitted perfectly, so gaps can occur.
         *
         *   This has to get called before calling ShadowManager::init. When calling this
         *   method after initialization, an assertion will get triggered.
         *
         * @param atlas_size Size of the shadow atlas in pixels
         */
        """
        pass

    def setMaxUpdates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_updates(const ShadowManager self, int max_updates)
        
        /**
         * @brief Sets the maximum amount of updates per frame.
         * @details This controls the maximum amount of updated ShadowSources per frame.
         *   The ShadowManager will take the first <max_updates> ShadowSources, and
         *   generate shadow maps for them every frame. If there are more ShadowSources
         *   waiting to get updated than available updates, the sources are sorted by
         *   priority, and the update of the less important sources is delayed to the
         *   next frame.
         *
         *   If the update count is set too low, and there are a lot of ShadowSources
         *   waiting to get updated, artifacts will occur, and there might be ShadowSources
         *   which never get updated, due to low priority.
         *
         *   If an update count of 0 is passed, no updates will happen. This also means
         *   that there are no shadows. This is not recommended.
         *
         *   If an update count < 0 is passed, undefined behaviour occurs.
         *
         *   This method has to get called before ShadowManager::init, otherwise an
         *   assertion will get triggered.
         *
         * @param max_updates Maximum amoumt of updates
         */
        """
        pass

    def setScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scene(const ShadowManager self, NodePath scene_parent)
        
        /**
         * @brief Sets the target scene
         * @details This sets the target scene for rendering shadows. All shadow cameras
         *   will be parented to this scene to render shadows.
         *
         *   Usually the scene will be ShowBase.render. If the scene is an empty or
         *   invalid NodePath, an assertion will be triggered.
         *
         *   This method has to get called before calling ShadowManager::init, or an
         *   assertion will get triggered.
         *
         * @param scene_parent The target scene
         */
        """
        pass

    def setTagStateManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tag_state_manager(const ShadowManager self, TagStateManager tag_mgr)
        
        /**
         * @brief Sets the handle to the TagStageManager.
         * @details This sets the handle to the TagStateManager used by the pipeline.
         *   Usually this is RenderPipeline.get_tag_mgr().
         *
         *   This has to get called before ShadowManager::init, otherwise an assertion
         *   will get triggered.
         *
         * @param tag_mgr [description]
         */
        """
        pass

    def set_atlas_graphics_output(self, const_ShadowManager_self, GraphicsOutput_graphics_output): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_atlas_graphics_output(const ShadowManager self, GraphicsOutput graphics_output)
        
        /**
         * @brief Sets the handle to the Shadow targets output
         * @details This sets the handle to the GraphicsOutput of the shadow atlas.
         *   Usually this is RenderTarget.get_internal_buffer(), whereas the RenderTarget
         *   is the target of the ShadowStage.
         *
         *   This is used for creating display regions and attaching cameras to them,
         *   for performing shadow updates.
         *
         *   This has to get called before ShadowManager::init, otherwise an assertion
         *   will be triggered.
         *
         * @param graphics_output [description]
         */
        """
        pass

    def set_atlas_size(self, const_ShadowManager_self, int_atlas_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_atlas_size(const ShadowManager self, int atlas_size)
        
        /**
         * @brief Sets the shadow atlas size
         * @details This sets the desired shadow atlas size. It should be big enough
         *   to store all important shadow sources, with some buffer, because the shadow
         *   maps usually won't be fitted perfectly, so gaps can occur.
         *
         *   This has to get called before calling ShadowManager::init. When calling this
         *   method after initialization, an assertion will get triggered.
         *
         * @param atlas_size Size of the shadow atlas in pixels
         */
        """
        pass

    def set_max_updates(self, const_ShadowManager_self, int_max_updates): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_updates(const ShadowManager self, int max_updates)
        
        /**
         * @brief Sets the maximum amount of updates per frame.
         * @details This controls the maximum amount of updated ShadowSources per frame.
         *   The ShadowManager will take the first <max_updates> ShadowSources, and
         *   generate shadow maps for them every frame. If there are more ShadowSources
         *   waiting to get updated than available updates, the sources are sorted by
         *   priority, and the update of the less important sources is delayed to the
         *   next frame.
         *
         *   If the update count is set too low, and there are a lot of ShadowSources
         *   waiting to get updated, artifacts will occur, and there might be ShadowSources
         *   which never get updated, due to low priority.
         *
         *   If an update count of 0 is passed, no updates will happen. This also means
         *   that there are no shadows. This is not recommended.
         *
         *   If an update count < 0 is passed, undefined behaviour occurs.
         *
         *   This method has to get called before ShadowManager::init, otherwise an
         *   assertion will get triggered.
         *
         * @param max_updates Maximum amoumt of updates
         */
        """
        pass

    def set_scene(self, const_ShadowManager_self, NodePath_scene_parent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scene(const ShadowManager self, NodePath scene_parent)
        
        /**
         * @brief Sets the target scene
         * @details This sets the target scene for rendering shadows. All shadow cameras
         *   will be parented to this scene to render shadows.
         *
         *   Usually the scene will be ShowBase.render. If the scene is an empty or
         *   invalid NodePath, an assertion will be triggered.
         *
         *   This method has to get called before calling ShadowManager::init, or an
         *   assertion will get triggered.
         *
         * @param scene_parent The target scene
         */
        """
        pass

    def set_tag_state_manager(self, const_ShadowManager_self, TagStateManager_tag_mgr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tag_state_manager(const ShadowManager self, TagStateManager tag_mgr)
        
        /**
         * @brief Sets the handle to the TagStageManager.
         * @details This sets the handle to the TagStateManager used by the pipeline.
         *   Usually this is RenderPipeline.get_tag_mgr().
         *
         *   This has to get called before ShadowManager::init, otherwise an assertion
         *   will get triggered.
         *
         * @param tag_mgr [description]
         */
        """
        pass

    def update(self, const_ShadowManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const ShadowManager self)
        
        /**
         * @brief Updates the ShadowManager
         * @details This updates the ShadowManager, processing all shadow sources which
         *   need to get updated.
         *
         *   This first collects all sources which require an update, sorts them by priority,
         *   and then processes the first <max_updates> ShadowSources.
         *
         *   This may not get called before ShadowManager::init, or an assertion will be
         *   thrown.
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

    atlas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    atlas_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_update_slots_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d._rplight.ShadowManager' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d._rplight.ShadowManager' objects>"
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.ShadowManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E5640>'
        'atlas': None, # (!) real value is "<attribute 'atlas' of 'panda3d._rplight.ShadowManager' objects>"
        'atlas_size': None, # (!) real value is "<attribute 'atlas_size' of 'panda3d._rplight.ShadowManager' objects>"
        'getAtlas': None, # (!) real value is "<method 'getAtlas' of 'panda3d._rplight.ShadowManager' objects>"
        'getAtlasSize': None, # (!) real value is "<method 'getAtlasSize' of 'panda3d._rplight.ShadowManager' objects>"
        'getNumUpdateSlotsLeft': None, # (!) real value is "<method 'getNumUpdateSlotsLeft' of 'panda3d._rplight.ShadowManager' objects>"
        'get_atlas': None, # (!) real value is "<method 'get_atlas' of 'panda3d._rplight.ShadowManager' objects>"
        'get_atlas_size': None, # (!) real value is "<method 'get_atlas_size' of 'panda3d._rplight.ShadowManager' objects>"
        'get_num_update_slots_left': None, # (!) real value is "<method 'get_num_update_slots_left' of 'panda3d._rplight.ShadowManager' objects>"
        'init': None, # (!) real value is "<method 'init' of 'panda3d._rplight.ShadowManager' objects>"
        'num_update_slots_left': None, # (!) real value is "<attribute 'num_update_slots_left' of 'panda3d._rplight.ShadowManager' objects>"
        'setAtlasGraphicsOutput': None, # (!) real value is "<method 'setAtlasGraphicsOutput' of 'panda3d._rplight.ShadowManager' objects>"
        'setAtlasSize': None, # (!) real value is "<method 'setAtlasSize' of 'panda3d._rplight.ShadowManager' objects>"
        'setMaxUpdates': None, # (!) real value is "<method 'setMaxUpdates' of 'panda3d._rplight.ShadowManager' objects>"
        'setScene': None, # (!) real value is "<method 'setScene' of 'panda3d._rplight.ShadowManager' objects>"
        'setTagStateManager': None, # (!) real value is "<method 'setTagStateManager' of 'panda3d._rplight.ShadowManager' objects>"
        'set_atlas_graphics_output': None, # (!) real value is "<method 'set_atlas_graphics_output' of 'panda3d._rplight.ShadowManager' objects>"
        'set_atlas_size': None, # (!) real value is "<method 'set_atlas_size' of 'panda3d._rplight.ShadowManager' objects>"
        'set_max_updates': None, # (!) real value is "<method 'set_max_updates' of 'panda3d._rplight.ShadowManager' objects>"
        'set_scene': None, # (!) real value is "<method 'set_scene' of 'panda3d._rplight.ShadowManager' objects>"
        'set_tag_state_manager': None, # (!) real value is "<method 'set_tag_state_manager' of 'panda3d._rplight.ShadowManager' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d._rplight.ShadowManager' objects>"
    }


class TagStateManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * @brief This class handles all different tag states
     * @details The TagStateManager stores a list of RenderStates assigned to different
     *   steps in the pipeline. For example, there are a list of shadow states, which
     *   are applied whenever objects are rendered from a shadow camera.
     *
     *   The Manager also stores a list of all cameras used in the different stages,
     *   to keep track of the states used and to be able to attach new states.
     */
    """
    def applyState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_state(const TagStateManager self, str state, NodePath np, Shader shader, str name, int sort)
        
        /**
         * @brief Applies a given state for a pass to a NodePath
         * @details This applies a shader to the given NodePath which is used when the
         *   NodePath is rendered by any registered camera for that pass.
         *   It also disables color write depending on the pass.
         *
         * @param np The nodepath to apply the shader to
         * @param shader A handle to the shader to apply
         * @param name Name of the state, should be a unique identifier
         * @param sort Determines the sort with which the shader will be applied.
         */
        
        /**
         * @brief Applies a given state to a NodePath
         * @details This applies a shader to the given NodePath which is used when the
         *   NodePath is rendered by any registered camera of the container.
         *
         * @param container The container which is used to store the state
         * @param np The nodepath to apply the shader to
         * @param shader A handle to the shader to apply
         * @param name Name of the state, should be a unique identifier
         * @param sort Changes the sort with which the shader will be applied.
         */
        """
        pass

    def apply_state(self, const_TagStateManager_self, str_state, NodePath_np, Shader_shader, str_name, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_state(const TagStateManager self, str state, NodePath np, Shader shader, str name, int sort)
        
        /**
         * @brief Applies a given state for a pass to a NodePath
         * @details This applies a shader to the given NodePath which is used when the
         *   NodePath is rendered by any registered camera for that pass.
         *   It also disables color write depending on the pass.
         *
         * @param np The nodepath to apply the shader to
         * @param shader A handle to the shader to apply
         * @param name Name of the state, should be a unique identifier
         * @param sort Determines the sort with which the shader will be applied.
         */
        
        /**
         * @brief Applies a given state to a NodePath
         * @details This applies a shader to the given NodePath which is used when the
         *   NodePath is rendered by any registered camera of the container.
         *
         * @param container The container which is used to store the state
         * @param np The nodepath to apply the shader to
         * @param shader A handle to the shader to apply
         * @param name Name of the state, should be a unique identifier
         * @param sort Changes the sort with which the shader will be applied.
         */
        """
        pass

    def cleanupStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cleanup_states(const TagStateManager self)
        
        /**
         * @brief Cleans up all registered states.
         * @details This cleans up all states which were registered to the TagStateManager.
         *   It also calls Camera::clear_tag_states() on the main_cam_node and all attached
         *   cameras.
         */
        """
        pass

    def cleanup_states(self, const_TagStateManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cleanup_states(const TagStateManager self)
        
        /**
         * @brief Cleans up all registered states.
         * @details This cleans up all states which were registered to the TagStateManager.
         *   It also calls Camera::clear_tag_states() on the main_cam_node and all attached
         *   cameras.
         */
        """
        pass

    def getMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mask(const TagStateManager self, str container_name)
        
        /**
         * @brief Returns the render mask for the given state
         * @details This returns the mask of a given render pass, which can be used
         *   to either show or hide objects from this pass.
         *
         * @param container_name Name of the render-pass
         * @return Bit mask of the render pass
         */
        """
        pass

    def get_mask(self, const_TagStateManager_self, str_container_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mask(const TagStateManager self, str container_name)
        
        /**
         * @brief Returns the render mask for the given state
         * @details This returns the mask of a given render pass, which can be used
         *   to either show or hide objects from this pass.
         *
         * @param container_name Name of the render-pass
         * @return Bit mask of the render pass
         */
        """
        pass

    def registerCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_camera(const TagStateManager self, str state, Camera source)
        
        /**
         * @brief Registers a new camera which renders a certain pass
         * @details This registers a new camera which will be used to render the given
         *   pass. The TagStateManager will keep track of the camera and
         *   applies all registered states onto the camera with Camera::set_tag_state.
         *   It also applies the appropriate camera mask to the camera,
         *   and sets an initial state to disable color write depending on the pass.
         *
         * @param source Camera which will be used to render shadows
         */
        
        /**
         * @brief Registers a new camera to a given container
         * @details This registers a new camera to a container, and sets its initial
         *   state as well as the camera mask.
         *
         * @param container The container to add the camera to
         * @param source The camera to add
         */
        """
        pass

    def register_camera(self, const_TagStateManager_self, str_state, Camera_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_camera(const TagStateManager self, str state, Camera source)
        
        /**
         * @brief Registers a new camera which renders a certain pass
         * @details This registers a new camera which will be used to render the given
         *   pass. The TagStateManager will keep track of the camera and
         *   applies all registered states onto the camera with Camera::set_tag_state.
         *   It also applies the appropriate camera mask to the camera,
         *   and sets an initial state to disable color write depending on the pass.
         *
         * @param source Camera which will be used to render shadows
         */
        
        /**
         * @brief Registers a new camera to a given container
         * @details This registers a new camera to a container, and sets its initial
         *   state as well as the camera mask.
         *
         * @param container The container to add the camera to
         * @param source The camera to add
         */
        """
        pass

    def unregisterCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unregister_camera(const TagStateManager self, str state, Camera source)
        
        /**
         * @brief Unregisters a camera from the list of shadow cameras
         * @details This unregisters a camera from the list of shadows cameras. It also
         *   resets all tag states of the camera, and also its initial state.
         *
         * @param source Camera to unregister
         */
        
        /**
         * @brief Unregisters a camera from a container
         * @details This unregisters a camera from the list of cameras of a given
         *   container. It also resets all tag states of the camera, and also its initial
         *   state.
         *
         * @param source Camera to unregister
         */
        """
        pass

    def unregister_camera(self, const_TagStateManager_self, str_state, Camera_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unregister_camera(const TagStateManager self, str state, Camera source)
        
        /**
         * @brief Unregisters a camera from the list of shadow cameras
         * @details This unregisters a camera from the list of shadows cameras. It also
         *   resets all tag states of the camera, and also its initial state.
         *
         * @param source Camera to unregister
         */
        
        /**
         * @brief Unregisters a camera from a container
         * @details This unregisters a camera from the list of cameras of a given
         *   container. It also resets all tag states of the camera, and also its initial
         *   state.
         *
         * @param source Camera to unregister
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d._rplight.TagStateManager' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d._rplight.TagStateManager' objects>"
        '__doc__': '/**\n * @brief This class handles all different tag states\n * @details The TagStateManager stores a list of RenderStates assigned to different\n *   steps in the pipeline. For example, there are a list of shadow states, which\n *   are applied whenever objects are rendered from a shadow camera.\n *\n *   The Manager also stores a list of all cameras used in the different stages,\n *   to keep track of the states used and to be able to attach new states.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d._rplight.TagStateManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE44E5470>'
        'applyState': None, # (!) real value is "<method 'applyState' of 'panda3d._rplight.TagStateManager' objects>"
        'apply_state': None, # (!) real value is "<method 'apply_state' of 'panda3d._rplight.TagStateManager' objects>"
        'cleanupStates': None, # (!) real value is "<method 'cleanupStates' of 'panda3d._rplight.TagStateManager' objects>"
        'cleanup_states': None, # (!) real value is "<method 'cleanup_states' of 'panda3d._rplight.TagStateManager' objects>"
        'getMask': None, # (!) real value is "<method 'getMask' of 'panda3d._rplight.TagStateManager' objects>"
        'get_mask': None, # (!) real value is "<method 'get_mask' of 'panda3d._rplight.TagStateManager' objects>"
        'registerCamera': None, # (!) real value is "<method 'registerCamera' of 'panda3d._rplight.TagStateManager' objects>"
        'register_camera': None, # (!) real value is "<method 'register_camera' of 'panda3d._rplight.TagStateManager' objects>"
        'unregisterCamera': None, # (!) real value is "<method 'unregisterCamera' of 'panda3d._rplight.TagStateManager' objects>"
        'unregister_camera': None, # (!) real value is "<method 'unregister_camera' of 'panda3d._rplight.TagStateManager' objects>"
    }


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B2B6709890>'

__spec__ = None # (!) real value is "ModuleSpec(name='panda3d._rplight', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B2B6709890>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\panda3d\\\\_rplight.cp311-win_amd64.pyd')"

