import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)

def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle BEST-OF SELECTION state (Task 3)
            if engine.selecting_best_of:
                engine.handle_best_of_selection_input(event)

            # Handle GAME OVER state
            elif engine.game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_r:
                        engine.reset_game()

        # Only play the game if not selecting best-of and not game over
        if not engine.selecting_best_of and not engine.game_over:
            engine.handle_input()
            engine.update()
            engine.render(SCREEN)
        else:
            # Still draw the paddles, ball, score for consistent visuals
            engine.render(SCREEN)
            # Show prompt overlays for special states
            if engine.selecting_best_of:
                engine.render_best_of_selection(SCREEN)
            elif engine.game_over:
                engine.render_game_over(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
