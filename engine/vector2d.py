"""
Vector2D class for 2D position and movement
"""

import math


class Vector2D:
    """A simple 2D vector class for positions and directions."""
    
    def __init__(self, x=0.0, y=0.0):
        """Initialize a 2D vector.
        
        Args:
            x: The x-coordinate (default: 0.0)
            y: The y-coordinate (default: 0.0)
        """
        self.x = float(x)
        self.y = float(y)
    
    def __add__(self, other):
        """Add two vectors together."""
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Subtract one vector from another."""
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Multiply vector by a scalar."""
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        """Divide vector by a scalar."""
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def __repr__(self):
        """String representation of the vector."""
        return f"Vector2D({self.x}, {self.y})"
    
    def magnitude(self):
        """Calculate the length of the vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self):
        """Return a normalized (unit length) version of the vector."""
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return self / mag
    
    def distance_to(self, other):
        """Calculate distance to another vector."""
        return (self - other).magnitude()
