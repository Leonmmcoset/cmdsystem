# encoding: utf-8
# module pygame.mask
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\mask.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module for image masks. """
# no imports

# functions

def from_surface(surface): # real signature unknown; restored from __doc__
    """
    from_surface(surface) -> Mask
    from_surface(surface, threshold=127) -> Mask
    Creates a Mask from the given surface
    """
    return Mask

def from_threshold(surface, color): # real signature unknown; restored from __doc__
    """
    from_threshold(surface, color) -> Mask
    from_threshold(surface, color, threshold=(0, 0, 0, 255), othersurface=None, palette_colors=1) -> Mask
    Creates a mask by thresholding Surfaces
    """
    return Mask

# classes

class MaskType(object):
    """
    Mask(size=(width, height)) -> Mask
    Mask(size=(width, height), fill=False) -> Mask
    pygame object for representing 2D bitmasks
    """
    def angle(self): # real signature unknown; restored from __doc__
        """
        angle() -> theta
        Returns the orientation of the set bits
        """
        pass

    def centroid(self): # real signature unknown; restored from __doc__
        """
        centroid() -> (x, y)
        Returns the centroid of the set bits
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        clear() -> None
        Sets all bits to 0
        """
        pass

    def connected_component(self): # real signature unknown; restored from __doc__
        """
        connected_component() -> Mask
        connected_component(pos) -> Mask
        Returns a mask containing a connected component
        """
        return Mask

    def connected_components(self): # real signature unknown; restored from __doc__
        """
        connected_components() -> [Mask, ...]
        connected_components(minimum=0) -> [Mask, ...]
        Returns a list of masks of connected components
        """
        pass

    def convolve(self, other): # real signature unknown; restored from __doc__
        """
        convolve(other) -> Mask
        convolve(other, output=None, offset=(0, 0)) -> Mask
        Returns the convolution of this mask with another mask
        """
        return Mask

    def copy(self): # real signature unknown; restored from __doc__
        """
        copy() -> Mask
        Returns a new copy of the mask
        """
        return Mask

    def count(self): # real signature unknown; restored from __doc__
        """
        count() -> bits
        Returns the number of set bits
        """
        pass

    def draw(self, other, offset): # real signature unknown; restored from __doc__
        """
        draw(other, offset) -> None
        Draws a mask onto another
        """
        pass

    def erase(self, other, offset): # real signature unknown; restored from __doc__
        """
        erase(other, offset) -> None
        Erases a mask from another
        """
        pass

    def fill(self): # real signature unknown; restored from __doc__
        """
        fill() -> None
        Sets all bits to 1
        """
        pass

    def get_at(self, pos): # real signature unknown; restored from __doc__
        """
        get_at(pos) -> int
        Gets the bit at the given position
        """
        return 0

    def get_bounding_rects(self): # real signature unknown; restored from __doc__
        """
        get_bounding_rects() -> [Rect, ...]
        Returns a list of bounding rects of connected components
        """
        pass

    def get_rect(self, **kwargs): # real signature unknown; restored from __doc__
        """
        get_rect(**kwargs) -> Rect
        Returns a Rect based on the size of the mask
        """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """
        get_size() -> (width, height)
        Returns the size of the mask
        """
        pass

    def invert(self): # real signature unknown; restored from __doc__
        """
        invert() -> None
        Flips all the bits
        """
        pass

    def outline(self): # real signature unknown; restored from __doc__
        """
        outline() -> [(x, y), ...]
        outline(every=1) -> [(x, y), ...]
        Returns a list of points outlining an object
        """
        pass

    def overlap(self, other, offset): # real signature unknown; restored from __doc__
        """
        overlap(other, offset) -> (x, y)
        overlap(other, offset) -> None
        Returns the point of intersection
        """
        pass

    def overlap_area(self, other, offset): # real signature unknown; restored from __doc__
        """
        overlap_area(other, offset) -> numbits
        Returns the number of overlapping set bits
        """
        pass

    def overlap_mask(self, other, offset): # real signature unknown; restored from __doc__
        """
        overlap_mask(other, offset) -> Mask
        Returns a mask of the overlapping set bits
        """
        return Mask

    def scale(self, (width, height)): # real signature unknown; restored from __doc__
        """
        scale((width, height)) -> Mask
        Resizes a mask
        """
        return Mask

    def set_at(self, pos): # real signature unknown; restored from __doc__
        """
        set_at(pos) -> None
        set_at(pos, value=1) -> None
        Sets the bit at the given position
        """
        pass

    def to_surface(self): # real signature unknown; restored from __doc__
        """
        to_surface() -> Surface
        to_surface(surface=None, setsurface=None, unsetsurface=None, setcolor=(255, 255, 255, 255), unsetcolor=(0, 0, 0, 255), dest=(0, 0)) -> Surface
        Returns a surface with the mask drawn on it
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """
        copy() -> Mask
        Returns a new copy of the mask
        """
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


Mask = MaskType


# variables with complex values

_PYGAME_C_API = None # (!) real value is '<capsule object "pygame.mask._PYGAME_C_API" at 0x0000024028C8BA50>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024028D32210>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.mask', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024028D32210>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\mask.cp311-win_amd64.pyd')"

