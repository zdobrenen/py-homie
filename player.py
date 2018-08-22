

from map import rooms


class Player(object):

    def __init__(self, name, age, health, damage, room):
        self.name = name
        self.age = age
        self.health = health
        self.damage = damage
        self.room = room


    def is_alive(self):

        return self.health > 0


    def move(self, direction):

        directions = {
            'N' : 'north',
            'S' : 'south',
            'E' : 'east',
            'W' : 'west'
        }


        current_room = rooms[self.room]
        next_room = getattr(current_room, direction)

        if next_room:
            self.room = next_room
        else:
            pass
