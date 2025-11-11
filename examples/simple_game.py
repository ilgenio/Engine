"""
Simple example game demonstrating the Engine usage
"""

import sys
import os

# Add parent directory to path so we can import engine
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine import Engine, GameObject, Vector2D


class MovingObject(GameObject):
    """A game object that moves across the screen."""
    
    def __init__(self, name="MovingObject", position=None, velocity=None):
        super().__init__(name, position)
        self.velocity = velocity if velocity else Vector2D(1, 0)
    
    def update(self, delta_time):
        """Update position based on velocity."""
        self.position = self.position + self.velocity * delta_time
    
    def render(self):
        """Simple text-based rendering."""
        print(f"{self.name}: Position({self.position.x:.2f}, {self.position.y:.2f})")


class BouncingBall(GameObject):
    """A ball that bounces within boundaries."""
    
    def __init__(self, name="Ball", position=None, velocity=None, bounds=(100, 100)):
        super().__init__(name, position)
        self.velocity = velocity if velocity else Vector2D(10, 10)
        self.bounds = bounds
    
    def update(self, delta_time):
        """Update position and bounce off boundaries."""
        # Update position
        self.position = self.position + self.velocity * delta_time
        
        # Bounce off boundaries
        if self.position.x < 0 or self.position.x > self.bounds[0]:
            self.velocity.x *= -1
            self.position.x = max(0, min(self.position.x, self.bounds[0]))
        
        if self.position.y < 0 or self.position.y > self.bounds[1]:
            self.velocity.y *= -1
            self.position.y = max(0, min(self.position.y, self.bounds[1]))
    
    def render(self):
        """Simple text-based rendering."""
        print(f"{self.name}: ({self.position.x:.1f}, {self.position.y:.1f}) " +
              f"Velocity: ({self.velocity.x:.1f}, {self.velocity.y:.1f})")


def main():
    """Run a simple demo game."""
    # Create the engine with 2 FPS for slow, visible updates
    engine = Engine(target_fps=2)
    
    # Create some game objects
    player = MovingObject("Player", Vector2D(0, 0), Vector2D(5, 2))
    ball = BouncingBall("Ball", Vector2D(50, 50), Vector2D(15, -10), bounds=(100, 75))
    
    # Add objects to engine
    engine.add_object(player)
    engine.add_object(ball)
    
    # Run for a limited time
    print("Starting simple game demo (runs for 5 seconds)...")
    print("=" * 60)
    
    import time
    start_time = time.time()
    
    try:
        # Start engine in a way that we can stop it after 5 seconds
        engine.running = True
        last_time = time.time()
        
        while engine.running and (time.time() - start_time) < 5:
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time
            
            engine._update(delta_time)
            print("\nFrame", engine.frame_count + 1)
            print("-" * 60)
            engine._render()
            
            engine.frame_count += 1
            engine.time_elapsed += delta_time
            
            # Sleep to maintain target FPS
            sleep_time = engine.frame_time - delta_time
            if sleep_time > 0:
                time.sleep(sleep_time)
        
        engine.stop()
        print("=" * 60)
        print(f"Average FPS: {engine.get_fps():.2f}")
        
    except KeyboardInterrupt:
        engine.stop()
        print("\nGame interrupted by user")


if __name__ == "__main__":
    main()
