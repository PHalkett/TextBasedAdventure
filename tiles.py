#The Coordinate Plane
import items, enemies, actions, world

#MapTile is actually an ABSTRACT base class because we don't want to create ANY instances of it
#In our game, we will only want to create specific types of tiles.
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y)

def intro_text(self):
    raise NotImplementedError()

def modify_player(self, player):
    raise NotImplementedError()
    
#These are here to warn us if we accidentally create a MapTile directly

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        Hi. Move. 
        """
    def modify_player(self, player):
        #Room has no action on player
        pass


#Loot of the Room lol
class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
        
    def add_loot(self, player):
        player.inventory.append(self.item)
        
    def modify_player(self, player):
        self.add_loot(player)
        
#Enemy Room
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
        
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Shiiiit, y'all just got slapped for {}. You have {} HP.".format(self.enemy.damage, the_player.hp))

#More Specific Map Tiles
class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        nada, G. keep schmovin.
        """
    def modify_player(self, player):
        #Room has no action on player
        pass

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Ewww, his legs are hairy like Daddy's!
            """
        else:
            return """
            Well, he certainly wasn't as hard as Daddy!'
            """

class TheOGRERoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Fee Fi Fo Fum, bitch.
            """
        else:
            return """
            At least he had good stats for the cost.
            """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
        
    def intro_text(self):
        return """
        shiny.
        """
        