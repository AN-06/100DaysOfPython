# 💎 Treasure Island Game

Welcome to the **Treasure Island Game**! This is an interactive web-based game built using **Flask**, a Python web framework. In this game, players are presented with a series of choices, and the story unfolds based on their decisions. The game demonstrates **conditional flow** in Python, allowing different game outcomes based on the user's input.

## ❓ How it Works

The game is designed with a step-by-step flow, where players must make choices to progress. The flow is controlled using **Python's conditional statements**, ensuring different results depending on the player's decisions. Here are the steps in the game:

1. **Step 1**: The player encounters a crossroad and must choose whether to go left or right.
   - Going **left** moves the player to the next step.
   - Going **right** ends the game with a "Game Over" message.
   
2. **Step 2**: The player encounters a lake and must decide whether to wait for a boat or swim across.
   - Choosing to **wait** progresses the player to the next step.
   - Choosing to **swim** results in a "Game Over" message.

3. **Step 3**: The player reaches an island with three doors and must choose one to enter.
   - **Red Door**: Game Over (a room full of fire).
   - **Yellow Door**: You win! You find the treasure.
   - **Blue Door**: Game Over (a room full of beasts).

The app uses Flask to handle routing and session management, and HTML is used to present the choices to the user.

## 🌟 Features

- **Conditional Flow**: The game's flow depends entirely on the user's choices. The Python backend handles all the logic and makes use of conditional statements (`if`, `elif`, `else`) to guide the user through the game.
- **Flask Session**: The game uses Flask sessions to store user choices and the current step.
- **Interactive UI**: The front-end is built with HTML, CSS, and minimal JavaScript (using Flask templating for dynamic content).

## 💻 Requirements

Before running the app, make sure you have the following installed:

- Python 3.x
- Flask

## 🚀 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/100DaysOfPython.git
   cd treasure-island-game
   ```


2. Navigate to the Project Directory:

   ```bash
    cd 100DaysOfPython/Day3
   ```
   
3. Install Flask :

    ```bash
     pip install Flask
    ```
     Run the Flask app:
       ```bash
          python app.py
       ```

4. Open your web browser and navigate to http://127.0.0.1:5000/ to start playing the game!
