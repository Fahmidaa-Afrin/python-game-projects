# 3D Games

This folder contains projects related to 3D game development.

- `A3_3D_Game.py`: A simple 3D game.
## Bullet Frenzy

`bullet_frenzy.py` is a 3D first-person shooter game developed using PyOpenGL. The player navigates a gridded arena, shooting at enemy spheres while managing health, score, and ammunition.

### Core Gameplay
The player controls a gun-wielding character from a first or third-person perspective. The objective is to shoot constantly spawning enemies to increase the score. The game ends if the player's health is depleted or if too many shots are missed.

### Features

-   **Player and Gun Mechanics:**
    -   **Movement:** Move forward (**W**) and backward (**S**).
    -   **Rotation:** Turn the gun left (**A**) and right (**D**).
    -   **Shooting:** Fire bullets with the **left mouse button**.

-   **Camera System:**
    -   **Vertical Movement:** Move the camera view up and down using the **UP** and **DOWN** arrow keys.
    -   **Horizontal Rotation:** Rotate the camera around the arena using the **LEFT** and **RIGHT** arrow keys.
    -   **Perspective Toggle:** Switch between a fixed third-person view and a gun-following first-person view with a **right mouse button click**.

-   **Enemies:**
    -   Five enemies are always present on the map.
    -   Enemies continuously move toward the player.
    -   When an enemy is destroyed, it respawns at a random location.
    -   Enemies have a continuous shrinking and expanding animation.

-   **Game State:**
    -   **Game Over:** The game ends if the player's life reaches zero (from enemy collisions) or if 10 bullets are missed. On game over, the player model falls to the ground.
    -   **Restart:** Press **'R'** to restart the game, resetting score, lives, and missed bullet count.

-   **Cheat Modes:**
    -   **Auto-Fire ('C' key):** Toggles a mode where the gun rotates 360 degrees and automatically fires at any enemy in its line of sight.
    -   **Auto-Follow ('V' key):** Toggles a camera mode that automatically follows the gun's movement, intended for use with the auto-fire cheat in first-person mode.

### Technical Implementation
-   **3D Graphics:** The game is rendered in 3D using PyOpenGL. The scene uses a perspective projection (`gluPerspective`) and a camera system (`gluLookAt`).
-   **Transformations:** Player movement, gun rotation, and bullet trajectories are handled using `glTranslatef` and `glRotatef`.
-   **Object Creation:** The player, enemies, and environment are constructed from primitive shapes like spheres (`gluSphere`), cylinders (`gluCylinder`), and cubes (`glutSolidCube`). The game floor is a dynamically generated checkerboard grid.
-   **Game Logic:**
    -   The main game loop is driven by the `idle` function, which updates enemy positions, bullet trajectories, and game state.
    -   Enemy AI is simple: they constantly move toward the player's current position.
    -   Collision detection between bullets and enemies, and between the player and enemies, is based on distance checks.
-   **State Management:** Global variables track the player's `life`, `score`, `bullet_missed` count, and the `game_finishing_status`. The positions of enemies and bullets are stored in lists and tuples.
-   **Cheat Mode Logic:** When cheat mode is active, the `idle` function continuously rotates the `gun_rotation_angle`. It calculates the angle to each enemy and fires a bullet if the enemy is within a small threshold of the gun's current angle.
-   **Camera Control:** The `setupCamera` function adjusts the `gluLookAt` parameters based on whether the game is in first-person or third-person mode. In first-person, the camera's position is tied to the player's head, and its look-at direction is determined by the `gun_rotation_angle`.
