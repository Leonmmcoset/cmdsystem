# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
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

def loadEggData(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    load_egg_data(EggData data, int cs)
    """
    pass

def loadEggFile(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    load_egg_file(const Filename filename, int cs, BamCacheRecord record)
    """
    pass

def load_egg_data(EggData_data, int_cs): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    load_egg_data(EggData data, int cs)
    """
    pass

def load_egg_file(const_Filename_filename, int_cs, BamCacheRecord_record): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    load_egg_file(const Filename filename, int cs, BamCacheRecord record)
    """
    pass

def parseEggData(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    parse_egg_data(str egg_syntax)
    
    /**
     * Parses an EggData from the raw egg syntax.
     */
    """
    pass

def parseEggNode(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    parse_egg_node(str egg_syntax)
    
    /**
     * Parses a single egg node from the raw egg syntax.
     */
    """
    pass

def parse_egg_data(str_egg_syntax): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    parse_egg_data(str egg_syntax)
    
    /**
     * Parses an EggData from the raw egg syntax.
     */
    """
    pass

def parse_egg_node(str_egg_syntax): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    parse_egg_node(str egg_syntax)
    
    /**
     * Parses a single egg node from the raw egg syntax.
     */
    """
    pass

def saveEggData(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    save_egg_data(EggData data, PandaNode node)
    """
    pass

def saveEggFile(*args, **kwargs): # real signature unknown
    """
    C++ Interface:
    save_egg_file(const Filename filename, PandaNode node, int cs)
    """
    pass

def save_egg_data(EggData_data, PandaNode_node): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    save_egg_data(EggData data, PandaNode node)
    """
    pass

def save_egg_file(const_Filename_filename, PandaNode_node, int_cs): # real signature unknown; restored from __doc__
    """
    C++ Interface:
    save_egg_file(const Filename filename, PandaNode node, int cs)
    """
    pass

# classes

from .EggObject import EggObject
from .EggNamedObject import EggNamedObject
from .EggNode import EggNode
from .EggAnimData import EggAnimData
from .EggAnimPreload import EggAnimPreload
from .EggAttributes import EggAttributes
from .EggGroupNode import EggGroupNode
from .EggRenderMode import EggRenderMode
from .EggTransform import EggTransform
from .EggGroup import EggGroup
from .EggBin import EggBin
from .EggBinMaker import EggBinMaker
from .EggComment import EggComment
from .EggPrimitive import EggPrimitive
from .EggCompositePrimitive import EggCompositePrimitive
from .EggCoordinateSystem import EggCoordinateSystem
from .EggCurve import EggCurve
from .EggData import EggData
from .EggFilenameNode import EggFilenameNode
from .EggExternalReference import EggExternalReference
from .EggNameUniquifier import EggNameUniquifier
from .EggGroupUniquifier import EggGroupUniquifier
from .EggLine import EggLine
from .EggMaterial import EggMaterial
from .EggMaterialCollection import EggMaterialCollection
from .EggNurbsCurve import EggNurbsCurve
from .EggSurface import EggSurface
from .EggNurbsSurface import EggNurbsSurface
from .EggPatch import EggPatch
from .EggPoint import EggPoint
from .EggPolygon import EggPolygon
from .EggPolysetMaker import EggPolysetMaker
from .EggPoolUniquifier import EggPoolUniquifier
from .EggSAnimData import EggSAnimData
from .EggSwitchCondition import EggSwitchCondition
from .EggSwitchConditionDistance import EggSwitchConditionDistance
from .EggTable import EggTable
from .EggTexture import EggTexture
from .EggTextureCollection import EggTextureCollection
from .EggTriangleFan import EggTriangleFan
from .EggTriangleStrip import EggTriangleStrip
from .EggUserData import EggUserData
from .EggVertex import EggVertex
from .EggVertexAux import EggVertexAux
from .EggVertexPool import EggVertexPool
from .EggVertexUV import EggVertexUV
from .EggXfmAnimData import EggXfmAnimData
from .EggXfmSAnim import EggXfmSAnim
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002ADE16F9A90>'

__spec__ = None # (!) real value is "ModuleSpec(name='panda3d.egg', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002ADE16F9A90>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\panda3d\\\\egg.cp311-win_amd64.pyd')"

