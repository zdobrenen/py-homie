

class MapTile(object):

    N = None
    S = None
    E = None
    W = None

    contents = {}

    def directions(self):

        labels = {
            'N': 'north',
            'S': 'south',
            'E': 'east',
            'W': 'west'
        }

        NSEW = [labels[d] for d in dir(self) if len(d) == 1 and d in "NSEW" and getattr(self, d)]
        return "You can go: \n" + "\n".join(NSEW)


class EntranceRoom(MapTile):
    N = "lobby_room"
    S = ""
    E = ""
    W = ""


class LobbyRoom(MapTile):
    N = "veg_room"
    S = "entrance_room"
    E = "bar_room"
    W = "green_room"


class BarRoom(MapTile):
    N = "clone_room"
    S = "skate_room"
    E = ""
    W = "lobby_room"


class GreenRoom(MapTile):
    N = "flower_room"
    S = "boys_room"
    E = "lobby_room"
    W = ""


class BoysRoom(MapTile):
    N = "green_room"
    S = ""
    E = ""
    W = ""


class FlowerRoom(MapTile):
    N = ""
    S = "green_room"
    E = "veg_room"
    W = ""


class VegRoom(MapTile):
    N = ""
    S = "lobby_room"
    E = "clone_room"
    W = "flower_room"


class CloneRoom(MapTile):
    N = ""
    S = "bar_room"
    E = ""
    W = "veg_room"


class SkateRoom(MapTile):
    N = "bar_room"
    S = ""
    E = ""
    W = ""


rooms = {

    'entrance_room': EntranceRoom(),
    'lobby_room': LobbyRoom(),
    'bar_room': BarRoom(),
    'green_room': GreenRoom(),
    'boys_room': BoysRoom(),
    'flower_room': FlowerRoom(),
    'veg_room': VegRoom(),
    'clone_room': CloneRoom(),
    'skate_room': SkateRoom()
}