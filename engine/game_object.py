"""
GameObject base class for all game entities
"""

from .vector2d import Vector2D


class GameObject:
    """Base class for all game objects in the engine."""
    
    def __init__(self, name="GameObject", position=None):
        """Initialize a game object.
        
        Args:
            name: A descriptive name for the object (default: "GameObject")
            position: Initial position as Vector2D (default: Vector2D(0, 0))
        """
        self.name = name
        self.position = position if position else Vector2D(0, 0)
        self.active = True
    
    def update(self, delta_time):
        """Update the game object's state.
        
        Called once per frame. Override this method in subclasses to implement
        custom behavior.
        
        Args:
            delta_time: Time elapsed since last frame in seconds
        """
        pass
    
    def render(self):
        """Render the game object.
        
        Called once per frame after update. Override this method in subclasses
        to implement custom rendering.
        """
        pass
    
    def __repr__(self):
        """String representation of the game object."""
        return f"{self.name} at {self.position}"
