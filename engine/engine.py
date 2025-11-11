"""
Main Engine class that manages the game loop
"""

import time


class Engine:
    """Main game engine class that manages the game loop and objects."""
    
    def __init__(self, target_fps=60):
        """Initialize the game engine.
        
        Args:
            target_fps: Target frames per second (default: 60)
        """
        self.target_fps = target_fps
        self.frame_time = 1.0 / target_fps
        self.running = False
        self.game_objects = []
        self.time_elapsed = 0.0
        self.frame_count = 0
    
    def add_object(self, game_object):
        """Add a game object to the engine.
        
        Args:
            game_object: A GameObject instance to add
        """
        self.game_objects.append(game_object)
    
    def remove_object(self, game_object):
        """Remove a game object from the engine.
        
        Args:
            game_object: A GameObject instance to remove
        """
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)
    
    def start(self):
        """Start the game loop."""
        self.running = True
        last_time = time.time()
        
        print(f"Engine started (Target FPS: {self.target_fps})")
        
        while self.running:
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time
            
            self._update(delta_time)
            self._render()
            
            self.frame_count += 1
            self.time_elapsed += delta_time
            
            # Sleep to maintain target FPS
            sleep_time = self.frame_time - delta_time
            if sleep_time > 0:
                time.sleep(sleep_time)
    
    def stop(self):
        """Stop the game loop."""
        self.running = False
        print(f"\nEngine stopped after {self.frame_count} frames ({self.time_elapsed:.2f}s)")
    
    def _update(self, delta_time):
        """Internal update method that updates all game objects.
        
        Args:
            delta_time: Time elapsed since last frame in seconds
        """
        for obj in self.game_objects:
            if obj.active:
                obj.update(delta_time)
    
    def _render(self):
        """Internal render method that renders all game objects."""
        for obj in self.game_objects:
            if obj.active:
                obj.render()
    
    def get_fps(self):
        """Get the current average FPS.
        
        Returns:
            Average frames per second
        """
        if self.time_elapsed > 0:
            return self.frame_count / self.time_elapsed
        return 0
