"""
Tests for the Engine class
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine import Engine, GameObject, Vector2D


class TestEngine(unittest.TestCase):
    """Test cases for Engine class."""
    
    def test_initialization(self):
        """Test engine initialization."""
        engine = Engine(target_fps=60)
        self.assertEqual(engine.target_fps, 60)
        self.assertAlmostEqual(engine.frame_time, 1.0/60)
        self.assertFalse(engine.running)
        self.assertEqual(len(engine.game_objects), 0)
        self.assertEqual(engine.frame_count, 0)
    
    def test_add_object(self):
        """Test adding game objects."""
        engine = Engine()
        obj1 = GameObject("Object1")
        obj2 = GameObject("Object2")
        
        engine.add_object(obj1)
        self.assertEqual(len(engine.game_objects), 1)
        self.assertIn(obj1, engine.game_objects)
        
        engine.add_object(obj2)
        self.assertEqual(len(engine.game_objects), 2)
        self.assertIn(obj2, engine.game_objects)
    
    def test_remove_object(self):
        """Test removing game objects."""
        engine = Engine()
        obj1 = GameObject("Object1")
        obj2 = GameObject("Object2")
        
        engine.add_object(obj1)
        engine.add_object(obj2)
        self.assertEqual(len(engine.game_objects), 2)
        
        engine.remove_object(obj1)
        self.assertEqual(len(engine.game_objects), 1)
        self.assertNotIn(obj1, engine.game_objects)
        self.assertIn(obj2, engine.game_objects)
    
    def test_remove_nonexistent_object(self):
        """Test removing an object that doesn't exist."""
        engine = Engine()
        obj = GameObject("Object")
        # Should not raise an error
        engine.remove_object(obj)
    
    def test_update_calls_object_update(self):
        """Test that engine update calls object update methods."""
        class CounterObject(GameObject):
            def __init__(self):
                super().__init__("Counter")
                self.update_count = 0
            
            def update(self, delta_time):
                self.update_count += 1
        
        engine = Engine()
        obj = CounterObject()
        engine.add_object(obj)
        
        self.assertEqual(obj.update_count, 0)
        engine._update(0.016)
        self.assertEqual(obj.update_count, 1)
        engine._update(0.016)
        self.assertEqual(obj.update_count, 2)
    
    def test_update_skips_inactive_objects(self):
        """Test that inactive objects are not updated."""
        class CounterObject(GameObject):
            def __init__(self):
                super().__init__("Counter")
                self.update_count = 0
            
            def update(self, delta_time):
                self.update_count += 1
        
        engine = Engine()
        obj = CounterObject()
        obj.active = False
        engine.add_object(obj)
        
        engine._update(0.016)
        self.assertEqual(obj.update_count, 0)
    
    def test_render_calls_object_render(self):
        """Test that engine render calls object render methods."""
        class CounterObject(GameObject):
            def __init__(self):
                super().__init__("Counter")
                self.render_count = 0
            
            def render(self):
                self.render_count += 1
        
        engine = Engine()
        obj = CounterObject()
        engine.add_object(obj)
        
        self.assertEqual(obj.render_count, 0)
        engine._render()
        self.assertEqual(obj.render_count, 1)
    
    def test_get_fps(self):
        """Test FPS calculation."""
        engine = Engine()
        self.assertEqual(engine.get_fps(), 0)
        
        engine.frame_count = 60
        engine.time_elapsed = 1.0
        self.assertEqual(engine.get_fps(), 60.0)
    
    def test_stop_sets_running_to_false(self):
        """Test that stop sets running to false."""
        engine = Engine()
        engine.running = True
        engine.stop()
        self.assertFalse(engine.running)


if __name__ == "__main__":
    unittest.main()
