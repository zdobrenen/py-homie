
def room_description(room, description):
    return description


class MapTile(object):

    N = None
    S = None
    E = None
    W = None

    contents = {}

    def description(self):
        pass


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
    name = 'Entrance Room'

    N = "lobby_room"
    S = ""
    E = ""
    W = ""

    def description(self):
        message = 'You are in the {}'.format(self.name)
        return room_description(self, message)


class LobbyRoom(MapTile):
    name = 'Lobby Room'

    N = "veg_room"
    S = "entrance_room"
    E = "bar_room"
    W = "green_room"

    def description(self):
        message = 'You are in the {}'.format(self.name)
        return room_description(self, message)


class BarRoom(MapTile):
    name = 'Bar Room'

    N = "clone_room"
    S = "skate_room"
    E = ""
    W = "lobby_room"

    def description(self):
        message = 'You are in the {}'.format(self.name)
        return room_description(self, message)


class GreenRoom(MapTile):
    name = 'Green Room'

    N = "flower_room"
    S = "boys_room"
    E = "lobby_room"
    W = ""

    def description(self):
        message = 'You are in the {}'.format(self.name)
        return room_description(self, message)


class BoysRoom(MapTile):
    name = 'Boys Room'

    N = "green_room"
    S = ""
    E = ""
    W = ""

    def description(self):
        message = 'You are in the {}'.format(self.name)
        return room_description(self, message)


class FlowerRoom(MapTile):
    name = 'Flower Room'

    N = ""
    S = "green_room"
    E = "veg_room"
    W = ""

    def description(self):
        message = 'You are in the {}'.format(self.name)
        return room_description(self, message)


class VegRoom(MapTile):
    name = 'Veg Room'

    N = ""
    S = "lobby_room"
    E = "clone_room"
    W = "flower_room"

    def description(self):
        message = 'You are in the {}'.format(self.name)
        return room_description(self, message)


class CloneRoom(MapTile):
    name = 'Clone Room'

    N = ""
    S = "bar_room"
    E = ""
    W = "veg_room"

    def description(self):
        message = 'You are in the {}'.format(self.name)
        return room_description(self, message)


class SkateRoom(MapTile):
    name = 'Skate Room'

    N = "bar_room"
    S = ""
    E = ""
    W = ""

    def description(self):
        message = 'You are in the {}'.format(self.name)
        return room_description(self, message)



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
