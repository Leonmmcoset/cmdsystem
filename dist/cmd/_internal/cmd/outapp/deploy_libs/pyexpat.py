# encoding: utf-8
# module deploy_libs.pyexpat
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\deploy_libs\pyexpat.pyd
# by generator 1.147
""" Python wrapper for Expat parser. """

# imports
import pyexpat.errors as errors # <module 'pyexpat.errors'>
import pyexpat.model as model # <module 'pyexpat.model'>
from pyexpat import XMLParserType


# Variables with simple values

EXPAT_VERSION = 'expat_2.5.0'

native_encoding = 'UTF-8'

XML_PARAM_ENTITY_PARSING_ALWAYS = 2
XML_PARAM_ENTITY_PARSING_NEVER = 0

XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE = 1

# functions

def ErrorString(*args, **kwargs): # real signature unknown
    """ Returns string error for given number. """
    pass

def ParserCreate(*args, **kwargs): # real signature unknown
    """ Return a new XML parser object. """
    pass

# classes

class ExpatError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



error = ExpatError


# variables with complex values

expat_CAPI = None # (!) real value is '<capsule object "pyexpat.expat_CAPI" at 0x000001F549A02550>'

features = [
    (
        'sizeof(XML_Char)',
        1,
    ),
    (
        'sizeof(XML_LChar)',
        1,
    ),
    (
        'XML_DTD',
        0,
    ),
    (
        'XML_CONTEXT_BYTES',
        1024,
    ),
    (
        'XML_NS',
        0,
    ),
    (
        'XML_BLAP_MAX_AMP',
        100,
    ),
    (
        'XML_BLAP_ACT_THRES',
        8388608,
    ),
]

version_info = (
    2,
    5,
    0,
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F5499BA250>'

__spec__ = None # (!) real value is "ModuleSpec(name='deploy_libs.pyexpat', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F5499BA250>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\deploy_libs\\\\pyexpat.pyd')"

