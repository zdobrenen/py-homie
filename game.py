import sys
import re
import random
import datetime


from player import Player
from map import rooms
from messages import insult



def user_name(retries=10):
    try:
        name = raw_input("Give me your name: ")

        if not isinstance(name, str):
            raise ValueError()

    except ValueError as e:
        print(insult())
        retries = retries - 1

        if retries > 0:
            return user_name(retries)
        else:
            print(insult())
            sys.exit(1)
    else:
        return name



def user_age(retries=10):
    try:
        age = input("Give me your age: ")

        if not isinstance(age, int):
            raise ValueError()

    except ValueError as e:
        print(insult())
        retries = retries - 1

        if retries > 0:
            return user_age(retries)
        else:
            print(insult())
            sys.exit(1)
    else:
        return age


def user_cmd(retries=10):
    try:
        cmd = raw_input("Give me your command: ")

        if not isinstance(cmd, str):
            raise ValueError()

    except ValueError as e:
        print(insult())
        retries = retries - 1

        if retries > 0:
            return user_cmd(retries)
        else:
            print(insult())
            sys.exit(1)
    else:
        return cmd


def validate_name(name):

    rules = {
        'one_numeric_char': '[0-9]',
        'one_special_char': '[^0-9a-zA-Z]+'
    }

    try:
        if len(name) < 5 or len(name) > 20:
            raise ValueError("invalid user name")
        elif sum([1 for m in re.finditer(rules['one_numeric_char'], name)]) < 1:
            raise ValueError("invalid user name, must contain at least one numeric character")
        elif sum([1 for m in re.finditer(rules['one_special_char'], name)]) < 1:
            raise ValueError("invalid user name, must contain at least one special character")
        else:
            return name
    except ValueError as e:
        print(e)
        return user_name()


def validate_age(age):

    try:
        if age < 6 or age > 110:
            raise ValueError("invalid user age")
        else:
            return age
    except ValueError as e:
        print(e)
        return user_age()



def play():

    print(" _______     ___    _  ______     .--.      .--.   ____   ,---------.   _______   .---.  .---. ")
    print("\  ____  \ .'   |  | ||    _ `''. |  |_     |  | .'  __ `.\          \ /   __  \  |   |  |_ _| ")
    print("| |    \ | |   .'  | || _ | ) _  \| _( )_   |  |/   '  \  \`--.  ,---'| ,_/  \__) |   |  ( ' ) ")
    print("| |____/ / .'  '_  | ||( ''_'  ) ||(_ o _)  |  ||___|  /  |   |   \ ,-./  )       |   '-(_{;}_)")
    print("|   _ _ '. '   ( \.-.|| . (_) `. || (_,_) \ |  |   _.-`   |   :_ _: \  '_ '`)     |      (_,_) ")
    print("|  ( ' )  \' (`. _` /||(_    ._) '|  |/    \|  |.'   _    |   (_I_)  > (_)  )  __ | _ _--.   | ")
    print("| (_{;}_) || (_ (_) _)|  (_.\.' / |  '  /\  `  ||  _( )_  |  (_(=)_)(  .  .-'_/  )|( ' ) |   | ")
    print("|  (_,_)  / \ /  . \ /|       .'  |    /  \    |\ (_ o _) /   (_I_)  `-'`-'     / (_{;}_)|   | ")
    print("/_______.'   ``-'`-'' '-----'`    `---'    `---` '.(_,_).'    '---'    `._____.'  '(_,_) '---' ")
    print(",---------. .---.  .---.     .-''-.            .-_'''-.      ____    ,---.    ,---.    .-''-.  ")
    print("\          \|   |  |_ _|   .'_ _   \          '_( )_   \   .'  __ `. |    \  /    |  .'_ _   \ ")
    print(" `--.  ,---'|   |  ( ' )  / ( ` )   '        |(_ o _)|  ' /   '  \  \|  ,  \/  ,  | / ( ` )   '")
    print("    |   \   |   '-(_{;}_). (_ o _)  |        . (_,_)/___| |___|  /  ||  |\_   /|  |. (_ o _)  |")
    print("    :_ _:   |      (_,_) |  (_,_)___|        |  |  .-----.   _.-`   ||  _( )_/ |  ||  (_,_)___|")
    print("    (_I_)   | _ _--.   | '  \   .---.        '  \  '-   .'.'   _    || (_ o _) |  |'  \   .---.")
    print("   (_(=)_)  |( ' ) |   |  \  `-'    /         \  `-'`   | |  _( )_  ||  (_,_)  |  | \  `-'    /")
    print("    (_I_)   (_{;}_)|   |   \       /           \        / \ (_ o _) /|  |      |  |  \       / ")
    print("    '---'   '(_,_) '---'    `'-..-'             `'-...-'   '.(_,_).' '--'      '--'   `'-..-'  ")
    print("")
    print("")
    print("")


    name = user_name()
    name = validate_name(name)

    age = user_age()
    age = validate_age(age)


    player = Player(name, age, 100, 0, 'entrance_room')

    while player.is_alive():

        cmd = user_cmd()

        player.move(cmd)
        player.description()


play()
