import pygame
from .paddle import Paddle
from .ball import Ball

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100

        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)

        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.max_score = 5
        self.game_over = False
        self.winner = None

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player.move(10, self.height)

    def update(self):
        if self.game_over:
            return

        self.ball.move()
        self.ball.check_collision(self.player, self.ai)

        if self.ball.x <= 0:
            self.ai_score += 1
            self.ball.reset()
        elif self.ball.x >= self.width:
            self.player_score += 1
            self.ball.reset()

        self.ai.auto_track(self.ball, self.height)

        # Check for game over
        if self.player_score >= self.max_score:
            self.game_over = True
            self.winner = "Player"
        elif self.ai_score >= self.max_score:
            self.game_over = True
            self.winner = "AI"

    def render(self, screen):
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width // 2, 0), (self.width // 2, self.height))

        # Draw score
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width // 4, 20))
        screen.blit(ai_text, (self.width * 3 // 4, 20))

    def render_game_over(self, screen):
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        msg_font = pygame.font.SysFont("Arial", 60)
        msg = msg_font.render(f"{self.winner} Wins!", True, WHITE)
        screen.blit(msg, (self.width // 2 - msg.get_width() // 2, self.height // 2 - msg.get_height()))

        hint_font = pygame.font.SysFont("Arial", 30)
        hint = hint_font.render("Press R to Restart or Q to Quit", True, WHITE)
        screen.blit(hint, (self.width // 2 - hint.get_width() // 2, self.height // 2 + 20))
