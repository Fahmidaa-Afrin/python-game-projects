# OpenGL Basics

This folder contains introductory projects exploring the fundamentals of OpenGL.

## Assignment 1, Task 1: Building a House in Rainfall

This project, implemented in `A1_Task_1.py`, involves drawing a house with animated rainfall using basic OpenGL primitives.

### Features:
- **House and Rain:** A house is drawn, and raindrops are animated to fall from top to bottom.
- **Rain Direction Control:**
    - The **left arrow key** gradually bends the rain to the left.
    - The **right arrow key** gradually bends the rain to the right.
- **Day/Night Cycle:**
    - The **'d' key** gradually changes the background from dark to light (night to day).
    - The **'n' key** gradually changes the background from light to dark (day to night).
- **Visibility:** The house and rain are visible against different background colors.

### Technical Implementation
- **Graphics:** The house is constructed using `GL_TRIANGLES`, `GL_LINES`, and `GL_POINTS`. Raindrops are drawn using `GL_LINES`.
- **Animation:** The falling rain effect is achieved by continuously updating the Y-coordinates of the raindrops in the `animate` function, which is registered with `glutIdleFunc`.
- **Day/Night Cycle:** The background color is controlled by a global `colour` variable, which is modified in the `keyboard_listener` and applied using `glClearColor`.
- **Rain Control:** The `special_key_listener` function modifies the X-coordinates of the raindrops when the left and right arrow keys are pressed, creating the bending effect.
- **State Management:** A global `updation` variable tracks the current bend amount to ensure newly generated raindrops are also bent correctly.

## Assignment 1, Task 2: Building the Amazing Box

This project, `A1_Task_2.py`, focuses on creating an interactive box with dynamic points.

### Features:
- **Point Spawning:** A **right mouse click** spawns a movable point with a random color at the cursor's location. The point moves in a random diagonal direction.
- **Bouncing:** Points bounce off the walls of the boundary.
- **Speed Control:**
    - **Up arrow key** increases the speed of all points.
    - **Down arrow key** decreases the speed of all points.
- **Blinking Points:** A **left mouse click** toggles a blinking effect for all points (cycling between their color and the background color).
- **Freeze/Unfreeze:** The **Spacebar** freezes and unfreezes all points, pausing and resuming their movement and interactions.

### Technical Implementation
- **Graphics:** Points are rendered using `GL_POINTS`, and the boundary is drawn with `GL_LINE_LOOP`.
- **Animation and Bouncing:** The `animate` function, registered with `glutIdleFunc`, updates the position of each point. When a point hits the boundary, its direction vector is inverted to simulate a bounce.
- **User Interaction:**
    - `mouse_listener`: Handles point creation (right-click) and toggles the blinking flag (left-click).
    - `special_key_listener`: Adjusts the global `speed` variable for all points.
    - `keyboard_listener`: Toggles the `frozen` boolean flag to pause or resume the animation.
- **Blinking Effect:** A global `bflag` controls the blinking. When active, the `animate` function periodically swaps the points' colors with the background color based on a time interval (`bgap`), creating a blinking illusion.
- **State Management:** The state of each point (position, color, direction) is stored in a global `points` list. Global flags like `bflag` and `frozen` manage the overall state of the simulation.
