"""
Tests for the Vector2D class
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine import Vector2D


class TestVector2D(unittest.TestCase):
    """Test cases for Vector2D class."""
    
    def test_initialization(self):
        """Test vector initialization."""
        v = Vector2D(3, 4)
        self.assertEqual(v.x, 3.0)
        self.assertEqual(v.y, 4.0)
    
    def test_default_initialization(self):
        """Test default vector initialization."""
        v = Vector2D()
        self.assertEqual(v.x, 0.0)
        self.assertEqual(v.y, 0.0)
    
    def test_addition(self):
        """Test vector addition."""
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        v3 = v1 + v2
        self.assertEqual(v3.x, 4.0)
        self.assertEqual(v3.y, 6.0)
    
    def test_subtraction(self):
        """Test vector subtraction."""
        v1 = Vector2D(5, 7)
        v2 = Vector2D(2, 3)
        v3 = v1 - v2
        self.assertEqual(v3.x, 3.0)
        self.assertEqual(v3.y, 4.0)
    
    def test_multiplication(self):
        """Test vector multiplication by scalar."""
        v1 = Vector2D(2, 3)
        v2 = v1 * 2
        self.assertEqual(v2.x, 4.0)
        self.assertEqual(v2.y, 6.0)
    
    def test_division(self):
        """Test vector division by scalar."""
        v1 = Vector2D(4, 6)
        v2 = v1 / 2
        self.assertEqual(v2.x, 2.0)
        self.assertEqual(v2.y, 3.0)
    
    def test_division_by_zero(self):
        """Test that division by zero raises an error."""
        v = Vector2D(1, 1)
        with self.assertRaises(ValueError):
            v / 0
    
    def test_magnitude(self):
        """Test vector magnitude calculation."""
        v = Vector2D(3, 4)
        self.assertEqual(v.magnitude(), 5.0)
    
    def test_normalize(self):
        """Test vector normalization."""
        v = Vector2D(3, 4)
        vn = v.normalize()
        self.assertAlmostEqual(vn.magnitude(), 1.0)
        self.assertAlmostEqual(vn.x, 0.6)
        self.assertAlmostEqual(vn.y, 0.8)
    
    def test_normalize_zero_vector(self):
        """Test normalization of zero vector."""
        v = Vector2D(0, 0)
        vn = v.normalize()
        self.assertEqual(vn.x, 0.0)
        self.assertEqual(vn.y, 0.0)
    
    def test_distance_to(self):
        """Test distance calculation between vectors."""
        v1 = Vector2D(0, 0)
        v2 = Vector2D(3, 4)
        self.assertEqual(v1.distance_to(v2), 5.0)
    
    def test_repr(self):
        """Test string representation."""
        v = Vector2D(1.5, 2.5)
        self.assertEqual(repr(v), "Vector2D(1.5, 2.5)")


if __name__ == "__main__":
    unittest.main()
