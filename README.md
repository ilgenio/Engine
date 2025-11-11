# Engine

A simple, educational game engine designed for students learning game development concepts.

## Features

- **Easy to Learn**: Simple, clean API designed for beginners
- **Core Game Loop**: Built-in game loop with configurable FPS
- **Game Objects**: Base GameObject class for creating game entities
- **2D Vector Math**: Vector2D class for positions and movements
- **No External Dependencies**: Uses only Python standard library

## Installation

### From Source

```bash
git clone https://github.com/ilgenio/Engine.git
cd Engine
pip install -e .
```

## Quick Start

Here's a simple example to get you started:

```python
from engine import Engine, GameObject, Vector2D

class MyObject(GameObject):
    def __init__(self):
        super().__init__("MyObject", Vector2D(0, 0))
        self.velocity = Vector2D(1, 1)
    
    def update(self, delta_time):
        self.position = self.position + self.velocity * delta_time
    
    def render(self):
        print(f"{self.name} at {self.position}")

# Create engine and add objects
engine = Engine(target_fps=60)
obj = MyObject()
engine.add_object(obj)

# Start the game loop
engine.start()
```

## Running Examples

The `examples/` directory contains sample games:

```bash
python examples/simple_game.py
```

## Core Components

### Engine

The main engine class that manages the game loop and game objects.

```python
engine = Engine(target_fps=60)
engine.add_object(game_object)
engine.start()
```

### GameObject

Base class for all game entities. Override `update()` and `render()` methods:

```python
class Player(GameObject):
    def update(self, delta_time):
        # Update game logic
        pass
    
    def render(self):
        # Render the object
        pass
```

### Vector2D

A simple 2D vector class for positions and directions:

```python
pos = Vector2D(10, 20)
velocity = Vector2D(1, 0)
new_pos = pos + velocity * delta_time
```

## Learning Resources

This engine is designed to teach fundamental game development concepts:

- **Game Loop**: Understanding frame-based updates
- **Delta Time**: Frame-rate independent movement
- **Object-Oriented Design**: Creating game entities as classes
- **Vector Math**: 2D position and movement calculations

## Contributing

This is an educational project. Feel free to extend it for your learning!

## License

MIT License - feel free to use this for learning and teaching.