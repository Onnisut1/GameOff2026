class Tilemap:
    def __init__(self, game, tile_size=32):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ";10"] = {"type": "placeholder", "variant": 1, "position": (3 + i, 10)}


    def render(self, surface):

        for tile in self.offgrid_tiles:
            surface.blit(self.game.assets[tile["type"]][tile["variant"]], tile["position"])
                    
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surface.blit(self.game.assets[tile["type"]][tile["variant"]], (tile["position"][0] * self.tile_size, tile["position"][1] * self.tile_size))
