

from map import rooms
from messages import insult


def player_description(player):
    message = []
    message.append('## {} \n'.format(player.name))
    message.append('## \n')
    message.append(rooms[player.room].description())

    return ''.join(message)


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


        try:
            current_room = rooms[self.room]
            next_room = getattr(current_room, direction)
        except Exception as e:
            print(e)
            print(insult())
        else:
            if next_room:
                self.room = next_room
            else:
                print(insult())


    def description(self):
        return player_description(self)
