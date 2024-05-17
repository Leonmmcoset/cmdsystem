# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


# Variables with simple values

Dtool_PyNativeInterface = 1

PTArray = 8
PTBlob = 7
PTClass = 10
PTDouble = 1
PTField = 9
PTInt = 2
PTInt64 = 4
PTInvalid = 0
PTString = 6
PTSwitch = 11
PTUint = 3
PTUint64 = 5
PT_array = 8
PT_blob = 7
PT_class = 10
PT_double = 1
PT_field = 9
PT_int = 2
PT_int64 = 4
PT_invalid = 0
PT_string = 6
PT_switch = 11
PT_uint = 3
PT_uint64 = 5

STBlob = 10
STBlob32 = 11
STChar = 19
STFloat64 = 8
STInt16 = 1
STInt16array = 12
STInt32 = 2
STInt32array = 13
STInt64 = 3
STInt8 = 0
STInt8array = 16
STInvalid = 20
STString = 9
STUint16 = 5
STUint16array = 14
STUint32 = 6
STUint32array = 15
STUint32uint8array = 18
STUint64 = 7
STUint8 = 4
STUint8array = 17
ST_blob = 10
ST_blob32 = 11
ST_char = 19
ST_float64 = 8
ST_int16 = 1
ST_int16array = 12
ST_int32 = 2
ST_int32array = 13
ST_int64 = 3
ST_int8 = 0
ST_int8array = 16
ST_invalid = 20
ST_string = 9
ST_uint16 = 5
ST_uint16array = 14
ST_uint32 = 6
ST_uint32array = 15
ST_uint32uint8array = 18
ST_uint64 = 7
ST_uint8 = 4
ST_uint8array = 17

# functions

def addFullscreenTestsize(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    add_fullscreen_testsize(int xsize, int ysize)
    
    // klunky interface since we cant pass array from python->C++
    """
    pass

def add_fullscreen_testsize(int_xsize, int_ysize): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    add_fullscreen_testsize(int xsize, int ysize)
    
    // klunky interface since we cant pass array from python->C++
    """
    pass

def allowAccessibilityShortcutKeys(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    allow_accessibility_shortcut_keys(bool allowKeys)
    """
    pass

def allow_accessibility_shortcut_keys(bool_allowKeys): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    allow_accessibility_shortcut_keys(bool allowKeys)
    """
    pass

def Dtool_BorrowThisReference(*args, **kwargs): # real signature unknown
    """
    Used to borrow 'this' pointer (to, from)
    Assumes no ownership.
    """
    pass

def getParticlePath(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    get_particle_path()
    """
    pass

def get_particle_path(): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    get_particle_path()
    """
    pass

def initAppForGui(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    init_app_for_gui()
    """
    pass

def init_app_for_gui(): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    init_app_for_gui()
    """
    pass

def queryFullscreenTestresult(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    query_fullscreen_testresult(int xsize, int ysize)
    """
    pass

def query_fullscreen_testresult(int_xsize, int_ysize): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    query_fullscreen_testresult(int xsize, int ysize)
    """
    pass

def runtestFullscreenSizes(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    runtest_fullscreen_sizes(GraphicsWindow win)
    """
    pass

def runtest_fullscreen_sizes(GraphicsWindow_win): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    runtest_fullscreen_sizes(GraphicsWindow win)
    """
    pass

def storeAccessibilityShortcutKeys(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    store_accessibility_shortcut_keys()
    
    // to handle windows stickykeys
    """
    pass

def store_accessibility_shortcut_keys(): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    store_accessibility_shortcut_keys()
    
    // to handle windows stickykeys
    """
    pass

def throwNewFrame(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    throw_new_frame()
    """
    pass

def throw_new_frame(): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    throw_new_frame()
    """
    pass

# classes

from .CConnectionRepository import CConnectionRepository
from .CInterval import CInterval
from .CConstraintInterval import CConstraintInterval
from .CConstrainHprInterval import CConstrainHprInterval
from .CConstrainPosHprInterval import CConstrainPosHprInterval
from .CConstrainPosInterval import CConstrainPosInterval
from .CConstrainTransformInterval import CConstrainTransformInterval
from .CDistributedSmoothNodeBase import CDistributedSmoothNodeBase
from .CIntervalManager import CIntervalManager
from .CLerpInterval import CLerpInterval
from .CLerpAnimEffectInterval import CLerpAnimEffectInterval
from .CLerpNodePathInterval import CLerpNodePathInterval
from .CMetaInterval import CMetaInterval
from .CMotionTrail import CMotionTrail
from .DCKeywordList import DCKeywordList
from .DCPackerInterface import DCPackerInterface
from .DCField import DCField
from .DCParameter import DCParameter
from .DCArrayParameter import DCArrayParameter
from .DCAtomicField import DCAtomicField
from .DCDeclaration import DCDeclaration
from .DCClass import DCClass
from .DCClassParameter import DCClassParameter
from .DCFile import DCFile
from .DCKeyword import DCKeyword
from .DCMolecularField import DCMolecularField
from .DCPackData import DCPackData
from .DCPacker import DCPacker
from .DCSimpleParameter import DCSimpleParameter
from .DCSwitch import DCSwitch
from .DCSwitchParameter import DCSwitchParameter
from .DCTypedef import DCTypedef
from .LerpBlendType import LerpBlendType
from .EaseInBlendType import EaseInBlendType
from .EaseInOutBlendType import EaseInOutBlendType
from .EaseOutBlendType import EaseOutBlendType
from .HideInterval import HideInterval
from .NoBlendType import NoBlendType
from .ShowInterval import ShowInterval
from .SmoothMover import SmoothMover
from .WaitInterval import WaitInterval
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000014442849D50>'

__spec__ = None # (!) real value is "ModuleSpec(name='panda3d.direct', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000014442849D50>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\panda3d\\\\direct.cp311-win_amd64.pyd')"

