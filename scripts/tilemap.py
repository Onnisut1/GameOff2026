import pygame

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {"placeholder"}
class Tilemap:
    def __init__(self, game, tile_size=32):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ";10"] = {"type": "placeholder", "variant": 1, "position": (3 + i, 10)}


    def tiles_around(self, position):
        tiles = []
        tile_location = (int(position[0] // self.tile_size), int(position[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_location = str(tile_location[0] + offset[0]) + ';' + str(tile_location[1] + offset[1])
            if check_location in self.tilemap:
                tiles.append(self.tilemap[check_location])
        return tiles   

    def physics_rects_around(self, position):
        rects = []
        for tile in self.tiles_around(position):
            if tile["type"] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile["position"][0] * self.tile_size, tile["position"][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
    
    def render(self, surface):
        for tile in self.offgrid_tiles:
            surface.blit(self.game.assets[tile["type"]][tile["variant"]], tile["position"])
                    
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surface.blit(self.game.assets[tile["type"]][tile["variant"]], (tile["position"][0] * self.tile_size, tile["position"][1] * self.tile_size))
