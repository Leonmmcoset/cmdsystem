# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class DisplayInformation(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class contains various display information.
     */
    """
    def getAvailablePageFileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_available_page_file_size(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getAvailablePhysicalMemory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_available_physical_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getAvailableProcessVirtualMemory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_available_process_virtual_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getCpuBrandIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cpu_brand_index(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getCpuBrandString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cpu_brand_string(DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getCpuFrequency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cpu_frequency(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getCpuTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cpu_time()
        
        /**
         * Equivalent to the rdtsc processor instruction.
         */
        """
        pass

    def getCpuVendorString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cpu_vendor_string(DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getCpuVersionInformation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cpu_version_information(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getCurrentCpuFrequency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_cpu_frequency(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getCurrentDisplayModeIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_display_mode_index(DisplayInformation self)
        
        /**
         * Returns the index of the current display mode (determined at the time of
         * application start) in the display mode array, or -1 if this could not be
         * determined.
         */
        """
        pass

    def getDeviceId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_device_id(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getDisplayMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_mode(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def getDisplayModeBitsPerPixel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_mode_bits_per_pixel(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def getDisplayModeFullscreenOnly(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_mode_fullscreen_only(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def getDisplayModeHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_mode_height(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def getDisplayModeRefreshRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_mode_refresh_rate(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def getDisplayModes(self, *args, **kwargs): # real signature unknown
        pass

    def getDisplayModeWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_mode_width(const DisplayInformation self, int display_index)
        
        // Older interface for display modes.
        
        /**
         *
         */
        """
        pass

    def getDisplayState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_state(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getDriverBuild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_build(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getDriverDateDay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_date_day(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getDriverDateMonth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_date_month(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getDriverDateYear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_date_year(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getDriverProduct(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_product(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getDriverSubVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_sub_version(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getDriverVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_driver_version(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getMaximumCpuFrequency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_maximum_cpu_frequency(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getMaximumWindowHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_maximum_window_height(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getMaximumWindowWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_maximum_window_width(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getMemoryLoad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_memory_load(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getNumCpuCores(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_cpu_cores(const DisplayInformation self)
        
        /**
         * Returns the number of individual CPU cores in the system, or 0 if this
         * number is not available.  A hyperthreaded CPU counts once here.
         */
        """
        pass

    def getNumLogicalCpus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_logical_cpus(const DisplayInformation self)
        
        /**
         * Returns the number of logical CPU's in the system, or 0 if this number is
         * not available.  A hyperthreaded CPU counts as two or more here.
         */
        """
        pass

    def getOsPlatformId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_os_platform_id(const DisplayInformation self)
        
        /**
         * Returns -1 if not set.
         */
        """
        pass

    def getOsVersionBuild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_os_version_build(const DisplayInformation self)
        
        /**
         * Returns -1 if not set.
         */
        """
        pass

    def getOsVersionMajor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_os_version_major(const DisplayInformation self)
        
        /**
         * Returns -1 if not set.
         */
        """
        pass

    def getOsVersionMinor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_os_version_minor(const DisplayInformation self)
        
        /**
         * Returns -1 if not set.
         */
        """
        pass

    def getPageFaultCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page_fault_count(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getPageFileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page_file_size(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getPageFileUsage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page_file_usage(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getPeakPageFileUsage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_peak_page_file_usage(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getPeakProcessMemory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_peak_process_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getPhysicalMemory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_physical_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getProcessMemory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_process_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getProcessVirtualMemory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_process_virtual_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getShaderModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_model(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getTextureMemory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getTotalDisplayModes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_display_modes(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getVendorId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vendor_id(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getVideoMemory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_video_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def getWindowBitsPerPixel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_window_bits_per_pixel(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_available_page_file_size(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_available_page_file_size(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_available_physical_memory(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_available_physical_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_available_process_virtual_memory(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_available_process_virtual_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_cpu_brand_index(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cpu_brand_index(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_cpu_brand_string(self, DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cpu_brand_string(DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_cpu_frequency(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cpu_frequency(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_cpu_time(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cpu_time()
        
        /**
         * Equivalent to the rdtsc processor instruction.
         */
        """
        pass

    def get_cpu_vendor_string(self, DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cpu_vendor_string(DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_cpu_version_information(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cpu_version_information(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_current_cpu_frequency(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_cpu_frequency(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_current_display_mode_index(self, DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_display_mode_index(DisplayInformation self)
        
        /**
         * Returns the index of the current display mode (determined at the time of
         * application start) in the display mode array, or -1 if this could not be
         * determined.
         */
        """
        pass

    def get_device_id(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_device_id(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_display_mode(self, const_DisplayInformation_self, int_display_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_mode(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def get_display_modes(self, *args, **kwargs): # real signature unknown
        pass

    def get_display_mode_bits_per_pixel(self, const_DisplayInformation_self, int_display_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_mode_bits_per_pixel(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def get_display_mode_fullscreen_only(self, const_DisplayInformation_self, int_display_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_mode_fullscreen_only(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def get_display_mode_height(self, const_DisplayInformation_self, int_display_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_mode_height(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def get_display_mode_refresh_rate(self, const_DisplayInformation_self, int_display_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_mode_refresh_rate(const DisplayInformation self, int display_index)
        
        /**
         *
         */
        """
        pass

    def get_display_mode_width(self, const_DisplayInformation_self, int_display_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_mode_width(const DisplayInformation self, int display_index)
        
        // Older interface for display modes.
        
        /**
         *
         */
        """
        pass

    def get_display_state(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_state(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_driver_build(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_build(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_driver_date_day(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_date_day(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_driver_date_month(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_date_month(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_driver_date_year(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_date_year(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_driver_product(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_product(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_driver_sub_version(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_sub_version(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_driver_version(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_driver_version(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_maximum_cpu_frequency(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_maximum_cpu_frequency(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_maximum_window_height(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_maximum_window_height(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_maximum_window_width(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_maximum_window_width(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_memory_load(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_memory_load(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_num_cpu_cores(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_cpu_cores(const DisplayInformation self)
        
        /**
         * Returns the number of individual CPU cores in the system, or 0 if this
         * number is not available.  A hyperthreaded CPU counts once here.
         */
        """
        pass

    def get_num_logical_cpus(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_logical_cpus(const DisplayInformation self)
        
        /**
         * Returns the number of logical CPU's in the system, or 0 if this number is
         * not available.  A hyperthreaded CPU counts as two or more here.
         */
        """
        pass

    def get_os_platform_id(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_os_platform_id(const DisplayInformation self)
        
        /**
         * Returns -1 if not set.
         */
        """
        pass

    def get_os_version_build(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_os_version_build(const DisplayInformation self)
        
        /**
         * Returns -1 if not set.
         */
        """
        pass

    def get_os_version_major(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_os_version_major(const DisplayInformation self)
        
        /**
         * Returns -1 if not set.
         */
        """
        pass

    def get_os_version_minor(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_os_version_minor(const DisplayInformation self)
        
        /**
         * Returns -1 if not set.
         */
        """
        pass

    def get_page_fault_count(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page_fault_count(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_page_file_size(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page_file_size(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_page_file_usage(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page_file_usage(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_peak_page_file_usage(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_peak_page_file_usage(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_peak_process_memory(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_peak_process_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_physical_memory(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_physical_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_process_memory(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_process_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_process_virtual_memory(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_process_virtual_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_shader_model(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_model(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_texture_memory(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_total_display_modes(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_display_modes(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_vendor_id(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vendor_id(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_video_memory(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_video_memory(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def get_window_bits_per_pixel(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_window_bits_per_pixel(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def updateCpuFrequency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_cpu_frequency(const DisplayInformation self, int processor_number)
        
        /**
         *
         */
        """
        pass

    def updateMemoryInformation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_memory_information(const DisplayInformation self)
        
        /**
         *
         */
        """
        pass

    def update_cpu_frequency(self, const_DisplayInformation_self, int_processor_number): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_cpu_frequency(const DisplayInformation self, int processor_number)
        
        /**
         *
         */
        """
        pass

    def update_memory_information(self, const_DisplayInformation_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_memory_information(const DisplayInformation self)
        
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

    DSCreateDeviceError = 4
    DSCreateWindowError = 3
    DSDirect3dCreateError = 2
    DSSuccess = 1
    DSUnknown = 0
    DS_create_device_error = 4
    DS_create_window_error = 3
    DS_direct_3d_create_error = 2
    DS_success = 1
    DS_unknown = 0
    DtoolClassDict = {
        'DSCreateDeviceError': 4,
        'DSCreateWindowError': 3,
        'DSDirect3dCreateError': 2,
        'DSSuccess': 1,
        'DSUnknown': 0,
        'DS_create_device_error': 4,
        'DS_create_window_error': 3,
        'DS_direct_3d_create_error': 2,
        'DS_success': 1,
        'DS_unknown': 0,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.DisplayInformation' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.DisplayInformation' objects>"
        '__doc__': '/**\n * This class contains various display information.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DisplayInformation' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DCC20>'
        'getAvailablePageFileSize': None, # (!) real value is "<method 'getAvailablePageFileSize' of 'panda3d.core.DisplayInformation' objects>"
        'getAvailablePhysicalMemory': None, # (!) real value is "<method 'getAvailablePhysicalMemory' of 'panda3d.core.DisplayInformation' objects>"
        'getAvailableProcessVirtualMemory': None, # (!) real value is "<method 'getAvailableProcessVirtualMemory' of 'panda3d.core.DisplayInformation' objects>"
        'getCpuBrandIndex': None, # (!) real value is "<method 'getCpuBrandIndex' of 'panda3d.core.DisplayInformation' objects>"
        'getCpuBrandString': None, # (!) real value is "<method 'getCpuBrandString' of 'panda3d.core.DisplayInformation' objects>"
        'getCpuFrequency': None, # (!) real value is "<method 'getCpuFrequency' of 'panda3d.core.DisplayInformation' objects>"
        'getCpuTime': None, # (!) real value is '<staticmethod(<built-in method getCpuTime of type object at 0x00007FFCFE2DCC20>)>'
        'getCpuVendorString': None, # (!) real value is "<method 'getCpuVendorString' of 'panda3d.core.DisplayInformation' objects>"
        'getCpuVersionInformation': None, # (!) real value is "<method 'getCpuVersionInformation' of 'panda3d.core.DisplayInformation' objects>"
        'getCurrentCpuFrequency': None, # (!) real value is "<method 'getCurrentCpuFrequency' of 'panda3d.core.DisplayInformation' objects>"
        'getCurrentDisplayModeIndex': None, # (!) real value is "<method 'getCurrentDisplayModeIndex' of 'panda3d.core.DisplayInformation' objects>"
        'getDeviceId': None, # (!) real value is "<method 'getDeviceId' of 'panda3d.core.DisplayInformation' objects>"
        'getDisplayMode': None, # (!) real value is "<method 'getDisplayMode' of 'panda3d.core.DisplayInformation' objects>"
        'getDisplayModeBitsPerPixel': None, # (!) real value is "<method 'getDisplayModeBitsPerPixel' of 'panda3d.core.DisplayInformation' objects>"
        'getDisplayModeFullscreenOnly': None, # (!) real value is "<method 'getDisplayModeFullscreenOnly' of 'panda3d.core.DisplayInformation' objects>"
        'getDisplayModeHeight': None, # (!) real value is "<method 'getDisplayModeHeight' of 'panda3d.core.DisplayInformation' objects>"
        'getDisplayModeRefreshRate': None, # (!) real value is "<method 'getDisplayModeRefreshRate' of 'panda3d.core.DisplayInformation' objects>"
        'getDisplayModeWidth': None, # (!) real value is "<method 'getDisplayModeWidth' of 'panda3d.core.DisplayInformation' objects>"
        'getDisplayModes': None, # (!) real value is "<method 'getDisplayModes' of 'panda3d.core.DisplayInformation' objects>"
        'getDisplayState': None, # (!) real value is "<method 'getDisplayState' of 'panda3d.core.DisplayInformation' objects>"
        'getDriverBuild': None, # (!) real value is "<method 'getDriverBuild' of 'panda3d.core.DisplayInformation' objects>"
        'getDriverDateDay': None, # (!) real value is "<method 'getDriverDateDay' of 'panda3d.core.DisplayInformation' objects>"
        'getDriverDateMonth': None, # (!) real value is "<method 'getDriverDateMonth' of 'panda3d.core.DisplayInformation' objects>"
        'getDriverDateYear': None, # (!) real value is "<method 'getDriverDateYear' of 'panda3d.core.DisplayInformation' objects>"
        'getDriverProduct': None, # (!) real value is "<method 'getDriverProduct' of 'panda3d.core.DisplayInformation' objects>"
        'getDriverSubVersion': None, # (!) real value is "<method 'getDriverSubVersion' of 'panda3d.core.DisplayInformation' objects>"
        'getDriverVersion': None, # (!) real value is "<method 'getDriverVersion' of 'panda3d.core.DisplayInformation' objects>"
        'getMaximumCpuFrequency': None, # (!) real value is "<method 'getMaximumCpuFrequency' of 'panda3d.core.DisplayInformation' objects>"
        'getMaximumWindowHeight': None, # (!) real value is "<method 'getMaximumWindowHeight' of 'panda3d.core.DisplayInformation' objects>"
        'getMaximumWindowWidth': None, # (!) real value is "<method 'getMaximumWindowWidth' of 'panda3d.core.DisplayInformation' objects>"
        'getMemoryLoad': None, # (!) real value is "<method 'getMemoryLoad' of 'panda3d.core.DisplayInformation' objects>"
        'getNumCpuCores': None, # (!) real value is "<method 'getNumCpuCores' of 'panda3d.core.DisplayInformation' objects>"
        'getNumLogicalCpus': None, # (!) real value is "<method 'getNumLogicalCpus' of 'panda3d.core.DisplayInformation' objects>"
        'getOsPlatformId': None, # (!) real value is "<method 'getOsPlatformId' of 'panda3d.core.DisplayInformation' objects>"
        'getOsVersionBuild': None, # (!) real value is "<method 'getOsVersionBuild' of 'panda3d.core.DisplayInformation' objects>"
        'getOsVersionMajor': None, # (!) real value is "<method 'getOsVersionMajor' of 'panda3d.core.DisplayInformation' objects>"
        'getOsVersionMinor': None, # (!) real value is "<method 'getOsVersionMinor' of 'panda3d.core.DisplayInformation' objects>"
        'getPageFaultCount': None, # (!) real value is "<method 'getPageFaultCount' of 'panda3d.core.DisplayInformation' objects>"
        'getPageFileSize': None, # (!) real value is "<method 'getPageFileSize' of 'panda3d.core.DisplayInformation' objects>"
        'getPageFileUsage': None, # (!) real value is "<method 'getPageFileUsage' of 'panda3d.core.DisplayInformation' objects>"
        'getPeakPageFileUsage': None, # (!) real value is "<method 'getPeakPageFileUsage' of 'panda3d.core.DisplayInformation' objects>"
        'getPeakProcessMemory': None, # (!) real value is "<method 'getPeakProcessMemory' of 'panda3d.core.DisplayInformation' objects>"
        'getPhysicalMemory': None, # (!) real value is "<method 'getPhysicalMemory' of 'panda3d.core.DisplayInformation' objects>"
        'getProcessMemory': None, # (!) real value is "<method 'getProcessMemory' of 'panda3d.core.DisplayInformation' objects>"
        'getProcessVirtualMemory': None, # (!) real value is "<method 'getProcessVirtualMemory' of 'panda3d.core.DisplayInformation' objects>"
        'getShaderModel': None, # (!) real value is "<method 'getShaderModel' of 'panda3d.core.DisplayInformation' objects>"
        'getTextureMemory': None, # (!) real value is "<method 'getTextureMemory' of 'panda3d.core.DisplayInformation' objects>"
        'getTotalDisplayModes': None, # (!) real value is "<method 'getTotalDisplayModes' of 'panda3d.core.DisplayInformation' objects>"
        'getVendorId': None, # (!) real value is "<method 'getVendorId' of 'panda3d.core.DisplayInformation' objects>"
        'getVideoMemory': None, # (!) real value is "<method 'getVideoMemory' of 'panda3d.core.DisplayInformation' objects>"
        'getWindowBitsPerPixel': None, # (!) real value is "<method 'getWindowBitsPerPixel' of 'panda3d.core.DisplayInformation' objects>"
        'get_available_page_file_size': None, # (!) real value is "<method 'get_available_page_file_size' of 'panda3d.core.DisplayInformation' objects>"
        'get_available_physical_memory': None, # (!) real value is "<method 'get_available_physical_memory' of 'panda3d.core.DisplayInformation' objects>"
        'get_available_process_virtual_memory': None, # (!) real value is "<method 'get_available_process_virtual_memory' of 'panda3d.core.DisplayInformation' objects>"
        'get_cpu_brand_index': None, # (!) real value is "<method 'get_cpu_brand_index' of 'panda3d.core.DisplayInformation' objects>"
        'get_cpu_brand_string': None, # (!) real value is "<method 'get_cpu_brand_string' of 'panda3d.core.DisplayInformation' objects>"
        'get_cpu_frequency': None, # (!) real value is "<method 'get_cpu_frequency' of 'panda3d.core.DisplayInformation' objects>"
        'get_cpu_time': None, # (!) real value is '<staticmethod(<built-in method get_cpu_time of type object at 0x00007FFCFE2DCC20>)>'
        'get_cpu_vendor_string': None, # (!) real value is "<method 'get_cpu_vendor_string' of 'panda3d.core.DisplayInformation' objects>"
        'get_cpu_version_information': None, # (!) real value is "<method 'get_cpu_version_information' of 'panda3d.core.DisplayInformation' objects>"
        'get_current_cpu_frequency': None, # (!) real value is "<method 'get_current_cpu_frequency' of 'panda3d.core.DisplayInformation' objects>"
        'get_current_display_mode_index': None, # (!) real value is "<method 'get_current_display_mode_index' of 'panda3d.core.DisplayInformation' objects>"
        'get_device_id': None, # (!) real value is "<method 'get_device_id' of 'panda3d.core.DisplayInformation' objects>"
        'get_display_mode': None, # (!) real value is "<method 'get_display_mode' of 'panda3d.core.DisplayInformation' objects>"
        'get_display_mode_bits_per_pixel': None, # (!) real value is "<method 'get_display_mode_bits_per_pixel' of 'panda3d.core.DisplayInformation' objects>"
        'get_display_mode_fullscreen_only': None, # (!) real value is "<method 'get_display_mode_fullscreen_only' of 'panda3d.core.DisplayInformation' objects>"
        'get_display_mode_height': None, # (!) real value is "<method 'get_display_mode_height' of 'panda3d.core.DisplayInformation' objects>"
        'get_display_mode_refresh_rate': None, # (!) real value is "<method 'get_display_mode_refresh_rate' of 'panda3d.core.DisplayInformation' objects>"
        'get_display_mode_width': None, # (!) real value is "<method 'get_display_mode_width' of 'panda3d.core.DisplayInformation' objects>"
        'get_display_modes': None, # (!) real value is "<method 'get_display_modes' of 'panda3d.core.DisplayInformation' objects>"
        'get_display_state': None, # (!) real value is "<method 'get_display_state' of 'panda3d.core.DisplayInformation' objects>"
        'get_driver_build': None, # (!) real value is "<method 'get_driver_build' of 'panda3d.core.DisplayInformation' objects>"
        'get_driver_date_day': None, # (!) real value is "<method 'get_driver_date_day' of 'panda3d.core.DisplayInformation' objects>"
        'get_driver_date_month': None, # (!) real value is "<method 'get_driver_date_month' of 'panda3d.core.DisplayInformation' objects>"
        'get_driver_date_year': None, # (!) real value is "<method 'get_driver_date_year' of 'panda3d.core.DisplayInformation' objects>"
        'get_driver_product': None, # (!) real value is "<method 'get_driver_product' of 'panda3d.core.DisplayInformation' objects>"
        'get_driver_sub_version': None, # (!) real value is "<method 'get_driver_sub_version' of 'panda3d.core.DisplayInformation' objects>"
        'get_driver_version': None, # (!) real value is "<method 'get_driver_version' of 'panda3d.core.DisplayInformation' objects>"
        'get_maximum_cpu_frequency': None, # (!) real value is "<method 'get_maximum_cpu_frequency' of 'panda3d.core.DisplayInformation' objects>"
        'get_maximum_window_height': None, # (!) real value is "<method 'get_maximum_window_height' of 'panda3d.core.DisplayInformation' objects>"
        'get_maximum_window_width': None, # (!) real value is "<method 'get_maximum_window_width' of 'panda3d.core.DisplayInformation' objects>"
        'get_memory_load': None, # (!) real value is "<method 'get_memory_load' of 'panda3d.core.DisplayInformation' objects>"
        'get_num_cpu_cores': None, # (!) real value is "<method 'get_num_cpu_cores' of 'panda3d.core.DisplayInformation' objects>"
        'get_num_logical_cpus': None, # (!) real value is "<method 'get_num_logical_cpus' of 'panda3d.core.DisplayInformation' objects>"
        'get_os_platform_id': None, # (!) real value is "<method 'get_os_platform_id' of 'panda3d.core.DisplayInformation' objects>"
        'get_os_version_build': None, # (!) real value is "<method 'get_os_version_build' of 'panda3d.core.DisplayInformation' objects>"
        'get_os_version_major': None, # (!) real value is "<method 'get_os_version_major' of 'panda3d.core.DisplayInformation' objects>"
        'get_os_version_minor': None, # (!) real value is "<method 'get_os_version_minor' of 'panda3d.core.DisplayInformation' objects>"
        'get_page_fault_count': None, # (!) real value is "<method 'get_page_fault_count' of 'panda3d.core.DisplayInformation' objects>"
        'get_page_file_size': None, # (!) real value is "<method 'get_page_file_size' of 'panda3d.core.DisplayInformation' objects>"
        'get_page_file_usage': None, # (!) real value is "<method 'get_page_file_usage' of 'panda3d.core.DisplayInformation' objects>"
        'get_peak_page_file_usage': None, # (!) real value is "<method 'get_peak_page_file_usage' of 'panda3d.core.DisplayInformation' objects>"
        'get_peak_process_memory': None, # (!) real value is "<method 'get_peak_process_memory' of 'panda3d.core.DisplayInformation' objects>"
        'get_physical_memory': None, # (!) real value is "<method 'get_physical_memory' of 'panda3d.core.DisplayInformation' objects>"
        'get_process_memory': None, # (!) real value is "<method 'get_process_memory' of 'panda3d.core.DisplayInformation' objects>"
        'get_process_virtual_memory': None, # (!) real value is "<method 'get_process_virtual_memory' of 'panda3d.core.DisplayInformation' objects>"
        'get_shader_model': None, # (!) real value is "<method 'get_shader_model' of 'panda3d.core.DisplayInformation' objects>"
        'get_texture_memory': None, # (!) real value is "<method 'get_texture_memory' of 'panda3d.core.DisplayInformation' objects>"
        'get_total_display_modes': None, # (!) real value is "<method 'get_total_display_modes' of 'panda3d.core.DisplayInformation' objects>"
        'get_vendor_id': None, # (!) real value is "<method 'get_vendor_id' of 'panda3d.core.DisplayInformation' objects>"
        'get_video_memory': None, # (!) real value is "<method 'get_video_memory' of 'panda3d.core.DisplayInformation' objects>"
        'get_window_bits_per_pixel': None, # (!) real value is "<method 'get_window_bits_per_pixel' of 'panda3d.core.DisplayInformation' objects>"
        'updateCpuFrequency': None, # (!) real value is "<method 'updateCpuFrequency' of 'panda3d.core.DisplayInformation' objects>"
        'updateMemoryInformation': None, # (!) real value is "<method 'updateMemoryInformation' of 'panda3d.core.DisplayInformation' objects>"
        'update_cpu_frequency': None, # (!) real value is "<method 'update_cpu_frequency' of 'panda3d.core.DisplayInformation' objects>"
        'update_memory_information': None, # (!) real value is "<method 'update_memory_information' of 'panda3d.core.DisplayInformation' objects>"
    }


