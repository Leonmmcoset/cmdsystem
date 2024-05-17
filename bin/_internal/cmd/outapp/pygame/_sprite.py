# encoding: utf-8
# module pygame._sprite
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\_sprite.cp311-win_amd64.pyd
# by generator 1.147
"""
pygame module with basic game object classes

This module contains several simple classes to be used within games. There
are the main Sprite class and several Group classes that contain Sprites.
The use of these classes is entirely optional when using Pygame. The classes
are fairly lightweight and only provide a starting place for the code
that is common to most games.

The Sprite class is intended to be used as a base class for the different
types of objects in the game. There is also a base Group class that simply
stores sprites. A game could create new types of Group classes that operate
on specially customized Sprite instances they contain.

The basic Sprite class can draw the Sprites it contains to a Surface. The
Group.draw() method requires that each Sprite have a Surface.image attribute
and a Surface.rect. The Group.clear() method requires these same attributes
and can be used to erase all the Sprites with background. There are also
more advanced Groups: pygame.sprite.RenderUpdates() and
pygame.sprite.OrderedUpdates().

Lastly, this module contains several collision functions. These help find
sprites inside multiple groups that have intersecting bounding rectangles.
To find the collisions, the Sprites are required to have a Surface.rect
attribute assigned.

The groups are designed for high efficiency in removing and adding Sprites
to them. They also allow cheap testing to see if a Sprite already exists in
a Group. A given Sprite can exist in any number of groups. A game could use
some groups to control object rendering, and a completely separate set of
groups to control interaction or player movement. Instead of adding type
attributes or bools to a derived Sprite class, consider keeping the
Sprites inside organized Groups. This will allow for easier lookup later
in the game.

Sprites and Groups manage their relationships with the add() and remove()
methods. These methods can accept a single or multiple group arguments for
membership.  The default initializers for these classes also take a
single group or list of groups as arguments for initial membership. It is safe
to repeatedly add and remove the same Sprite from a Group.

While it is possible to design sprite and group classes that don't derive
from the Sprite and AbstractGroup classes below, it is strongly recommended
that you extend those when you create a new Sprite or Group class.

Sprites are not thread safe, so lock them yourself if using threads.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import pygame as pygame # C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\__init__.py
from pygame.mask import from_surface

from pygame.time import get_ticks


# functions

def collide_circle(left, right): # real signature unknown; restored from __doc__
    """
    detect collision between two sprites using circles
    
        pygame.sprite.collide_circle(left, right): return bool
    
        Tests for collision between two sprites by testing whether two circles
        centered on the sprites overlap. If the sprites have a "radius" attribute,
        then that radius is used to create the circle; otherwise, a circle is
        created that is big enough to completely enclose the sprite's rect as
        given by the "rect" attribute. This function is intended to be passed as
        a collided callback function to the *collide functions. Sprites must have a
        "rect" and an optional "radius" attribute.
    
        New in pygame 1.8.0
    """
    return False

def collide_mask(SpriteLeft, SpriteRight): # real signature unknown; restored from __doc__
    """
    collision detection between two sprites, using masks.
    
        pygame.sprite.collide_mask(SpriteLeft, SpriteRight): bool
    
        Tests for collision between two sprites by testing if their bitmasks
        overlap. If the sprites have a "mask" attribute, that is used as the mask;
        otherwise, a mask is created from the sprite image. Intended to be passed
        as a collided callback function to the *collide functions. Sprites must
        have a "rect" and an optional "mask" attribute.
    
        New in pygame 1.8.0
    """
    pass

def collide_rect(left, right): # real signature unknown; restored from __doc__
    """
    collision detection between two sprites, using rects.
    
        pygame.sprite.collide_rect(left, right): return bool
    
        Tests for collision between two sprites. Uses the pygame.Rect colliderect
        function to calculate the collision. It is intended to be passed as a
        collided callback function to the *collide functions. Sprites must have
        "rect" attributes.
    
        New in pygame 1.8.0
    """
    return False

def groupcollide(groupa, groupb, dokilla, dokillb): # real signature unknown; restored from __doc__
    """
    detect collision between a group and another group
    
        pygame.sprite.groupcollide(groupa, groupb, dokilla, dokillb):
            return dict
    
        Given two groups, this will find the intersections between all sprites in
        each group. It returns a dictionary of all sprites in the first group that
        collide. The value for each item in the dictionary is a list of the sprites
        in the second group it collides with. The two dokill arguments control if
        the sprites from either group will be automatically removed from all
        groups. Collided is a callback function used to calculate if two sprites
        are colliding. it should take two sprites as values, and return a bool
        value indicating if they are colliding. If collided is not passed, all
        sprites must have a "rect" value, which is a rectangle of the sprite area
        that will be used to calculate the collision.
    """
    return {}

def spritecollide(sprite, group, dokill, collided=None): # real signature unknown; restored from __doc__
    """
    find Sprites in a Group that intersect another Sprite
    
        pygame.sprite.spritecollide(sprite, group, dokill, collided=None):
            return Sprite_list
    
        Return a list containing all Sprites in a Group that intersect with another
        Sprite. Intersection is determined by comparing the Sprite.rect attribute
        of each Sprite.
    
        The dokill argument is a bool. If set to True, all Sprites that collide
        will be removed from the Group.
    
        The collided argument is a callback function used to calculate if two
        sprites are colliding. it should take two sprites as values, and return a
        bool value indicating if they are colliding. If collided is not passed, all
        sprites must have a "rect" value, which is a rectangle of the sprite area,
        which will be used to calculate the collision.
    """
    pass

def spritecollideany(sprite, group): # real signature unknown; restored from __doc__
    """
    finds any sprites in a group that collide with the given sprite
    
        pygame.sprite.spritecollideany(sprite, group): return sprite
    
        Given a sprite and a group of sprites, this will return return any single
        sprite that collides with with the given sprite. If there are no
        collisions, then this returns None.
    
        If you don't need all the features of the spritecollide function, this
        function will be a bit quicker.
    
        Collided is a callback function used to calculate if two sprites are
        colliding. It should take two sprites as values and return a bool value
        indicating if they are colliding. If collided is not passed, then all
        sprites must have a "rect" value, which is a rectangle of the sprite area,
        which will be used to calculate the collision.
    """
    return pygame.sprite

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class AbstractGroup(object):
    """
    base class for containers of sprites
    
        AbstractGroup does everything needed to behave as a normal group. You can
        easily subclass a new group class from this or the other groups below if
        you want to add more features.
    
        Any AbstractGroup-derived sprite groups act like sequences and support
        iteration, len, and so on.
    """
    def add(self, sprite, p_list, group, *more): # real signature unknown; restored from __doc__
        """
        add sprite(s) to group
        
                Group.add(sprite, list, group, ...): return None
        
                Adds a sprite or sequence of sprites to a group.
        """
        pass

    def add_internal(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, surface, bgd): # real signature unknown; restored from __doc__
        """
        erase the previous position of all sprites
        
                Group.clear(surface, bgd): return None
        
                Clears the area under every drawn sprite in the group. The bgd
                argument should be Surface which is the same dimensions as the
                screen surface. The bgd could also be a function which accepts
                the given surface and the area to be cleared as arguments.
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        copy a group with all the same sprites
        
                Group.copy(): return Group
        
                Returns a copy of the group that is an instance of the same class
                and has the same sprites in it.
        """
        return Group

    def draw(self, surface): # real signature unknown; restored from __doc__
        """
        draw all sprites onto the surface
        
                Group.draw(surface): return None
        
                Draws all of the member sprites onto the given surface.
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        remove all sprites
        
                Group.empty(): return None
        
                Removes all the sprites from the group.
        """
        pass

    def has(self, sprite_or_group, *more): # real signature unknown; restored from __doc__
        """
        ask if group has a sprite or sprites
        
                Group.has(sprite or group, ...): return bool
        
                Returns True if the given sprite or sprites are contained in the
                group. Alternatively, you can get the same information using the
                'in' operator, e.g. 'sprite in group', 'subgroup in group'.
        """
        return False

    def has_internal(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, sprite, p_list, or_group, *more): # real signature unknown; restored from __doc__
        """
        remove sprite(s) from group
        
                Group.remove(sprite, list, or group, ...): return None
        
                Removes a sprite or sequence of sprites from a group.
        """
        pass

    def remove_internal(self, *args, **kwargs): # real signature unknown
        pass

    def sprites(self, *args, **kwargs): # real signature unknown
        """
        get a list of sprites in the group
        
                Group.sprite(): return list
        
                Returns an object that can be looped over with a 'for' loop. (For now,
                it is always a list, but this could change in a future version of
                pygame.) Alternatively, you can get the same information by iterating
                directly over the sprite group, e.g. 'for sprite in group'.
        """
        pass

    def update(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        call the update method of every member sprite
        
                Group.update(*args, **kwargs): return None
        
                Calls the update method of every member sprite. All arguments that
                were passed to this method are passed to the Sprite update function.
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """
        return number of sprites in group
        
                Group.len(group): return int
        
                Returns the number of sprites contained in the group.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    lostsprites = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    spritedict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _spritegroup = True
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002044EFDBF30>'


class collide_circle_ratio(object):
    """
    detect collision between two sprites using scaled circles
    
        This callable class checks for collisions between two sprites using a
        scaled version of a sprite's radius. It is created with a ratio as the
        argument to the constructor. The instance is then intended to be passed as
        a collided callback function to the *collide functions.
    
        New in pygame 1.8.1
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """
        detect collision between two sprites using scaled circles
        
                pygame.sprite.collide_circle_radio(ratio)(left, right): return bool
        
                Tests for collision between two sprites by testing whether two circles
                centered on the sprites overlap after scaling the circle's radius by
                the stored ratio. If the sprites have a "radius" attribute, that is
                used to create the circle; otherwise, a circle is created that is big
                enough to completely enclose the sprite's rect as given by the "rect"
                attribute. Intended to be passed as a collided callback function to the
                *collide functions. Sprites must have a "rect" and an optional "radius"
                attribute.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        creates a new collide_circle_ratio callable instance
        
                The given ratio is expected to be a floating point value used to scale
                the underlying sprite radius before checking for collisions.
        
                When the ratio is ratio=1.0, then it behaves exactly like the
                collide_circle method.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pygame._sprite\', \'__doc__\': "detect collision between two sprites using scaled circles\\n\\n    This callable class checks for collisions between two sprites using a\\n    scaled version of a sprite\'s radius. It is created with a ratio as the\\n    argument to the constructor. The instance is then intended to be passed as\\n    a collided callback function to the *collide functions.\\n\\n    New in pygame 1.8.1\\n\\n    ", \'__init__\': <cyfunction collide_circle_ratio.__init__ at 0x000002044F04F850>, \'__call__\': <cyfunction collide_circle_ratio.__call__ at 0x000002044F04F920>, \'__dict__\': <attribute \'__dict__\' of \'collide_circle_ratio\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'collide_circle_ratio\' objects>})'


class collide_rect_ratio(object):
    """
    A callable class that checks for collisions using scaled rects
    
        The class checks for collisions between two sprites using a scaled version
        of the sprites' rects. Is created with a ratio; the instance is then
        intended to be passed as a collided callback function to the *collide
        functions.
    
        New in pygame 1.8.1
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """
        detect collision between two sprites using scaled rects
        
                pygame.sprite.collide_rect_ratio(ratio)(left, right): return bool
        
                Tests for collision between two sprites. Uses the pygame.Rect
                colliderect function to calculate the collision after scaling the rects
                by the stored ratio. Sprites must have "rect" attributes.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        create a new collide_rect_ratio callable
        
                Ratio is expected to be a floating point value used to scale
                the underlying sprite rect before checking for collisions.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pygame._sprite\', \'__doc__\': "A callable class that checks for collisions using scaled rects\\n\\n    The class checks for collisions between two sprites using a scaled version\\n    of the sprites\' rects. Is created with a ratio; the instance is then\\n    intended to be passed as a collided callback function to the *collide\\n    functions.\\n\\n    New in pygame 1.8.1\\n\\n    ", \'__init__\': <cyfunction collide_rect_ratio.__init__ at 0x000002044F04F510>, \'__call__\': <cyfunction collide_rect_ratio.__call__ at 0x000002044F04F5E0>, \'__dict__\': <attribute \'__dict__\' of \'collide_rect_ratio\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'collide_rect_ratio\' objects>})'


class Sprite(object):
    """
    simple base class for visible game objects
    
        pygame.sprite.Sprite(*groups): return Sprite
    
        The base class for visible game objects. Derived classes will want to
        override the Sprite.update() method and assign Sprite.image and Sprite.rect
        attributes.  The initializer can accept any number of Group instances that
        the Sprite will become a member of.
    
        When subclassing the Sprite class, be sure to call the base initializer
        before adding the Sprite to Groups.
    """
    def add(self, *groups): # real signature unknown; restored from __doc__
        """
        add the sprite to groups
        
                Sprite.add(*groups): return None
        
                Any number of Group instances can be passed as arguments. The
                Sprite will be added to the Groups it is not already a member of.
        """
        pass

    def add_internal(self, *args, **kwargs): # real signature unknown
        pass

    def alive(self): # real signature unknown; restored from __doc__
        """
        does the sprite belong to any groups
        
                Sprite.alive(): return bool
        
                Returns True when the Sprite belongs to one or more Groups.
        """
        return False

    def groups(self): # real signature unknown; restored from __doc__
        """
        list of Groups that contain this Sprite
        
                Sprite.groups(): return group_list
        
                Returns a list of all the Groups that contain this Sprite.
        """
        pass

    def kill(self): # real signature unknown; restored from __doc__
        """
        remove the Sprite from all Groups
        
                Sprite.kill(): return None
        
                The Sprite is removed from all the Groups that contain it. This won't
                change anything about the state of the Sprite. It is possible to
                continue to use the Sprite after this method has been called, including
                adding it to Groups.
        """
        pass

    def remove(self, *groups): # real signature unknown; restored from __doc__
        """
        remove the sprite from groups
        
                Sprite.remove(*groups): return None
        
                Any number of Group instances can be passed as arguments. The Sprite
                will be removed from the Groups it is currently a member of.
        """
        pass

    def remove_internal(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        method to control sprite behavior
        
                Sprite.update(*args, **kwargs):
        
                The default implementation of this method does nothing; it's just a
                convenient "hook" that you can override. This method is called by
                Group.update() with whatever arguments you give it.
        
                There is no need to use this method if not using the convenience
                method by the same name in the Group class.
        """
        pass

    def __init__(self, *groups): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _Sprite__g = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FFFA386A830>, '__repr__': <method '__repr__' of 'pygame._sprite.Sprite' objects>, '__init__': <slot wrapper '__init__' of 'pygame._sprite.Sprite' objects>, 'add': <cyfunction Sprite.add at 0x000002044F01DF20>, 'remove': <cyfunction Sprite.remove at 0x000002044F01F370>, 'update': <cyfunction Sprite.update at 0x000002044F04C1E0>, 'kill': <cyfunction Sprite.kill at 0x000002044F04C2B0>, 'groups': <cyfunction Sprite.groups at 0x000002044F04C380>, 'alive': <cyfunction Sprite.alive at 0x000002044F04C450>, '__dict__': <attribute '__dict__' of 'pygame._sprite.Sprite' objects>, '_Sprite__g': <attribute '_Sprite__g' of 'pygame._sprite.Sprite' objects>, 'image': <attribute 'image' of 'pygame._sprite.Sprite' objects>, 'rect': <attribute 'rect' of 'pygame._sprite.Sprite' objects>, '__doc__': 'simple base class for visible game objects\\n\\n    pygame.sprite.Sprite(*groups): return Sprite\\n\\n    The base class for visible game objects. Derived classes will want to\\n    override the Sprite.update() method and assign Sprite.image and Sprite.rect\\n    attributes.  The initializer can accept any number of Group instances that\\n    the Sprite will become a member of.\\n\\n    When subclassing the Sprite class, be sure to call the base initializer\\n    before adding the Sprite to Groups.\\n\\n    ', '__pyx_vtable__': <capsule object NULL at 0x000002044EFDBF60>, '__reduce__': <method '__reduce_cython__' of 'pygame._sprite.Sprite' objects>, '__setstate__': <method '__setstate_cython__' of 'pygame._sprite.Sprite' objects>, 'add_internal': <cyfunction Sprite.add_internal at 0x000002044F04C040>, 'remove_internal': <cyfunction Sprite.remove_internal at 0x000002044F04C110>})"
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002044EFDBF60>'


class DirtySprite(Sprite):
    """
    a more featureful subclass of Sprite with more attributes
    
        pygame.sprite.DirtySprite(*groups): return DirtySprite
    
        Extra DirtySprite attributes with their default values:
    
        dirty = 1
            If set to 1, it is repainted and then set to 0 again.
            If set to 2, it is always dirty (repainted each frame;
            flag is not reset).
            If set to 0, it is not dirty and therefore not repainted again.
    
        blendmode = 0
            It's the special_flags argument of Surface.blit; see the blendmodes in
            the Surface.blit documentation
    
        source_rect = None
            This is the source rect to use. Remember that it is relative to the top
            left corner (0, 0) of self.image.
    
        visible = 1
            Normally this is 1. If set to 0, it will not be repainted. (If you
            change visible to 1, you must set dirty to 1 for it to be erased from
            the screen.)
    
        _layer = 0
            0 is the default value but this is able to be set differently
            when subclassing.
    """
    def _get_visible(self, *args, **kwargs): # real signature unknown
        """ return the visible value of that sprite """
        pass

    def _set_visible(self, *args, **kwargs): # real signature unknown
        """ set the visible value (0 or 1) and makes the sprite dirty """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """you can make this sprite disappear without removing it from the group,
assign 0 for invisible and 1 for visible"""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class RenderPlain(AbstractGroup):
    """
    container class for many Sprites
    
        pygame.sprite.Group(*sprites): return Group
    
        A simple container for Sprite objects. This class can be subclassed to
        create containers with more specific behaviors. The constructor takes any
        number of Sprite arguments to add to the Group. The group supports the
        following standard Python operations:
    
            in      test if a Sprite is contained
            len     the number of Sprites contained
            bool    test if any Sprites are contained
            iter    iterate through all the Sprites
    
        The Sprites in the Group are not ordered, so the Sprites are drawn and
        iterated over in no particular order.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002044EFDBF90>'


RenderClear = RenderPlain


Group = RenderPlain


class GroupSingle(AbstractGroup):
    """
    A group container that holds a single most recent item.
    
        This class works just like a regular group, but it only keeps a single
        sprite in the group. Whatever sprite has been added to the group last will
        be the only sprite in the group.
    
        You can access its one sprite as the .sprite attribute.  Assigning to this
        attribute will properly remove the old sprite and then add the new one.
    """
    def add_internal(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def has_internal(self, *args, **kwargs): # real signature unknown
        pass

    def remove_internal(self, *args, **kwargs): # real signature unknown
        pass

    def sprites(self, *args, **kwargs): # real signature unknown
        pass

    def _get_sprite(self, *args, **kwargs): # real signature unknown
        pass

    def _set_sprite(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    sprite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sprite contained in this group"""

    _GroupSingle__sprite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002044F02C0C0>'


class LayeredUpdates(AbstractGroup):
    """
    LayeredUpdates Group handles layers, which are drawn like OrderedUpdates
    
        pygame.sprite.LayeredUpdates(*sprites, **kwargs): return LayeredUpdates
    
        This group is fully compatible with pygame.sprite.Sprite.
        New in pygame 1.8.0
    """
    def add(self, *sprites, **kwargs): # real signature unknown; restored from __doc__
        """
        add a sprite or sequence of sprites to a group
        
                LayeredUpdates.add(*sprites, **kwargs): return None
        
                If the sprite you add has an attribute _layer, then that layer will be
                used. If **kwarg contains 'layer', then the passed sprites will be
                added to that layer (overriding the sprite._layer attribute). If
                neither the sprite nor **kwarg has a 'layer', then the default layer is
                used to add the sprites.
        """
        pass

    def add_internal(self, *args, **kwargs): # real signature unknown
        """
        Do not use this method directly.
        
                It is used by the group to add a sprite internally.
        """
        pass

    def change_layer(self, sprite, new_layer): # real signature unknown; restored from __doc__
        """
        change the layer of the sprite
        
                LayeredUpdates.change_layer(sprite, new_layer): return None
        
                The sprite must have been added to the renderer already. This is not
                checked.
        """
        pass

    def draw(self, surface): # real signature unknown; restored from __doc__
        """
        draw all sprites in the right order onto the passed surface
        
                LayeredUpdates.draw(surface): return Rect_list
        """
        pass

    def get_bottom_layer(self): # real signature unknown; restored from __doc__
        """
        return the bottom layer
        
                LayeredUpdates.get_bottom_layer(): return layer
        """
        pass

    def get_layer_of_sprite(self, *args, **kwargs): # real signature unknown
        """
        return the layer that sprite is currently in
        
                If the sprite is not found, then it will return the default layer.
        """
        pass

    def get_sprite(self, idx): # real signature unknown; restored from __doc__
        """
        return the sprite at the index idx from the groups sprites
        
                LayeredUpdates.get_sprite(idx): return sprite
        
                Raises IndexOutOfBounds if the idx is not within range.
        """
        return pygame.sprite

    def get_sprites_at(self, pos): # real signature unknown; restored from __doc__
        """
        return a list with all sprites at that position
        
                LayeredUpdates.get_sprites_at(pos): return colliding_sprites
        
                Bottom sprites are listed first; the top ones are listed last.
        """
        pass

    def get_sprites_from_layer(self, layer): # real signature unknown; restored from __doc__
        """
        return all sprites from a layer ordered as they where added
        
                LayeredUpdates.get_sprites_from_layer(layer): return sprites
        
                Returns all sprites from a layer. The sprites are ordered in the
                sequence that they where added. (The sprites are not removed from the
                layer.
        """
        pass

    def get_top_layer(self): # real signature unknown; restored from __doc__
        """
        return the top layer
        
                LayeredUpdates.get_top_layer(): return layer
        """
        pass

    def get_top_sprite(self): # real signature unknown; restored from __doc__
        """
        return the topmost sprite
        
                LayeredUpdates.get_top_sprite(): return Sprite
        """
        return Sprite

    def layers(self): # real signature unknown; restored from __doc__
        """
        return a list of unique defined layers defined.
        
                LayeredUpdates.layers(): return layers
        """
        pass

    def move_to_back(self, sprite): # real signature unknown; restored from __doc__
        """
        move the sprite to the bottom layer
        
                LayeredUpdates.move_to_back(sprite): return None
        
                Moves the sprite to the bottom layer by moving it to a new layer below
                the current bottom layer.
        """
        pass

    def move_to_front(self, sprite): # real signature unknown; restored from __doc__
        """
        bring the sprite to front layer
        
                LayeredUpdates.move_to_front(sprite): return None
        
                Brings the sprite to front by changing the sprite layer to the top-most
                layer. The sprite is added at the end of the list of sprites in that
                top-most layer.
        """
        pass

    def remove_internal(self, *args, **kwargs): # real signature unknown
        """
        Do not use this method directly.
        
                The group uses it to add a sprite.
        """
        pass

    def remove_sprites_of_layer(self, layer_nr): # real signature unknown; restored from __doc__
        """
        remove all sprites from a layer and return them as a list
        
                LayeredUpdates.remove_sprites_of_layer(layer_nr): return sprites
        """
        pass

    def sprites(self, first_back, last_top): # real signature unknown; restored from __doc__
        """
        return a ordered list of sprites (first back, last top).
        
                LayeredUpdates.sprites(): return sprites
        """
        pass

    def switch_layer(self, layer1_nr, layer2_nr): # real signature unknown; restored from __doc__
        """
        switch the sprites from layer1_nr to layer2_nr
        
                LayeredUpdates.switch_layer(layer1_nr, layer2_nr): return None
        
                The layers number must exist. This method does not check for the
                existence of the given layers.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        initialize an instance of LayeredUpdates with the given attributes
        
                You can set the default layer through kwargs using 'default_layer'
                and an integer for the layer. The default layer is 0.
        
                If the sprite you add has an attribute _layer, then that layer will be
                used. If **kwarg contains 'layer', then the passed sprites will be
                added to that layer (overriding the sprite._layer attribute). If
                neither the sprite nor **kwarg has a 'layer', then the default layer is
                used to add the sprites.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _default_layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _spritelayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _spritelist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _init_rect = None # (!) real value is '<rect(0, 0, 0, 0)>'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002044F02C060>'


class LayeredDirty(LayeredUpdates):
    """
    LayeredDirty Group is for DirtySprites; subclasses LayeredUpdates
    
        pygame.sprite.LayeredDirty(*sprites, **kwargs): return LayeredDirty
    
        This group requires pygame.sprite.DirtySprite or any sprite that
        has the following attributes:
            image, rect, dirty, visible, blendmode (see doc of DirtySprite).
    
        It uses the dirty flag technique and is therefore faster than
        pygame.sprite.RenderUpdates if you have many static sprites.  It
        also switches automatically between dirty rect updating and full
        screen drawing, so you do no have to worry which would be faster.
    
        As with the pygame.sprite.Group, you can specify some additional attributes
        through kwargs:
            _use_update: True/False   (default is False)
            _default_layer: default layer where the sprites without a layer are
                added
            _time_threshold: treshold time for switching between dirty rect mode
                and fullscreen mode; defaults to updating at 80 frames per second,
                which is equal to 1000.0 / 80.0
    
        New in pygame 1.8.0
    """
    def add_internal(self, *args, **kwargs): # real signature unknown
        """
        Do not use this method directly.
        
                It is used by the group to add a sprite internally.
        """
        pass

    def change_layer(self, sprite, new_layer): # real signature unknown; restored from __doc__
        """
        change the layer of the sprite
        
                LayeredUpdates.change_layer(sprite, new_layer): return None
        
                The sprite must have been added to the renderer already. This is not
                checked.
        """
        pass

    def clear(self, surface, bgd): # real signature unknown; restored from __doc__
        """
        use to set background
        
                Group.clear(surface, bgd): return None
        """
        pass

    def draw(self, surface, bgd=None): # real signature unknown; restored from __doc__
        """
        draw all sprites in the right order onto the given surface
        
                LayeredDirty.draw(surface, bgd=None): return Rect_list
        
                You can pass the background too. If a self.bgd is already set to some
                value that is not None, then the bgd argument has no effect.
        """
        pass

    def get_clip(self): # real signature unknown; restored from __doc__
        """
        get the area where drawing will occur
        
                LayeredDirty.get_clip(): return Rect
        """
        return pygame.Rect(*(), **{})

    def repaint_rect(self, screen_rect): # real signature unknown; restored from __doc__
        """
        repaint the given area
        
                LayeredDirty.repaint_rect(screen_rect): return None
        
                screen_rect is in screen coordinates.
        """
        pass

    def set_clip(self, screen_rect=None): # real signature unknown; restored from __doc__
        """
        clip the area where to draw; pass None (default) to reset the clip
        
                LayeredDirty.set_clip(screen_rect=None): return None
        """
        pass

    def set_timing_threshold(self, *args, **kwargs): # real signature unknown
        """
        set the threshold in milliseconds
        
                (time_ms): return None
        
                Defaults to 1000.0 / 80.0. This means that the screen will be painted
                using the flip method rather than the update method if the update
                method is taking so long to update the screen that the frame rate falls
                below 80 frames per second.
        """
        pass

    def set_timing_treshold(self, time_ms): # real signature unknown; restored from __doc__
        """
        set the treshold in milliseconds
        
                DEPRECATED: misspelled 'threshold'
        
                set_timing_treshold(time_ms): return None
        
                Defaults to 1000.0 / 80.0. This means that the screen will be painted
                using the flip method rather than the update method if the update
                method is taking so long to update the screen that the frame rate falls
                below 80 frames per second.
        """
        pass

    def __init__(self, *sprites, **kwargs): # real signature unknown; restored from __doc__
        """
        initialize group.
        
                pygame.sprite.LayeredDirty(*sprites, **kwargs): return LayeredDirty
        
                You can specify some additional attributes through kwargs:
                    _use_update: True/False   (default is False)
                    _default_layer: default layer where the sprites without a layer are
                        added
                    _time_threshold: treshold time for switching between dirty rect
                        mode and fullscreen mode; defaults to updating at 80 frames per
                        second, which is equal to 1000.0 / 80.0
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _bgd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _clip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _time_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _use_update = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002044F02C090>'


class RenderUpdates(Group):
    """
    Group class that tracks dirty updates
    
        pygame.sprite.RenderUpdates(*sprites): return RenderUpdates
    
        This class is derived from pygame.sprite.Group(). It has an enhanced draw
        method that tracks the changed areas of the screen.
    """
    def draw(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *sprites): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002044EFDBFC0>'


class OrderedUpdates(RenderUpdates):
    """
    RenderUpdates class that draws Sprites in order of addition
    
        pygame.sprite.OrderedUpdates(*sprites): return OrderedUpdates
    
        This class derives from pygame.sprite.RenderUpdates().  It maintains
        the order in which the Sprites were added to the Group for rendering.
        This makes adding and removing Sprites from the Group a little
        slower than regular Groups.
    """
    def add_internal(self, *args, **kwargs): # real signature unknown
        pass

    def remove_internal(self, *args, **kwargs): # real signature unknown
        pass

    def sprites(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *sprites): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _spritelist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002044F02C030>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002044C3A8BD0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame._sprite', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002044C3A8BD0>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\_sprite.cp311-win_amd64.pyd')"

__test__ = {}

