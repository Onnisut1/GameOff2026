import pygame
import sys  

from scripts.entities import PhysicsEntity
from scripts.utilities import load_image
class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Shift Wizard")

        self.screen = pygame.display.set_mode((1280, 720))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "player": load_image("Hattivatti.png")
        }

        self.player = PhysicsEntity(self, "player", (50, 50), (16, 16))
        
    def run(self):
        while True:
            self.screen.fill("grey")

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_a:
                        self.movement[0] = False

            

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

Game().run()
