# 2D Games

This folder contains projects related to 2D game development.

## Assignment 2: "Catch the Diamonds!"

`A2_2D_Game.py` is a 2D game built from the ground up using the **Midpoint Line Drawing algorithm**, where every object on the screen is rendered using only the `GL_POINTS` primitive.

### Core Gameplay
The player controls a catcher at the bottom of the screen to catch diamonds falling from the top. The score increases with each successful catch, but missing a single diamond results in a game over.

### Features

-   **Player Control:**
    -   Move the catcher horizontally using the **left and right arrow keys**.
    -   The catcher is constrained within the screen boundaries.

-   **Diamonds:**
    -   Fall one at a time from a random horizontal position at the top.
    -   Each new diamond has a random, bright color.
    -   The falling speed gradually increases over time to raise the difficulty.

-   **Game State:**
    -   **Catch:** If the catcher collides with a diamond, the score increases by 1, and a new diamond spawns.
    -   **Game Over:** If a diamond is missed, the game ends. The catcher turns red and becomes immobile, and the final score is displayed.

-   **On-Screen UI Buttons:**
    -   **Restart (Teal Left Arrow):** Click to start a new game at any time, resetting the score and diamond speed.
    -   **Play/Pause (Amber Middle Icon):** Toggles the game's state. The icon dynamically changes to reflect the current state (Play or Pause).
    -   **Exit (Red Cross):** Terminates the application.

-   **Cheat Mode:**
    -   Press the **'c' key** to toggle an auto-play mode.
    -   In Cheat Mode, the catcher automatically moves to catch every diamond perfectly.

### Technical Implementation
-   **Graphics:** All shapes (catcher, diamonds, UI buttons) are drawn exclusively using a custom Midpoint Line Drawing algorithm. The core logic resides in the `mpl` function, which is adapted for all 8 zones using `find_zone`, `convert_zone`, and `bring_back_zoneo` helper functions.
-   **Collision Detection:** A simple bounding box check is used to detect collisions. A catch is registered if the diamond's x-coordinate is within the catcher's horizontal bounds when its y-coordinate reaches the catcher's height.
-   **Framerate Independence:** Delta timing is implemented in the `animate` function to ensure consistent game speed across different hardware. The diamond's falling speed (`d_speed`) is increased based on the time elapsed between frames.
-   **Game State Management:** Global flags like `flag_play_pause`, `stop_game`, and `cheat_mode` control the game's state (playing, paused, game over, or auto-play).
-   **User Input:**
    -   `special_key_listener`: Manages catcher movement.
    -   `keyboard_listener`: Toggles cheat mode.
    -   `mouse_listener`: Handles clicks on the UI buttons (restart, play/pause, exit).
