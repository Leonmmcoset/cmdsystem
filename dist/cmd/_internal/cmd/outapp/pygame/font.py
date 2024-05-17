# encoding: utf-8
# module pygame.font
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\font.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module for loading and rendering fonts """
# no imports

# Variables with simple values

UCS4 = 1

# functions

def get_default_font(): # real signature unknown; restored from __doc__
    """
    get_default_font() -> string
    get the filename of the default font
    """
    return ""

def get_fonts(): # reliably restored by inspect
    """
    pygame.font.get_fonts() -> list
        get a list of system font names
    
        Returns the list of all found system fonts. Note that
        the names of the fonts will be all lowercase with spaces
        removed. This is how pygame internally stores the font
        names for matching.
    """
    pass

def get_init(): # real signature unknown; restored from __doc__
    """
    get_init() -> bool
    true if the font module is initialized
    """
    return False

def get_sdl_ttf_version(*args, **kwargs): # real signature unknown
    """
    get_init() -> bool
    true if the font module is initialized
    """
    pass

def init(): # real signature unknown; restored from __doc__
    """
    init() -> None
    initialize the font module
    """
    pass

def match_font(name, bold=False, italic=False): # reliably restored by inspect
    """
    pygame.font.match_font(name, bold=0, italic=0) -> name
        find the filename for the named system font
    
        This performs the same font search as the SysFont()
        function, only it returns the path to the TTF file
        that would be loaded. The font name can also be an
        iterable of font names or a string/bytes of comma-separated
        font names to try.
    
        If no match is found, None is returned.
    """
    pass

def quit(): # real signature unknown; restored from __doc__
    """
    quit() -> None
    uninitialize the font module
    """
    pass

def SysFont(name, size, bold=False, italic=False, constructor=None): # reliably restored by inspect
    """
    pygame.font.SysFont(name, size, bold=False, italic=False, constructor=None) -> Font
        Create a pygame Font from system font resources.
    
        This will search the system fonts for the given font
        name. You can also enable bold or italic styles, and
        the appropriate system font will be selected if available.
    
        This will always return a valid Font object, and will
        fallback on the builtin pygame font if the given font
        is not found.
    
        Name can also be an iterable of font names, a string of
        comma-separated font names, or a bytes of comma-separated
        font names, in which case the set of names will be searched
        in order. Pygame uses a small set of common font aliases. If the
        specific font you ask for is not available, a reasonable
        alternative may be used.
    
        If optional constructor is provided, it must be a function with
        signature constructor(fontpath, size, bold, italic) which returns
        a Font instance. If None, a pygame.font.Font object is created.
    """
    pass

# classes

class FontType(object):
    """
    Font(file_path=None, size=12) -> Font
    Font(file_path, size) -> Font
    Font(pathlib.Path, size) -> Font
    Font(object, size) -> Font
    create a new Font object from a file
    """
    def get_ascent(self): # real signature unknown; restored from __doc__
        """
        get_ascent() -> int
        get the ascent of the font
        """
        return 0

    def get_bold(self): # real signature unknown; restored from __doc__
        """
        get_bold() -> bool
        check if text will be rendered bold
        """
        return False

    def get_descent(self): # real signature unknown; restored from __doc__
        """
        get_descent() -> int
        get the descent of the font
        """
        return 0

    def get_height(self): # real signature unknown; restored from __doc__
        """
        get_height() -> int
        get the height of the font
        """
        return 0

    def get_italic(self): # real signature unknown; restored from __doc__
        """
        get_italic() -> bool
        check if the text will be rendered italic
        """
        return False

    def get_linesize(self): # real signature unknown; restored from __doc__
        """
        get_linesize() -> int
        get the line space of the font text
        """
        return 0

    def get_strikethrough(self): # real signature unknown; restored from __doc__
        """
        get_strikethrough() -> bool
        check if text will be rendered with a strikethrough
        """
        return False

    def get_underline(self): # real signature unknown; restored from __doc__
        """
        get_underline() -> bool
        check if text will be rendered with an underline
        """
        return False

    def metrics(self, text): # real signature unknown; restored from __doc__
        """
        metrics(text) -> list
        gets the metrics for each character in the passed string
        """
        return []

    def render(self, text, antialias, color, background=None): # real signature unknown; restored from __doc__
        """
        render(text, antialias, color, background=None) -> Surface
        draw text on a new Surface
        """
        pass

    def set_bold(self, bool): # real signature unknown; restored from __doc__
        """
        set_bold(bool) -> None
        enable fake rendering of bold text
        """
        pass

    def set_italic(self, bool): # real signature unknown; restored from __doc__
        """
        set_italic(bool) -> None
        enable fake rendering of italic text
        """
        pass

    def set_script(self, p_str): # real signature unknown; restored from __doc__
        """
        set_script(str) -> None
        set the script code for text shaping
        """
        pass

    def set_strikethrough(self, bool): # real signature unknown; restored from __doc__
        """
        set_strikethrough(bool) -> None
        control if text is rendered with a strikethrough
        """
        pass

    def set_underline(self, bool): # real signature unknown; restored from __doc__
        """
        set_underline(bool) -> None
        control if text is rendered with an underline
        """
        pass

    def size(self, text): # real signature unknown; restored from __doc__
        """
        size(text) -> (width, height)
        determine the amount of space needed to render text
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    bold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """bold -> bool
Gets or sets whether the font should be rendered in (faked) bold."""

    italic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """italic -> bool
Gets or sets whether the font should be rendered in (faked) italics."""

    strikethrough = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """strikethrough -> bool
Gets or sets whether the font should be rendered with a strikethrough."""

    underline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """underline -> bool
Gets or sets whether the font should be rendered with an underline."""



Font = FontType


# variables with complex values

_PYGAME_C_API = None # (!) real value is '<capsule object "pygame.font._PYGAME_C_API" at 0x000001F224768420>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F224762E50>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.font', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F224762E50>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\font.cp311-win_amd64.pyd')"

