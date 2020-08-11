_world = {}
starting_position = (0, 0)

#If we were trying to do this normally, we would do some bullshit where it's like:
#tile_map = [[FindGoldRoom(),GiantSpiderRoom(),None,None,None],
#            [None,StartingRoom(),EmptyCave(),EmptyCave(),None]]]]

#We can use this method as an alternative but ONLY because all of our tile classes derive from the same base class 
#with a common constructor that accepts the same parameters.

def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
            
def tile_exists(x, y):
    return _world.get((x, y))