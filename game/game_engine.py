import pygame
import os
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

        # Scores for individual games
        self.player_score = 0
        self.ai_score = 0

        # Match wins for multiple games in best-of series
        self.player_match_wins = 0
        self.ai_match_wins = 0

        self.font = pygame.font.SysFont("Arial", 30)
        self.max_score = 5  # points per game to win
        self.best_of_rounds = None  # user selects 3,5,7
        self.selecting_best_of = True  # initially wait for user's best-of input

        self.game_over = False
        self.winner = None

        # Sound: Score feedback
        self.score_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'score.wav'))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if not self.selecting_best_of and not self.game_over:
            if keys[pygame.K_w]:
                self.player.move(-10, self.height)
            if keys[pygame.K_s]:
                self.player.move(10, self.height)

    def update(self):
        if self.game_over or self.selecting_best_of:
            return

        self.ball.move()
        self.ball.check_collision(self.player, self.ai)

        if self.ball.x <= 0:
            self.ai_score += 1
            self.score_sound.play()  # Sound feedback for AI scoring
            self.ball.reset()
            if self.check_game_winner():
                self.ai_match_wins += 1
                self.handle_match_progress()

        elif self.ball.x >= self.width:
            self.player_score += 1
            self.score_sound.play()  # Sound feedback for player scoring
            self.ball.reset()
            if self.check_game_winner():
                self.player_match_wins += 1
                self.handle_match_progress()

        self.ai.auto_track(self.ball, self.height)

    def check_game_winner(self):
        return self.player_score >= self.max_score or self.ai_score >= self.max_score

    def handle_match_progress(self):
        # Reset game scores after a game finishes
        self.player_score = 0
        self.ai_score = 0

        # Calculate required wins for best-of rounds (e.g., 3 means 2 wins needed)
        match_wins_required = (self.best_of_rounds // 2) + 1

        if self.player_match_wins >= match_wins_required:
            self.game_over = True
            self.winner = "Player"
        elif self.ai_match_wins >= match_wins_required:
            self.game_over = True
            self.winner = "AI"

    def render(self, screen):
        # Normal gameplay rendering
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width // 2, 0), (self.width // 2, self.height))

        # Draw individual game score
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width // 4, 20))
        screen.blit(ai_text, (self.width * 3 // 4, 20))

        # Draw match wins if best-of selected and playing
        if self.best_of_rounds and not self.selecting_best_of:
            match_text = self.font.render(f"Match - Player: {self.player_match_wins} AI: {self.ai_match_wins}", True, WHITE)
            screen.blit(match_text, (self.width // 2 - match_text.get_width() // 2, 60))

        # Draw best-of selection prompt
        if self.selecting_best_of:
            self.render_best_of_selection(screen)

    def render_game_over(self, screen):
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        msg_font = pygame.font.SysFont("Arial", 60)
        msg = msg_font.render(f"{self.winner} Wins The Match!", True, WHITE)
        screen.blit(msg, (self.width // 2 - msg.get_width() // 2, self.height // 2 - msg.get_height() - 30))

        # Display final match scores (games won)
        score_font = pygame.font.SysFont("Arial", 40)
        final_score = score_font.render(
            f"Final Match Score: Player {self.player_match_wins} - {self.ai_match_wins} AI",
            True,
            WHITE
        )
        screen.blit(final_score, (self.width // 2 - final_score.get_width() // 2, self.height // 2 + 10))

        hint_font = pygame.font.SysFont("Arial", 30)
        hint_restart = hint_font.render("Press R to Replay or Q to Quit", True, WHITE)
        screen.blit(hint_restart, (self.width // 2 - hint_restart.get_width() // 2, self.height // 2 + 50))

    def render_best_of_selection(self, screen):
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        prompt_font = pygame.font.SysFont("Arial", 40)
        prompt = prompt_font.render("Choose Best Of Rounds: 3, 5 or 7", True, WHITE)
        screen.blit(prompt, (self.width // 2 - prompt.get_width() // 2, self.height // 2 - 60))

        note_font = pygame.font.SysFont("Arial", 30)
        note = note_font.render("Press 3, 5 or 7 to select, Q to Quit", True, WHITE)
        screen.blit(note, (self.width // 2 - note.get_width() // 2, self.height // 2))

    def handle_best_of_selection_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                self.best_of_rounds = 3
                self.selecting_best_of = False
            elif event.key == pygame.K_5:
                self.best_of_rounds = 5
                self.selecting_best_of = False
            elif event.key == pygame.K_7:
                self.best_of_rounds = 7
                self.selecting_best_of = False
            elif event.key == pygame.K_q:
                pygame.quit()
                exit()

    def reset_game(self):
        self.player_score = 0
        self.ai_score = 0
        self.player_match_wins = 0
        self.ai_match_wins = 0
        self.game_over = False
        self.winner = None
        self.selecting_best_of = True
        self.best_of_rounds = None
        self.ball.reset()
