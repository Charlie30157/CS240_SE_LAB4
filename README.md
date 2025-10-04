# Project: Real-Time Ping Pong

This project is a terminal-based ping pong game using **Pygame**. It introduces students to interactive game design using object-oriented principles and real-time graphical rendering.

---

## What’s Provided

A partially working version of a ping pong game with:

- Player and AI-controlled paddles
- Ball movement with basic collision
- Score display

You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional.

---

## Getting Started

### Setup

1. Clone the repo or download the project folder.
2. Make sure you have Python 3.10+ installed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

---

## Initial Prompt Template (To Use With LLM)

Use this to begin your interaction with the LLM:

```
I’m working on a real-time Ping Pong game using Python and Pygame. I have a partially working project structure. Please help me understand how the logic is organized and guide me on implementing missing features. Review any code I send to ensure it aligns with the expected behavior.
```

---

## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Refine Ball Collision

> The ball sometimes passes through paddles at high speed. Investigate and enhance collision accuracy.

### Task 2: Implement Game Over Condition

> Add a screen that displays the winner once one player reaches a defined score (e.g., 5), then gracefully exits or restarts.

### Task 3: Add Replay Option

> After Game Over, allow the user to play again with best of 3, 5, or 7 option, or exit.

### Task 4: Add Sound Feedback

> Add basic sound effects for paddle hit, wall bounce, and score.

---

## Expected Behavior

- Smooth paddle movement using `W` and `S`
- AI tracks and plays competitively
- Ball rebounds on paddle and wall hits
- Score updates on each miss
- Game ends and optionally restarts when limit reached

---

## Folder Structure

```
pygame-pingpong/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   ├── paddle.py
│   └── ball.py
└── README.md
```

---

## Submission Checklist

- [] All 4 tasks completed
- [] Game behaves as expected
- [] No bugs or crashes
- [] Code reviewed with LLM
- [] Final score and winner display works correctly
- [] Score appears correctly on both player and AI sides
- [] Dependencies listed in `requirements.txt`
- [] README is followed during setup and testing
- [] Codebase is clean, modular, and understandable


# Ping Pong Game (Pygame Edition)

This is an enhanced implementation of the classic Ping Pong (Pong) game using Python and Pygame, featuring multi-game matches, replay options, and audio feedback.

---

## Features

### Task 1: Accurate Ball-Paddle Collision
- Improved collision detection ensures the ball never passes through paddles at high speed.
- Robust gameplay at all frame rates.

### Task 2: Game Over Condition
- A match ends when a player reaches the winning score (default: 5 points).
- Winner is displayed with an overlay.
- Option to restart or quit after match end.

### Task 3: Best-of-N Replay Option
- After each match, choose 'best of 3', '5', or '7' format for rematches.
- Shows current match series score.
- Flexible match restarts; user can exit any time.

### Task 4: Sound Feedback
- Audio effect for paddle hits.
- Distinct sound for wall bounces.
- Separate sound for scoring events.

---

## Controls

- **W/S**: Move player paddle up/down
- **3/5/7**: Select best-of rounds at startup or post-match
- **R**: Restart match after game over
- **Q**: Quit the game (at any prompt or screen)

---

## Installation & Execution

1. **Install dependencies (Python >= 3.8):**

