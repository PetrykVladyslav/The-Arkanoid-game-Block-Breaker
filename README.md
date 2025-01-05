# The Arkanoid game "Block Breaker"
"Blocks Break" is a classic arcade game in which the player controls a platform by hitting a ball to destroy blocks on the screen. Each block is assigned a number of points. The game offers a variety of levels, changing colors of the ball, as well as the opportunity to beat a personal best.

• Functionality
Controls:
The player controls the platform by moving it left and right using the arrow keys.
The reflection of the ball from the platform allows you to destroy the blocks.

Mechanics of blocks:
The blocks have different points values. Some blocks are "special" (gold) and hide special contents until they are destroyed.

The glasses system:
Points are awarded for each destroyed block. The current score and record are displayed.

Menu:
The game has a main menu with options: Start the game. Change the color of the ball. Log out of the game. The game completion screen displays the result, record, and restart buttons.

Changing the color of the ball:
The unique function of changing the color of the ball through the interactive color settings menu (RGB sliders).

• Features
Generating blocks:
Each level consists of randomly generated rows of blocks with a different number of points. The color of the blocks is also randomly selected.

Complexity:
With each level, the ball moves faster, increasing the difficulty of the game. Special blocks add an element of surprise.

Intuitive interface:
Simple keyboard controls. A minimalistic but functional interface for displaying scores and records.

Visual customization:
The player can choose the color of the ball through a special menu.

Performance optimization:
The game runs smoothly even on weak devices.

• Technical implementation
Gameplay: The logic of the ball's movement and collision with blocks is implemented through updating coordinates and checking the intersection of objects (pygame.Rect). Blocks are objects of the Block class.

Menu:
The main menu and the color change menu are created using the Pygame interface elements. The user interacts with buttons located in separate rectangular areas.

Game Physics:
The reflection of the ball from the walls, platform and blocks is implemented. Accelerate the ball with each new level.

![Image](https://github.com/PetrykVladyslav/The-Arkanoid-game-Block-Breaker-/blob/main/Images/photo.jpg)

Blocks Break is a simple but addictive arcade game with customization elements and increasing difficulty. Due to its flexibility and use of Pygame, the project demonstrates skills in working with game mechanics, graphical interface and interaction logic.
