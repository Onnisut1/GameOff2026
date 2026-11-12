import pygame
import sys  

from scripts.entities import PhysicsEntity
from scripts.utilities import load_image, load_images
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Shift Wizard")

        self.screen = pygame.display.set_mode((1280, 720))

        self.display = pygame.Surface((640, 480))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "placeholder": load_images("tiles/placeholder"), 
            "player": load_image("Hattivatti.png")

        }

        self.player = PhysicsEntity(self, "player", (50, 50), (32, 32))

        self.tilemap = Tilemap(self, tile_size=32)
        
    def run(self):
        while True:
            self.display.fill("grey")

            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0) * 5)
            self.player.render(self.display)

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

            

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()))
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

Game().run()
