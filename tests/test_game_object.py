"""
Tests for the GameObject class
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine import GameObject, Vector2D


class TestGameObject(unittest.TestCase):
    """Test cases for GameObject class."""
    
    def test_initialization(self):
        """Test game object initialization."""
        obj = GameObject("TestObject", Vector2D(10, 20))
        self.assertEqual(obj.name, "TestObject")
        self.assertEqual(obj.position.x, 10.0)
        self.assertEqual(obj.position.y, 20.0)
        self.assertTrue(obj.active)
    
    def test_default_initialization(self):
        """Test default game object initialization."""
        obj = GameObject()
        self.assertEqual(obj.name, "GameObject")
        self.assertEqual(obj.position.x, 0.0)
        self.assertEqual(obj.position.y, 0.0)
        self.assertTrue(obj.active)
    
    def test_update_method(self):
        """Test that update method can be called."""
        obj = GameObject()
        # Should not raise any errors
        obj.update(0.016)
    
    def test_render_method(self):
        """Test that render method can be called."""
        obj = GameObject()
        # Should not raise any errors
        obj.render()
    
    def test_custom_subclass(self):
        """Test creating a custom GameObject subclass."""
        class CustomObject(GameObject):
            def __init__(self):
                super().__init__("Custom", Vector2D(0, 0))
                self.counter = 0
            
            def update(self, delta_time):
                self.counter += 1
        
        obj = CustomObject()
        self.assertEqual(obj.counter, 0)
        obj.update(0.1)
        self.assertEqual(obj.counter, 1)
        obj.update(0.1)
        self.assertEqual(obj.counter, 2)
    
    def test_repr(self):
        """Test string representation."""
        obj = GameObject("Player", Vector2D(5, 10))
        self.assertIn("Player", repr(obj))


if __name__ == "__main__":
    unittest.main()
