import pygame
import random
import os

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

        base_dir = os.path.dirname(os.path.abspath(__file__))
        asset_dir = os.path.join(base_dir, '..', 'assets', 'sounds')

        # Load sound effects
        self.paddle_sound = pygame.mixer.Sound(os.path.join(asset_dir, 'paddle_hit.wav'))
        self.wall_sound = pygame.mixer.Sound(os.path.join(asset_dir, 'wall_hit.wav'))

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.wall_sound.play()  # play wall bounce sound
            self.velocity_y *= -1

    def check_collision(self, player, ai):
        steps = max(abs(self.velocity_x), abs(self.velocity_y))
        if steps == 0:
            steps = 1
        for _ in range(int(steps)):
            # Move stepwise
            self.rect().x += self.velocity_x / steps
            self.rect().y += self.velocity_y / steps
            if self.rect().colliderect(player.rect()):
                self.paddle_sound.play()  # play paddle hit sound
                self.velocity_x *= -1
                break
            elif self.rect().colliderect(ai.rect()):
                self.paddle_sound.play()  # play paddle hit sound
                self.velocity_x *= -1
                break

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
